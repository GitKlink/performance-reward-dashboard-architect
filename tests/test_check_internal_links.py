from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "check-internal-links.py"
SPEC = importlib.util.spec_from_file_location("check_internal_links", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Unable to load {MODULE_PATH}")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class InternalLinkTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def write(self, path: str, content: str) -> Path:
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        return target

    def test_valid_relative_link_passes(self) -> None:
        self.write("docs/target.md", "# Target\n")
        source = self.write("README.md", "See [target](docs/target.md).\n")

        self.assertEqual([], MODULE.check_file(source, self.root))

    def test_missing_relative_link_fails(self) -> None:
        source = self.write("README.md", "See [missing](docs/missing.md).\n")

        findings = MODULE.check_file(source, self.root)
        self.assertEqual(1, len(findings))
        self.assertEqual("docs/missing.md", findings[0].target)

    def test_external_and_anchor_links_are_ignored(self) -> None:
        source = self.write(
            "README.md",
            "[web](https://example.com) [section](#section) [mail](mailto:a@example.com)\n",
        )

        self.assertEqual([], MODULE.check_file(source, self.root))

    def test_fenced_code_links_are_ignored(self) -> None:
        source = self.write(
            "README.md",
            "```markdown\n[example](missing.md)\n```\n",
        )

        self.assertEqual([], MODULE.check_file(source, self.root))

    def test_root_relative_link_is_checked_from_repository_root(self) -> None:
        self.write("docs/target.md", "# Target\n")
        source = self.write("nested/README.md", "[target](/docs/target.md)\n")

        self.assertEqual([], MODULE.check_file(source, self.root))


if __name__ == "__main__":
    unittest.main()
