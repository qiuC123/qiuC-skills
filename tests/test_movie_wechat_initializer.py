import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


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
