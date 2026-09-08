import contextlib
import io
import json
import runpy
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


SKILL = Path(__file__).resolve().parents[1] / "movie-wechat-illustrated-explainer"
SCRIPT = SKILL / "scripts" / "init_project.py"


class MovieWechatInitializerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.video = self.base / "测试影片.mkv"
        self.subtitle = self.base / "中文字幕.ass"
        # The initializer validates paths; media decoding belongs to source acceptance.
        self.video.write_bytes(b"initializer fixture")
        self.subtitle.write_text("[Script Info]\n", encoding="utf-8")
        self.root = self.base / "公众号项目"

    def run_init(self, *extra):
        return subprocess.run(
            [sys.executable, "-X", "utf8", str(SCRIPT), "--root", str(self.root),
             "--title", "测试影片", "--video", str(self.video),
             "--subtitle", str(self.subtitle), *extra],
            capture_output=True, text=True, encoding="utf-8",
        )

    def make_symlink(self, link, target, *, directory=False):
        try:
            link.symlink_to(target, target_is_directory=directory)
        except (NotImplementedError, OSError) as exc:
            self.skipTest(f"Symbolic links unavailable in this environment: {exc}")

    def assert_rejected_in_both_modes(self):
        for extra in (("--dry-run",), ()):
            result = self.run_init(*extra)
            self.assertEqual(result.returncode, 2, result.stdout)

    def test_dry_run_does_not_write(self):
        result = self.run_init("--dry-run")
        self.assertEqual(result.returncode, 0, result.stderr)
        plan = json.loads(result.stdout)
        self.assertTrue(plan["dry_run"])
        self.assertIn(str(self.root / "project.json"), plan["files"])
        self.assertFalse(self.root.exists())

    def test_initialization_preserves_sources_and_creates_utf8_templates(self):
        originals = {p: p.read_bytes() for p in (self.video, self.subtitle)}
        result = self.run_init()
        self.assertEqual(result.returncode, 0, result.stderr)
        plan = json.loads(result.stdout)
        for name in plan["directories"]:
            self.assertTrue(Path(name).is_dir(), name)
        for name in plan["files"]:
            data = Path(name).read_bytes()
            data.decode("utf-8")
            self.assertNotIn(b"\r", data)
        project = json.loads((self.root / "project.json").read_text(encoding="utf-8"))
        self.assertEqual(project["title"], "测试影片")
        self.assertEqual(project["source"]["video"], str(self.video.resolve()))
        self.assertEqual(project["source"]["subtitle"], str(self.subtitle.resolve()))
        self.assertEqual(project["current_phase"], 0)
        self.assertFalse(project["publication_authorized"])
        self.assertFalse(list(self.root.rglob("build_manifest.json")))
        for path, data in originals.items():
            self.assertEqual(path.read_bytes(), data)

        facts = (self.root / "02_事实表" / "事实表模板.md").read_text(encoding="utf-8")
        header = next(line for line in facts.splitlines() if line.startswith("| fact_id |"))
        for field in ("claim_type", "evidence_source", "evidence_level"):
            self.assertIn(field, header)
        ledger = (self.root / "05_必选截图" / "导出记录.md").read_text(encoding="utf-8")
        self.assertIn("| source_video_hash_or_id |", ledger)

    def test_nonempty_project_with_unrelated_files_is_supported(self):
        self.root.mkdir()
        unrelated = self.root / "用户笔记.md"
        unrelated.write_text("保留已有笔记\n", encoding="utf-8")
        (self.root / "02_事实表").mkdir()
        before = unrelated.read_bytes()
        result = self.run_init()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(unrelated.read_bytes(), before)
        self.assertTrue((self.root / "project.json").is_file())

    def test_directory_conflicts_are_rejected_before_creating_anything(self):
        for index, relative in enumerate(("02_事实表", "06_公众号排版稿/工作文件")):
            with self.subTest(directory=relative):
                self.root = self.base / f"目录冲突-{index}"
                conflict = self.root / relative
                conflict.parent.mkdir(parents=True)
                conflict.write_text("existing file", encoding="utf-8")
                before = set(self.root.rglob("*"))
                self.assert_rejected_in_both_modes()
                self.assertEqual(set(self.root.rglob("*")), before)
                self.assertEqual(conflict.read_text(encoding="utf-8"), "existing file")

    def test_project_root_symlinks_are_rejected(self):
        for exists in (False, True):
            with self.subTest(target_exists=exists):
                target = self.base / f"外部目录-{exists}"
                if exists:
                    target.mkdir()
                self.root = self.base / f"链接项目-{exists}"
                self.make_symlink(self.root, target, directory=True)
                self.assert_rejected_in_both_modes()
                self.assertTrue(self.root.is_symlink())
                self.assertEqual(target.exists(), exists)
                if exists:
                    self.assertEqual(list(target.iterdir()), [])

    def test_template_file_symlinks_are_rejected(self):
        for exists in (False, True):
            with self.subTest(target_exists=exists):
                self.root = self.base / f"文件链接项目-{exists}"
                self.root.mkdir()
                target = self.base / f"外部文件-{exists}.json"
                if exists:
                    target.write_text("keep external data", encoding="utf-8")
                link = self.root / "project.json"
                self.make_symlink(link, target)
                self.assert_rejected_in_both_modes()
                self.assertEqual(list(self.root.iterdir()), [link])
                self.assertEqual(target.exists(), exists)
                if exists:
                    self.assertEqual(target.read_text(encoding="utf-8"), "keep external data")

    def test_internal_directory_symlinks_are_rejected(self):
        for exists in (False, True):
            with self.subTest(target_exists=exists):
                self.root = self.base / f"内部目录链接-{exists}"
                self.root.mkdir()
                target = self.base / f"外部写入目录-{exists}"
                if exists:
                    target.mkdir()
                link = self.root / "00_总控"
                self.make_symlink(link, target, directory=True)
                self.assert_rejected_in_both_modes()
                self.assertEqual(list(self.root.iterdir()), [link])
                self.assertEqual(target.exists(), exists)
                if exists:
                    self.assertEqual(list(target.iterdir()), [])

    def test_file_created_after_preflight_is_not_overwritten(self):
        # Insert a competing file immediately before the actual open, after all
        # existence checks. The output must survive this race unchanged.
        main = runpy.run_path(str(SCRIPT))["main"]
        target = self.root / "project.json"
        original_open = Path.open
        inserted = False

        def competing_open(path, *args, **kwargs):
            nonlocal inserted
            if path == target and not inserted:
                inserted = True
                with original_open(target, "w", encoding="utf-8") as handle:
                    handle.write("written by another process\n")
            return original_open(path, *args, **kwargs)

        argv = [str(SCRIPT), "--root", str(self.root), "--title", "测试影片",
                "--video", str(self.video), "--subtitle", str(self.subtitle)]
        with mock.patch.object(sys, "argv", argv), \
                mock.patch.object(Path, "open", new=competing_open), \
                contextlib.redirect_stdout(io.StringIO()), \
                contextlib.redirect_stderr(io.StringIO()):
            result = main()
        self.assertTrue(inserted)
        self.assertEqual(result, 2)
        self.assertEqual(target.read_text(encoding="utf-8"), "written by another process\n")

    def test_repeat_initialization_preserves_edited_files(self):
        self.assertEqual(self.run_init().returncode, 0)
        article = self.root / "03_顺序解说稿" / "正文.md"
        article.write_text("人工编辑的正文\n", encoding="utf-8")
        before = {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        result = self.run_init()
        self.assertEqual(result.returncode, 2)
        self.assertIn("Refusing to overwrite", result.stderr)
        self.assertEqual(before, {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()})

    def test_invalid_inputs_do_not_create_project(self):
        for value in ("0", "101"):
            with self.subTest(blocks=value):
                self.assertEqual(self.run_init("--blocks", value).returncode, 2)
                self.assertFalse(self.root.exists())
        self.video.unlink()
        result = self.run_init()
        self.assertEqual(result.returncode, 2)
        self.assertIn("Master video does not exist", result.stderr)
        self.assertFalse(self.root.exists())


if __name__ == "__main__":
    unittest.main()
