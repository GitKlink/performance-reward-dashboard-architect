---
artifact_id: ARCH-CORE-001
status: PLACEHOLDER
phase: 1
priority: critical
depends_on:
  - artifact_id: STD-CORE-001
    path: ../standards/naming-standard.md
  - artifact_id: STD-CORE-002
    path: ../standards/research-standard.md
  - artifact_id: STD-CORE-003
    path: ../standards/citation-standard.md
  - artifact_id: EX-CORE-001
    path: ../../knowledge/research-register/trials/cursor-rules-and-skills-trial.md
  - artifact_id: EX-CORE-002
    path: ../../knowledge/research-register/trials/internal-source-of-truth-decision-trial.md
blocks:
  - ARCH-CORE-002
  - ARCH-CORE-003
  - STD-CORE-004
  - final Cursor agent structure
content_version: 0.1.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Agent architecture

## Document state

This is the first substantive architecture draft. The lifecycle status remains `PLACEHOLDER` until the complete Phase 1 architecture set has been drafted and reconciled in the artifact register.

## Purpose

Define the Cursor-native component architecture for the Performance & Reward Dashboard Architect.

The architecture must allow the agent to move from an ambiguous dashboard request to an implementable Power BI design while keeping domain knowledge, methods, visual standards, implementation constraints, and quality assurance modular and maintainable.

## Product mission

The agent helps users design Performance & Reward decision products for:

- executives and committees;
- Business Partners;
- people managers;
- Reward Partners;
- Performance & Reward specialists;
- people-analytics and reporting teams.

It supports:

- interactive Power BI dashboards;
- static or deck-style Power BI pages;
- hybrid reports that combine guided summary pages with exploratory diagnostics;
- design critique and redesign;
- dashboard requirements discovery;
- KPI and analytical architecture;
- implementation handoff.

The agent does not merely recommend charts. It connects:

```text
Audience
→ decision and action
→ Performance & Reward question
→ value-driver and diagnostic logic
→ measures and comparators
→ consumption mode
→ storyline and visual form
→ Power BI implementation
→ quality assurance
```

## Non-goals

The agent is not intended to:

- make remuneration, performance, employment, or legal decisions on behalf of accountable people;
- replace organisation-specific policy or governance approval;
- infer employee-level conclusions from incomplete or inappropriate data;
- create final DAX or semantic models without sufficient source and grain information;
- treat consulting methods as universal rules;
- force every dashboard into one visual style;
- load the complete knowledge repository into every conversation;
- present draft repository content as approved external fact.

## Architecture principles

### 1. Thin orchestrator, thick capabilities

The persistent project rule coordinates the workflow but does not contain full domain knowledge or detailed design methods.

Cursor project rules are persistent reusable instructions stored under `.cursor/rules`.[^cursor-rules] Persistent context should therefore remain concise and stable.

Detailed methods belong in dynamically selected Agent Skills. Cursor describes skills as `SKILL.md` packages that can contain instructions, scripts, and commands and can be discovered when relevant.[^cursor-skills]

### 2. One authority per concept

Each concept has one owning artifact:

- architecture owns component boundaries;
- standards own authoring and governance rules;
- knowledge packs own subject-matter content;
- schemas own output fields and constraints;
- skills own procedures and selection logic;
- templates render schemas for human use;
- examples demonstrate behaviour;
- evaluations test behaviour.

### 3. Decision-first routing

The agent identifies audience, decision, action, and consumption mode before selecting metrics or visuals.

### 4. Progressive context loading

Only the minimum relevant rules, skills, knowledge references, examples, and schemas should enter the active context.

### 5. Evidence and project judgement remain separate

External research, repository synthesis, organisation-specific policy, and user decisions must not be blended into one apparent source of truth.

### 6. Drafts guide development; approval governs release

Draft architecture and knowledge may support controlled downstream authoring. Runtime release components and mandatory dependencies require approval before `v0.1.0`.

### 7. Human accountability remains explicit

The agent recommends, challenges, structures, and verifies. The user owns business decisions, policy choices, data access, and final approval.

## Component model

