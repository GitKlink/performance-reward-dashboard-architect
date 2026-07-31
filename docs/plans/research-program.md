---
artifact_id: PLAN-CORE-001
status: PLACEHOLDER
phase: 1
priority: critical
depends_on:
  - artifact_id: STD-CORE-002
    path: ../standards/research-standard.md
  - artifact_id: STD-CORE-003
    path: ../standards/citation-standard.md
  - artifact_id: ARCH-CORE-001
    path: ../architecture/agent-architecture.md
  - artifact_id: KNOW-CORE-001
    path: ../../knowledge/research-register/README.md
blocks:
  - domain research waves
content_version: 0.1.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Research program

## Document state

This is the first substantive draft. The lifecycle status remains `PLACEHOLDER` until research records, ownership, and the first audience and holistic P&R workstreams are underway.

## Purpose

Sequence the evidence and synthesis required to create reliable audience, Performance & Reward, consulting, visual-design, visualisation, dashboard-experience, and Power BI knowledge packs.

The program supports staged delivery of a useful agent rather than attempting to research the complete catalogue before any skills are built.

## Research principles

1. Research a decision or capability, not a broad topic.
2. Build shared foundations before specialist packs.
3. Research only enough to support the next usable capability while preserving quality.
4. Parallelise independent workstreams; serialise shared definitions.
5. Store evidence and synthesis in the repository rather than in chat history.
6. Distinguish stable theory, current product behaviour, professional practice, regulation, and project decisions.
7. Treat proprietary market data and methods as constrained inputs.
8. Use implementation and benchmark results to refine earlier research.
9. Keep current-product and regulatory refresh work separate from stable theory.
10. Stop research when additional sources no longer change selection rules or known limitations materially.

## Research output chain

```text
Research question
→ source plan
→ source records
→ claims matrix
→ synthesis and selection rules
→ knowledge artifact
→ skill procedure
→ example and benchmark
→ implementation feedback
→ refreshed knowledge
```

## Workstream map

| Workstream | Primary output | Main consumers |
|---|---|---|
| Cursor platform | current component and compatibility knowledge | architecture, skills, subagents, release |
| Audience and decision | audience archetypes and decision modes | discovery, routing, UX, story |
| Holistic P&R | value-driver tree and domain boundaries | all P&R domain skills |
| KPI and analytics | metric architecture and diagnostic methods | KPI and diagnostic skills |
| Specialist P&R | domain knowledge packs | specialist analysis skills |
| Consulting communication | technique catalogue and selection rules | storyline and executive skills |
| Visual design | hierarchy, typography, colour, accessibility | visual and QA skills |
| Data visualisation | relationship and exhibit patterns | chart-selection skills |
| Dashboard experience | static, interactive, hybrid, audience modes | UX and page-design skills |
| Power BI | feasibility and implementation knowledge | Power BI skills and verifier |
| Governance and release | privacy, licensing, validation, packaging | assurance and release |

## Research waves

### Wave 0 — Repository and current-product baseline

Status: substantially complete for development.

Questions:

- What Cursor components and paths are currently supported?
- How do rules, skills, subagents, commands, hooks, and packaging differ?
- What product behaviours require verification before activation?
- How should source and release governance operate?

Outputs:

- current-product trial;
- naming, research, and citation standards;
- architecture drafts;
- source register;
- release refresh triggers.

Refresh: before runtime activation and every release candidate.

### Wave 1 — Audience and decision foundation

Priority: immediate after Phase 1 architecture.

Questions:

- What decisions do executives, Business Partners, people managers, Reward Partners, specialists, and reporting teams make with P&R information?
- What actions follow from each decision?
- How do reading time, detail tolerance, risk, cadence, and data access differ?
- When should a product be static, interactive, or hybrid?
- Which requirements should be discovered rather than assumed?

Outputs:

- audience archetypes;
- decision-mode catalogue;
- consumption-mode framework;
- discovery-question bank;
- audience and decision selection rules;
- initial audience benchmarks.

Skills enabled:

- `audience-decision-framing`;
- `dashboard-discovery`;
- `grill-dashboard-requirements`;
- consumption-mode selection.

### Wave 2 — Holistic Performance & Reward foundation

Priority: immediate after Wave 1 begins; audience findings and P&R work may overlap where dependencies are explicit.

Questions:

