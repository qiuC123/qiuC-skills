#!/usr/bin/env python3
"""Initialize a non-destructive movie WeChat article workspace."""

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
        description="Create a staged movie-to-WeChat illustrated article workspace."
    )
    parser.add_argument("--root", required=True, help="New or empty project directory")
    parser.add_argument("--title", required=True, help="Film title")
    parser.add_argument("--video", required=True, help="Existing local master video")
    parser.add_argument("--subtitle", help="Existing local ASS/SRT subtitle")
    parser.add_argument("--blocks", type=int, default=10, help="Initial virtual block count")
    parser.add_argument("--dry-run", action="store_true", help="Print the plan without writing")
    return parser.parse_args()


def validate_args(args: argparse.Namespace) -> tuple[Path, Path, Path | None]:
    root = Path(args.root).expanduser().resolve()
    video = Path(args.video).expanduser().resolve()
    subtitle = Path(args.subtitle).expanduser().resolve() if args.subtitle else None

    if args.blocks < 1 or args.blocks > 100:
        raise ValueError("--blocks must be between 1 and 100")
    if not video.is_file():
        raise FileNotFoundError(f"Master video does not exist: {video}")
    if subtitle is not None and not subtitle.is_file():
        raise FileNotFoundError(f"Subtitle does not exist: {subtitle}")
    if root.exists() and not root.is_dir():
        raise NotADirectoryError(f"Project root is not a directory: {root}")
    return root, video, subtitle


def templates(title: str, video: Path, subtitle: Path | None, blocks: int) -> dict[str, str]:
    subtitle_text = str(subtitle) if subtitle else ""
    project = {
        "schema_version": 1,
        "title": title,
        "source": {"video": str(video), "subtitle": subtitle_text},
        "virtual_block_count": blocks,
        "current_phase": 0,
        "status": "initialized",
        "publication_authorized": False,
    }
    return {
        "project.json": json.dumps(project, ensure_ascii=False, indent=2) + "\n",
        "00_总控/阶段状态.md": (
            f"# {title}：公众号图文解说阶段状态\n\n"
            "- 当前阶段：0（编辑目标与授权）\n"
            "- 下一批准门：确认素材验收与虚拟分段\n"
            "- 上传／发布授权：否\n"
        ),
        "01_素材验收/素材验收.md": (
            f"# {title}：素材验收与虚拟分段\n\n"
            f"- 主片：`{video}`\n"
            f"- 字幕：`{subtitle_text or '未提供'}`\n"
            f"- 初始虚拟块数：{blocks}\n\n"
            "## 待核验\n\n"
            "- 分辨率、时长、帧率、轨道、文件大小与哈希\n"
            "- 字幕编码、事件范围与同步情况\n"
            "- 章节／镜头索引、人物首次出场与身份公开表\n"
        ),
        "01_素材验收/人物公开表.md": (
            "# 人物公开表\n\n"
            "| character_id | 当前可称名 | 首次出现 | 首次清晰正脸 | 首次报姓名 | 身份揭晓 | 能力揭晓 | 服装／身份状态 | 防剧透规则 | 识别用截图候选 |\n"
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
        ),
        "02_事实表/事实表模板.md": (
            "# 分块事实表模板\n\n"
            "| fact_id | 起止时间 | 地点 | 当时已知身份 | 说话者／动作主体 | 画面动作 | 对白摘要 | 直接结果 | 下一剧情作用 | 截图候选 | 证据等级 | 不确定项 |\n"
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
        ),
        "02_事实表/争议清单.md": (
            "# 争议与待复核清单\n\n"
            "| dispute_id | 时间范围 | 风险断言 | 电影支持 | 未知部分 | 安全写法 | 禁止写法 | 复核方式 | 状态 |\n"
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
        ),
        "03_顺序解说稿/正文.md": f"# {title}\n",
        "03_顺序解说稿/章节覆盖图.md": (
            "# 章节覆盖图\n\n"
            "| chapter_id | 章节标题 | 时间范围 | 当前目标 | 必需事件 | 与下一章的因果交接 | 必需人物 | 需安全处理的争议 |\n"
            "| --- | --- | --- | --- | --- | --- | --- | --- |\n"
        ),
        "04_截图清单/截图清单.md": (
            "# 公众号截图清单\n\n"
            "| shot_id | paragraph_id | fact_ids | 必选／备选 | 用途 | 主时间码 | 备用时间码／范围 | 可见主体 | 构图要求 | 身份顺序 | 风险 | 输出文件名 |\n"
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
        ),
        "05_必选截图/导出记录.md": (
            "# 截图导出记录\n\n"
            "| shot_id | 源时间码 | 文件名 | 宽 | 高 | 像素格式 | 字节数 | SHA-256 | 视觉检查 |\n"
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
        ),
    }


def main() -> int:
    args = parse_args()
    try:
        root, video, subtitle = validate_args(args)
        files = templates(args.title, video, subtitle, args.blocks)
        planned = [root / rel for rel in files]
        conflicts = [path for path in planned if path.exists()]
        if conflicts:
            conflict_lines = "\n".join(str(path) for path in conflicts)
            raise FileExistsError(f"Refusing to overwrite existing files:\n{conflict_lines}")

        plan = {
            "root": str(root),
            "directories": [str(root / rel) for rel in DIRECTORIES],
            "files": [str(path) for path in planned],
            "dry_run": args.dry_run,
        }
        if args.dry_run:
            print(json.dumps(plan, ensure_ascii=False, indent=2))
            return 0

        root.mkdir(parents=True, exist_ok=True)
        for rel in DIRECTORIES:
            (root / rel).mkdir(parents=True, exist_ok=True)
        for rel, content in files.items():
            path = root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("w", encoding="utf-8", newline="\n") as handle:
                handle.write(content)
        print(json.dumps(plan, ensure_ascii=False, indent=2))
        return 0
    except (ValueError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