```text
┌─────────────────────────────────────────────────────────────┐
│ User request, repository context, and project artifacts     │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ Thin project orchestrator rule                              │
│ - classify request                                          │
│ - establish audience and decision                           │
│ - select skills and subagents                               │
│ - maintain workflow state                                   │
│ - enforce output and safety gates                           │
└───────────────┬──────────────────────┬──────────────────────┘
                │                      │
                ▼                      ▼
┌──────────────────────────┐  ┌───────────────────────────────┐
│ Agent Skills             │  │ Context-isolated subagents    │
│ - reusable methods       │  │ - deep research               │
│ - domain procedures      │  │ - independent critique        │
│ - output production      │  │ - Power BI verification       │
└───────────────┬──────────┘  └──────────────┬────────────────┘
                │                            │
                └──────────────┬─────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ Governed repository support                                 │
│ knowledge │ schemas │ templates │ examples │ scripts        │
└──────────────────────────────┬──────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ Quality assurance and implementation handoff                │
│ evidence │ metric │ visual │ audience │ Power BI │ release  │
└─────────────────────────────────────────────────────────────┘
```

## Component responsibilities

### Project orchestrator rule

**Location**

```text
.cursor/rules/performance-reward-dashboard-architect.mdc
```

**Responsibilities**

- establish the user's objective, audience, decision, action, and constraints;
- identify the Performance & Reward domain and value-driver branch;
- determine static, interactive, or hybrid consumption;
- select and sequence the minimum sufficient skills;
- delegate context-heavy work to subagents;
- maintain assumptions, open questions, and workflow stage;
- enforce schema-backed outputs;
- require appropriate quality checks;
- stop activation or release of placeholders;
- preserve user ownership of decisions.

**Must not contain**

- full KPI catalogues;
- every consulting method;
- every visual pattern;
- detailed Power BI documentation;
- extensive worked examples;
- organisation-specific confidential rules;
- duplicated skill instructions.

### Agent Skills

**Location**

```text
.cursor/skills/<capability-group>/<skill-name>/SKILL.md
```

**Use for**

- repeatable methods;
- domain-specific analytical workflows;
- consulting and visual-design techniques;
- schema-backed artifact creation;
- explicit review procedures;
- reusable scripts or assets.

**Skill contract**

Each active skill will eventually define:

- purpose and bounded responsibility;
- invocation and non-invocation conditions;
- required inputs;
- missing-information behaviour;
- method and selection rules;
- knowledge references;
- output schema;
- anti-patterns;
- quality checks;
- representative examples;
- version and status.

**Selection principle**

Invoke the minimum sufficient set. A skill is not loaded merely because its topic is broadly related.

### Subagents

**Location**

```text
.cursor/agents/<role-name>.md
```

Cursor introduced subagents as independent agents with separate context for discrete specialised work.[^cursor-skills]

The initial architecture uses three custom roles:

| Subagent | Purpose | Typical trigger |
|---|---|---|
| Research synthesiser | Deep evidence gathering and concise synthesis | current, disputed, niche, or source-intensive question |
| Dashboard design critic | Independent challenge of story, audience fit, density, and design logic | design review or pre-handoff quality check |
| Power BI verifier | Implementation feasibility, model, DAX, interaction, security, accessibility, performance, and export review | implementation plan or final design verification |

**Subagent rules**

- receive a bounded task and explicit output contract;
- receive only relevant context and repository paths;
- return concise findings, not full conversation transcripts;
- do not become a source of truth;
- cite evidence or repository authorities;
- identify assumptions and unresolved questions;
- do not silently modify governance decisions.

**Do not delegate when**

- the task is short and deterministic;
- the parent already has the required context;
- delegation cost exceeds the likely benefit;
- the task depends on active interactive decisions from the user;
- a skill or script provides the complete method.

### Knowledge packs

**Location**

```text
knowledge/
```

**Own**

- audience archetypes;
- Performance & Reward value-driver models;
- domain definitions and KPI catalogues;
- consulting-method evidence;
- visual-design and visualisation research;
- Power BI capability and constraint knowledge;
- governance and risk information.

**Do not own**

- invocation logic;
- final user-facing artifact layout;
- runtime orchestration;
- duplicated copies of source content.

Knowledge packs are referenced by skills and loaded only when relevant.

### Schemas

**Location**

```text
schemas/
```

Schemas define machine-readable output contracts for:

- research records;
- audience and decision profiles;
- KPI definitions;
- dashboard briefs;
- page and visual specifications;
- design reviews;
- implementation handoffs.

Schemas own field meaning, required values, status, and compatibility rules. Templates and skills consume them.

### Templates

**Location**

```text
templates/
```

Templates provide usable Markdown or structured forms that implement schemas. They do not redefine fields or add hidden policy.

