---
status: PLACEHOLDER
phase: 1
priority: critical
depends_on:
  - docs/architecture/skill-routing-model.md
  - docs/standards/skill-authoring-standard.md
blocks:
  - active Cursor skills
last_reviewed: 2026-07-17
---

# Cursor skill inventory

## Current state

The repository contains **49 planned skill folders** across nine capability groups.

Every `SKILL.md` remains a safe non-invokable placeholder. None currently contains active Cursor skill frontmatter.

Do not remove the placeholder protection until the skill has entered controlled activation testing under the skill-authoring standard.

## Capability groups

| Group | Count | Purpose |
|---|---:|---|
| Discovery | 3 | requirements, audience, and decision framing |
| Strategy | 3 | value-driver, KPI, and analytical reasoning |
| Performance & Reward | 10 | holistic and specialist domain analysis |
| Consulting | 5 | story structure and executive communication |
| Visual design | 6 | hierarchy, layout, typography, colour, density, and accessibility |
| Visualisation | 6 | chart and exhibit selection and specialist visual forms |
| Experience | 4 | dashboard information architecture and product mode |
| Power BI | 7 | feasibility, model, DAX, interaction, performance, security, and theme |
| Assurance | 5 | metric, visual, accessibility, executive, and complete design review |
| **Total** | **49** | |

## Discovery

```text
audience-decision-framing
dashboard-discovery
grill-dashboard-requirements
```

## Strategy

```text
value-driver-modelling
kpi-measure-design
people-analytics-diagnostics
```

## Performance & Reward

```text
holistic-pr-value-drivers          # must be renamed before activation
performance-management-analysis
fixed-reward-analysis
variable-reward-analysis
market-position-analysis
job-architecture-analysis
pay-equity-analysis
talent-retention-analysis
total-rewards-analysis
reward-governance-analysis
```

Required rename:

```text
holistic-pr-value-drivers
→ holistic-performance-reward-value-drivers
```

The rename must update every architecture, routing, example, and evaluation reference in the same change.

## Consulting

```text
consulting-storyline
executive-message-writing
deck-story-architecture
action-title-writing
issue-tree-design
```

## Visual design

```text
visual-hierarchy-design
dashboard-layout-composition
typography-for-data
colour-and-semantic-notation
data-ink-optimisation
accessibility-design
```

## Visualisation

```text
chart-selection
consulting-exhibit-design
distribution-visualisation
variance-visualisation
table-and-matrix-design
ibcs-application
```

## Experience

```text
dashboard-information-architecture
guided-analytics-design
interactive-dashboard-ux
static-deck-style-design
```

`guided-analytics-design` owns selection and integration of guided, exploratory, action, static, interactive, and hybrid experience modes. It should not duplicate the detailed interactive or static implementation skills.

## Power BI

```text
power-bi-feasibility
semantic-model-design
dax-measure-design
power-bi-interaction-design
power-bi-performance
power-bi-security
power-bi-theme-design
```

Static export requirements currently belong across `static-deck-style-design`, `power-bi-feasibility`, and Power BI knowledge. A separate export skill should be added only if implementation trials show a distinct reusable workflow.

## Assurance

```text
review-dashboard
metric-qa
visual-qa
accessibility-review
executive-readability-test
```

Power BI implementation assurance is initially performed by the `power-bi-verifier` subagent using Power BI skills and implementation-review schemas. Add a separate skill only if a stable standalone procedure emerges.

## Canonical architecture-name mapping

Architecture drafts must use actual folder names.

| Conceptual wording | Canonical skill |
|---|---|
| holistic P&R value drivers | `holistic-performance-reward-value-drivers` after rename |
| interactive versus static design | `guided-analytics-design` |
| static report design | `static-deck-style-design` |
| dashboard critique | `review-dashboard` |
| Power BI interaction build | `power-bi-interaction-design` |
| Power BI theme and layout | `power-bi-theme-design` plus `dashboard-layout-composition` where needed |
| variance and driver visualisation | `variance-visualisation` plus analytical method as needed |
| Power BI implementation review | `power-bi-verifier` subagent plus relevant Power BI skills |
| Power BI export design | `static-deck-style-design` plus `power-bi-feasibility` unless a later distinct skill is approved |

Do not introduce additional skill names only to make architecture prose symmetrical. Add a skill when it owns a distinct reusable method and passes the normal design test.

## Activation waves

### Wave A — Foundational vertical slice

```text
audience-decision-framing
dashboard-discovery
value-driver-modelling
kpi-measure-design
holistic-performance-reward-value-drivers
consulting-storyline
visual-hierarchy-design
chart-selection
guided-analytics-design
power-bi-feasibility
review-dashboard
```

These skills should support one end-to-end design and critique workflow before broader activation.

### Wave B — Initial dashboard products and domains

```text
people-analytics-diagnostics
performance-management-analysis
fixed-reward-analysis
variable-reward-analysis
dashboard-information-architecture
interactive-dashboard-ux
static-deck-style-design
consulting-exhibit-design
distribution-visualisation
variance-visualisation
table-and-matrix-design
metric-qa
visual-qa
accessibility-design
accessibility-review
executive-readability-test
```

### Wave C — Implementation depth

```text
semantic-model-design
dax-measure-design
power-bi-interaction-design
power-bi-performance
power-bi-security
power-bi-theme-design
dashboard-layout-composition
typography-for-data
colour-and-semantic-notation
data-ink-optimisation
executive-message-writing
action-title-writing
deck-story-architecture
issue-tree-design
```

### Wave D — Remaining specialist breadth

```text
market-position-analysis
job-architecture-analysis
pay-equity-analysis
talent-retention-analysis
total-rewards-analysis
reward-governance-analysis
ibcs-application
grill-dashboard-requirements
```

Activation order may change when a benchmark or user need requires a later-wave capability. Dependencies and benchmark coverage must be updated rather than activating it informally.

## Skill activation requirements

Before any placeholder becomes an active draft skill:

- exact current Cursor frontmatter is verified;
- folder and skill name agree;
- invocation and non-invocation conditions are testable;
- knowledge and schema dependencies exist;
- output contract is defined;
- positive, negative, ambiguous, and missing-input cases exist;
- context load is proportionate;
- placeholder protection is removed intentionally;
- skill metadata validation passes.

Before release approval:

- automatic invocation is tested where enabled;
- explicit invocation is tested;
- benchmark outputs pass agreed thresholds;
- adjacent-skill interactions are tested;
- mandatory dependencies are approved;
- release package resolves all references and assets;
- no critical or major finding remains.

## What each placeholder must contain before activation

- valid `name` and precise `description`;
- `Use when` and `Do not use when`;
- required inputs;
- missing-information behaviour;
- ordered method and selection rules;
- knowledge and schema references;
- structured output contract;
- anti-patterns and quality checks;
- compact examples or links;
- handoff requirements;
- status, version, and compatibility metadata.

## Anti-patterns

- Activating all 49 skills simultaneously.
- Keeping different names in architecture, folder paths, and frontmatter.
- Creating a new skill for every conceptual label used in prose.
- Duplicating one method across several audience-specific skills.
- Putting shared P&R definitions inside each skill.
- Using assurance skills as a substitute for domain or metric design.
- Making disruptive review or grilling workflows automatic.
- Treating a placeholder path as evidence the capability exists.
