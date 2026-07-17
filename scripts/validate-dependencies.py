#!/usr/bin/env python3
"""Validate artifact IDs, paths, dependencies, statuses, and frontmatter.

Requires PyYAML. Run from the repository root:

    python scripts/validate-dependencies.py
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment failure
    raise SystemExit(
        "PyYAML is required. Install development dependencies with "
        "`python -m pip install -r requirements-dev.txt`."
    ) from exc


STATUS_ORDER = {
    "PLACEHOLDER": 0,
    "RESEARCH IN PROGRESS": 1,
    "DRAFT": 2,
    "IN REVIEW": 3,
    "APPROVED": 4,
    "SUPERSEDED": -1,
}

REQUIRED_REGISTER_FIELDS = {
    "artifact_id",
    "path",
    "type",
    "domain",
    "phase",
    "status",
    "depends_on",
    "blocks",
}


@dataclass(frozen=True)
class Finding:
    """One validation result."""

    level: str
    message: str

    def render(self) -> str:
        return f"{self.level}: {self.message}"


def load_yaml(path: Path) -> Any:
    """Safely load one YAML file."""

    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise
    except yaml.YAMLError as exc:
        raise ValueError(f"invalid YAML in {path}: {exc}") from exc


def parse_frontmatter(path: Path) -> dict[str, Any] | None:
    """Return YAML frontmatter for Markdown or MDC files, when present."""

    if path.suffix.lower() not in {".md", ".mdc"}:
        return None

    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None

    try:
        closing_index = next(
            index
            for index, line in enumerate(lines[1:], start=1)
            if line.strip() == "---"
        )
    except StopIteration as exc:
        raise ValueError(f"unterminated YAML frontmatter in {path}") from exc

    raw = "\n".join(lines[1:closing_index])
    try:
        parsed = yaml.safe_load(raw) or {}
    except yaml.YAMLError as exc:
        raise ValueError(f"invalid YAML frontmatter in {path}: {exc}") from exc

    if not isinstance(parsed, dict):
        raise ValueError(f"frontmatter in {path} must be a mapping")
    return parsed


def dependency_id(value: Any) -> str:
    """Return an artifact ID from canonical or legacy dependency syntax."""

    if isinstance(value, str):
        return value.split(":", 1)[0].strip()

    if isinstance(value, dict):
        if "artifact_id" in value:
            result = value["artifact_id"]
            if not isinstance(result, str):
                raise ValueError(f"dependency artifact_id must be a string: {value!r}")
            return result.strip()

        # Legacy YAML from `- ID: path` parses as a single-key mapping.
        if len(value) == 1:
            key = next(iter(value))
            if isinstance(key, str):
                return key.strip()

    raise ValueError(f"unsupported dependency declaration: {value!r}")


def iter_dependency_ids(values: Any) -> Iterable[str]:
    """Yield dependency IDs from a YAML list."""

    if values is None:
        return ()
    if not isinstance(values, list):
        raise ValueError("depends_on must be a YAML list")
    return tuple(dependency_id(value) for value in values)


def find_cycles(graph: dict[str, tuple[str, ...]]) -> list[list[str]]:
    """Return dependency cycles using depth-first search."""

    cycles: list[list[str]] = []
    state: dict[str, int] = {}
    stack: list[str] = []

    def visit(node: str) -> None:
        marker = state.get(node, 0)
        if marker == 1:
            start = stack.index(node)
            cycles.append(stack[start:] + [node])
            return
        if marker == 2:
            return

        state[node] = 1
        stack.append(node)
        for dependency in graph.get(node, ()):
            if dependency in graph:
                visit(dependency)
        stack.pop()
        state[node] = 2

    for node in graph:
        if state.get(node, 0) == 0:
            visit(node)
    return cycles


def validate_repository(root: Path) -> list[Finding]:
    """Validate the repository and return every detected finding."""

    findings: list[Finding] = []
    register_path = root / "ARTIFACT-REGISTER.yaml"

    if not register_path.exists():
        return [Finding("ERROR", "ARTIFACT-REGISTER.yaml does not exist")]

    try:
        payload = load_yaml(register_path)
    except (ValueError, FileNotFoundError) as exc:
        return [Finding("ERROR", str(exc))]

    if not isinstance(payload, dict) or not isinstance(payload.get("artifacts"), list):
        return [Finding("ERROR", "artifact register must contain an `artifacts` list")]

    artifacts = payload["artifacts"]
    by_id: dict[str, dict[str, Any]] = {}
    by_path: dict[str, str] = {}
    graph: dict[str, tuple[str, ...]] = {}

    for index, artifact in enumerate(artifacts, start=1):
        prefix = f"artifact entry {index}"
        if not isinstance(artifact, dict):
            findings.append(Finding("ERROR", f"{prefix} must be a mapping"))
            continue

        missing = sorted(REQUIRED_REGISTER_FIELDS - artifact.keys())
        if missing:
            findings.append(
                Finding("ERROR", f"{prefix} missing fields: {', '.join(missing)}")
            )
            continue

        artifact_id = artifact["artifact_id"]
        path_value = artifact["path"]
        status = artifact["status"]

        if not isinstance(artifact_id, str) or not artifact_id:
            findings.append(Finding("ERROR", f"{prefix} has invalid artifact_id"))
            continue
        if artifact_id in by_id:
            findings.append(Finding("ERROR", f"duplicate artifact_id {artifact_id}"))
        else:
            by_id[artifact_id] = artifact

        if not isinstance(path_value, str) or not path_value:
            findings.append(Finding("ERROR", f"{artifact_id} has invalid path"))
            continue
        if path_value in by_path:
            findings.append(
                Finding(
                    "ERROR",
                    f"duplicate path {path_value} for {artifact_id} and {by_path[path_value]}",
                )
            )
        else:
            by_path[path_value] = artifact_id

        if status not in STATUS_ORDER:
            findings.append(
                Finding("ERROR", f"{artifact_id} has unsupported status {status!r}")
            )

        try:
            graph[artifact_id] = tuple(iter_dependency_ids(artifact["depends_on"]))
        except ValueError as exc:
            findings.append(Finding("ERROR", f"{artifact_id}: {exc}"))
            graph[artifact_id] = ()

    for artifact_id, artifact in by_id.items():
        path_value = artifact["path"]
        artifact_path = root / path_value
        if not artifact_path.exists():
            findings.append(
                Finding("ERROR", f"{artifact_id} path does not exist: {path_value}")
            )
            continue
        if not artifact_path.is_file():
            findings.append(
                Finding("ERROR", f"{artifact_id} path is not a file: {path_value}")
            )
            continue

        try:
            frontmatter = parse_frontmatter(artifact_path)
        except ValueError as exc:
            findings.append(Finding("ERROR", str(exc)))
            continue

        if frontmatter is not None:
            for key in ("artifact_id", "status", "phase"):
                if key not in frontmatter:
                    findings.append(
                        Finding("ERROR", f"{path_value} frontmatter missing {key}")
                    )
                    continue
                if frontmatter[key] != artifact[key]:
                    findings.append(
                        Finding(
                            "ERROR",
                            f"{path_value} {key}={frontmatter[key]!r} "
                            f"does not match register {artifact[key]!r}",
                        )
                    )

            try:
                file_dependencies = tuple(
                    iter_dependency_ids(frontmatter.get("depends_on", []))
                )
            except ValueError as exc:
                findings.append(Finding("ERROR", f"{path_value}: {exc}"))
            else:
                register_dependencies = graph.get(artifact_id, ())
                if file_dependencies != register_dependencies:
                    findings.append(
                        Finding(
                            "ERROR",
                            f"{path_value} depends_on {file_dependencies!r} "
                            f"does not match register {register_dependencies!r}",
                        )
                    )

    for artifact_id, dependencies in graph.items():
        for dependency in dependencies:
            if dependency not in by_id:
                findings.append(
                    Finding(
                        "ERROR",
                        f"{artifact_id} depends on unregistered artifact {dependency}",
                    )
                )

    for cycle in find_cycles(graph):
        findings.append(
            Finding("ERROR", "dependency cycle detected: " + " -> ".join(cycle))
        )

    for artifact_id, artifact in by_id.items():
        status = artifact["status"]
        if status not in {"IN REVIEW", "APPROVED"}:
            continue

        required_rank = (
            STATUS_ORDER["DRAFT"]
            if status == "IN REVIEW"
            else STATUS_ORDER["APPROVED"]
        )
        for dependency in graph.get(artifact_id, ()):
            dependency_artifact = by_id.get(dependency)
            if dependency_artifact is None:
                continue
            dependency_status = dependency_artifact["status"]
            dependency_rank = STATUS_ORDER.get(dependency_status, -1)
            if dependency_rank < required_rank:
                findings.append(
                    Finding(
                        "ERROR",
                        f"{artifact_id} is {status} but dependency {dependency} "
                        f"is only {dependency_status}",
                    )
                )

    return findings


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="repository root containing ARTIFACT-REGISTER.yaml",
    )
    parser.add_argument(
        "--warnings-as-errors",
        action="store_true",
        help="return a non-zero exit code when warnings are present",
    )
    return parser


def main() -> int:
    """Run validation and return a process exit code."""

    args = build_parser().parse_args()
    findings = validate_repository(args.root.resolve())

    errors = [item for item in findings if item.level == "ERROR"]
    warnings = [item for item in findings if item.level == "WARNING"]

    for finding in findings:
        print(finding.render())

    if errors:
        print(f"\nValidation failed with {len(errors)} error(s).")
        return 1
    if warnings and args.warnings_as_errors:
        print(f"\nValidation failed with {len(warnings)} warning(s).")
        return 2

    print(
        f"Validation passed with {len(warnings)} warning(s)."
        if warnings
        else "Validation passed."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
