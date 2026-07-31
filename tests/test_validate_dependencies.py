from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate-dependencies.py"
SPEC = importlib.util.spec_from_file_location("validate_dependencies", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Unable to load {MODULE_PATH}")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def frontmatter(
    artifact_id: str,
    *,
    status: str = "DRAFT",
    phase: int = 0,
    dependencies: tuple[str, ...] = (),
) -> str:
    lines = [
        "---",
        f"artifact_id: {artifact_id}",
        f"status: {status}",
        f"phase: {phase}",
    ]
    if dependencies:
        lines.append("depends_on:")
        for dependency in dependencies:
            lines.extend(
                [
                    f"  - artifact_id: {dependency}",
                    "    path: placeholder.md",
                ]
            )
    else:
        lines.append("depends_on: []")
    lines.extend(["---", "# Test artifact", ""])
    return "\n".join(lines)


class DependencyValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def write_register(self, artifacts: list[dict[str, object]]) -> None:
        import yaml

        payload = {
            "register": {"artifact_id": "CTRL-CORE-004"},
            "artifacts": artifacts,
        }
        (self.root / "ARTIFACT-REGISTER.yaml").write_text(
            yaml.safe_dump(payload, sort_keys=False),
            encoding="utf-8",
        )

    @staticmethod
    def artifact(
        artifact_id: str,
        path: str,
        *,
        status: str = "DRAFT",
        dependencies: tuple[str, ...] = (),
    ) -> dict[str, object]:
        return {
            "artifact_id": artifact_id,
            "path": path,
            "type": "STD",
            "domain": "CORE",
            "phase": 0,
            "status": status,
            "minimum_status_to_unblock": "APPROVED",
            "depends_on": list(dependencies),
            "blocks": [],
        }

    def write_markdown(
        self,
        path: str,
        artifact_id: str,
        *,
        status: str = "DRAFT",
        dependencies: tuple[str, ...] = (),
    ) -> None:
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            frontmatter(
                artifact_id,
                status=status,
                dependencies=dependencies,
            ),
            encoding="utf-8",
        )

    def messages(self) -> list[str]:
        return [
            finding.message
            for finding in MODULE.validate_repository(self.root)
        ]

    def test_valid_repository_passes(self) -> None:
        artifacts = [
            self.artifact("CTRL-CORE-001", "a.md"),
            self.artifact(
                "STD-CORE-001",
                "b.md",
                dependencies=("CTRL-CORE-001",),
            ),
        ]
        self.write_register(artifacts)
        self.write_markdown("a.md", "CTRL-CORE-001")
        self.write_markdown(
            "b.md",
            "STD-CORE-001",
            dependencies=("CTRL-CORE-001",),
        )

        self.assertEqual([], self.messages())

    def test_missing_registered_path_fails(self) -> None:
        self.write_register([self.artifact("CTRL-CORE-001", "missing.md")])

        self.assertTrue(
            any("path does not exist" in message for message in self.messages())
        )

    def test_duplicate_id_fails(self) -> None:
        self.write_register(
            [
                self.artifact("CTRL-CORE-001", "a.md"),
                self.artifact("CTRL-CORE-001", "b.md"),
            ]
        )
        self.write_markdown("a.md", "CTRL-CORE-001")
        self.write_markdown("b.md", "CTRL-CORE-001")

        self.assertTrue(
            any("duplicate artifact_id" in message for message in self.messages())
        )

    def test_unregistered_dependency_fails(self) -> None:
        self.write_register(
            [
                self.artifact(
                    "STD-CORE-001",
                    "a.md",
                    dependencies=("MISSING-001",),
                )
            ]
        )
        self.write_markdown(
            "a.md",
            "STD-CORE-001",
            dependencies=("MISSING-001",),
        )

        self.assertTrue(
            any("unregistered artifact" in message for message in self.messages())
        )

    def test_dependency_cycle_fails(self) -> None:
        self.write_register(
            [
                self.artifact(
                    "STD-CORE-001",
                    "a.md",
                    dependencies=("STD-CORE-002",),
                ),
                self.artifact(
                    "STD-CORE-002",
                    "b.md",
                    dependencies=("STD-CORE-001",),
                ),
            ]
        )
        self.write_markdown(
            "a.md",
            "STD-CORE-001",
            dependencies=("STD-CORE-002",),
        )
        self.write_markdown(
            "b.md",
            "STD-CORE-002",
            dependencies=("STD-CORE-001",),
        )

        self.assertTrue(
            any("dependency cycle detected" in message for message in self.messages())
        )

    def test_frontmatter_mismatch_fails(self) -> None:
        self.write_register([self.artifact("STD-CORE-001", "a.md")])
        self.write_markdown("a.md", "STD-CORE-999")

        self.assertTrue(
            any("does not match register" in message for message in self.messages())
        )

    def test_approved_artifact_requires_approved_dependency(self) -> None:
        self.write_register(
            [
                self.artifact("CTRL-CORE-001", "a.md", status="DRAFT"),
                self.artifact(
                    "STD-CORE-001",
                    "b.md",
                    status="APPROVED",
                    dependencies=("CTRL-CORE-001",),
                ),
            ]
        )
        self.write_markdown("a.md", "CTRL-CORE-001", status="DRAFT")
        self.write_markdown(
            "b.md",
            "STD-CORE-001",
            status="APPROVED",
            dependencies=("CTRL-CORE-001",),
        )

        self.assertTrue(
            any("is APPROVED but dependency" in message for message in self.messages())
        )


if __name__ == "__main__":
    unittest.main()