- What enterprise outcomes does P&R influence?
- What is the causal chain from strategy and work architecture through performance, reward, career, trust, attraction, and retention?
- Which domains share measures, and which require separate ownership?
- How do BAU and non-BAU conditions alter the same value-driver tree?
- Which measures are outcomes, drivers, controls, context, or diagnostics?

Outputs:

- holistic value-driver tree;
- domain boundary map;
- BAU and non-BAU scenario catalogue;
- shared terminology;
- KPI classification framework;
- cross-domain business-question catalogue.

Skills enabled:

- `holistic-performance-reward-value-drivers`;
- `value-driver-modelling`;
- shared foundation for all specialist domains.

### Wave 3 — KPI and people-analytics foundation

Priority: parallel with Wave 2 after shared terminology is stable enough.

Questions:

- What must every KPI definition contain?
- Which aggregation, cohort, effective-date, and denominator failures are common in people analytics?
- How should outcome, driver, control, context, and diagnostic measures be separated?
- Which diagnostic patterns are appropriate for variance, contribution, distribution, cohort, concentration, and scenario analysis?
- How should sample size, confidence, privacy, and causality be handled?

Outputs:

- KPI-definition knowledge;
- calculation and aggregation guidance;
- analytical-method catalogue;
- diagnostic selection rules;
- metric anti-patterns;
- KPI and analytics benchmarks.

Skills enabled:

- `kpi-measure-design`;
- `people-analytics-diagnostics`;
- `metric-qa`.

### Wave 4 — Communication, visual, and experience foundation

Priority: build in parallel workstreams after audience framing is available.

#### Consulting communication

Questions:

- When should answer-first, Pyramid Principle, SCQA, issue trees, action titles, or decision matrices be used?
- Which claims are published methods, observed conventions, or repository synthesis?
- How should executive and diagnostic story structures differ?

Outputs:

- technique catalogue;
- selection matrix;
- storyline patterns;
- action-title guidance;
- executive and diagnostic examples.

#### Visual design

Questions:

- Which perceptual and hierarchy principles have empirical support?
- How should typography, colour, layout, density, data-ink, and accessibility be applied to Power BI?
- Which principles are stable and which are heuristics?

Outputs:

- visual hierarchy knowledge;
- typography and colour guidance;
- layout and accessibility patterns;
- anti-patterns.

#### Visualisation

Questions:

- Which chart or exhibit fits each analytical relationship and precision need?
- How should tables, distributions, variance, drivers, scenarios, and portfolios be shown?
- How should current IBCS guidance be applied selectively?

Outputs:

- relationship-to-chart map;
- chart and exhibit catalogue;
- current IBCS knowledge;
- misuse conditions.

#### Dashboard experience

Questions:

- How do guided, exploratory, action, and static products differ?
- What information architecture fits each audience and decision?
- How should overview, diagnosis, detail, and action be sequenced?

Outputs:

- information-architecture patterns;
- static, interactive, and hybrid design rules;
- audience-specific page patterns.

Skills enabled:

- consulting storyline and executive writing;
- visual hierarchy and chart selection;
- interactive and static design;
- accessibility and visual QA.

### Wave 5 — Initial specialist P&R domains

Priority: fixed reward, performance management, and variable reward first because they cover the highest-value initial dashboard scenarios.

#### Fixed reward

Research:

- salary structures and position measures;
- range penetration, compa-ratio, compression, new-hire premium, market movement, budget allocation, affordability, fairness, and exceptions;
- employee-level planning and governance.

#### Performance management

Research:

- process completion;
- rating distribution and differentiation;
- calibration;
- manager and cohort consistency;
- performance signal credibility;
- limitations of outcome interpretation.

#### Variable reward

Research:

- target opportunity;
- proration;
- enterprise and individual multipliers;
- rating differentiation;
- caps and controls;
- allocation, calibration, affordability, and employee-level outputs.

Outputs for each domain:

- value-driver branch;
- business questions;
- KPI catalogue and definitions;
- diagnostic patterns;
- audience treatment;
- BAU and non-BAU scenarios;
- governance and anti-patterns;
- corresponding skills and benchmarks.

### Wave 6 — Power BI implementation foundation

May begin in parallel with Wave 4 where visual concepts need feasibility checks.

Questions:

- What semantic-model patterns support effective-dated worker and reward data?
- Which DAX patterns are required for populations, time, variance, and distributions?
- Which interactions, tooltips, drill paths, field parameters, bookmarks, and export patterns are feasible and maintainable?
- What security, performance, accessibility, and static-export constraints affect design?
- Which current features need release-time verification?

Outputs:

- feasibility knowledge;
- semantic-model patterns;
- DAX patterns;
- interaction and export guidance;
- security and accessibility guidance;
- performance anti-patterns;
- implementation tests.

Skills enabled:

- `power-bi-feasibility`;
- semantic-model and DAX design;
- interaction, export, theme, performance, and security skills;
- Power BI verifier.

### Wave 7 — Remaining specialist domains

Develop after the shared foundation and initial domains are proving stable:

- market competitiveness;
- job architecture;
- pay equity;
- talent and retention;
- benefits and recognition;
- governance and controls;
- total rewards integration.

Order may change based on benchmark gaps and user demand.

### Wave 8 — Integrated refresh and release evidence

Runs during Phase 12 and Phase 13.

Questions:

- Which research assumptions failed in implementation?
- Are source records current?
- Are domains contradictory or duplicated?
- Does current Cursor and Power BI behaviour still match the knowledge packs?
- Are public examples and packages safe and licensed?

Outputs:

- refreshed sources and knowledge;
- contradiction resolutions;
- release evidence record;
- residual-risk register;
- next-version research backlog.

## Prioritised backlog

### Priority 0 — Required for foundational MVP

- current Cursor skills and subagents verification;
- audience and decision framework;
- holistic P&R value-driver tree;
- KPI-definition framework;
- consulting storyline selection;
- visual hierarchy;
- chart selection;
- interactive versus static design;
- Power BI feasibility.

### Priority 1 — Required for initial benchmark domains

- fixed reward;
- performance management;
- variable reward;
- executive summary patterns;
- Business Partner diagnostic patterns;
- manager action patterns;
- security and export.

### Priority 2 — Broaden analytical and implementation depth

- detailed diagnostics;
- semantic-model patterns;
- DAX patterns;
- accessibility;
- current IBCS;
- theme and layout implementation;
- complete assurance methods.

### Priority 3 — Expand specialist coverage

- market competitiveness;
- job architecture;
- pay equity;
- talent and retention;
- total rewards;
- governance and controls.

## Source plan by workstream

| Workstream | Preferred sources | Secondary use | Key caution |
|---|---|---|---|
| Cursor | official documentation and changelog | reproducible issue reports | current behaviour changes quickly |
| Power BI | Microsoft Learn and official product material | reproducible community cases | distinguish Desktop, Service, export, preview, and version |
| P&R professional practice | regulators, professional bodies, methodology owners, academic research | established consulting and vendor synthesis | commercial methods and samples vary |
| Consulting | original author and official firm publication | representative public examples | do not universalise firm-specific claims |
| Visual perception | original research and established texts | later reviews | do not convert rankings into absolute rules |
| Accessibility | recognised standards and official platform guidance | practitioner testing | separate compliance from aesthetic preference |
| Regulation | legislation and regulator guidance | legal commentary | jurisdiction and effective date are mandatory |
| Market data | approved licensed providers and public methodology | public labour data | do not reproduce licensed tables |

## Research record assignment

Every workstream should have:

```yaml
research_owner:
reviewer:
research_question:
decisions_supported:
downstream_artifacts:
source_classes:
freshness_requirement:
expected_outputs:
due_phase:
status:
```

One owner coordinates synthesis even where several subagents research in parallel.

## Parallelisation rules

Safe to parallelise:

- independent source searches for one research question;
- consulting, visual-design, and Power BI workstreams after audience foundations exist;
- separate specialist domains after shared terminology is defined;
- evidence gathering and implementation experiments where outputs are reconciled.

Do not parallelise without a shared foundation:

- competing definitions of the same KPI;
- domain boundaries;
- audience taxonomy;
- schema field semantics;
- release compatibility decisions;
- one artifact edited concurrently by several agents without merge ownership.

## Research subagent contract

Input:

```yaml
task:
research_question:
decisions_supported:
scope:
exclusions:
required_sources:
freshness:
existing_authorities:
required_output:
maximum_detail:
```

Return:

```yaml
executive_summary:
findings:
selection_rules:
claims_matrix:
techniques_considered:
techniques_rejected:
conflicts_and_gaps:
recommended_repository_changes:
sources:
next_review_trigger:
```

