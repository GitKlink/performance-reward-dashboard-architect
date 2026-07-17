---
artifact_id: ARCH-CORE-003
status: PLACEHOLDER
phase: 1
priority: critical
depends_on:
  - artifact_id: ARCH-CORE-001
    path: agent-architecture.md
  - artifact_id: ARCH-CORE-002
    path: context-management-strategy.md
blocks:
  - active Cursor skills
  - main orchestrator rule
  - routing evaluations
content_version: 0.1.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Skill-routing model

## Document state

This is the first substantive routing draft. The lifecycle status remains `PLACEHOLDER` until the Phase 1 architecture set, skill inventory, and benchmark routes are reconciled.

## Purpose

Define how the Cursor agent selects and sequences the minimum appropriate skills and subagents for a Performance & Reward dashboard request.

Agent Skills are dynamically discoverable and can be invoked explicitly, making them appropriate for modular procedures that should not remain in persistent context.[^cursor-skills]

## Routing objective

For each request, select the smallest capability set that can produce a trustworthy result.

```text
Minimum sufficient routing
≠ fewest possible skills
≠ every plausibly related skill
```

A route is sufficient when it covers:

- audience and decision;
- relevant Performance & Reward domain;
- analytical and metric needs;
- consumption mode;
- requested output;
- implementation and quality risks appropriate to the task.

## Routing inputs

The router resolves six primary dimensions.

### Audience

```text
executive
board-or-committee
business-partner
people-manager
reward-partner
performance-reward-specialist
people-analytics-or-reporting
operational-team
```

### Decision mode

```text
monitor
diagnose
compare
decide
plan
allocate
calibrate
forecast
explain
govern
execute
review
```

### Performance & Reward domain

```text
cross-domain-performance-reward
performance-management
fixed-reward
variable-reward
market-competitiveness
job-architecture
pay-equity
talent-and-retention
total-rewards
governance-and-controls
```

### Consumption mode

```text
interactive
static
hybrid
not-yet-decided
```

### Workflow stage

```text
discovery
business-framing
analysis
metric-design
story-and-page-design
visual-design
power-bi-implementation
critique
release-preparation
```

### Requested output

```text
requirements-interview
dashboard-brief
value-driver-tree
kpi-definition
analytical-plan
page-architecture
wireframe-or-page-specification
visual-specification
interaction-specification
executive-storyline
design-review
implementation-handoff
power-bi-review
complete-dashboard-design
```

## Secondary routing signals

Use these only after the primary dimensions:

- business-as-usual or non-BAU condition;
- reading time;
- data sensitivity;
- employee-level detail;
- regulatory or legal risk;
- available source data and grain;
- existing dashboard or greenfield design;
- implementation deadline;
- need for external research;
- user expertise;
- output intended for export or presentation;
- requirement for planning, calibration, or allocation workflow.

## Routing sequence

```text
1. Clarify task and requested output
2. Resolve audience and decision
3. Resolve domain and business question
4. Resolve workflow stage
5. Resolve consumption mode
6. Add analytical and KPI capabilities
7. Add communication and visual capabilities
8. Add Power BI capabilities where implementation matters
9. Add quality review proportional to risk
10. Delegate context-heavy work only where useful
11. Remove unnecessary skills
```

## Routing decision tree

```text
Has the user supplied a clear audience, decision, and output?
├─ No → dashboard-discovery or grill-dashboard-requirements
└─ Yes
   ↓
Is the business question cross-domain or domain-specific?
├─ Cross-domain → holistic-performance-reward-value-drivers
└─ Domain-specific → relevant domain analysis skill
   ↓
Are metrics or diagnostics required?
├─ Metrics → kpi-measure-design
├─ Diagnosis → people-analytics-diagnostics
└─ Neither → continue
   ↓
What is the consumption mode?
├─ Static → consulting-storyline + static-report-design
├─ Interactive → dashboard-information-architecture + interactive-dashboard-ux
└─ Hybrid → both, with explicit page-role separation
   ↓
Is visual selection or page composition required?
├─ Yes → visual-hierarchy-design + chart-selection + relevant specialist visual skills
└─ No → continue
   ↓
Is implementation or feasibility in scope?
├─ Yes → power-bi-feasibility + relevant Power BI skills
└─ No → record implementation assumptions
   ↓
What assurance is proportionate?
├─ Design critique → dashboard-critique
├─ Metric risk → metric-qa
├─ Implementation risk → power-bi-implementation-review
└─ Release candidate → complete assurance suite
```

## Skill-route layers

