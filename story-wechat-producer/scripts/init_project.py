#!/usr/bin/env python3
"""Initialize a non-destructive WeChat workspace for film, animation, or manga."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


DIRECTORIES = [
    "00_总控",
    "01_素材验收",
    "02_事实表",
    "02_事实表/分块事实表",
    "02_事实表/临时争议帧",
    "03_顺序解说稿",
    "04_截图清单",
    "05_必选截图",
    "05_必选截图/原片PNG",
    "05_必选截图/发布版图片",
    "06_公众号排版稿",
    "06_公众号排版稿/工作文件",
    "06_公众号排版稿/QA",
    "07_封面",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a source-indexed story-to-WeChat illustrated article workspace."
    )
    parser.add_argument(
        "--root", required=True,
        help="Project directory with no conflicting template files or directory paths",
    )
    parser.add_argument("--title", required=True, help="Story or project title")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--video", help="Existing local video (legacy single-source mode)")
    source.add_argument("--sources-json", help="Source registry JSON or legacy project JSON")
    parser.add_argument("--subtitle", help="Existing local ASS/SRT subtitle")
    parser.add_argument("--source-type", choices=("film", "animation"), help="Type for --video")
    parser.add_argument("--version", help="Edition or cut for --video")
    parser.add_argument("--blocks", type=int, default=10, help="Initial virtual block count")
    parser.add_argument("--dry-run", action="store_true", help="Print the plan without writing")
    return parser.parse_args()


def existing_source_path(value: object, base_dir: Path, *, allow_directory: bool = False) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Source paths must be non-empty strings")
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = base_dir / path
    path = path.resolve()
    if not path.is_file() and not (allow_directory and path.is_dir()):
        raise FileNotFoundError(f"Source does not exist or has an unsupported path type: {path}")
    return str(path)


def normalize_source_registry(data: object, base_dir: Path) -> list[dict]:
    """Read v2 sources or a v1 project without mutating the input or source files."""
    if isinstance(data, dict) and "sources" in data:
        entries = data["sources"]
    elif isinstance(data, dict) and isinstance(data.get("source"), dict):
        legacy = data["source"]
        entries = [{
            "source_id": "FILM-01", "source_type": "film",
            "version": legacy.get("version", "unverified"),
            "video": legacy.get("video", ""), "subtitle": legacy.get("subtitle", ""),
        }]
    else:
        entries = data
    if not isinstance(entries, list) or not entries:
        raise ValueError("Source registry must contain a non-empty sources list")

    normalized = []
    seen_ids, seen_orders = set(), set()
    for index, entry in enumerate(entries, 1):
        if not isinstance(entry, dict):
            raise ValueError("Each source must be an object")
        item = dict(entry)
        source_id = item.get("source_id")
        if not isinstance(source_id, str) or not source_id.strip() or source_id in seen_ids:
            raise ValueError("Every source needs a unique non-empty source_id")
        seen_ids.add(source_id)
        source_type = item.get("source_type")
        if source_type not in ("film", "animation", "manga"):
            raise ValueError(f"Unsupported source_type for {source_id}: {source_type}")
        order = item.get("order", index)
        if type(order) is not int or order < 1 or order in seen_orders:
            raise ValueError("Source order must be a unique positive integer")
        seen_orders.add(order)
        item["order"] = order
        item.setdefault("version", "unverified")
        if not isinstance(item["version"], str) or not item["version"].strip():
            raise ValueError(f"Version must be a non-empty string for {source_id}")

        if source_type in ("film", "animation"):
            for key in ("video", "subtitle"):
                if key in item and not isinstance(item[key], str):
                    raise ValueError(f"Source path {key} for {source_id} must be a string")
            if not item.get("video") and not item.get("subtitle"):
                raise ValueError(f"Video source {source_id} needs a video or subtitle path")
            for key in ("video", "subtitle"):
                if item.get(key):
                    item[key] = existing_source_path(item[key], base_dir)
        else:
            item["path"] = existing_source_path(item.get("path"), base_dir, allow_directory=True)
            item.setdefault("reading_order", "unverified")
            if item["reading_order"] not in ("rtl", "ltr", "vertical", "unverified"):
                raise ValueError(f"Unsupported manga reading_order for {source_id}")
        normalized.append(item)
    return sorted(normalized, key=lambda item: item["order"])


def validate_args(args: argparse.Namespace) -> tuple[Path, list[dict]]:
    root = Path(args.root).expanduser().absolute()
    reject_symlink(root)
    root = root.resolve()
    if args.blocks < 1 or args.blocks > 100:
        raise ValueError("--blocks must be between 1 and 100")
    if root.exists() and not root.is_dir():
        raise NotADirectoryError(f"Project root is not a directory: {root}")

    if args.sources_json:
        if args.subtitle or args.source_type or args.version:
            raise ValueError("--subtitle, --source-type, and --version belong to --video mode")
        registry = Path(args.sources_json).expanduser().resolve()
        data = json.loads(registry.read_text(encoding="utf-8-sig"))
        sources = normalize_source_registry(data, registry.parent)
    else:
        video = Path(args.video).expanduser().resolve()
        if not video.is_file():
            raise FileNotFoundError(f"Master video does not exist: {video}")
        source_type = args.source_type or "film"
        sources = normalize_source_registry([{
            "source_id": "FILM-01" if source_type == "film" else "AN-01",
            "source_type": source_type, "version": args.version or "unverified",
            "video": str(video), "subtitle": args.subtitle or "",
        }], Path.cwd())
    return root, sources


def reject_symlink(path: Path) -> None:
    if path.is_symlink():
        raise ValueError(f"Refusing symbolic link in project path: {path}")


def validate_directory_chain(path: Path) -> None:
    """Check existing directory components before any mkdir or file write."""
    for directory in reversed((path, *path.parents)):
        reject_symlink(directory)
        if directory.exists() and not directory.is_dir():
            raise NotADirectoryError(f"Project directory path is not a directory: {directory}")


def validate_plan(root: Path, files: dict[str, str]) -> list[Path]:
    """Use the same complete destination preflight for dry runs and real runs."""
    planned = [root / rel for rel in files]
    directories = [root, *(root / rel for rel in DIRECTORIES)]
    directories.extend(path.parent for path in planned)
    for directory in directories:
        validate_directory_chain(directory)

    conflicts = []
    for path in planned:
        reject_symlink(path)
        if path.exists():
            conflicts.append(path)
    if conflicts:
        conflict_lines = "\n".join(str(path) for path in conflicts)
        raise FileExistsError(f"Refusing to overwrite existing files:\n{conflict_lines}")
    return planned


def templates(title: str, sources: list[dict], blocks: int) -> dict[str, str]:
    project = {
        "schema_version": 2,
        "title": title,
        "sources": sources,
        "virtual_block_count": blocks,
        "current_phase": 0,
        "status": "initialized",
        "publication_authorized": False,
    }
    if len(sources) == 1 and sources[0].get("video"):
        project["source"] = {
            "video": sources[0]["video"], "subtitle": sources[0].get("subtitle", ""),
        }
    source_summary = "".join(
        f"- {item['source_id']}（{item['source_type']}，{item['version']}）："
        f"`{item.get('video') or item.get('path') or item.get('subtitle')}`\n"
        for item in sources
    )
    return {
        "project.json": json.dumps(project, ensure_ascii=False, indent=2) + "\n",
        "00_总控/阶段状态.md": (
            f"# {title}：公众号图文解说阶段状态\n\n"
            "- 当前阶段：0（编辑目标与授权）\n"
            "- 本次授权范围：待根据用户请求记录；已授权阶段可连续执行\n"
            "- 用户指定的检查点：待记录；未指定时不逐阶段重复询问\n"
            "- 上传／发布授权：否\n"
        ),
        "01_素材验收/素材验收.md": (
            f"# {title}：素材验收与虚拟分段\n\n"
            "素材注册表见 project.json 的 sources；路径存在不等于已经核验内容。\n\n"
            f"{source_summary}"
            f"- 初始虚拟块数：{blocks}\n\n"
            "## 待核验\n\n"
            "- 影视：逐源分辨率、时长、帧率、轨道与字幕同步；只有字幕时视听待核\n"
            "- 漫画：版本／卷章、文件页与印刷页映射、阅读方向、跨页与格序\n"
            "- 素材大小、必要哈希、所选集章范围与排除内容\n"
            "- 章节／镜头／页格索引、人物首次出场与身份公开表\n"
        ),
        "01_素材验收/人物公开表.md": (
            "# 人物公开表\n\n"
            "| character_id | 当前可称名 | 首次出现 | 首次清晰正脸 | 首次报姓名 | 身份揭晓 | 能力揭晓 | 服装／身份状态 | 防剧透规则 | 识别用截图候选 |\n"
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
        ),
        "02_事实表/事实表模板.md": (
            "# 分块事实表模板\n\n"
            "claim_type 区分 observable_fact（观察事实）、character_statement（角色陈述）、"
            "inference（推断）、interpretation（主题解读）；evidence_source 记录原片画面、音频、"
            "字幕、漫画页格／气泡／旁白框及实际核验情况。source_locator 使用源时间或卷章／页／格，"
            "文件页与印刷页分开；外部补充另记。明确说过一句话，不等于其内容已经证实。\n\n"
            "| fact_id | source_id | source_locator | 地点 | 当时已知身份 | 说话者／动作主体 | 画面动作 | 对白摘要 | 直接结果 | 下一剧情作用 | 配图候选 | claim_type | evidence_source | evidence_level（证据等级） | 不确定项 |\n"
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
        ),
        "02_事实表/争议清单.md": (
            "# 争议与待复核清单\n\n"
            "| dispute_id | source_refs | 风险断言 | 当前版本支持 | 未知部分 | 安全写法 | 禁止写法 | 复核方式 | 状态 |\n"
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
        ),
        "03_顺序解说稿/正文.md": f"# {title}\n",
        "03_顺序解说稿/章节覆盖图.md": (
            "# 章节覆盖图\n\n"
            "| chapter_id | 章节标题 | source_refs | 当前目标 | 必需事件 | 与下一章的因果交接 | 必需人物 | 需安全处理的争议 |\n"
            "| --- | --- | --- | --- | --- | --- | --- | --- |\n"
        ),
        "04_截图清单/截图清单.md": (
            "# 公众号配图清单（沿用截图清单文件名）\n\n"
            "| shot_id | paragraph_id | fact_ids | 必选／备选 | 用途 | source_id | main_locator | alternative_source_ref | 可见主体 | 构图／裁图坐标 | 身份顺序 | 风险 | 输出文件名 |\n"
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
        ),
        "05_必选截图/导出记录.md": (
            "# 截图导出记录\n\n"
            "| shot_id | source_id | source_locator | source_hash_or_version | source_video_hash_or_id | 导出／裁图参数 | 文件名 | 宽 | 高 | 像素格式 | 字节数 | SHA-256 | 视觉检查 |\n"
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
        ),
    }


def main() -> int:
    args = parse_args()
    try:
        root, sources = validate_args(args)
        files = templates(args.title, sources, args.blocks)
        planned = validate_plan(root, files)

        plan = {
            "root": str(root),
            "directories": [str(root / rel) for rel in DIRECTORIES],
            "files": [str(path) for path in planned],
            "dry_run": args.dry_run,
        }
        if args.dry_run:
            print(json.dumps(plan, ensure_ascii=False, indent=2))
            return 0

        for directory in [root, *(root / rel for rel in DIRECTORIES)]:
            validate_directory_chain(directory)
            directory.mkdir(parents=True, exist_ok=True)
        for rel, content in files.items():
            path = root / rel
            validate_directory_chain(path.parent)
            reject_symlink(path)
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("x", encoding="utf-8", newline="\n") as handle:
                handle.write(content)
        print(json.dumps(plan, ensure_ascii=False, indent=2))
        return 0
    except (ValueError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