The parent or research owner reconciles parallel returns into one authority.

## Research review gates

### Development-ready synthesis

- research question and consumer are clear;
- primary sources are represented;
- material uncertainty is visible;
- definitions and selection rules are usable;
- public-repository constraints are satisfied;
- no known critical contradiction remains.

This is enough to support draft skills.

### Review-ready knowledge

- claims matrix complete;
- source diversity and freshness appropriate;
- domain overlap reviewed;
- examples and benchmark cases exercise the knowledge;
- implementation feedback incorporated;
- no unresolved major finding.

### Release-ready knowledge

- required independent review complete;
- current sources reverified;
- mandatory dependencies approved;
- package includes required provenance and licences;
- no critical or major release finding remains.

## Stop conditions

Stop and ask for a decision when:

- the work depends on organisation policy not supplied;
- licensed content cannot be used safely;
- jurisdictions conflict materially;
- several definitions remain valid and the choice affects outputs;
- data availability makes the intended KPI infeasible;
- research reveals a privacy, legal, or security risk;
- downstream scope has changed materially.

Stop additional source gathering when:

- high-quality evidence converges;
- new sources repeat established claims;
- selection rules and limitations are stable;
- the remaining gap requires implementation testing rather than more reading;
- cost or licence access exceeds the value for the current phase.

## Rework triggers

Reopen research when:

- official product behaviour changes;
- regulation or policy changes;
- a benchmark exposes a contradiction;
- a skill cannot use the knowledge without hidden assumptions;
- implementation proves a proposed pattern infeasible;
- a domain pack duplicates another authority;
- a source is withdrawn, superseded, or found unreliable;
- a release expands jurisdiction or audience.

## Review cadence

| Content | Default cadence |
|---|---|
| Cursor and Power BI current behaviour | before activation and each release candidate |
| Preview or beta product features | each material use |
| Regulation | before affected release and when change is announced |
| Market movement | each relevant effective period |
| Audience and project architecture | after initial benchmark implementation and major version changes |
| Stable research | when later evidence or implementation materially challenges it |
| P&R domain knowledge | at least each major release and when policy or market practice changes |

## Research completion measures

Track:

- workstreams with a defined decision use;
- required primary-source coverage;
- claims with confidence and limitations;
- duplicate definitions found and resolved;
- knowledge packs consumed successfully by skills;
- benchmark failures caused by missing or weak research;
- stale current-product sources;
- unresolved cross-domain contradictions;
- proprietary or restricted material safely excluded;
- research handoff completeness.

Avoid measuring success by source count or document length alone.

## Initial assignments

### Next workstream 1

```yaml
workstream: audience-and-decision
outputs:
  - audience archetypes
  - decision modes
  - consumption modes
  - discovery questions
skills_enabled:
  - audience-decision-framing
  - dashboard-discovery
  - grill-dashboard-requirements
```

### Next workstream 2

```yaml
workstream: holistic-performance-reward
outputs:
  - value-driver tree
  - domain boundaries
  - BAU and non-BAU scenarios
  - KPI classification
skills_enabled:
  - holistic-performance-reward-value-drivers
  - value-driver-modelling
```

### Next workstream 3

```yaml
workstream: kpi-and-analytics
outputs:
  - KPI definition framework
  - diagnostic method catalogue
  - metric anti-patterns
skills_enabled:
  - kpi-measure-design
  - people-analytics-diagnostics
  - metric-qa
```

These may overlap after terminology and ownership are agreed.

## Anti-patterns

- Researching all 49 skills before building any.
- Treating source quantity as quality.
- Letting each domain invent its own shared terminology.
- Copying proprietary frameworks into the public repository.
- Using one consulting firm as the universal design authority.
- Treating current product documentation as permanently stable.
- Completing research without a downstream artifact.
- Keeping research only in a subagent transcript.
- Skipping negative or contradictory evidence.
- Using implementation anecdotes as universal truth.
- Waiting until Phase 12 to validate all source links and metadata.

## Draft acceptance assessment

This draft defines:

- workstreams and eight research waves;
- prioritised backlog;
- source strategy;
- assignments and parallelisation;
- research handoffs;
- development, review, and release gates;
- stop and rework conditions;
- cadence and completion measures;
- immediate next workstreams.

It must be reconciled with the implementation roadmap, actual knowledge inventory, research-record schema, and available contributors before status changes.
