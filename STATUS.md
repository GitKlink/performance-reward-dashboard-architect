---
artifact_id: CTRL-CORE-003
status: DRAFT
phase: 0
priority: critical
depends_on:
  - CTRL-CORE-001: BUILD-ORDER.md
  - CTRL-CORE-002: DEPENDENCIES.md
blocks:
  - release decisions
content_version: 0.3.0
last_reviewed: 2026-07-17
next_review: 2026-07-24
---

# Repository Status

This is the authoritative high-level completion register.

## Current milestone

`v0.1 — Cursor Agent Foundation`

## Current branch

```text
scaffold/repository-foundation
```

## Current activity

Phase 0 repository governance is in progress.

The complete initial scaffold has been created. The first three substantive standards exist as drafts:

- `STD-CORE-001` — naming standard;
- `STD-CORE-002` — research standard;
- `STD-CORE-003` — citation standard.

The initial artifact register and research register now exist, and two representative standards trials have been completed:

- `EX-CORE-001` — current Cursor rules and skills evidence;
- `EX-FIXED-001` — new-hire premium KPI definition.

Both trials passed with documented open questions. The standards remain `DRAFT` pending independent review, metadata reconciliation, and validation design.

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
| 0 | Repository controls | DRAFT | Core standards, register structure, and two trials completed |
| 1 | Architecture and standards | PLACEHOLDER | Blocked by Phase 0 review |
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
| 12 | Evaluation and validation | PLACEHOLDER | Not started |
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
- five validation-script placeholders.

## Completed Phase 0 work

1. Assigned immutable IDs to repository controls and active Phase 0/1 artifacts.
2. Defined dependency types, status semantics, source-of-truth rules, and change-impact handling.
3. Defined the central research-register structure.
4. Added reusable source records for current Cursor evidence and new-hire premium research.
5. Trialled the standards against one current-product question.
6. Trialled the standards against one Performance & Reward KPI.
7. Recorded the required rename from `holistic-pr-value-drivers` to `holistic-performance-reward-value-drivers` before Phase 4.

## Phase 0 work remaining

1. Reconcile active file frontmatter with `ARTIFACT-REGISTER.yaml`.
2. Define validator behaviour for IDs, paths, statuses, dependencies, and citation records.
3. Complete three remaining trial types: consulting attribution, stable research finding, and internal project decision.
4. Conduct independent review of `STD-CORE-001` to `STD-CORE-003`.
5. Resolve review findings and move eligible controls to `IN REVIEW`.
6. Merge the scaffold and governance pull request when the review gate is satisfied.

## Immediate next action

Implement the Phase 0 validation design and remaining evidence trials, then review the standards as a complete governance set.
