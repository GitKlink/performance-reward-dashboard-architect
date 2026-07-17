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
content_version: 0.2.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Repository scripts

## Purpose

This directory contains deterministic validation and generation utilities for repository governance. Scripts enforce approved standards; they do not silently invent, reinterpret, or rewrite policy.

## Development environment

Use Python 3.11 or later.

```bash
python3 -m pip install -r requirements-dev.txt
```

Run the full test suite:

```bash
python3 -m unittest discover -s tests -p "test_*.py"
```

## Script contract

Every active script must define:

- authoritative inputs;
- supported runtime;
- command-line arguments;
- read and write behaviour;
- exit codes;
- deterministic validation rules;
- actionable findings;
- tests and fixtures;
- limitations and non-goals.

Scripts default to read-only behaviour unless mutation is explicitly documented and approved.

## Exit codes

| Code | Meaning |
|---:|---|
| `0` | Validation completed successfully |
| `1` | Validation failed or required input was invalid |
| `2` | Warnings were promoted to errors |
| `3` | Environment or dependency failure |

## Active scripts

### `validate-dependencies.py`

Validates:

- artifact-ID and path uniqueness;
- registered-file existence;
- required register fields;
- lifecycle statuses;
- dependency references and cycles;
- frontmatter/register agreement;
- dependency maturity for `IN REVIEW` and `APPROVED` artifacts.

```bash
python3 scripts/validate-dependencies.py
```

The validator accepts canonical dependency objects and temporarily recognises legacy Phase 0 forms with warnings.

### `validate-source-register.py`

Validates:

- required source-record fields;
- source-ID and URL uniqueness;
- source quality and lifecycle enums;
- publication, update, and retrieval dates;
- current-product freshness warnings;
- relevant-artifact references;
- central source IDs cited by research-register Markdown files.

```bash
python3 scripts/validate-source-register.py
```

### `check-internal-links.py`

Validates repository-local Markdown and MDC links while ignoring external URLs, anchor-only links, and fenced-code examples.

```bash
python3 scripts/check-internal-links.py
```

## Planned scripts

### `validate-skill-frontmatter.py`

Blocked by the skill-authoring standard and current Cursor schema verification.

### `validate-schemas.py`

Blocked by Phase 2 schema design.

### `generate-status-index.py`

Will generate a human-readable index from `ARTIFACT-REGISTER.yaml`. Generated output must never become a competing source of truth.

## Continuous integration

`.github/workflows/repository-validation.yml` runs:

1. development-dependency installation;
2. all unit tests;
3. artifact dependency validation;
4. source-register validation;
5. internal-link validation.

The workflow currently runs for pushes to `main` and `scaffold/repository-foundation` and for pull requests targeting `main`.

## Test coverage

Current tests cover:

- valid and invalid artifact graphs;
- missing paths, duplicate IDs, unresolved dependencies, and cycles;
- frontmatter/register mismatch and approval maturity;
- valid, external, anchor, fenced-code, root-relative, and missing Markdown links;
- valid and duplicate source records;
- invalid evidence levels;
- unknown artifact and central source references;
- legacy descriptive source-to-artifact references.

## Safety rules

- Use safe YAML loading.
- Never execute repository content as code.
- Do not follow external links during core validation.
- Do not mutate authoritative files during validation.
- Do not refresh dates automatically.
- Do not expose credentials, environment variables, or private paths.
- Return all detectable findings in one run where practical.

## Acceptance criteria

This artifact can move to `IN REVIEW` when:

- all active scripts and the workflow are registered;
- all tests and branch-wide validators pass;
- remaining legacy metadata is either migrated or explicitly accepted for the review period;
- validator outputs are suitable for future required status checks;
- independent review confirms that scripts enforce rather than redefine the standards.
