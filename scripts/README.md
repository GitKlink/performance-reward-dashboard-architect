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
content_version: 0.3.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Repository scripts

## Purpose

This directory contains deterministic validation and generation utilities. Scripts enforce documented repository policy; they do not silently invent, reinterpret, or rewrite it.

## Development environment

Use Python 3.11 or later.

```bash
python3 -m pip install -r requirements-dev.txt
```

Run all tests:

```bash
python3 -m unittest discover -s tests -p "test_*.py"
```

## Script contract

Every active script defines:

- authoritative inputs;
- supported runtime;
- command-line arguments;
- read and write behaviour;
- exit codes;
- deterministic validation rules;
- actionable findings;
- tests and fixtures;
- limitations and non-goals.

Validation scripts are read-only.

## Exit codes

| Code | Meaning |
|---:|---|
| `0` | Validation passed |
| `1` | Validation or input failed |
| `2` | Warnings were promoted to failures |
| `3` | Environment or dependency failure |

## Active validators

### `validate-dependencies.py`

Checks:

- artifact-ID and path uniqueness;
- registered-file existence;
- required register fields;
- lifecycle statuses;
- dependency references and cycles;
- frontmatter/register agreement;
- approval maturity.

```bash
python3 scripts/validate-dependencies.py --warnings-as-errors
```

### `validate-source-register.py`

Checks:

- required source fields;
- source-ID and URL uniqueness;
- evidence and lifecycle enums;
- publication, update, and retrieval dates;
- current-product freshness;
- artifact references;
- central source IDs used in research records.

```bash
python3 scripts/validate-source-register.py --warnings-as-errors
```

### `validate-schemas.py`

Checks every `schemas/*.schema.yaml` file for:

- valid YAML;
- JSON Schema Draft 2020-12 structure;
- stable `$id` and repository artifact metadata;
- filename and schema-subject agreement;
- required fields declared in `properties`;
- duplicate schema and artifact IDs;
- optional valid and invalid fixture behaviour.

```bash
python3 scripts/validate-schemas.py --warnings-as-errors
```

Fixture naming:

```text
schemas/examples/<subject>.valid.yaml
schemas/examples/<subject>.invalid.yaml
```

### `check-internal-links.py`

Checks repository-local Markdown and MDC links while ignoring external URLs, anchor-only links, and fenced-code examples.

```bash
python3 scripts/check-internal-links.py
```

## Planned scripts

### `validate-skill-frontmatter.py`

Next after current Cursor skill metadata is verified and the first foundational skills enter activation testing.

### Template-to-schema validation

Will verify template schema declarations, versions, required-field mappings, and duplicate template IDs.

### `generate-status-index.py`

Will generate a human-readable index from `ARTIFACT-REGISTER.yaml`. Generated output cannot become a competing authority.

### Release validation

Later validators will check package dependency closure, status eligibility, manifests, hashes, placeholder exclusion, and reproducibility.

## Continuous integration

`.github/workflows/repository-validation.yml` runs:

1. dependency installation;
2. all unit tests;
3. artifact dependency validation with warnings as failures;
4. source-register validation with warnings as failures;
5. JSON Schema validation with warnings as failures;
6. internal-link validation.

The workflow runs for pushes to `main` and `scaffold/repository-foundation` and for pull requests targeting `main`.

## Current test coverage

The suite currently contains **25 test scenarios**:

- 7 dependency-validator scenarios;
- 5 internal-link scenarios;
- 6 source-register scenarios;
- 7 JSON Schema scenarios.

Coverage includes:

- valid and invalid artifact graphs;
- missing paths, duplicate IDs, unresolved dependencies, and cycles;
- frontmatter/register mismatch and approval maturity;
- local, external, anchor, fenced-code, root-relative, and missing Markdown links;
- valid and duplicate source records;
- invalid evidence levels and unknown references;
- valid and invalid JSON Schemas;
- duplicate schema IDs;
- valid and invalid schema fixtures.

## Safety rules

- Use safe YAML loading.
- Never execute repository content as code.
- Do not follow external links during core validation.
- Do not mutate authoritative artifacts during validation.
- Do not refresh evidence dates automatically.
- Do not expose credentials, environment variables, or private paths.
- Return all detectable findings in one run where practical.
- Do not turn subjective design preferences into deterministic failures.

## Acceptance criteria

This script set is development-ready when:

- all active validators have tests;
- CI is green;
- warnings that indicate metadata drift fail CI;
- validators enforce documented standards;
- new schema and skill validators are added as those artifact classes become active.

Release approval additionally requires package, compatibility, privacy, security, and integrated evaluation checks defined in the release architecture.