A route is assembled from layers rather than one flat catalogue.

### Layer A — Discovery and framing

Candidate skills:

- `dashboard-discovery`
- `grill-dashboard-requirements`
- `audience-decision-framing`
- `value-driver-modelling`

Use when the request is ambiguous, conflicting, broad, or not yet connected to a decision.

### Layer B — Performance & Reward domain

Candidate skills:

- `holistic-performance-reward-value-drivers`
- `performance-management-analysis`
- `fixed-reward-analysis`
- `variable-reward-analysis`
- `market-position-analysis`
- `job-architecture-analysis`
- `pay-equity-analysis`
- `talent-retention-analysis`
- `total-rewards-analysis`
- `reward-governance-analysis`

Select one primary domain skill unless the business question genuinely spans multiple domains.

### Layer C — Metrics and diagnostics

Candidate skills:

- `kpi-measure-design`
- `people-analytics-diagnostics`
- distribution, variance, driver, and table visualisation skills where available.

Invoke only when measures, calculations, analytical relationships, or diagnosis are in scope.

### Layer D — Consulting communication

Candidate skills:

- `consulting-storyline`
- `executive-message-writing`
- `insight-commentary`
- `deck-story-architecture`

Use based on audience, decision, and output. Do not invoke all communication skills for every page.

### Layer E — Information and visual design

Candidate skills:

- `dashboard-information-architecture`
- `visual-hierarchy-design`
- `dashboard-layout-composition`
- `typography-for-data`
- `colour-and-semantic-notation`
- `accessibility-design`
- `chart-selection`
- `consulting-exhibit-design`
- `ibcs-application`
- specialist visualisation skills.

Select only those required by the output and analytical relationship.

### Layer F — Consumption experience

Candidate skills:

- `interactive-dashboard-ux`
- `static-report-design`
- `consulting-slide-layout`
- `power-bi-export-design`
- `executive-deck-sequencing`

Interactive and static skills may coexist for hybrid reports, but each page must have a declared role.

### Layer G — Power BI implementation

Candidate skills:

- `power-bi-feasibility`
- `semantic-model-design`
- `dax-measure-design`
- `power-bi-interaction-build`
- `power-bi-performance`
- `power-bi-theme-and-layout`
- `power-bi-security`

Use when implementation details affect the recommendation or the requested output includes a build handoff.

### Layer H — Assurance

Candidate skills:

- `dashboard-critique`
- `visual-qa`
- `metric-qa`
- `power-bi-implementation-review`
- `accessibility-review`
- `executive-readability-test`

Select assurance based on risk and workflow stage. Full assurance is reserved for release candidates or explicit comprehensive reviews.

## Foundational skill policy

No skill is literally invoked for every request.

The following are foundational candidates:

- `audience-decision-framing`
- `dashboard-discovery`
- `value-driver-modelling`
- `kpi-measure-design`
- `holistic-performance-reward-value-drivers`
- `consulting-storyline`
- `visual-hierarchy-design`
- `chart-selection`
- `interactive-vs-static-design` or equivalent consumption-mode capability
- `power-bi-feasibility`

A foundational candidate is selected only when its decision is unresolved or its output is needed.

Example: a user asking for a metric-definition review does not need page-layout or chart-selection skills.

## Automatic versus explicit invocation

### Automatic invocation

A skill may be selected automatically when:

- the request clearly matches its bounded responsibility;
- required inputs are present or can be resolved safely;
- the skill is necessary for a trustworthy result;
- invocation will not materially expand scope without user agreement;
- its status permits controlled use.

Examples:

- `audience-decision-framing` for a dashboard request with no decision stated;
- `kpi-measure-design` when the user requests KPI definitions;
- `power-bi-feasibility` when a proposed visual or interaction may not be implementable;
- `metric-qa` when reviewing a calculation.

### Explicit invocation

Prefer explicit invocation when:

- the workflow is intensive or disruptive;
- multiple valid approaches exist and the user has requested one;
- the skill performs a formal review or grilling process;
- the user requests a reusable artifact;
- the action may generate many files;
- the skill is specialised and not safely inferred from ordinary wording.

Examples:

- `/grill-dashboard-requirements`
- `/review-dashboard`
- `/create-dashboard-brief`
- `/run-evaluations`

Exact command names and Cursor syntax remain subject to Phase 1 verification.

### Manual-only candidates

Skills should be manual-only when they:

- conduct prolonged adversarial questioning;
- change repository-wide architecture;
- produce release artifacts;
- run expensive comprehensive evaluations;
- could overwrite or restructure many artifacts;
- require explicit user authority.

