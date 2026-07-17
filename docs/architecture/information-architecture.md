---
artifact_id: ARCH-CORE-004
status: PLACEHOLDER
phase: 1
priority: high
depends_on:
  - artifact_id: ARCH-CORE-001
    path: agent-architecture.md
  - artifact_id: STD-CORE-001
    path: ../standards/naming-standard.md
blocks:
  - repository navigation
  - release packaging
content_version: 0.1.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Repository information architecture

## Document state

This is the first substantive draft. The lifecycle status remains `PLACEHOLDER` until the complete Phase 1 architecture set is reconciled.

## Purpose

Define how contributors and Cursor agents locate authoritative instructions, domain knowledge, methods, schemas, examples, evaluations, implementation assets, and release files without relying on conversation history.

## Design principles

1. One artifact type has one default home.
2. One concept has one authoritative owner.
3. Runtime components and development evidence are visibly separate.
4. Folder structure communicates role, not lifecycle status.
5. Indexes point to authorities and never duplicate them.
6. Skills reference shared knowledge rather than copying it.
7. A new contributor can start from a small number of entry points.
8. Generated content is distinguishable from authored content.
9. Release packaging can be derived from explicit metadata and manifests.
10. Placeholder and superseded content cannot be mistaken for active capability.

## Repository map

```text
performance-reward-dashboard-architect/
├── README.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── BUILD-ORDER.md
├── DEPENDENCIES.md
├── STATUS.md
├── ARTIFACT-REGISTER.yaml
├── AGENTS.md                         # optional runtime entry point; decision pending
├── .cursor/
│   ├── rules/                        # persistent project behaviour
│   ├── agents/                       # custom context-isolated subagents
│   ├── skills/                       # dynamically selected capabilities
│   ├── commands/                     # optional explicit workflows
│   └── environment.json              # optional environment definition if adopted
├── .github/
│   ├── workflows/                    # CI and release automation
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
├── docs/
│   ├── architecture/                 # component and repository architecture
│   ├── standards/                    # authoring, research, evaluation, release rules
│   ├── plans/                        # research, implementation, and release plans
│   ├── decisions/                    # architecture decision records when added
│   └── reviews/                      # formal integrated review records
├── knowledge/
│   ├── audiences/
│   ├── performance-reward/
│   ├── consulting/
│   ├── visual-design/
│   ├── visualisation/
│   ├── dashboard-experience/
│   ├── power-bi/
│   └── research-register/
├── schemas/                          # machine-readable output contracts
├── templates/                        # human-usable schema implementations
├── examples/                         # synthetic worked examples
├── evaluations/                      # benchmark prompts, expected results, regressions
├── scripts/                          # deterministic validation and generation
├── tests/                            # automated tests for scripts and contracts
└── release/                          # generated manifests or package staging if adopted
```

Directories are created only when they contain substantive artifacts. Empty conceptual folders do not need to be committed merely to mirror the target map.

## Top-level entry points

### `README.md`

For first-time users and contributors.

Must explain:

- product purpose;
- current status;
- intended runtime surface;
- where to begin;
- installation or use instructions when available;
- release and safety warnings.

### `STATUS.md`

For current work.

Must explain:

- current phase;
- active branch;
- completed and in-progress work;
- validation status;
- immediate next action.

It is not a detailed project plan or changelog.

### `BUILD-ORDER.md`

For sequence and phase gates.

### `DEPENDENCIES.md`

For dependency semantics and source-of-truth rules.

### `ARTIFACT-REGISTER.yaml`

For machine-readable artifact identity, path, status, phase, and direct dependencies.

### `CHANGELOG.md`

For notable repository and release changes.

### `CONTRIBUTING.md`

For contribution workflow, validation, review, privacy, and authoring expectations.

## Artifact-location decision table

