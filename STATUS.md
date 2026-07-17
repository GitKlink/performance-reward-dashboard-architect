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
content_version: 0.8.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
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

Phase 0 is **provisionally complete for development** and Phase 1 architecture work has started.

The decision was made to concentrate comprehensive independent testing in Phase 12 and final approval in Phase 13 rather than blocking every development phase with a formal review ceremony.

Phase 0 artifacts remain `DRAFT`. They are sufficient to guide controlled development because:

- the scaffold and governance controls exist;
- five representative trials exercised the standards;
- internal critical and major defects were corrected;
- dependency, source, link, and unit-test validation pass;
- placeholder runtime components cannot activate accidentally.

## Current Phase 1 focus

The active sequence is:

1. agent architecture;
2. context-management strategy;
3. skill-routing model;
4. repository information architecture;
5. release architecture;
6. skill, example, and evaluation standards;
7. research, implementation, and release plans.

The first substantive artifact is `ARCH-CORE-001`.

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

- artifact and source registers;
- dependency, source-register, and internal-link validators;
- 18 unit-test scenarios;
- GitHub Actions quality gate;
- internal pre-review record `EVAL-QA-001`.

## Automated validation status

The current CI workflow validates:

- artifact IDs, paths, dependencies, cycles, frontmatter, and maturity;
- source IDs, evidence levels, lifecycle states, dates, artifact references, and central source citations;
- repository-local Markdown links;
- all 18 current unit-test scenarios.

Warnings fail CI for dependency and source-register validation.

## Testing strategy

### During development

- continuous repository validation;
- local checks for each new knowledge pack, schema, skill, and workflow;
- representative examples sufficient to expose obvious architectural defects;
- correction of critical issues when discovered.

### Phase 12

- independent architecture review;
- complete benchmark and routing suite;
- context-load and handoff testing;
- cross-skill contradiction analysis;
- audience and consumption-mode scenarios;
- metric, Power BI, accessibility, privacy, licensing, and security review;
- regression testing.

### Phase 13

- final approval of runtime artifacts and mandatory dependencies;
- release-package validation;
- final regression run;
- `v0.1.0` preparation.

## Important current-product finding

IBCS Version 2.0 was released on 2026-06-11 and replaced the prior conceptual, perceptual, and semantic chapter structure with Notation and Composition aligned with ISO 24896. Later IBCS work must use the current baseline.

## Status definitions

| Status | Meaning |
|---|---|
| `PLACEHOLDER` | Planned scope only |
| `RESEARCH IN PROGRESS` | Evidence gathering is active |
| `DRAFT` | Substantive content suitable for controlled development |
| `IN REVIEW` | Formal review candidate |
| `APPROVED` | Authoritative for release dependencies |
| `SUPERSEDED` | Replaced by a named artifact |

## Phase summary

| Phase | Name | Status | Current result |
|---:|---|---|---|
| 0 | Repository foundation | DRAFT — provisionally complete | Development unblocked; full review deferred to Phase 12 |
| 1 | Architecture and standards | IN PROGRESS | Agent architecture drafting started |
| 2 | Schemas and templates | PLACEHOLDER | Starts after usable Phase 1 drafts exist |
| 3 | Audience and decision foundation | PLACEHOLDER | Not started |
| 4 | Holistic P&R foundation | PLACEHOLDER | Not started |
| 5 | Specialist P&R domains | PLACEHOLDER | Not started |
| 6 | Consulting communication | PLACEHOLDER | Not started |
| 7 | Visual-design foundation | PLACEHOLDER | Not started |
| 8 | Visualisation patterns | PLACEHOLDER | Not started |
| 9 | Dashboard experience | PLACEHOLDER | Not started |
| 10 | Power BI implementation | PLACEHOLDER | Not started |
| 11 | Orchestrator and subagents | PLACEHOLDER | Not started |
| 12 | Comprehensive evaluation | PLACEHOLDER | Main independent testing phase |
| 13 | Integration and release | PLACEHOLDER | Final approval and release |

## Immediate next action

Complete the first draft of `ARCH-CORE-001`, then use it to author the context-management strategy and skill-routing model.
