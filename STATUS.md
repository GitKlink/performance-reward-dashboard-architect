---
artifact_id: CTRL-CORE-003
status: DRAFT
phase: 0
priority: critical
depends_on:
  - artifact_id: CTRL-CORE-001
    path: BUILD-ORDER.md
  - artifact_id: CTRL-CORE-002
    path: DEPENDENCIES.md
blocks:
  - release decisions
content_version: 0.6.0
last_reviewed: 2026-07-17
next_review: 2026-07-24
---

# Repository status

This is the authoritative high-level completion register.

## Current milestone

`v0.1 — Cursor Agent Foundation`

## Current branch

```text
scaffold/repository-foundation
```

## Current activity

Phase 0 repository governance is ready for independent content review after automated validation.

The complete initial scaffold has been created. The first three substantive standards exist as drafts:

- `STD-CORE-001` — naming standard;
- `STD-CORE-002` — research standard;
- `STD-CORE-003` — citation standard.

The artifact register and central research register exist. All five representative standards trials required for Phase 0 have been completed:

- `EX-CORE-001` — current Cursor rules and skills evidence;
- `EX-FIXED-001` — new-hire premium KPI definition;
- `EX-CONSULT-001` — consulting-firm technique attribution;
- `EX-VIZ-001` — stable graphical-perception research;
- `EX-CORE-002` — internal source-of-truth decision.

The branch now includes:

- artifact dependency validation;
- source-register validation;
- internal-link validation;
- 18 unit-test scenarios;
- a GitHub Actions workflow running the complete validation suite.

The latest workflow run passed all tests and validators.

The standards remain `DRAFT` pending canonical metadata migration and independent review under GitHub issue #2.

## Important current-product finding

IBCS Version 2.0 was released on 2026-06-11 and changed the prior conceptual, perceptual, and semantic chapter structure into Notation and Composition aligned with ISO 24896. Existing scaffold references to IBCS 1.2 or the previous structure must be reviewed before the IBCS knowledge pack is authored.

## Status definitions

| Status | Meaning |
|---|---|
| `PLACEHOLDER` | Scope and instructions exist; substantive content does not |
| `RESEARCH IN PROGRESS` | Evidence gathering has started |
| `DRAFT` | Substantive content exists but has not passed review |
| `IN REVIEW` | Acceptance criteria are being assessed |
| `APPROVED` | Authoritative and available to dependent artifacts |
| `SUPERSEDED` | Replaced by a named authoritative artifact |

## Phase summary

| Phase | Name | Status | Current result |
|---:|---|---|---|
| 0 | Repository controls | DRAFT | Core standards, five trials, reconciled register, 18 tests, three validators, and successful CI |
| 1 | Architecture and standards | PLACEHOLDER | Artifact-specific placeholders complete; blocked by Phase 0 review |
| 2 | Schemas and templates | PLACEHOLDER | Blocked by Phase 1 and approved standards |
| 3 | Audience and decision foundation | PLACEHOLDER | Not started |
| 4 | Holistic P&R foundation | PLACEHOLDER | Not started |
| 5 | Specialist P&R domains | PLACEHOLDER | Not started |
| 6 | Consulting communication | PLACEHOLDER | Not started |
| 7 | Visual-design foundation | PLACEHOLDER | Not started |
| 8 | Visualisation patterns | PLACEHOLDER | Not started |
| 9 | Dashboard experience | PLACEHOLDER | Not started |
| 10 | Power BI implementation | PLACEHOLDER | Not started |
| 11 | Orchestrator and subagents | PLACEHOLDER | Not started |
| 12 | Evaluation and validation | PLACEHOLDER | Repository validation foundation implemented early as a Phase 0 control |
| 13 | Integration and release | PLACEHOLDER | Not started |

## Completed Phase 0 work

1. Assigned immutable IDs to repository controls and active Phase 0/1 artifacts.
2. Defined dependency types, status semantics, source-of-truth rules, and change-impact handling.
3. Defined the central research-register structure.
4. Added reusable source records for Cursor, P&R, consulting, graphical-perception, and IBCS research.
5. Completed all five representative standards trials.
6. Recorded the required rename from `holistic-pr-value-drivers` to `holistic-performance-reward-value-drivers` before Phase 4.
7. Defined validation-script contracts and development dependencies.
8. Implemented the dependency validator and seven unit tests.
9. Reconciled Phase 0 and Phase 1 artifacts in `ARTIFACT-REGISTER.yaml`.
10. Replaced generic Phase 1 placeholders with artifact-specific instructions and canonical metadata.
11. Implemented internal-link validation and five tests.
12. Implemented source-register validation and six tests.
13. Added a GitHub Actions workflow running all tests and validators.
14. Passed the complete automated validation suite.
15. Opened issue #2 for the required independent review.

## Phase 0 work remaining

1. Register the validation workflow and newly activated validators in `ARTIFACT-REGISTER.yaml`.
2. Migrate remaining active Phase 0 files from accepted legacy dependency syntax to canonical dependency objects.
3. Complete independent review under issue #2.
4. Resolve critical and major review findings.
5. Move eligible controls to `IN REVIEW`.
6. Merge pull request #1 when the review gate is satisfied.

## Immediate next action

Complete the Phase 0 independent review and resolve its findings before beginning substantive Phase 1 architecture work.