## Audience routing

| Audience | Default emphasis | Common skills | Common exclusions |
|---|---|---|---|
| Executive or committee | decision, variance, material risk, forecast, action | audience framing, storyline, exhibit design, static or guided UX, readability | dense employee detail, unrestricted exploration |
| Business Partner | diagnosis, segmentation, stakeholder explanation | diagnostics, distributions, information architecture, interactive UX, commentary | oversimplified scorecard-only design |
| People manager | accountable population, exceptions, workflow | manager framing, action UX, security, contextual definitions | complex analytical methods without action value |
| Reward Partner | allocation, calibration, controls, employee export | reward domain, KPI design, diagnostics, interaction, security, implementation | high-level summary without planning detail |
| Specialist or analytics | definition, method, data quality, reconciliation | domain analysis, KPI design, diagnostics, model and DAX, metric QA | unnecessary executive simplification |

Audience routing changes emphasis rather than automatically selecting every skill in the row.

## Decision-mode routing

| Decision mode | Analytical emphasis | Typical capability additions |
|---|---|---|
| Monitor | status, trend, tolerance, exceptions | KPI design, trend visuals, guided summary |
| Diagnose | distribution, segmentation, drivers, cohorts | diagnostics, distribution and driver visualisation, exploratory UX |
| Compare | benchmark, peer, target, variance | KPI design, comparison visuals, table or matrix design |
| Decide | alternatives, implications, recommendation | storyline, decision framing, scenario exhibit |
| Plan | forecast, capacity, timing, scenarios | scenario analysis, planning UX, implementation feasibility |
| Allocate | budget, constraints, trade-offs, cases | reward domain, allocation logic, employee workflow, controls |
| Calibrate | distributions, consistency, outliers, evidence | performance or reward domain, diagnostics, guided workflow, security |
| Forecast | assumptions, ranges, drivers, uncertainty | scenario analysis, variance visualisation, executive storyline |
| Govern | controls, policy, completeness, audit trail | governance analysis, metric QA, security, table design |
| Execute | tasks, deadlines, accountable population | manager action UX, exceptions, workflow, security |
| Review | defects, gaps, contradictions, feasibility | relevant assurance skills and critic subagent |

## Consumption-mode routing

### Static

Required considerations:

- governing message;
- fixed reading order;
- direct labels;
- visible assumptions and sources;
- export-safe layout;
- no dependence on hover;
- page-level implication or decision.

Common skills:

- consulting storyline;
- executive message writing;
- consulting exhibit design;
- static report design;
- Power BI export design.

### Interactive

Required considerations:

- information architecture;
- persistent filter context;
- drill-down and drill-through;
- tooltips and detail on demand;
- reset and navigation;
- security;
- performance.

Common skills:

- dashboard information architecture;
- interactive dashboard UX;
- chart selection;
- Power BI interaction and security.

### Hybrid

Route static and interactive capabilities with explicit page roles:

```text
summary pages = guided, conclusion-led, export-safe
analysis pages = exploratory, diagnostic, interaction-rich
action pages = workflow-led and security-controlled
```

Do not make every page both presentation-led and exploration-led.

## Domain routing rules

### Cross-domain

Use the holistic value-driver skill when:

- the user asks what P&R should measure overall;
- the dashboard spans performance, reward, talent, fairness, and governance;
- domain boundaries are unclear;
- the request concerns enterprise P&R strategy or executive portfolio value.

Do not use it merely because a specialist metric has downstream workforce implications.

### Specialist domains

Select a domain skill only when the business question falls within its defined boundary.

Examples:

- salary investment, range position, compression, and pay movement → fixed reward;
- target opportunity, performance multiplier, payout, and allocation → variable reward;
- performance process, rating pattern, completion, and differentiation → performance management;
- external benchmark, market movement, and match quality → market competitiveness;
- job profiles, levels, families, and career structure → job architecture;
- unexplained pay differences and fairness diagnostics → pay equity;
- critical population loss and retention risk → talent and retention;
- benefits, recognition, and employee value proposition → total rewards;
- policy compliance, completeness, controls, and auditability → governance.

When two domains are materially linked, select one primary skill and one supporting skill rather than invoking every related domain.

## Skill sequencing

Default sequence:

```text
Discovery
→ audience and decision
→ value-driver or domain framing
→ KPI and analytical design
→ storyline and information architecture
→ visual and consumption design
→ Power BI feasibility and implementation
→ proportional assurance
→ output handoff
```

Exceptions:

