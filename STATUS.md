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
content_version: 1.0.0
last_reviewed: 2026-07-31
next_review: 2026-08-31
---

# Repository status

This is the authoritative high-level completion register.

## Current milestone

`v0.1 — Domain-first Performance & Reward Architect`

## Current branch

```text
scaffold/repository-foundation
```

## Current activity

The programme has been reprioritised around Performance & Reward domain knowledge following the emergence of maintained Microsoft Power BI skills.

The immediate objective is no longer to finish every generic architecture, audience, visualisation, dashboard, and Power BI layer before beginning the domain. The repository will complete the minimum operating foundation needed for safe authoring, then begin the shared Performance & Reward ontology and highest-value specialist packs.

Generic Power BI capabilities will be assessed for delegation to Microsoft skills. Repository-owned authority remains with business definitions, calculations, processes, decisions, grain, history, controls, governance, and domain-specific implementation constraints.

## Completed foundation

Completed substantive drafts include:

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

Eight development schemas and aligned Markdown templates exist for:

- research records;
- audience and decision profiles;
- KPI definitions;
- dashboard briefs;
- page specifications;
- visual specifications;
- design reviews;
- implementation handoffs.

The files retain draft or placeholder lifecycle states until cross-artifact consistency and artifact-register reconciliation are complete.

## Skill inventory

The repository retains 49 safe non-invokable skill placeholders across nine capability groups.

The inventory will now be classified into four treatments:

1. **Domain core** — accelerate and retain locally;
2. **Domain-aware implementation** — retain where Performance & Reward changes the technical answer;
3. **Microsoft-delegated** — route to maintained Microsoft Power BI skills;
4. **Deprioritised generic** — leave as a placeholder or thin reference until a documented gap exists.

No skill is active yet.

## Domain-first workstream

### Shared ontology

The first new substantive domain artifacts will define:

- domain boundaries and shared terminology;
- business processes and decision points;
- holistic value drivers;
- KPI classes;
- grain, effective dating, population, and time conventions;
- cross-domain relationships;
- sensitivity, governance, and control classifications;
- BAU and non-BAU scenarios.

### Specialist pack order

1. Fixed reward
2. Variable reward
3. Performance management
4. Job architecture
5. Market competitiveness
6. Governance and controls
7. Pay equity
8. Talent and retention
9. Benefits and recognition

### First vertical slices

The first workflows used to validate the architecture will be:

1. pre-EOY salary and bonus planning;
2. manager salary review;
3. fixed-reward budget allocation.

These will force early resolution of point-in-time modelling, employee and position history, budget and recommendation facts, audience differences, sensitive-data controls, and non-technical semantic-model design.

## Microsoft Power BI skill integration

A new integration workstream will establish:

- the Microsoft skill inventory;
- overlap with the repository's planned skills;
- delegate, supplement, override, or retain decisions;
- domain-context injection requirements;
- validation and fallback rules;
- a maintained gap register.

This workstream does not block the start of domain ontology authoring.

## Automated validation

The repository includes:

- dependency validation;
- source-register validation;
- internal-link validation;
- JSON Schema validation;
- 25 unit-test scenarios;
- GitHub Actions running the active suite.

The last recorded workflow passed with dependency, source, and schema warnings treated as failures. Validation must be rerun after the control-file and dependency reconciliation changes.

## Revised phase summary

| Phase | Name | Status | Current result |
|---:|---|---|---|
| 0 | Minimum operating foundation | IN PROGRESS | Core controls, architecture, schemas, and templates exist; reconciliation remains |
| 1 | P&R ontology and shared foundation | STARTING | First substantive domain workstream |
| 2 | Core specialist P&R domains | PLACEHOLDER | Fixed reward is first pack |
| 3 | Domain workflows and product archetypes | PLACEHOLDER | First three vertical slices selected |
| 4 | P&R audiences and decision treatment | PLACEHOLDER | Generic archetypes narrowed to domain roles |
| 5 | Microsoft Power BI skill integration | STARTING | Inventory and overlap assessment required |
| 6 | P&R-specific Power BI implementation | PLACEHOLDER | Generic implementation guidance narrowed |
| 7 | Domain communication and visual patterns | PLACEHOLDER | Previous generic phases consolidated |
| 8 | Orchestration and comprehensive evaluation | PLACEHOLDER | Main independent testing phase |
| 9 | Integration and release | PLACEHOLDER | Final approval and release |

## Current limitations

- `DEPENDENCIES.md`, `ARTIFACT-REGISTER.yaml`, and planning artifacts still reflect the previous 14-phase sequence.
- Phase metadata in existing files has not yet been migrated to the revised phase model.
- The 49 skill placeholders have not yet been classified against Microsoft Power BI skills.
- Domain ontology artifacts do not yet exist.
- Schema fixtures and template-to-schema validation remain incomplete.
- Current Cursor skill and subagent metadata still requires activation-time verification.
- No skill has been activated.

## Immediate next actions

1. Reconcile `DEPENDENCIES.md`, the artifact register, and planning artifacts with the revised build order.
2. Inventory and classify all 49 skill placeholders as domain core, domain-aware implementation, Microsoft-delegated, or deprioritised generic.
3. Create the Performance & Reward ontology artifact set.
4. Begin the fixed-reward specialist pack.
5. Use pre-EOY salary and bonus planning as the first end-to-end validation slice.