| Artifact | Default location | Owner of meaning | May be packaged at runtime? |
|---|---|---|---|
| Persistent Cursor instruction | `.cursor/rules/` | rule file, constrained by architecture | yes |
| Agent Skill | `.cursor/skills/<group>/<skill>/` | `SKILL.md` | yes |
| Custom subagent | `.cursor/agents/` | subagent file | yes |
| Explicit command | `.cursor/commands/` | command file | yes, if adopted |
| Architecture | `docs/architecture/` | architecture artifact | usually no |
| Standard | `docs/standards/` | standard artifact | only if needed by runtime contributors |
| Plan | `docs/plans/` | plan artifact | no |
| Architecture decision | `docs/decisions/` | decision record | usually no |
| Shared subject knowledge | `knowledge/<domain>/` | knowledge artifact | yes when a packaged skill depends on it |
| Source record or evidence trial | `knowledge/research-register/` | source or research artifact | normally no, except required provenance |
| Output schema | `schemas/` | schema | yes when runtime outputs use it |
| Output template | `templates/` | schema plus template | yes when runtime outputs use it |
| Worked example | `examples/` | example artifact | selectively |
| Benchmark or regression | `evaluations/` | evaluation artifact | no for minimal runtime; yes for development distribution |
| Validator or generator | `scripts/` | script contract and governing standard | selectively |
| Automated test | `tests/` | test module | no for minimal runtime; yes for source distribution |
| CI workflow | `.github/workflows/` | infrastructure artifact | source repository only |
| Release manifest | `release/` or generated artifact | release architecture | distribution metadata |

## Folder responsibilities

### `.cursor/`

Contains only Cursor runtime or workspace configuration.

It must not become a general documentation folder.

#### `.cursor/rules/`

Contains concise persistent behaviour.

Do not place:

- full domain knowledge;
- large examples;
- source records;
- one-off project decisions;
- release notes.

#### `.cursor/skills/`

Each skill owns one bounded reusable capability.

A skill folder may contain:

```text
SKILL.md
references/
assets/
scripts/
```

Local references are appropriate when they are useful only to that skill. Shared subject matter belongs in `knowledge/`.

#### `.cursor/agents/`

Contains only custom subagent definitions. Research outputs and handoffs belong in governed artifacts outside this directory.

#### `.cursor/commands/`

Contains explicit reusable workflows only when commands are adopted and do not duplicate skills.

### `docs/`

Contains repository governance and design decisions about the agent itself.

It does not contain the primary P&R or visualisation knowledge used by skills.

#### `docs/architecture/`

Owns:

- component boundaries;
- context strategy;
- routing;
- repository layout;
- release packaging.

#### `docs/standards/`

Owns:

- naming;
- research and citation;
- skill and example authoring;
- evaluation;
- future release and security rules.

#### `docs/plans/`

Owns time-bound sequencing and milestones. Plans do not redefine architecture or standards.

#### `docs/decisions/`

When added, contains immutable decision records for material choices with alternatives and revisit triggers.

#### `docs/reviews/`

Contains integrated formal review records after the evaluation standard is defined. Early evidence-governance trials may remain under the research register.

### `knowledge/`

Contains governed subject matter shared by multiple capabilities.

#### `knowledge/audiences/`

Audience archetypes, decision needs, reading behaviour, common actions, detail tolerance, and failure modes.

#### `knowledge/performance-reward/`

Cross-domain and specialist P&R definitions, value drivers, business questions, KPIs, diagnostics, risks, and use cases.

#### `knowledge/consulting/`

Published and synthesised communication techniques, attribution classifications, selection rules, and misuse conditions.

#### `knowledge/visual-design/`

Visual perception, hierarchy, typography, colour, layout, accessibility, and design principles.

#### `knowledge/visualisation/`

Analytical relationships, chart and exhibit patterns, IBCS treatment, tables, distributions, variance, and anti-patterns.

#### `knowledge/dashboard-experience/`