- critique starts from the existing artifact and relevant assurance skills;
- metric review may begin with KPI design and metric QA;
- implementation troubleshooting may begin with Power BI verification after reading the approved design;
- explicit user workflows may skip discovery when inputs are complete.

## Dependency handling

A skill may depend on:

- another skill's output;
- a knowledge pack;
- a schema;
- an implementation capability;
- an audience or decision profile.

Routing must:

1. resolve mandatory prerequisites;
2. avoid loading optional dependencies without need;
3. preserve the order required by output contracts;
4. stop when a missing prerequisite creates material risk;
5. label assumptions when proceeding with a reversible gap.

## Conflict resolution

When skills recommend different actions, resolve in this order:

1. user decision and organisation policy;
2. privacy, security, legal, and governance constraints;
3. audience and decision usefulness;
4. metric and analytical integrity;
5. accessibility;
6. Power BI feasibility;
7. communication and visual preference;
8. aesthetic consistency.

Examples:

- A visually elegant chart loses to a more accessible alternative when the difference is material.
- An executive desire for simplicity does not justify a misleading aggregated KPI.
- A useful interaction is removed when it creates unacceptable security or export risk.
- An IBCS convention may be adapted where audience comprehension or platform constraints require it, with the deviation recorded.

## Subagent routing

### Research synthesiser

Invoke when:

- facts are current, niche, disputed, or source-intensive;
- several evidence classes must be reconciled;
- the parent context would be overwhelmed by research;
- a knowledge pack requires a claims matrix.

Do not invoke for common stable concepts already governed in the repository.

### Dashboard design critic

Invoke when:

- a complete page or multi-page design exists;
- independent challenge is requested;
- an executive or high-stakes product is approaching handoff;
- density, story, audience fit, or contradiction risk is material.

Do not invoke before the design has enough substance to critique.

### Power BI verifier

Invoke when:

- implementation feasibility affects the design;
- model, DAX, interaction, export, security, or performance risk is material;
- an implementation handoff is being prepared;
- a build claims readiness.

Do not use it as a substitute for business framing or visual-design review.

## Route-pruning rules

After assembling a candidate route, remove a skill when:

- another selected skill already owns the required output;
- the skill's output is not consumed later;
- the relevant decision has already been confirmed and persisted;
- the task does not include its domain or workflow stage;
- it would add detail that the requested output does not need;
- its primary value is covered by a deterministic script;
- its content is already present in the current artifact and no review is needed.

Ask:

```text
What failure would occur if this skill were removed?
```

If no material failure is identifiable, remove it.

## Ambiguity protocol

### Low-impact ambiguity

Proceed with a labelled assumption and record it.

Example: draft page count where the user requested an initial concept.

### Material design ambiguity

Ask one focused question at a time or use dashboard discovery.

Example: whether executives must approve an allocation or merely monitor it.

### Externally verifiable ambiguity

Research it rather than asking the user.

Example: current Power BI feature support or current regulation.

### High-risk ambiguity

Stop until resolved.

Examples:

- employee access population;
- policy threshold with financial consequences;
- legal interpretation;
- metric denominator that changes the conclusion;
- use of protected or confidential data.

## Fallback route

When routing confidence is low:

```text
dashboard-discovery
→ audience-decision-framing
→ value-driver-modelling
→ propose two candidate routes
→ ask the user to choose the business direction
```

Do not default immediately to chart selection or visual redesign.

## Example routes

### Executive fixed-reward summary

```yaml
audience: executive
decision_mode: decide
performance_reward_domain: fixed-reward
consumption_mode: static
workflow_stage: complete-dashboard-design
route:
  - audience-decision-framing
  - fixed-reward-analysis
  - kpi-measure-design
  - consulting-storyline
  - executive-message-writing
  - consulting-exhibit-design
  - visual-hierarchy-design
  - static-report-design
  - power-bi-export-design
  - executive-readability-test
conditional:
  - people-analytics-diagnostics: if driver analysis is required
  - power-bi-feasibility: if implementation constraints are in scope
```

### Business Partner performance diagnostic

```yaml
audience: business-partner
decision_mode: diagnose
performance_reward_domain: performance-management
consumption_mode: interactive
workflow_stage: complete-dashboard-design
route:
  - audience-decision-framing
  - performance-management-analysis
  - kpi-measure-design
  - people-analytics-diagnostics
  - dashboard-information-architecture
  - chart-selection
  - distribution-visualisation
  - interactive-dashboard-ux
  - power-bi-feasibility
  - metric-qa
```