### Examples

**Location**

```text
examples/
```

Examples demonstrate approved or draft methods using synthetic data. They are selected by audience, decision mode, domain, and consumption mode.

Examples do not become universal patterns merely because they exist.

### Evaluations

**Location**

```text
evaluations/
```

Evaluations contain:

- benchmark prompts;
- expected behaviours;
- acceptable alternatives;
- critical failure conditions;
- routing tests;
- regression results.

Comprehensive testing is concentrated in Phase 12.

### Scripts and CI

**Location**

```text
scripts/
.github/workflows/
```

Scripts provide deterministic checks and generation utilities. They enforce documented standards but do not create hidden policy.

Current checks cover artifact dependencies, source records, internal links, and unit tests. Later checks will cover schemas, active skill metadata, status indexes, package contents, and regression execution.

### Commands

Commands are optional explicit workflows for common user actions, such as reviewing a dashboard or creating a dashboard brief.

They are added only when they improve discoverability without duplicating a skill. The exact current Cursor command format remains a Phase 1 verification item.

## Authority hierarchy

When artifacts conflict, use this order:

1. User's explicit decision, where lawful and within scope
2. Approved organisation-specific policy supplied for the project
3. Approved repository controls and architecture
4. Approved schemas and standards
5. Approved knowledge packs
6. Approved skill procedures
7. Draft repository artifacts with visible status and limitations
8. Examples
9. Model inference

External evidence does not override the user's organisation-specific policy automatically. The agent must identify the conflict and require a decision.

A later downstream artifact cannot silently redefine an upstream authority.

## Runtime and development boundary

### Maintained source repository

The repository contains:

- runtime Cursor components;
- supporting knowledge;
- schemas and templates;
- evidence records;
- examples and evaluations;
- validation scripts;
- architecture and governance documentation.

### Runtime package

The minimum runtime package is expected to contain:

```text
.cursor/
knowledge/               # only knowledge required by packaged skills
schemas/                 # runtime output contracts
 templates/              # required output templates
README.md
LICENSE
```

The exact package is defined later in `ARCH-CORE-005`.

Development-only trials, incomplete examples, internal review records, and test fixtures may remain outside the release package.

## Orchestration workflow

### Stage 1 — Intake

Capture:

- user request;
- current artifact or screenshot where provided;
- available data and model constraints;
- deadline and expected deliverable;
- known policy or governance constraints.

### Stage 2 — Audience and decision framing

Determine:

- primary and secondary audiences;
- decision owner;
- decision or action;
- decision frequency;
- reading time;
- required detail;
- consequences of error;
- exclusions.

If these are unknown and materially affect design, the agent asks targeted questions or uses a structured discovery skill.

### Stage 3 — Performance & Reward framing

Determine:

- domain;
- value-driver branch;
- primary business question;
- outcome, driver, control, and context measures;
- BAU or non-BAU condition;
- governance and privacy risk.

### Stage 4 — Analytical architecture

Define:

- grain and population;
- metric definitions;
- comparators and targets;
- time logic;
- segmentation;
- diagnostic methods;
- known limitations;
- evidence requirements.

### Stage 5 — Consumption mode

Select:

- static;
- interactive;
- hybrid.

Then select the experience mode:

- executive decision product;
- Business Partner diagnostic product;
- manager action product;
- specialist analytical or operational product.

### Stage 6 — Story and visual form

Define:

- governing message or page question;
- page sequence;
- information hierarchy;
- chart and exhibit patterns;
- interaction model;
- commentary and action treatment;
- accessibility requirements.

### Stage 7 — Power BI feasibility

Validate:

- semantic-model feasibility;
- DAX complexity;
- interaction support;
- export behaviour;
- row-level security;
- performance;
- accessibility;
- maintainability.

### Stage 8 — Quality assurance

Review:

- decision usefulness;
- audience fit;
- P&R accuracy;
- metric integrity;
- analytical sufficiency;
- story and hierarchy;
- density and usability;
- accessibility;
- implementation feasibility;
- governance and evidence.

### Stage 9 — Output and handoff

Produce one or more schema-backed artifacts:

- dashboard brief;
- KPI specification;
- page architecture;
- visual and interaction specification;
- implementation handoff;
- design-review report;
- executive storyline.

## Routing dimensions

The routing model uses six dimensions:

| Dimension | Examples |
|---|---|
| Audience | executive, Business Partner, manager, Reward Partner, specialist |
| Decision mode | monitor, diagnose, compare, decide, plan, allocate, calibrate, forecast, govern, execute |
| Performance & Reward domain | performance, fixed reward, variable reward, market, job architecture, equity, talent, total rewards, governance |
| Consumption mode | static, interactive, hybrid |
| Workflow stage | discovery, analysis, design, implementation, review |
| Requested output | brief, KPI definition, wireframe, page specification, critique, handoff |

The detailed routing logic belongs in `ARCH-CORE-003`.

## Core design modes

### Executive decision product

Characteristics:

- conclusion-led;
- few decision-relevant measures;
- strong comparator and variance logic;
- explicit implications and actions;
- dominant exhibit or evidence hierarchy;
- guided reading order;
- low or tightly controlled interaction;
- export-safe presentation quality.

### Business Partner diagnostic product

Characteristics:

- overview followed by segmentation and diagnosis;
- distributions, cohorts, peers, and driver analysis;
- moderate to high interaction;
- drill-through and export where useful;
- enough context to support stakeholder conversations;
- transparent definitions and limitations.

### Manager action product

Characteristics:

- accountable population;
- prioritised exceptions and deadlines;
- team and employee detail where authorised;
- guided workflow;
- simple contextual definitions;
- strong security and privacy;
- clear handoff or completion action.

### Specialist analytical product

Characteristics:

- deeper methodological and data-quality detail;
- flexible segmentation and validation;
- explicit calculation logic;
- diagnostic and reconciliation views;
- less presentation simplification where precision requires detail.

## Human decision points

The agent requires explicit user ownership for:

- target audience priority where audiences conflict;
- business decision and action;
- organisation-specific policy interpretation;
- KPI thresholds and tolerance bands;
- confidentiality and access rules;
- acceptable metric proxies;
- trade-offs between simplicity and diagnostic depth;
- final visual and interaction choices where multiple valid options exist;
- release approval.

The agent may recommend a default but must identify it as a recommendation.

## Assumptions and uncertainty

Every major output should distinguish:

- confirmed fact;
- repository standard;
- user decision;
- project assumption;
- external evidence;
- inference;
- unresolved question;
- implementation risk.

Missing information is handled according to materiality:

- proceed with a labelled assumption when reversible and low risk;
- ask the user when the decision materially affects the product;
- research when the fact is externally verifiable and current;
- stop when privacy, legality, policy, or calculation integrity cannot be protected.

## Context strategy boundary

This architecture sets the principle; `ARCH-CORE-002` defines the detailed mechanism.

The main context should contain:

- current request and agreed brief;
- active decisions and assumptions;
- relevant skill instructions;
- concise subagent returns;
- current working artifacts.

It should not contain:

- every P&R metric;
- all consulting research;
- the complete visual pattern catalogue;
- full Power BI documentation;
- large unrelated examples;
- full research transcripts.

## Privacy and safety

The architecture assumes Performance & Reward work may involve sensitive employee and remuneration data.

Rules:

- public repository examples use synthetic data;
- employee-level detail is included only where the audience, decision, and access model require it;
- recommendations identify privacy, confidentiality, and minimum-cell risks;
- the agent does not infer protected attributes or sensitive employee conclusions from inadequate data;
- organisation-specific confidential policies are not committed to the public repository;
- implementation handoffs identify row-level security and export risks;
- legal and regulatory questions require current authoritative evidence and accountable review.

## Representative workflow traces

### Trace A — Executive fixed-reward static summary

```text
Audience: executive committee
Decision: endorse or redirect reward investment
Domain: fixed reward
Mode: static or hybrid
Skills: audience framing → fixed reward analysis → KPI design → storyline → executive exhibit → static design → Power BI feasibility → executive readability review
Output: action-led summary page and implementation specification
```

Expected architecture behaviour:

- prioritise affordability, allocation, market risk, fairness, and material exceptions;
- use a small number of linked measures and comparators;
- avoid employee-level detail on the summary;
- make the required decision explicit;
- ensure export-safe layout.

### Trace B — Business Partner performance diagnostic

```text
Audience: Business Partner
Decision: diagnose inconsistent performance outcomes and prepare stakeholder discussion
Domain: performance management
Mode: interactive
Skills: discovery → audience framing → performance analysis → KPI design → people analytics diagnostics → information architecture → interactive UX → Power BI feasibility → metric review
Output: overview, diagnostic pages, drill-through design, and KPI definitions
```

