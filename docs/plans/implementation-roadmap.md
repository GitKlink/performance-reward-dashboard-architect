---
artifact_id: PLAN-CORE-002
status: PLACEHOLDER
phase: 1
priority: high
depends_on:
  - artifact_id: CTRL-CORE-001
    path: ../../BUILD-ORDER.md
  - artifact_id: ARCH-CORE-001
    path: ../architecture/agent-architecture.md
  - artifact_id: ARCH-CORE-003
    path: ../architecture/skill-routing-model.md
blocks:
  - milestone planning
content_version: 0.1.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Implementation roadmap

## Document state

This is the first substantive roadmap draft. The lifecycle status remains `PLACEHOLDER` until the Phase 1 architecture set is reconciled and the first Phase 2 milestone begins.

## Purpose

Translate the build order and architecture into manageable milestones that produce a useful Cursor agent before the complete 49-skill catalogue is finished.

## Delivery strategy

### Build a coherent vertical slice first

The first usable agent should support a complete workflow for a limited set of high-value dashboard scenarios:

```text
ambiguous request
→ audience and decision framing
→ holistic or specialist P&R question
→ KPI and analytical design
→ storyline and visual design
→ static or interactive page specification
→ Power BI feasibility
→ design review and implementation handoff
```

### Do not activate the whole scaffold at once

The initial public release should contain a tested core rather than dozens of shallow skills.

### Keep development gates lightweight

- automated repository validation runs continuously;
- each artifact receives enough local testing to support the next dependency;
- comprehensive cross-system testing occurs in Phase 12;
- final approval occurs in Phase 13.

### Use implementation to refine standards

Architecture, schemas, and standards remain drafts while foundational skills and benchmarks expose weaknesses.

## MVP boundary

### Required for `v0.1.0`

#### Runtime coordination

- one thin project orchestrator rule;
- three focused subagents where current Cursor behaviour supports them;
- bounded handoff and context-management rules.

#### Foundational skills

- `audience-decision-framing`;
- `dashboard-discovery`;
- `value-driver-modelling`;
- `kpi-measure-design`;
- `holistic-performance-reward-value-drivers`;
- `consulting-storyline`;
- `visual-hierarchy-design`;
- `chart-selection`;
- interactive-versus-static design capability;
- `power-bi-feasibility`;
- one dashboard critique capability.

#### Initial P&R coverage

- holistic P&R foundation;
- fixed reward;
- performance management;
- variable reward at a level sufficient for the initial benchmarks.

#### Output contracts

- audience and decision profile;
- KPI definition;
- dashboard brief;
- page specification;
- visual specification;
- design review;
- implementation handoff.

#### Benchmarks

- executive fixed-reward summary;
- executive performance summary;
- Business Partner diagnostic;
- manager action dashboard;
- static executive export;
- routing and privacy adversarial cases.

#### Validation and release

- skill metadata validation;
- schema validation;
- package dependency closure;
- integrated evaluation suite;
- release manifest and migration guidance.

### Deferred beyond `v0.1.0` where necessary

- complete specialist coverage for every P&R domain;
- marketplace or plugin distribution;
- advanced organisation overlay tooling;
- every consulting technique as a separate skill;
- exhaustive Power BI DAX pattern library;
- generated visual mockups for every pattern;
- automated scoring of subjective design quality;
- multilingual support;
- industry-specific regulatory packs.

Deferred items may still be included when they are required by an initial benchmark and can be completed without destabilising the core.

## Milestones

### Milestone 0 — Repository foundation

Status: provisionally complete for development.

Deliverables:

- repository scaffold;
- build and dependency controls;
- naming, research, and citation standards;
- artifact and source registers;
- five standards trials;
- validation scripts, tests, and CI;
- safe placeholder behaviour.

Exit criteria:

- internal critical and major defects resolved;
- CI green;
- development unblocked;
- comprehensive review tracked for Phase 12.

### Milestone 1 — Architecture and standards

Status: in progress.

Deliverables:

- agent architecture;
- context-management strategy;
- skill-routing model;
- repository information architecture;
- release architecture;
- skill-authoring standard;
- example-authoring standard;
- evaluation standard;
- research program;
- implementation roadmap;
- release plan.

