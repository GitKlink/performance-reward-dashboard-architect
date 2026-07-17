---
artifact_id: SCRIPT-CORE-001
status: DRAFT
phase: 0
priority: high
depends_on:
  - artifact_id: CTRL-CORE-002
    path: ../DEPENDENCIES.md
  - artifact_id: CTRL-CORE-004
    path: ../ARTIFACT-REGISTER.yaml
  - artifact_id: STD-CORE-001
    path: ../docs/standards/naming-standard.md
blocks:
  - repository validation workflow
  - Phase 0 review
content_version: 0.1.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Repository scripts

## Purpose

This directory contains deterministic validation and generation utilities for repository governance. Scripts must enforce approved standards; they must not silently invent or rewrite policy.

## Development environment

Use Python 3.11 or later.

Install development dependencies from the repository root:

```bash
python -m pip install -r requirements-dev.txt
```

Initial dependency:

```text
PyYAML
```

## Script contract

Every active script must define:

- purpose and authoritative inputs;
- supported Python version;
- command-line arguments;
- read and write behaviour;
- exit codes;
- deterministic validation rules;
- actionable error messages;
- tests and fixtures;
- limitations and non-goals.

Scripts must default to read-only behaviour unless generation or mutation is explicitly part of their documented purpose.

## Exit-code convention

| Code | Meaning |
|---:|---|
| `0` | Validation or generation completed successfully |
| `1` | Validation failed or required input was invalid |
| `2` | Warnings were promoted to errors by command-line option |
| `3` | Environment or dependency failure |

A script may use additional codes only when documented in its module docstring and this file.

## Active scripts

### `validate-dependencies.py`

Status: `DRAFT`

Validates:

- uniqueness of artifact IDs and paths;
- existence of registered files;
- required register fields;
- supported status values;
- dependency references;
- dependency cycles;
- agreement between Markdown/MDC frontmatter and `ARTIFACT-REGISTER.yaml`;
- minimum dependency maturity for `IN REVIEW` and `APPROVED` artifacts.

Run:

```bash
python scripts/validate-dependencies.py
```

Specify another repository root:

```bash
python scripts/validate-dependencies.py --root /path/to/repository
```

Promote warnings to errors:

```bash
python scripts/validate-dependencies.py --warnings-as-errors
```

The validator accepts the canonical dependency structure:

```yaml
depends_on:
  - artifact_id: STD-CORE-001
    path: docs/standards/naming-standard.md
```

During Phase 0 migration it also recognises legacy string and one-key mapping forms. New or materially edited artifacts must use the canonical structure.

## Planned scripts

### `validate-skill-frontmatter.py`

Will validate active Cursor skill metadata, folder/name agreement, invocation descriptions, placeholder safety, and required authoring sections. It remains blocked by the skill-authoring standard and current Cursor schema verification.

### `validate-schemas.py`

Will validate repository schemas and template-to-schema alignment. It remains blocked by Phase 2 schema design.

### `check-internal-links.py`

Will validate relative Markdown links, registered paths, source references, and renamed-artifact migrations.

### `generate-status-index.py`

Will generate a human-readable status summary from `ARTIFACT-REGISTER.yaml`. Generated output must never become a competing source of truth.

## Testing

Tests live under:

```text
tests/
```

Run all tests:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

A validation script cannot move to `IN REVIEW` until tests cover:

- a valid repository;
- missing registered path;
- duplicate ID;
- unresolved dependency;
- dependency cycle;
- frontmatter/register mismatch;
- invalid status progression.

## Safety rules

- Never execute arbitrary content from repository files.
- Use safe YAML loading.
- Do not follow external links during core validation.
- Do not mutate source artifacts during validation.
- Do not refresh review dates automatically.
- Do not expose credentials, environment variables, or private paths in normal output.
- Return all detectable errors in one run where practical.

## Acceptance criteria

This artifact can move to `IN REVIEW` when the dependency validator and its tests pass locally and against the active branch, the artifact register includes all active scripts, and output is suitable for future CI use.