Guided, exploratory, static, interactive, hybrid, executive, Business Partner, manager, and specialist experience patterns.

#### `knowledge/power-bi/`

Current Power BI feasibility, semantic-model, DAX, interaction, performance, security, export, accessibility, and theme knowledge.

#### `knowledge/research-register/`

Source records, claim matrices, evidence trials, and evidence-governance reviews.

## Shared knowledge versus skill-local references

Place content in shared `knowledge/` when:

- more than one skill needs it;
- it defines a domain concept or KPI;
- it needs independent evidence review;
- it has a refresh cycle separate from the skill;
- it is useful outside one workflow.

Place content in a skill-local `references/` folder when:

- it supports only that skill;
- it is tightly coupled to the skill's method;
- sharing it would create an artificial general concept;
- it is an example, checklist, or compact reference used only during skill execution.

When uncertain, prefer shared knowledge for definitions and local references for execution aids.

## Schemas and templates

### `schemas/`

Owns:

- field names and definitions;
- required and optional status;
- allowed values;
- version and compatibility rules;
- validation constraints.

Suggested naming:

```text
research-record.schema.yaml
audience-decision-profile.schema.yaml
kpi-definition.schema.yaml
dashboard-brief.schema.yaml
page-specification.schema.yaml
visual-specification.schema.yaml
design-review.schema.yaml
implementation-handoff.schema.yaml
```

### `templates/`

Mirrors schema subjects:

```text
research-record.md
audience-decision-profile.md
kpi-definition.md
dashboard-brief.md
page-specification.md
visual-specification.md
design-review.md
implementation-handoff.md
```

A template may provide instructions and examples but cannot change schema semantics.

## Examples and evaluations

### `examples/`

Organise primarily by audience and product mode, with domain encoded in filenames or metadata.

Suggested structure:

```text
examples/
├── executive/
├── business-partner/
├── manager/
├── specialist/
├── interactive/
└── static/
```

Avoid deep duplication such as maintaining the same complete example under audience, domain, and format folders.

Each example should declare:

- audience;
- decision;
- domain;
- consumption mode;
- workflow stage;
- synthetic-data status;
- skills demonstrated;
- assumptions;
- limitations.

### `evaluations/`

Suggested structure:

```text
evaluations/
├── scenarios/
├── expected-results/
├── routing/
├── regression/
└── results/
```

Scenario and expected-result IDs must remain linked through metadata rather than filename guesswork.

## Navigation by contributor task

### “I need to understand the project”

Read:

1. `README.md`
2. `STATUS.md`
3. relevant section of `BUILD-ORDER.md`
4. `docs/architecture/agent-architecture.md`

### “I need to author a skill”

Read:

1. skill-authoring standard;
2. routing model;
3. relevant knowledge pack;
4. output schema;
5. one matching example;
6. skill validation rules.

### “I need to research a P&R topic”

Read:

1. research and citation standards;
2. relevant existing knowledge;
3. source register;
4. research program;
5. downstream skill or schema that will consume the result.

### “I need to design a benchmark”

Read:

1. evaluation standard;
2. example-authoring standard;
3. routing model;
4. relevant skills and schemas;
5. existing scenarios and expected results.

### “I need to use the agent”

Read:

1. release README;
2. available skills or commands;
3. supported workflows;
4. version and compatibility notes.

### “I need to prepare a release”

Read:

1. release architecture;
2. release plan;
3. evaluation results;
4. artifact register;
5. release manifest;
6. changelog and migration notes.

## Cross-linking rules

### Required links

A governed artifact should link to:

- direct dependencies where useful to readers;
- schemas it implements or produces;
- knowledge authorities it materially relies on;
- downstream artifacts only where navigation value is high;
- superseding artifact when status is `SUPERSEDED`.

### Avoid

- exhaustive “related links” sections that become stale;
- circular narrative links without formal dependencies;
- raw local file-system paths;
- duplicated source lists where claim-level citations suffice;
- links to placeholder files presented as completed guidance.

