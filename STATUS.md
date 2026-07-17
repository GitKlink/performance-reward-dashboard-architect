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
content_version: 0.4.0
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

Phase 0 repository governance and validation are in progress.

The complete initial scaffold has been created. The first three substantive standards exist as drafts:

- `STD-CORE-001` — naming standard;
- `STD-CORE-002` — research standard;
- `STD-CORE-003` — citation standard.

The initial artifact register and central research register exist. All five representative standards trials required for Phase 0 have now been completed:

- `EX-CORE-001` — current Cursor rules and skills evidence;
- `EX-FIXED-001` — new-hire premium KPI definition;
- `EX-CONSULT-001` — consulting-firm technique attribution;
- `EX-VIZ-001` — stable graphical-perception research;
- `EX-CORE-002` — internal source-of-truth decision.

A first dependency validator and seven unit tests have also been implemented. The test suite covers a valid repository, missing paths, duplicate IDs, unresolved dependencies, dependency cycles, frontmatter mismatches, and invalid approval maturity.

The standards remain `DRAFT` pending full branch validation, active-metadata reconciliation, and independent review.

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
| 0 | Repository controls | DRAFT | Core standards, five trials, source register, and initial validator completed |
| 1 | Architecture and standards | PLACEHOLDER | Blocked by Phase 0 validation and review |
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
| 12 | Evaluation and validation | PLACEHOLDER | Initial repository validator started early as a Phase 0 control |
| 13 | Integration and release | PLACEHOLDER | Not started |

## Scaffold inventory

The branch contains the planned repository locations for:

- repository controls and project files;
- four safe, non-applying Cursor rule placeholders;
- three non-operational Cursor subagent placeholders;
- forty-nine Cursor skill placeholders across nine capability groups;
- architecture, standards, and planning artifacts;
- audience, P&R, consulting, visual-design, visualisation, and Power BI knowledge packs;
- eight output schemas and nine output templates;
- audience and format examples;
- five benchmark scenarios with expected-result locations;
- validation and generation scripts.

## Completed Phase 0 work

1. Assigned immutable IDs to repository controls and active Phase 0/1 artifacts.
2. Defined dependency types, status semantics, source-of-truth rules, and change-impact handling.
3. Defined the central research-register structure.
4. Added reusable source records for Cursor, P&R, consulting, graphical-perception, and IBCS research.
5. Completed all five representative standards trials.
6. Recorded the required rename from `holistic-pr-value-drivers` to `holistic-performance-reward-value-drivers` before Phase 4.
7. Defined validation-script contracts and development dependencies.
8. Implemented the initial dependency validator.
9. Added seven passing unit-test scenarios for the validator in an isolated local test fixture.

## Phase 0 work remaining

1. Add the newest trials and validation artifacts to `ARTIFACT-REGISTER.yaml`.
2. Reconcile active file frontmatter with the canonical dependency-object format.
3. Run the dependency validator against the complete branch and resolve all findings.
4. Add source-register validation and internal-link validation design.
5. Conduct independent review of `STD-CORE-001` to `STD-CORE-003` and the five trials.
6. Resolve review findings and move eligible controls to `IN REVIEW`.
7. Merge the scaffold and governance pull request when the review gate is satisfied.

## Immediate next action

Complete artifact-register reconciliation and run the dependency validator against the full branch before beginning substantive Phase 1 architecture work.