Expected architecture behaviour:

- support segmentation, distributions, cohorts, and comparison;
- distinguish incomplete process data from genuine performance patterns;
- preserve context through filters and drill-through;
- avoid causal claims unsupported by evidence.

### Trace C — Manager reward action dashboard

```text
Audience: people manager
Decision: complete employee reward recommendations within policy
Domain: fixed and variable reward
Mode: guided interactive
Skills: discovery → manager audience framing → reward-domain analysis → KPI and control design → action workflow → security → Power BI feasibility → usability review
Output: prioritised team actions, employee detail, control flags, and completion workflow
```

Expected architecture behaviour:

- limit the population to authorised employees;
- prioritise cases requiring action;
- provide contextual policy guidance without overwhelming the manager;
- separate recommendation support from final accountable decision;
- protect sensitive exports.

## Component-selection rules

Use a **skill** when:

- the method is repeatable;
- the required context is bounded;
- the output contract is stable;
- the capability may be selected dynamically.

Use a **subagent** when:

- the work is context-heavy or long-running;
- independent critique materially improves quality;
- parallel research or verification is useful;
- the parent should receive a concise structured return.

Use a **knowledge pack** when:

- the content is shared across multiple skills;
- evidence and definitions need one authority;
- the material is referenced more often than executed.

Use a **schema** when:

- downstream artifacts need stable fields;
- validation or interoperability matters;
- multiple templates or skills create the same artifact type.

Use a **script** when:

- the check or transformation is deterministic;
- machine validation is more reliable than prose instruction;
- the script can operate without inventing business judgement.

Use a **project rule** only when:

- the behaviour should persist across most relevant agent turns;
- omission would create repeated or material failure;
- the instruction is concise enough for persistent context.

## Anti-patterns

- One monolithic prompt containing every capability.
- Persistent rules containing full P&R knowledge packs.
- A separate subagent for every small skill.
- Skills that duplicate shared definitions.
- Examples treated as standards.
- Templates redefining schema fields.
- Visual selection before audience and decision framing.
- KPI selection before population, grain, and time logic are understood.
- Power BI implementation promised before feasibility checks.
- One dashboard structure reused for every audience.
- Formal review ceremonies at every phase that prevent learning through implementation.
- Deferring all automated validation until release.
- Treating passing CI as proof of domain or design quality.

## Architecture decisions established

1. The repository is the maintained source of truth for development and release.
2. The runtime agent uses a thin project orchestrator and dynamically selected skills.
3. Shared knowledge remains outside persistent rules and generally outside individual skill bodies.
4. Subagents are limited to context-heavy research, independent critique, and implementation verification.
5. Schemas own output contracts; templates implement them.
6. Comprehensive independent testing occurs in Phase 12 rather than blocking every development phase.
7. Draft artifacts may support controlled downstream development but cannot enter the release package as approved dependencies.

## Decisions deferred

The following are resolved in later Phase 1 artifacts:

- precise context budgets and handoff thresholds;
- automatic versus explicit skill invocation rules;
- whether `AGENTS.md` is required in addition to the main project rule;
- final custom-subagent metadata and tool configuration;
- exact command strategy;
- release package manifest;
- plugin packaging or marketplace distribution;
- hooks used for runtime or release validation;
- artifact status-transition automation.

## Draft acceptance assessment

This draft establishes:

- product boundary and users;
- component model and responsibilities;
- authority hierarchy;
- orchestration workflow;
- runtime versus development boundary;
- human decision points;
- privacy and uncertainty treatment;
- three representative workflow traces;
- component selection rules and anti-patterns.

Before the artifact leaves `PLACEHOLDER`, it must be reconciled with:

- `ARCH-CORE-002` context-management strategy;
- `ARCH-CORE-003` skill-routing model;
- `ARCH-CORE-004` information architecture;
- `ARCH-CORE-005` release architecture;
- current official Cursor component schemas.

## Sources

[^cursor-rules]: Cursor, “Rules,” updated date not stated, retrieved 2026-07-17, https://docs.cursor.com/context/rules. Central source ID: `cursor-rules`.

[^cursor-skills]: Cursor, “Subagents, Skills, and Image Generation,” release 2.4, 2026, retrieved 2026-07-17, https://cursor.com/changelog/2-4. Central source ID: `cursor-2-4-subagents-skills`.