Exit criteria:

- architecture files contain substantive draft content;
- component responsibilities do not materially overlap;
- draft route traces cover executive, Business Partner, manager, KPI-only, and critique tasks;
- draft standards define usable field contracts and checks;
- current Cursor-sensitive assumptions are identified;
- immediate Phase 2 deliverables are clear;
- CI remains green.

### Milestone 2 — Output contracts and templates

Deliverables:

- research-record schema and template;
- audience and decision schema and template;
- KPI-definition schema and template;
- dashboard-brief schema and template;
- page and visual specification schemas and templates;
- design-review schema and template;
- implementation-handoff schema and template;
- schema validator and tests.

Entry criteria:

- architecture and standards drafts are usable;
- field ownership is clear.

Exit criteria:

- schemas parse and validate;
- templates map one-to-one to schema fields;
- one end-to-end synthetic workflow uses the contracts;
- version and migration fields are defined;
- validator passes.

### Milestone 3 — Audience and holistic P&R foundation

Deliverables:

- audience archetypes;
- decision-mode catalogue;
- consumption-mode framework;
- discovery question bank;
- holistic P&R value-driver tree;
- domain boundary map;
- BAU and non-BAU scenarios;
- KPI classification framework;
- initial audience and value-driver examples.

Skills developed as controlled drafts:

- `audience-decision-framing`;
- `dashboard-discovery`;
- `grill-dashboard-requirements`;
- `value-driver-modelling`;
- `holistic-performance-reward-value-drivers`.

Exit criteria:

- audience and decision profile can be produced from realistic prompts;
- cross-domain requests route coherently;
- domain boundaries are explicit;
- manager, Business Partner, and executive needs are distinguishable;
- foundational routing tests pass locally.

### Milestone 4 — KPI, analytics, and initial domain knowledge

Deliverables:

- KPI-definition knowledge;
- analytical and diagnostic method catalogue;
- metric anti-patterns;
- fixed-reward knowledge pack;
- performance-management knowledge pack;
- variable-reward knowledge pack;
- initial domain KPI definitions and examples.

Skills developed:

- `kpi-measure-design`;
- `people-analytics-diagnostics`;
- `metric-qa`;
- fixed-reward analysis;
- performance-management analysis;
- variable-reward analysis.

Exit criteria:

- benchmark metrics have complete definitions;
- calculation and population risks are visible;
- new-hire premium and other trial concepts are reconciled into domain knowledge;
- specialist and holistic definitions do not materially conflict;
- at least one scenario per initial domain passes a development smoke test.

### Milestone 5 — Communication, visual, and dashboard experience

Deliverables:

- consulting technique catalogue;
- storyline and action-title rules;
- visual hierarchy, typography, colour, layout, data-ink, and accessibility knowledge;
- relationship-to-chart map;
- chart and exhibit catalogue;
- current IBCS treatment;
- static, interactive, hybrid, executive, Business Partner, and manager patterns.

Skills developed:

- consulting storyline;
- executive message writing;
- visual hierarchy;
- chart selection;
- information architecture;
- static report design;
- interactive dashboard UX;
- accessibility and visual QA.

Exit criteria:

- the same P&R question produces materially different products for different audiences;
- chart recommendations state analytical relationship and misuse conditions;
- static pages are self-contained and export-safe;
- interactive pages preserve context and support diagnosis;
- visual and communication choices are traceable to selection rules.

### Milestone 6 — Power BI implementation foundation

Deliverables:

- Power BI feasibility knowledge;
- semantic-model patterns;
- DAX patterns required by initial benchmarks;
- interaction and export guidance;
- security, accessibility, performance, and theme guidance;
- implementation handoff examples.

Skills developed:

- `power-bi-feasibility`;
- semantic-model design;
- DAX measure design;
- interaction build;
- export design;
- performance;
- security;
- theme and layout;
- implementation review.

Exit criteria:

- benchmark designs have plausible implementation paths;
- data grain and effective-date assumptions are explicit;
- employee-level workflows identify security requirements;
- static export limitations are tested;
- implementation handoffs are complete enough for a Power BI developer.

### Milestone 7 — Runtime orchestrator and subagents

Deliverables:

- main project rule;
- decision on `AGENTS.md`;
- research synthesiser;
- dashboard design critic;
- Power BI verifier;
- active foundational skill metadata;
- explicit commands where adopted;
- runtime context and handoff integration.

Entry criteria:

- foundational skills and schemas operate as drafts;
- current Cursor metadata is reverified.

Exit criteria:

- skills are discoverable and explicit invocation works;
- automatic routing passes initial cases;
- subagents return bounded structured outputs;
- placeholder runtime components remain inactive;
- context-loading behaviour is acceptable;
- a complete workflow runs in a clean Cursor workspace.

### Milestone 8 — Benchmark suite and integrated correction

Corresponds to Phase 12.

Deliverables:

- complete evaluation schemas and records;
- routing, skill, audience, domain, Power BI, privacy, and release scenarios;
- independent review;
- cross-skill contradiction report;
- context-load report;
- regression suite;
- corrected release candidate.

Exit criteria:

- no unresolved critical or major finding;
- release thresholds met;
- regressions pass;
- current Cursor and Power BI assumptions verified;
- package profiles build successfully;
- runtime and mandatory dependencies ready for approval.

### Milestone 9 — Release `v0.1.0`

Corresponds to Phase 13.

Deliverables:

- approved runtime artifacts;
- release manifest;
- minimal and standard package profiles;
- migration and rollback notes;
- checksums;
- release notes;
- tagged source commit.

Exit criteria:

- final package tests pass;
- privacy, security, licence, and compatibility checks pass;
- release authority records approval;
- `v0.1.0` published.

## Dependency-aware sequence

```text
M0 foundation
→ M1 architecture
→ M2 schemas
→ M3 audience and holistic P&R
→ M4 KPI and initial P&R domains
→ M5 communication, visual, and experience
→ M6 Power BI
→ M7 runtime orchestration
→ M8 integrated evaluation
→ M9 release
```

Permitted overlap:

- M3 audience and holistic P&R research may run in parallel after shared ownership is clear;
- M4 KPI research may begin while M3 domain boundaries stabilise;
- M5 consulting, visual, and experience workstreams may run in parallel;
- M6 Power BI feasibility may begin early for designs that require validation;
- evaluation fixtures should be added throughout development even though comprehensive execution occurs in M8.

## Milestone deliverable checklist

Every milestone should produce:

- governed artifacts with IDs and status;
- updated artifact dependencies;
- source records where external claims are used;
- validation or benchmark evidence appropriate to the stage;
- updated status and changelog;
- explicit open questions;
- next-action handoff.

## Definition of done for development milestones

A development milestone is done when:

- planned substantive artifacts exist;
- no known critical defect remains;
- material assumptions are visible;
- downstream work can proceed without conversation memory;
- relevant local tests pass;
- repository CI is green;
- status and dependencies are current.

It does not require final independent approval unless it is M8 or M9.

## Work ownership

Each active artifact should have one integration owner even when research or drafting is parallelised.

Roles:

| Role | Responsibility |
|---|---|
| Product decision owner | confirms scope, priorities, and user-facing trade-offs |
| Artifact owner | integrates content and resolves conflicts |
| Research contributor | gathers and synthesises evidence |
| Skill author | implements procedure and references |
| Benchmark author | creates scenarios and expected results |
| Technical verifier | checks Cursor or Power BI implementation |
| Independent reviewer | reviews integrated release candidate |
| Release authority | records final approval |

One person may perform several roles during development, but Phase 12 independent review must preserve meaningful separation.

## Resourcing assumptions

- The project is primarily developed through Cursor and connected agents.
- The user remains the decision owner for product scope and business trade-offs.
- Deep research is delegated into bounded workstreams.
- No background work is assumed unless explicitly scheduled or executed through available tooling.
- Current product facts require internet access and official sources.
- Power BI feasibility may require practical testing outside static documentation.
- Organisation-specific P&R policy is not assumed from the public repository.

## Risk register