### Link direction

Prefer:

```text
procedure → definition
example → method and schema
skill → knowledge and schema
template → schema
evaluation → tested artifact
```

Do not make upstream standards depend on downstream examples merely to create convenient navigation.

## Index strategy

Indexes improve discovery but are never authorities.

### Human-readable indexes

Possible indexes:

- skills by capability group;
- knowledge by domain;
- schemas and templates;
- benchmark scenarios;
- artifacts by status;
- sources due for refresh.

### Generated indexes

Generated indexes must:

- identify their source data;
- state that they are generated;
- include generation timestamp or source commit;
- never contain definitions absent from the source artifacts;
- be reproducible;
- be regenerated rather than manually edited.

`ARTIFACT-REGISTER.yaml` remains authoritative for artifact identity and status.

## Status visibility

Every substantive governed Markdown or MDC file exposes lifecycle status in frontmatter.

### Placeholder

The opening content must explain what remains to be completed. Runtime placeholders must be non-operational.

### Draft

The file must identify material limitations, unresolved questions, or required reconciliation.

### In review

The review target and issue or review artifact should be identifiable.

### Approved

The file should identify content version, review date, and future review trigger.

### Superseded

The file must link to `superseded_by` and must not appear as current guidance in generated indexes.

## Runtime versus development visibility

The repository README and release manifest must distinguish:

```text
source repository
runtime package
development-only artifacts
generated release artifacts
```

A consumer should not need to understand research trials or repository governance to use the packaged agent.

A contributor should be able to trace runtime behaviour back to source knowledge, schemas, and evaluations.

## Release-discovery metadata

Each runtime skill should eventually declare or expose enough metadata to determine:

- its status and version;
- required knowledge files;
- required schemas and templates;
- local assets and scripts;
- compatible agent version;
- whether it is included in the release package.

The release architecture will define the final manifest fields.

## Misplaced-content checklist

Before adding a file, ask:

- Is this a definition, procedure, output contract, presentation form, example, test, or project decision?
- Is there already an authoritative artifact for the concept?
- Will more than one skill need it?
- Does it need independent evidence review?
- Is it runtime content or development support?
- Does its folder imply a status or audience it does not have?
- Can it be generated from another authority?
- Would moving it later break many links?

## Duplication checklist

Potential duplication exists when:

- the same definition appears in multiple skills;
- a template restates schema field semantics differently;
- a rule includes a complete method already in a skill;
- an example introduces a new formula;
- audience guidance is copied into every domain pack;
- Power BI constraints are repeated across visual skills;
- source details appear in several files without stable source IDs;
- a generated index becomes manually maintained.

Resolve duplication by assigning one owner and replacing copies with concise references.

## Anti-patterns

- One `docs/` directory containing every artifact type.
- Organising all knowledge by skill rather than subject.
- Creating one copy of a KPI definition per audience.
- Using folder names such as `final`, `old`, or `new` for lifecycle.
- Shipping tests and research trails accidentally in the minimal runtime package.
- Hiding active rules in ordinary documentation folders.
- Creating multiple README files that disagree on current status.
- Using examples as navigation authorities.
- Maintaining status manually in several independent indexes.
- Deep folder nesting that makes paths harder to understand than the content.

## Draft acceptance assessment

This draft defines:

- repository map;
- top-level entry points;
- artifact-location rules;
- folder responsibilities;
- shared versus local knowledge;
- schema, template, example, and evaluation organisation;
- contributor navigation paths;
- cross-linking and index rules;
- status and runtime visibility;
- duplication and misplaced-content checks.

Before the artifact leaves `PLACEHOLDER`, it must be reconciled with:

- the final skill folder inventory;
- the Phase 2 schema and template names;
- the release manifest;
- generated index scripts;
- the decision on `AGENTS.md`, commands, and optional environment configuration.
