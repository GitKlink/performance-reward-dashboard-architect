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
content_version: 0.7.0
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

Phase 0 governance is internally corrected and ready for a genuinely independent review.

The complete Cursor-native scaffold, three core governance standards, five representative trials, artifact and source registers, validation suite, tests, and CI workflow are present.

The standards remain `DRAFT` because the independent-review gate has not yet been satisfied.

## Phase 0 package

### Core standards

- `STD-CORE-001` — naming standard
- `STD-CORE-002` — research standard
- `STD-CORE-003` — citation standard

### Representative trials

- `EX-CORE-001` — current Cursor rules and skills evidence
- `EX-FIXED-001` — new-hire premium KPI definition
- `EX-CONSULT-001` — consulting-firm technique attribution
- `EX-VIZ-001` — stable graphical-perception research
- `EX-CORE-002` — internal source-of-truth decision

### Governance and validation

- reconciled `ARTIFACT-REGISTER.yaml`
- central source register with immutable artifact references
- artifact dependency validator
- source-register validator
- internal-link validator
- 18 unit-test scenarios
- GitHub Actions quality gate
- internal pre-review record `EVAL-QA-001`

## Automated validation status

The current CI workflow passes with warnings treated as failures for dependency and source-register validation.

It validates:

- artifact IDs, paths, dependencies, cycles, frontmatter, and maturity;
- source IDs, evidence levels, lifecycle states, dates, artifact references, and central source citations;
- repository-local Markdown links;
- all 18 unit-test scenarios.

## Internal pre-review outcome

The internal pre-review initially identified one critical, seven major, and four minor findings.

All internal critical and major findings have been resolved, including:

- phase approval deadlock;
- research-record schema circular dependency;
- missing `TEST` and `INFRA` artifact types;
- unregistered validation infrastructure;
- descriptive source-to-artifact references;
- legacy dependency metadata;
- new-hire premium survivorship bias;
- reviewer-independence rules.

`EVAL-QA-001` now records the outcome:

```text
PASS TO INDEPENDENT REVIEW
```

This does not authorise a status transition.

## Important current-product finding

IBCS Version 2.0 was released on 2026-06-11 and replaced the prior conceptual, perceptual, and semantic chapter structure with Notation and Composition aligned with ISO 24896. Any scaffold assumptions based on IBCS 1.2 must be reviewed before the IBCS knowledge pack is authored.

## Status definitions

| Status | Meaning |
|---|---|
| `PLACEHOLDER` | Scope exists; substantive content does not |
| `RESEARCH IN PROGRESS` | Evidence gathering is active |
| `DRAFT` | Substantive content exists but has not passed review |
| `IN REVIEW` | Acceptance criteria are being assessed |
| `APPROVED` | Authoritative for dependent work |
| `SUPERSEDED` | Replaced by a named artifact |

## Phase summary

| Phase | Name | Status | Current result |
|---:|---|---|---|
| 0 | Repository controls | DRAFT | Internally corrected; independent review pending |
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

## Phase 0 work remaining

1. Complete the independent review under GitHub issue #2.
2. Resolve any independent critical and major findings.
3. Move eligible controls and standards to `IN REVIEW`.
4. Complete final approval review and mark eligible Phase 0 artifacts `APPROVED`.
5. Merge pull request #1.
6. Begin substantive Phase 1 architecture work.

## Immediate next action

Run the independent Phase 0 review from a fresh reviewer context with no authority to approve its own corrections.
