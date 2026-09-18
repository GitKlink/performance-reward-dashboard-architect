#!/usr/bin/env python3
"""Validate artifact IDs, paths, dependencies, statuses, and frontmatter.

Run from the repository root:

    python scripts/validate-dependencies.py

The validator is read-only. It accepts the canonical dependency-object format and
legacy Phase 0 string forms while those files are being migrated.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "PyYAML is required. Run `python -m pip install -r requirements-dev.txt`."
    ) from exc


STATUS_ORDER = {
    "PLACEHOLDER": 0,
    "RESEARCH IN PROGRESS": 1,
    "DRAFT": 2,
    "IN REVIEW": 3,
    "APPROVED": 4,
    "SUPERSEDED": -1,
}
ARTIFACT_ID_PATTERN = re.compile(r"^[A-Z]+-[A-Z]+-[0-9]{3}$")
REQUIRED_FIELDS = {
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
    level: str
    message: str

    def render(self) -> str:
        return f"{self.level}: {self.message}"


def load_yaml(path: Path) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise ValueError(f"invalid YAML in {path}: {exc}") from exc


def parse_frontmatter(path: Path) -> dict[str, Any] | None:
    if path.suffix.lower() not in {".md", ".mdc"}:
        return None

    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return None

    try:
        closing = next(
            index
            for index, line in enumerate(lines[1:], start=1)
            if line.strip() == "---"
        )
    except StopIteration as exc:
        raise ValueError(f"unterminated YAML frontmatter in {path}") from exc

    try:
        parsed = yaml.safe_load("\n".join(lines[1:closing])) or {}
    except yaml.YAMLError as exc:
        raise ValueError(f"invalid YAML frontmatter in {path}: {exc}") from exc

    if not isinstance(parsed, dict):
        raise ValueError(f"frontmatter in {path} must be a mapping")
    return parsed


def normalise_path(value: str) -> str:
    """Normalise a repository-relative POSIX path without touching the file system."""

    parts: list[str] = []
    for part in PurePosixPath(value).parts:
        if part in {"", "."}:
            continue
        if part == "..":
            if parts:
                parts.pop()
            continue
        parts.append(part)
    return "/".join(parts)


def resolve_dependency(
    value: Any,
    *,
    by_id: dict[str, dict[str, Any]],
    by_path: dict[str, str],
) -> tuple[str, bool]:
    """Return ``(artifact_id, used_legacy_syntax)`` for one declaration."""

    if isinstance(value, dict):
        if "artifact_id" in value:
            artifact_id = value["artifact_id"]
            if not isinstance(artifact_id, str) or not artifact_id.strip():
                raise ValueError(f"invalid dependency artifact_id: {value!r}")
            return artifact_id.strip(), False

        # Legacy `- ARTIFACT-ID: path` YAML form.
        if len(value) == 1:
            key, path_value = next(iter(value.items()))
            if isinstance(key, str) and key in by_id:
                return key, True
            if isinstance(path_value, str):
                resolved = by_path.get(normalise_path(path_value))
                if resolved:
                    return resolved, True

    if isinstance(value, str):
        candidate = value.split(":", 1)[0].strip()
        if candidate in by_id:
            return candidate, candidate != value.strip()

        resolved = by_path.get(normalise_path(value.strip()))
        if resolved:
            return resolved, True

        return candidate, True

    raise ValueError(f"unsupported dependency declaration: {value!r}")


def resolve_dependencies(
    values: Any,
    *,
    by_id: dict[str, dict[str, Any]],
    by_path: dict[str, str],
) -> tuple[tuple[str, ...], bool]:
    if values is None:
        return (), False
    if not isinstance(values, list):
        raise ValueError("depends_on must be a YAML list")

    resolved: list[str] = []
    used_legacy = False
    for value in values:
        artifact_id, legacy = resolve_dependency(
            value,
            by_id=by_id,
            by_path=by_path,
        )
        resolved.append(artifact_id)
        used_legacy = used_legacy or legacy
    return tuple(resolved), used_legacy


def find_cycles(graph: dict[str, tuple[str, ...]]) -> list[list[str]]:
    cycles: list[list[str]] = []
    state: dict[str, int] = {}
    stack: list[str] = []

    def visit(node: str) -> None:
        marker = state.get(node, 0)
        if marker == 1:
            start = stack.index(node)
            cycle = stack[start:] + [node]
            if cycle not in cycles:
                cycles.append(cycle)
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
    findings: list[Finding] = []
    register_path = root / "ARTIFACT-REGISTER.yaml"
    if not register_path.exists():
        return [Finding("ERROR", "ARTIFACT-REGISTER.yaml does not exist")]

    try:
        payload = load_yaml(register_path)
    except ValueError as exc:
        return [Finding("ERROR", str(exc))]

    artifacts = payload.get("artifacts") if isinstance(payload, dict) else None
    if not isinstance(artifacts, list):
        return [Finding("ERROR", "artifact register must contain an `artifacts` list")]

    by_id: dict[str, dict[str, Any]] = {}
    by_path: dict[str, str] = {}

    for index, artifact in enumerate(artifacts, start=1):
        prefix = f"artifact entry {index}"
        if not isinstance(artifact, dict):
            findings.append(Finding("ERROR", f"{prefix} must be a mapping"))
            continue

        missing = sorted(REQUIRED_FIELDS - artifact.keys())
        if missing:
            findings.append(
                Finding("ERROR", f"{prefix} missing fields: {', '.join(missing)}")
            )
            continue

        artifact_id = artifact["artifact_id"]
        path_value = artifact["path"]
        status = artifact["status"]

        if not isinstance(artifact_id, str) or not ARTIFACT_ID_PATTERN.fullmatch(
            artifact_id
        ):
            findings.append(Finding("ERROR", f"{prefix} has invalid artifact_id"))
            continue
        if artifact_id in by_id:
            findings.append(Finding("ERROR", f"duplicate artifact_id {artifact_id}"))
        else:
            by_id[artifact_id] = artifact

        if not isinstance(path_value, str) or not path_value.strip():
            findings.append(Finding("ERROR", f"{artifact_id} has invalid path"))
            continue
        canonical_path = normalise_path(path_value)
        if canonical_path != path_value:
            findings.append(
                Finding(
                    "ERROR",
                    f"{artifact_id} path is not canonical: {path_value!r}",
                )
            )
        if canonical_path in by_path:
            findings.append(
                Finding(
                    "ERROR",
                    f"duplicate path {canonical_path} for {artifact_id} and "
                    f"{by_path[canonical_path]}",
                )
            )
        else:
            by_path[canonical_path] = artifact_id

        if status not in STATUS_ORDER:
            findings.append(
                Finding("ERROR", f"{artifact_id} has unsupported status {status!r}")
            )

    graph: dict[str, tuple[str, ...]] = {}
    for artifact_id, artifact in by_id.items():
        try:
            dependencies, legacy = resolve_dependencies(
                artifact["depends_on"],
                by_id=by_id,
                by_path=by_path,
            )
        except ValueError as exc:
            findings.append(Finding("ERROR", f"{artifact_id}: {exc}"))
            dependencies = ()
            legacy = False
        graph[artifact_id] = dependencies
        if legacy:
            findings.append(
                Finding(
                    "WARNING",
                    f"{artifact_id} uses legacy dependency syntax in the register",
                )
            )

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

        if artifact_path.suffix.lower() in {".md", ".mdc"} and frontmatter is None:
            findings.append(
                Finding("ERROR", f"{path_value} is registered but has no frontmatter")
            )
            continue
        if frontmatter is None:
            continue

        for key in ("artifact_id", "status", "phase"):
            if key not in frontmatter:
                findings.append(
                    Finding("ERROR", f"{path_value} frontmatter missing {key}")
                )
            elif frontmatter[key] != artifact[key]:
                findings.append(
                    Finding(
                        "ERROR",
                        f"{path_value} {key}={frontmatter[key]!r} does not match "
                        f"register {artifact[key]!r}",
                    )
                )

        try:
            file_dependencies, legacy = resolve_dependencies(
                frontmatter.get("depends_on", []),
                by_id=by_id,
                by_path=by_path,
            )
        except ValueError as exc:
            findings.append(Finding("ERROR", f"{path_value}: {exc}"))
            continue

        if legacy:
            findings.append(
                Finding(
                    "WARNING",
                    f"{path_value} uses legacy dependency syntax; migrate to "
                    "dependency objects",
                )
            )

        register_dependencies = graph.get(artifact_id, ())
        if set(file_dependencies) != set(register_dependencies):
            findings.append(
                Finding(
                    "ERROR",
                    f"{path_value} depends_on {file_dependencies!r} does not match "
                    f"register {register_dependencies!r}",
                )
            )
        elif len(file_dependencies) != len(set(file_dependencies)):
            findings.append(
                Finding("ERROR", f"{path_value} contains duplicate dependencies")
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
            if STATUS_ORDER.get(dependency_status, -1) < required_rank:
                findings.append(
                    Finding(
                        "ERROR",
                        f"{artifact_id} is {status} but dependency {dependency} is "
                        f"only {dependency_status}",
                    )
                )

    return findings


def build_parser() -> argparse.ArgumentParser:
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
        help="return exit code 2 when warnings are present",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    findings = validate_repository(args.root.resolve())
    errors = [finding for finding in findings if finding.level == "ERROR"]
    warnings = [finding for finding in findings if finding.level == "WARNING"]

    for finding in findings:
        print(finding.render())

    if errors:
        print(f"\nValidation failed with {len(errors)} error(s).")
        return 1
    if warnings and args.warnings_as_errors:
        print(f"\nValidation failed with {len(warnings)} warning(s).")
        return 2

    if warnings:
        print(f"\nValidation passed with {len(warnings)} warning(s).")
    else:
        print("Validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
