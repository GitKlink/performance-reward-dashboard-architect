#!/usr/bin/env python3
"""Validate repository JSON Schemas written in YAML.

The validator checks JSON Schema Draft 2020-12 structure, repository metadata,
identifier uniqueness, filenames, and optional example fixtures. It is read-only.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "PyYAML is required. Run `python3 -m pip install -r requirements-dev.txt`."
    ) from exc

try:
    from jsonschema import Draft202012Validator, FormatChecker
    from jsonschema.exceptions import SchemaError, ValidationError
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "jsonschema is required. Run `python3 -m pip install -r requirements-dev.txt`."
    ) from exc


SCHEMA_DIALECT = "https://json-schema.org/draft/2020-12/schema"
ALLOWED_STATUSES = {"DRAFT", "IN REVIEW", "APPROVED", "SUPERSEDED"}


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


def schema_files(root: Path) -> list[Path]:
    return sorted((root / "schemas").glob("*.schema.yaml"))


def format_error_path(error: ValidationError) -> str:
    if not error.absolute_path:
        return "$"
    return "$" + "".join(
        f"[{item}]" if isinstance(item, int) else f".{item}"
        for item in error.absolute_path
    )


def validate_schema_file(path: Path, root: Path) -> tuple[list[Finding], dict[str, Any] | None]:
    findings: list[Finding] = []
    relative = path.relative_to(root)

    try:
        schema = load_yaml(path)
    except ValueError as exc:
        return [Finding("ERROR", str(exc))], None

    if not isinstance(schema, dict):
        return [Finding("ERROR", f"{relative} must contain a schema mapping")], None

    if schema.get("$schema") != SCHEMA_DIALECT:
        findings.append(
            Finding(
                "ERROR",
                f"{relative} must declare JSON Schema Draft 2020-12",
            )
        )

    schema_id = schema.get("$id")
    if not isinstance(schema_id, str) or not schema_id.startswith(
        "urn:performance-reward-dashboard-architect:schema:"
    ):
        findings.append(Finding("ERROR", f"{relative} has an invalid or missing $id"))

    if schema.get("type") != "object":
        findings.append(Finding("ERROR", f"{relative} top-level type must be object"))

    if schema.get("additionalProperties") is not False:
        findings.append(
            Finding("ERROR", f"{relative} must set top-level additionalProperties: false")
        )

    repository = schema.get("x-repository")
    if not isinstance(repository, dict):
        findings.append(Finding("ERROR", f"{relative} missing x-repository metadata"))
    else:
        for field in (
            "artifact_id",
            "status",
            "phase",
            "schema_version",
            "content_version",
            "owner",
        ):
            if field not in repository:
                findings.append(
                    Finding("ERROR", f"{relative} x-repository missing {field}")
                )
        status = repository.get("status")
        if status not in ALLOWED_STATUSES:
            findings.append(
                Finding("ERROR", f"{relative} has unsupported schema status {status!r}")
            )
        if repository.get("phase") != 2:
            findings.append(
                Finding("ERROR", f"{relative} x-repository phase must be 2")
            )

    required = schema.get("required")
    properties = schema.get("properties")
    if not isinstance(required, list) or not required:
        findings.append(Finding("ERROR", f"{relative} must define required fields"))
    if not isinstance(properties, dict) or not properties:
        findings.append(Finding("ERROR", f"{relative} must define properties"))
    elif isinstance(required, list):
        undeclared = sorted(set(required) - set(properties))
        if undeclared:
            findings.append(
                Finding(
                    "ERROR",
                    f"{relative} required fields are not declared in properties: "
                    + ", ".join(undeclared),
                )
            )

    expected_subject = path.name.removesuffix(".schema.yaml")
    if isinstance(schema_id, str) and f":{expected_subject}:" not in schema_id:
        findings.append(
            Finding(
                "ERROR",
                f"{relative} $id subject does not match filename {expected_subject!r}",
            )
        )

    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        location = "$" + "".join(f".{item}" for item in exc.absolute_path)
        findings.append(
            Finding(
                "ERROR",
                f"{relative} is not a valid Draft 2020-12 schema at {location}: "
                f"{exc.message}",
            )
        )

    return findings, schema


def validate_example_fixtures(
    root: Path,
    schemas_by_subject: dict[str, dict[str, Any]],
) -> list[Finding]:
    findings: list[Finding] = []
    example_root = root / "schemas" / "examples"
    if not example_root.exists():
        return findings

    for path in sorted(example_root.glob("*.yaml")):
        relative = path.relative_to(root)
        name = path.name
        if ".valid." in name:
            expected_valid = True
            subject = name.split(".valid.", 1)[0]
        elif ".invalid." in name:
            expected_valid = False
            subject = name.split(".invalid.", 1)[0]
        else:
            findings.append(
                Finding(
                    "WARNING",
                    f"{relative} is ignored because its filename is not "
                    "<subject>.valid.yaml or <subject>.invalid.yaml",
                )
            )
            continue

        schema = schemas_by_subject.get(subject)
        if schema is None:
            findings.append(
                Finding("ERROR", f"{relative} has no matching schema for {subject}")
            )
            continue

        try:
            instance = load_yaml(path)
        except ValueError as exc:
            findings.append(Finding("ERROR", str(exc)))
            continue

        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = sorted(validator.iter_errors(instance), key=lambda item: list(item.path))

        if expected_valid and errors:
            for error in errors:
                findings.append(
                    Finding(
                        "ERROR",
                        f"{relative} expected valid but failed at "
                        f"{format_error_path(error)}: {error.message}",
                    )
                )
        elif not expected_valid and not errors:
            findings.append(
                Finding("ERROR", f"{relative} expected invalid but passed validation")
            )

    return findings


def validate_repository(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    paths = schema_files(root)
    if not paths:
        return [Finding("ERROR", "no *.schema.yaml files found under schemas/")]

    ids: dict[str, Path] = {}
    artifact_ids: dict[str, Path] = {}
    schemas_by_subject: dict[str, dict[str, Any]] = {}

    for path in paths:
        file_findings, schema = validate_schema_file(path, root)
        findings.extend(file_findings)
        if schema is None:
            continue

        schema_id = schema.get("$id")
        if isinstance(schema_id, str):
            if schema_id in ids:
                findings.append(
                    Finding(
                        "ERROR",
                        f"duplicate schema $id {schema_id} in "
                        f"{path.relative_to(root)} and {ids[schema_id].relative_to(root)}",
                    )
                )
            else:
                ids[schema_id] = path

        repository = schema.get("x-repository")
        artifact_id = repository.get("artifact_id") if isinstance(repository, dict) else None
        if isinstance(artifact_id, str):
            if artifact_id in artifact_ids:
                findings.append(
                    Finding(
                        "ERROR",
                        f"duplicate schema artifact_id {artifact_id} in "
                        f"{path.relative_to(root)} and "
                        f"{artifact_ids[artifact_id].relative_to(root)}",
                    )
                )
            else:
                artifact_ids[artifact_id] = path

        subject = path.name.removesuffix(".schema.yaml")
        schemas_by_subject[subject] = schema

    findings.extend(validate_example_fixtures(root, schemas_by_subject))
    return findings


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="repository root containing schemas/",
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
        print(f"\nSchema validation failed with {len(errors)} error(s).")
        return 1
    if warnings and args.warnings_as_errors:
        print(f"\nSchema validation failed with {len(warnings)} warning(s).")
        return 2

    if warnings:
        print(f"\nSchema validation passed with {len(warnings)} warning(s).")
    else:
        print(f"Schema validation passed for {len(schema_files(args.root.resolve()))} schema(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
