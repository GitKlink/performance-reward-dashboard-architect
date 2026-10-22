"""Tests for non-destructive project-local copying; never touch Power BI files."""

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/install_into_project.py"
spec = importlib.util.spec_from_file_location("project_installer", SCRIPT)
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class ProjectLocalInstallTests(unittest.TestCase):
    def fixture(self, project):
        return {
            Path(".agents/skills/power-bi-architect/dax-measure-standards-review/SKILL.md"): b"some skills\n",
            Path("docs/power-bi-architect/README.md"): b"local docs\n",
            Path("docs/power-bi-architect/installation.json"): b'{"schema_version":"test"}\n',
        }, {"architect_git_sha": "a" * 40, "standards_git_sha": "b" * 40,
            "skills_dir": ".agents/skills"}

    def test_plan_does_not_write_and_apply_adds_to_existing_project(self):
        with tempfile.TemporaryDirectory() as base:
            root = Path(base)
            project = root / "My PBIP"
            project.mkdir()
            (project / ".agents/skills/existing-skill").mkdir(parents=True)
            (project / ".agents/skills/existing-skill/SKILL.md").write_text("keep", encoding="utf-8")
            (project / "AGENTS.md").write_text("preserve", encoding="utf-8")
            contents = self.fixture(project)
            with patch.object(installer, "build_files", return_value=contents):
                text = installer.install(project, root / "standards")
                self.assertIn("PLAN ONLY", text)
                self.assertIn(".agents/skills/power-bi-architect/dax-measure-standards-review", text)
                self.assertFalse((project / "docs").exists())
                applied = installer.install(project, root / "standards", apply=True)
                self.assertIn("INSTALLED 3 files", applied)
                self.assertIn("ALREADY INSTALLED", installer.install(project, root / "standards", apply=True))
            self.assertEqual((project / "AGENTS.md").read_text(encoding="utf-8"), "preserve")
            self.assertEqual((project / ".agents/skills/existing-skill/SKILL.md").read_text(encoding="utf-8"), "keep")
            self.assertTrue((project / ".agents/skills/power-bi-architect/dax-measure-standards-review/SKILL.md").is_file())
            self.assertFalse((project / ".agents/skills/dax-measure-standards-review").exists())

    def test_existing_modified_installed_file_blocks_without_replacement(self):
        with tempfile.TemporaryDirectory() as base:
            root = Path(base)
            project = root / "pbip"
            project.mkdir()
            path = project / ".agents/skills/power-bi-architect/dax-measure-standards-review/SKILL.md"
            path.parent.mkdir(parents=True)
            path.write_text("human authored", encoding="utf-8")
            contents = self.fixture(project)
            with patch.object(installer, "build_files", return_value=contents):
                with self.assertRaisesRegex(installer.InstallError, "must not be overwritten"):
                    installer.install(project, root / "standards", apply=True)
            self.assertEqual(path.read_text(encoding="utf-8"), "human authored")
            self.assertFalse((project / "docs").exists())

    def test_partial_install_blocks(self):
        with tempfile.TemporaryDirectory() as base:
            root = Path(base)
            project = root / "pbip"
            project.mkdir()
            path = project / "docs/power-bi-architect/README.md"
            path.parent.mkdir(parents=True)
            path.write_bytes(b"local docs\n")
            contents = self.fixture(project)
            with patch.object(installer, "build_files", return_value=contents):
                with self.assertRaises(installer.InstallError):
                    installer.install(project, root / "standards", apply=True)

    def test_existing_symlink_path_blocks(self):
        with tempfile.TemporaryDirectory() as base:
            root = Path(base)
            project = root / "pbip"
            project.mkdir()
            other = root / "external"
            other.mkdir()
            try:
                (project / "docs").symlink_to(other, target_is_directory=True)
            except OSError:
                self.skipTest("Symlinks unavailable")
            contents = self.fixture(project)
            with patch.object(installer, "build_files", return_value=contents):
                with self.assertRaisesRegex(installer.InstallError, "symlink"):
                    installer.install(project, root / "standards", apply=True)


    def test_uses_existing_cursor_skills_folder(self):
        with tempfile.TemporaryDirectory() as base:
            project = Path(base)
            (project / ".cursor/skills/unrelated").mkdir(parents=True)
            self.assertEqual(installer.select_skills_dir(project), Path(".cursor/skills"))
            self.assertEqual(installer.select_skills_dir(project, ".agents/skills"), Path(".agents/skills"))

    def test_both_skills_folders_require_explicit_choice(self):
        with tempfile.TemporaryDirectory() as base:
            project = Path(base)
            (project / ".cursor/skills").mkdir(parents=True)
            (project / ".agents/skills").mkdir(parents=True)
            with self.assertRaisesRegex(installer.InstallError, "choose one"):
                installer.select_skills_dir(project)
            self.assertEqual(installer.select_skills_dir(project, ".cursor/skills"),
                             Path(".cursor/skills"))

    def test_defaults_to_agents_skills_when_none_exist(self):
        with tempfile.TemporaryDirectory() as base:
            self.assertEqual(installer.select_skills_dir(Path(base)), Path(".agents/skills"))

    def test_git_blob_is_deterministic(self):
        self.assertEqual(
            installer.blob_sha(b"test\n"),
            "9daeafb9864cf43055ae93beb0afd6c7d144bfa4",
        )


if __name__ == "__main__":
    unittest.main()
