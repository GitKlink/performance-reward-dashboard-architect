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
content_version: 0.9.0
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

Phase 1 has a complete first-pass architecture and standards set. Phase 2 output contracts and templates are now in progress.

Comprehensive independent testing remains concentrated in Phase 12, followed by final approval and release in Phase 13.

## Phase 1 draft set

Completed first substantive drafts:

- `ARCH-CORE-001` — agent architecture;
- `ARCH-CORE-002` — context-management strategy;
- `ARCH-CORE-003` — skill-routing model;
- `ARCH-CORE-004` — repository information architecture;
- `ARCH-CORE-005` — release architecture;
- `STD-CORE-004` — skill-authoring standard;
- `STD-CORE-005` — example-authoring standard;
- `STD-CORE-006` — evaluation standard;
- `PLAN-CORE-001` — research program;
- `PLAN-CORE-002` — implementation roadmap;
- `PLAN-CORE-003` — release plan.

The files retain `PLACEHOLDER` lifecycle status until the cross-artifact consistency pass and artifact-register reconciliation are complete.

## Skill inventory

The repository retains 49 safe non-invokable skill placeholders across nine capability groups.

Completed consistency work:

- replaced `holistic-pr-value-drivers` with `holistic-performance-reward-value-drivers`;
- documented the exact canonical inventory;
- mapped conceptual architecture labels to actual folder names;
- defined four activation waves;
- retained placeholder protection for every skill.

## Phase 2 schemas

Eight development schemas now use JSON Schema Draft 2020-12 expressed in YAML:

- research record;
- audience and decision profile;
- KPI definition;
- dashboard brief;
- page specification;
- visual specification;
- design review;
- implementation handoff.

They define stable IDs, required fields, controlled values, status, versions, and repository metadata.

## Phase 2 templates

Eight Markdown templates are aligned to the schema set:

- research record;
- audience and decision profile;
- KPI definition;
- dashboard brief;
- page specification;
- visual specification;
- design review;
- implementation handoff.

`wireframe-specification.md` remains a derived placeholder pending practical page and visual examples.

## Automated validation

The repository now includes:

- dependency validation;
- source-register validation;
- internal-link validation;
- JSON Schema validation;
- 25 unit-test scenarios;
- GitHub Actions running the complete active suite.

The latest workflow run passed successfully with dependency, source, and schema warnings treated as failures.

## Development strategy

### During development

- substantive drafts may guide downstream work;
- assumptions and limitations remain visible;
- CI and local checks run continuously;
- each vertical slice receives representative tests;
- critical defects return to the owning upstream artifact.

### Phase 12

- independent architecture review;
- complete routing and skill benchmarks;
- context-load and handoff testing;
- cross-skill contradiction analysis;
- audience and product-mode scenarios;
- metric, Power BI, accessibility, privacy, security, evidence, and licensing review;
- regression testing.

### Phase 13

- runtime and mandatory dependency approval;
- release-package validation;
- final regression;
- `v0.1.0` publication.

## Phase summary

| Phase | Name | Status | Current result |
|---:|---|---|---|
| 0 | Repository foundation | DRAFT — provisionally complete | Development unblocked; full review deferred to Phase 12 |
| 1 | Architecture and standards | DRAFT CONTENT COMPLETE | Consistency and register reconciliation remain |
| 2 | Schemas and templates | IN PROGRESS | Eight schemas and eight templates drafted; fixtures and template validation remain |
| 3 | Audience and decision foundation | PLACEHOLDER | Starts after the first Phase 2 vertical slice validates |
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

## Current limitations

- Phase 1 artifact statuses and register entries still need reconciliation.
- The eight schemas and active schema validator need artifact-register entries.
- Template frontmatter must be standardised with immutable artifact IDs and phase metadata before registration.
- Valid and invalid schema fixtures have not yet been committed.
- Template-to-schema mapping validation has not yet been implemented.
- Current Cursor skill and subagent metadata still requires activation-time verification.
- No skill has been activated.

## Immediate next action

Add schema fixtures and template validation, reconcile Phase 1 and Phase 2 artifact metadata, then build the first audience-to-page synthetic vertical slice.
