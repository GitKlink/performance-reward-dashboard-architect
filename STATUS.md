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
content_version: 1.1.0
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

The programme is being rebuilt around repository-owned Performance & Reward semantics with maintained Microsoft Power BI skills used as implementation capabilities where appropriate.

The current development pattern is a vertical slice:

```text
shared ontology
  -> specialist domain knowledge
  -> repeatable analysis skill
  -> workflow and benchmark scenario
  -> Microsoft Power BI implementation delegation
```

No skill is active yet. Domain and skill drafts remain subject to evidence review, dependency reconciliation, benchmark testing, and activation controls.

## Completed foundation

Substantive drafts exist for:

- five core architecture artifacts;
- skill, example, evaluation, research, citation, and naming standards;
- research, implementation, and release plans;
- eight schemas and aligned templates;
- repository dependency, source, schema, template, and link validation.

## Domain-first progress

### Shared ontology

`knowledge/performance-reward/holistic-value-driver-tree.md` is now a substantive draft defining:

- overall Performance & Reward outcomes;
- eight connected value-driver branches;
- decision and outcome chains;
- cross-domain relationships;
- analytical dimensions;
- grain, time, population, and lifecycle conventions;
- diagnostic and governance principles;
- Microsoft Power BI delegation boundaries.

### Completed specialist vertical slices

#### Fixed reward

Drafted:

- `knowledge/performance-reward/fixed-reward.md`;
- `.cursor/skills/performance-reward/fixed-reward-analysis/SKILL.md`.

Coverage includes positioning, movement, budget, compression, new-hire premium, effective dating, recommendation-to-payment lifecycle, audience routes, modelling implications, and controls.

#### Variable reward

Drafted:

- `knowledge/performance-reward/variable-reward.md`;
- `.cursor/skills/performance-reward/variable-reward-analysis/SKILL.md`.

Coverage includes eligibility, target opportunity, pro-ration, organisational and individual factors, funded pools, differentiation, salary concentration, fairness, calibration, approvals, payment reconciliation, and GVRP-style analysis.

#### Performance management

Drafted:

- `knowledge/performance-reward/performance-management.md`;
- `.cursor/skills/performance-reward/performance-management-analysis/SKILL.md`.

Coverage includes lifecycle stages, completion, assessment quality, outcome distributions, manager patterns, calibration movement, fairness, governance, downstream reward linkage, and historical accountability.

### Activation state

All three specialist skills remain deliberately disabled through `activation: DISABLED` until:

- dependencies are reviewed;
- the skill-authoring standard is satisfied;
- benchmark scenarios pass;
- routing boundaries are tested;
- Microsoft delegation and fallback behaviour is verified.

## Specialist pack order

1. Fixed reward — DRAFT
2. Variable reward — DRAFT
3. Performance management — DRAFT
4. Job architecture — NEXT
5. Market competitiveness
6. Governance and controls
7. Pay equity
8. Talent and retention
9. Benefits and recognition

Governance and controls is also a cross-cutting dependency and may be advanced before the full sequence reaches it.

## First workflow slices

The selected validation workflows remain:

1. pre-EOY salary and bonus planning;
2. manager salary review;
3. fixed-reward budget allocation;
4. variable-reward calibration;
5. performance outcome reporting.

The first workflow should combine the fixed-reward, variable-reward, and performance-management slices and force resolution of shared population, history, budget, lifecycle, and security rules.

## Microsoft Power BI skill integration

The planned classification remains:

1. **Domain core** — retain and accelerate locally;
2. **Domain-aware implementation** — retain where Performance & Reward changes the technical answer;
3. **Microsoft-delegated** — route to maintained Microsoft skills;
4. **Deprioritised generic** — leave as placeholders or thin references until a gap exists.

The 49 skill placeholders still require a formal file-by-file classification register.

## Revised phase summary

| Phase | Name | Status | Current result |
|---:|---|---|---|
| 0 | Minimum operating foundation | IN PROGRESS | Core controls and tooling exist; register reconciliation remains |
| 1 | P&R ontology and shared foundation | IN PROGRESS | Holistic ontology drafted; shared process and KPI controls remain |
| 2 | Core specialist P&R domains | IN PROGRESS | Fixed reward, variable reward, and performance management drafted |
| 3 | Domain workflows and product archetypes | STARTING | First five workflow slices selected |
| 4 | P&R audiences and decision treatment | PLACEHOLDER | Generic archetypes still require domain-role refocus |
| 5 | Microsoft Power BI skill integration | STARTING | Formal overlap classification remains |
| 6 | P&R-specific Power BI implementation | PLACEHOLDER | Domain contracts now beginning to define requirements |
| 7 | Domain communication and visual patterns | PLACEHOLDER | Generic content remains deprioritised |
| 8 | Orchestration and comprehensive evaluation | PLACEHOLDER | Activation and routing tests not yet run |
| 9 | Integration and release | PLACEHOLDER | Release remains blocked |

## Current limitations

- `ARTIFACT-REGISTER.yaml` and some planning metadata still reflect the previous phase model.
- The skill inventory has not been formally classified against Microsoft Power BI skills.
- Shared business-process, KPI-classification, sensitivity, and governance ontology artifacts remain incomplete.
- The governance-and-controls specialist dependency is still a placeholder.
- No workflow artifact or new benchmark scenario has been implemented yet.
- Formal sources have not yet been registered for the new domain drafts.
- No skill has been activated.

## Immediate next actions

1. Draft governance and controls as the cross-cutting dependency.
2. Draft job architecture and market competitiveness vertical slices.
3. Implement the pre-EOY salary and bonus planning workflow contract.
4. Create benchmark scenarios for fixed reward, variable reward, and performance management.
5. Build the formal Microsoft skill-overlap classification register.
6. Reconcile `ARTIFACT-REGISTER.yaml` and remaining phase metadata.