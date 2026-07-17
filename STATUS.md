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
content_version: 0.2.0
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

The complete initial scaffold has been created. The first three substantive standards now exist as drafts:

- `STD-CORE-001` — naming standard;
- `STD-CORE-002` — research standard;
- `STD-CORE-003` — citation standard.

These standards are not yet approved. They must be trialled against representative artifacts and independently reviewed before they can unblock downstream work at release quality.

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
| 0 | Repository controls | DRAFT | Naming, research, and citation standards drafted |
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

## Phase 0 work remaining

1. Assign immutable artifact IDs to repository control files.
2. Expand the file-level dependency register.
3. Define the central research-register structure.
4. Trial the standards against one current-product claim and one P&R KPI.
5. Record naming migrations identified by the scaffold review.
6. Move the three standards to `IN REVIEW` only after those trials pass.

## Immediate next action

Implement the detailed artifact and dependency register, then use it to validate Phase 1 architecture placeholders before substantive architecture work begins.
