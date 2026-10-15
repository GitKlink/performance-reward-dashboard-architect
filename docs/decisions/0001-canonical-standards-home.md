---
decision_id: ADR-0001
title: Canonical Power BI and Fabric Engineering Standards Home
status: proposed-for-review
decision_date: 2026-10-16
owner: GitKlink
tracking_issue: 5
implementation_issue: 21
---

# ADR-0001 — Canonical Power BI / Fabric engineering standards home

## Context

Wayfinder is a Power BI/Fabric-focused end-to-end analytical-product architect. Its work spans source extraction, historical/analytical transformations, Power Query, semantic modelling, DAX, reports and validation. Its engineering standards must not be silently duplicated across the architect, reusable library and project repositories.

Issue #4 established the conceptual authority map. Issue #5 asked for a physical standards authority. On 16 October 2026 the dedicated-standards-repository option was selected for this project.

## Decision

**Use a dedicated repository, `GitKlink/power-bi-fabric-standards`, as the canonical source of Power BI/Fabric-focused analytical engineering policies.** This is a repository-home decision, not a premature choice of installation mechanisms or target Cursor architecture.

Scope includes:

1. Semantic-model structure, metadata, governed-measure representation, navigation, naming and quality.
2. DAX expression and engineering conventions.
3. Power Query / M engineering and Dataflows conventions.
4. Data-architecture and analytical-modelling policy needed for source-to-Power-BI workflows, including appropriate Kimball, temporal and Data Vault-inspired practices.
5. Power BI report/analytics UX and visual/application rules within this vertical slice.
6. Validation/conformance policy applied across those layers.

The standards repository is **not** a universal enterprise architecture or all-purpose web/app design system.

## Ownership boundaries

| Owner | Authority | Non-goal |
|---|---|---|
| `power-bi-fabric-standards` | Generic Power BI/Fabric-facing engineering policy, naming, metadata, quality and governance | Domain-specific business truth; generic reusable runtime implementations |
| Wayfinder / architect | Orchestration: find/apply policy, select workflows, delegate capability, coordinate domains and projects | Duplicate full normative standards |
| Performance & Reward domain pack | Business meaning, KPI semantics, populations, lifecycle, data/analytical contracts, business decisions | Define generic DAX/semantic-model engineering convention |
| `dax-m-query-library` | Reusable executable DAX, M, Python and Deneb assets, examples and tests | Be the engineering standards authority |
| Microsoft-maintained Power BI/Fabric skills | Upstream platform operations and technical validation where suitable | Replace our engineering-policy or domain authority |
| PBIP / analytical project | Project-local implementation, accepted local configuration and decision record | Uncontrolled fork of canonical governance |

An explicit, approved domain-specific exception may refine a general rule without transferring generic authority to a domain pack.

## Proposed repository taxonomy

Create subdirectories only when they have actual content:

```
semantic-model/
dax/
power-query/
data-architecture/
reporting-ux/
validation/
```

Normative, approved policy must be distinguishable from drafts, guidance, research, examples and improvement-backlog proposals. A future index/metadata contract should make status, ownership, version and applicability discoverable without parsing entire documents.

## Consumption and versioning principles

- Cite or reference canonical standards; do **not** maintain hand-edited copies in the architect or implementation library.
- Consumers must be able to identify the effective standards version, owner and approval state.
- Local loading, Git pins/tags, manifests, generated indexes and installation/bootstrap mechanics remain open to research synthesis ticket #17 (R8); this ADR does **not** invent a settled packaging choice.
- Microsoft's Power BI/Fabric skills should be delegated to for platform operations and augmented by these policy and domain layers, rather than forked by default.

## Migration decision

Migrate the existing File Library `Semantic Model Standards/` pack **semantically unchanged** into `semantic-model/`, maintaining original relative paths and content before any refactor. Inventory targets are the existing README, `semantic_measure_standard.md`, `business_glossary.md`, improvement backlog and seven domain extensions (Workforce, Organisation, Performance, Fixed Reward, Variable Reward, Equity, International Assignments).

The current independent existence of each of the seven original domain Markdown source files must be verified. References and HTML explorer renderings are not themselves proof of byte-identical original files. Do not mark parity accepted unless the source files and resulting content have been checked.

Only after migration parity is verified should issue #6 decide how current domain extension text is separated between P&R business truth and generic semantic-model representation.

## Alternatives considered

- **Place standards inside Wayfinder:** simpler initial checkout but blurs reusable engineering-policy ownership and leads to standards following one orchestrator.
- **Place standards inside `dax-m-query-library`:** conflicts with the agreed implementation-only boundary.
- **Maintain standards only in the File Library:** preserves existing drafts but lacks a single versioned, reviewable engineering policy home.

A dedicated repository is the recommended scope and authority fit for the current Power BI vertical slice.

## Status and next actions

- **Decision:** dedicated repository selected.
- **Not complete:** physical repository not created through the current GitHub connector; no Semantic Model Standards migrated.
- **Implementation:** issue #21 creates the repository, inventories/copies eleven source files and verifies migration parity.
- **Architecture research:** issue #17 remains open; it governs how the sources are installed/loaded/composed, not this canonical-home decision.
- **Decision tracking:** issue #5. Promote ADR status to accepted following PR review, and close #5 when the decision record is merged; do not misrepresent migration as complete.

## References

- [#4 — Repository topology / authority map](https://github.com/GitKlink/performance-reward-dashboard-architect/issues/4)
- [#5 — Canonical standards home decision](https://github.com/GitKlink/performance-reward-dashboard-architect/issues/5)
- [#6 — P&R domain authority versus semantic representation](https://github.com/GitKlink/performance-reward-dashboard-architect/issues/6)
- [#17 — R8 target architecture synthesis](https://github.com/GitKlink/performance-reward-dashboard-architect/issues/17)
- [#21 — Standards repository creation and migration](https://github.com/GitKlink/performance-reward-dashboard-architect/issues/21)