| Risk | Probability | Impact | Mitigation | Trigger |
|---|---|---|---|---|
| Scope expands to all 49 skills before a usable core exists | high | high | enforce MVP boundary and milestone sequence | new skills added without benchmark need |
| Architecture becomes a large monolithic prompt | medium | high | thin rule, skills, knowledge, context tests | rules duplicate methods or knowledge |
| Cursor product behaviour changes | high | medium-high | release-time verification and compatibility manifest | new Cursor release or failed discovery |
| P&R domains overlap or contradict | medium | high | holistic value-driver and domain boundary authority | duplicate KPI definitions |
| Schemas churn after many skills depend on them | medium | high | prototype schemas before broad activation | repeated local field additions |
| Over-testing slows development | medium | medium | local smoke checks; comprehensive Phase 12 testing | formal review demanded for every draft |
| Too little early testing creates unusable integration | medium | high | continuous CI and representative vertical slices | downstream work cannot consume outputs |
| Public repository exposes confidential material | low-medium | critical | synthetic-data, redaction, licence and release checks | screenshots or real values committed |
| Skills trigger too broadly | high | high | description standard, routing cases, pruning | unrelated prompts invoke multiple skills |
| Context overload degrades long workflows | high | high | context strategy and handoffs | repeated questions or contradictions |
| Power BI design is visually strong but infeasible | medium | high | early feasibility checks and verifier | unsupported interaction or export dependency |
| Examples overfit evaluation | medium | medium | acceptable alternatives and adversarial cases | outputs copy benchmark phrasing |
| One long-lived PR becomes difficult to review | high | medium | create phase branches or smaller PRs after foundation | changed-file count obscures new work |
| Standards remain placeholders indefinitely | medium | medium | reconciliation checkpoint after foundational trials | content exists but status never matures |

## Immediate risk action

The current foundation PR is already large. After Phase 1 draft completion, prefer:

- merging the foundation branch when CI is green and repository safety is confirmed; or
- starting a new phase branch from the foundation head if merge timing requires further user review.

Do not continue all later phases indefinitely in one unbounded pull request.

## Progress reporting

### `STATUS.md`

Update when:

- phase or milestone changes;
- a major deliverable completes;
- validation status changes;
- a new blocker appears;
- the immediate next action changes.

### `CHANGELOG.md`

Update for notable architecture, capability, schema, validation, or release changes.

### Artifact register

Update IDs, paths, status, phase, and direct dependencies.

### Pull request

Summarise:

- delivered result;
- status and limitations;
- tests and validation;
- review focus;
- next work.

### Milestone status format

```yaml
milestone:
status:
completed:
in_progress:
blocked:
validation:
risks:
next_action:
```

## Reprioritisation process

Reprioritise when:

- user demand changes MVP value;
- a benchmark exposes missing foundation;
- Cursor or Power BI changes invalidate architecture;
- a domain proves larger than expected;
- release safety requires earlier work;
- a high-value vertical slice can be completed sooner.

Process:

1. identify the decision and evidence;
2. assess dependency impact;
3. update MVP boundary if required;
4. update build order only when the sequence itself changes;
5. update roadmap and status;
6. preserve deferred work in backlog;
7. avoid adding unowned scope.

## Context and handoff strategy

Create a major handoff:

- at each milestone boundary;
- before switching to a large new domain;
- when the active context shows degradation;
- when work passes to a new agent or contributor;
- before integrated evaluation.

Handoffs reference artifacts rather than duplicating them.

## Current milestone checklist

### Milestone 1 — Remaining work

- [x] agent architecture draft;
- [x] context-management strategy draft;
- [x] skill-routing model draft;
- [x] repository information architecture draft;
- [x] release architecture draft;
- [x] skill-authoring standard draft;
- [x] example-authoring standard draft;
- [x] evaluation standard draft;
- [x] research program draft;
- [x] implementation roadmap draft;
- [ ] release plan draft;
- [ ] cross-artifact consistency pass;
- [ ] current Cursor component verification pass;
- [ ] artifact register and status reconciliation;
- [ ] decide branch and pull-request transition into Milestone 2.

## Draft acceptance assessment

This roadmap defines:

- MVP and deferred scope;
- ten milestones;
- deliverables, entry criteria, and exit criteria;
- permitted parallel work;
- ownership and resourcing;
- risk register;
- progress reporting;
- reprioritisation and handoffs;
- current Milestone 1 checklist.

It must be updated after the Phase 1 consistency pass and before Milestone 2 begins.