### Manager reward action dashboard

```yaml
audience: people-manager
decision_mode: execute
performance_reward_domain:
  - fixed-reward
  - variable-reward
consumption_mode: interactive
workflow_stage: complete-dashboard-design
route:
  - audience-decision-framing
  - fixed-reward-analysis
  - variable-reward-analysis
  - kpi-measure-design
  - dashboard-information-architecture
  - interactive-dashboard-ux
  - power-bi-security
  - power-bi-feasibility
  - accessibility-review
conditional:
  - people-analytics-diagnostics: only for prioritisation or exception logic
```

### Existing executive dashboard critique

```yaml
audience: executive
workflow_stage: critique
requested_output: design-review
route:
  - audience-decision-framing
  - dashboard-critique
  - visual-qa
  - executive-readability-test
  - metric-qa
conditional:
  - relevant domain analysis: when KPI or interpretation defects are in scope
  - power-bi-implementation-review: when feasibility or export is questioned
subagent:
  - dashboard-design-critic: for independent high-stakes review
```

### KPI definition only

```yaml
workflow_stage: metric-design
requested_output: kpi-definition
route:
  - audience-decision-framing
  - relevant-domain-analysis
  - kpi-measure-design
  - metric-qa
excluded:
  - consulting-storyline
  - visual-hierarchy-design
  - chart-selection
  - interactive-dashboard-ux
```

## False-positive routing examples

A routing false positive occurs when an unnecessary capability is selected.

Test cases:

- chart selection invoked for a formula-only request;
- fixed-reward analysis invoked because the word “reward” appears in a recognition dashboard;
- executive storytelling invoked for a technical semantic-model review;
- all P&R domain skills invoked for a cross-domain overview;
- Power BI security invoked for a public aggregate mockup with no implementation scope;
- research subagent invoked for stable knowledge already governed locally.

## False-negative routing examples

A routing false negative occurs when a necessary capability is omitted.

Test cases:

- no security skill for employee-level manager data;
- no static export skill for a board pack;
- no KPI design for a request to redefine range penetration;
- no diagnostic skill for a distribution-health question;
- no Power BI feasibility for a complex interaction request;
- no governance skill for cycle-completeness and policy-control reporting;
- no accessibility review for a colour-dependent exception design.

## Routing evaluation fields

Each benchmark should record:

```yaml
scenario_id:
input_prompt:
resolved_dimensions:
expected_required_skills:
expected_optional_skills:
expected_excluded_skills:
expected_subagents:
expected_sequence:
critical_routing_failures:
acceptable_alternatives:
actual_route:
findings:
```

## Routing quality measures

Phase 12 should assess:

- required-skill recall;
- unnecessary-skill rate;
- domain-selection accuracy;
- audience-mode accuracy;
- consumption-mode accuracy;
- subagent overuse and underuse;
- route-order violations;
- context loaded per route;
- benchmark output quality after routing;
- consistency between automatic and explicit invocation.

No numeric release thresholds are approved yet. The evaluation standard will define them from benchmark trials.

## Anti-patterns

- Selecting skills from keywords alone.
- Invoking every foundational skill for every request.
- Routing to visual design before resolving the decision.
- Treating an audience label as a complete requirements profile.
- Using the holistic P&R skill as a substitute for specialist analysis.
- Using subagents for trivial tasks.
- Loading multiple overlapping domain skills without a primary domain.
- Allowing one skill to redefine another skill's authoritative inputs.
- Ignoring consumption mode until after page design.
- Omitting implementation checks because the visual concept looks plausible.
- Performing the complete assurance suite during every early draft.
- Deferring all assurance until release.

## Draft acceptance assessment

This draft defines:

- routing dimensions and secondary signals;
- route layers and skill groups;
- automatic, explicit, and manual-only invocation;
- audience, decision, consumption, and domain rules;
- sequencing and dependency handling;
- conflict and ambiguity protocols;
- subagent triggers;
- route pruning;
- representative routes;
- false-positive and false-negative tests;
- evaluation fields and measures.

Before the artifact leaves `PLACEHOLDER`, it must be reconciled with:

- the final skill inventory and folder names;
- the skill-authoring standard;
- current Cursor skill metadata and invocation behaviour;
- benchmark scenario files;
- the main orchestrator rule;
- context-load tests.

## Source

[^cursor-skills]: Cursor, “Subagents, Skills, and Image Generation,” release 2.4, 2026, retrieved 2026-07-17, https://cursor.com/changelog/2-4. Central source ID: `cursor-2-4-subagents-skills`.
