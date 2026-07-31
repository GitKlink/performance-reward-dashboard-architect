---
artifact_id: STD-CORE-004
status: PLACEHOLDER
phase: 1
priority: critical
depends_on:
  - artifact_id: ARCH-CORE-001
    path: ../architecture/agent-architecture.md
  - artifact_id: ARCH-CORE-002
    path: ../architecture/context-management-strategy.md
  - artifact_id: ARCH-CORE-003
    path: ../architecture/skill-routing-model.md
  - artifact_id: STD-CORE-001
    path: naming-standard.md
  - artifact_id: STD-CORE-002
    path: research-standard.md
  - artifact_id: STD-CORE-003
    path: citation-standard.md
blocks:
  - all active Cursor skills
content_version: 0.1.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Skill-authoring standard

## Document state

This is the first substantive draft. The lifecycle status remains `PLACEHOLDER` until the first foundational skills, skill validator, and current Cursor discovery behaviour are tested together.

## Purpose

Define the required structure, metadata, invocation logic, evidence boundaries, context strategy, output contracts, safety controls, and quality requirements for every active Agent Skill in this repository.

Cursor Agent Skills are packaged in `SKILL.md` files and are intended for dynamically loaded domain knowledge, workflows, scripts, and reusable commands.[^cursor-skills][^cursor-practices]

## Scope

This standard applies to:

- project skills under `.cursor/skills/`;
- skill-local references, assets, and scripts;
- automatic and explicit invocation;
- skill status and versioning;
- skill-to-knowledge and skill-to-schema dependencies;
- skill tests and benchmark scenarios;
- release packaging of skills.

It does not define custom subagent files, project rules, or output schemas beyond how skills consume them.

## Skill design principles

1. One skill owns one bounded reusable capability.
2. The skill description supports reliable routing and includes when to use it.
3. The skill explicitly states when not to use it.
4. Shared definitions remain in governed knowledge packs.
5. Output structures reference schemas rather than inventing fields.
6. The skill loads the minimum context needed for its task.
7. Business decisions remain with the user.
8. Deterministic checks belong in scripts where practical.
9. Draft skills cannot appear as approved runtime capabilities.
10. A skill is evaluated through real scenarios, not only prose review.

## Location and naming

Canonical path:

```text
.cursor/skills/<capability-group>/<skill-name>/SKILL.md
```

Examples:

```text
.cursor/skills/discovery/audience-decision-framing/SKILL.md
.cursor/skills/performance-reward/fixed-reward-analysis/SKILL.md
.cursor/skills/visualisation/chart-selection/SKILL.md
.cursor/skills/power-bi/power-bi-feasibility/SKILL.md
.cursor/skills/assurance/dashboard-critique/SKILL.md
```

Rules:

- `<skill-name>` uses lowercase kebab-case;
- frontmatter `name` matches `<skill-name>` exactly;
- `SKILL.md` uses the required uppercase filename;
- capability groups follow the approved repository information architecture;
- skill names describe a capability or workflow rather than a persona;
- renaming preserves the immutable artifact ID and includes a migration.

## Skill directory structure

```text
<skill-name>/
├── SKILL.md
├── references/       # optional skill-specific compact references
├── assets/           # optional templates, examples, or static resources
└── scripts/          # optional deterministic utilities
```

Do not create empty optional directories.

## Frontmatter contract

The provisional Cursor-compatible baseline is:

```yaml
---
name: skill-name
description: >-
  What the skill does and the conditions under which it should be used.
paths:
  - optional/path/glob/**
disable-model-invocation: false
metadata:
  artifact_id: SKILL-XXX-001
  status: DRAFT
  content_version: 0.1.0
---
```

### Product fields

The currently expected product-facing fields are:

| Field | Requirement | Purpose |
|---|---|---|
| `name` | required | skill identity and explicit invocation name |
| `description` | required | discovery and routing signal |
| `paths` | optional | path-based applicability where supported and useful |
| `disable-model-invocation` | optional | prevent automatic model selection for manual-only skills |
| `metadata` | optional | repository governance metadata where product support permits |

The exact current schema must be reverified against official Cursor documentation and tested in the installed Cursor version before activation or release.

### Repository governance metadata

Where Cursor accepts nested metadata without affecting discovery, include:

```yaml
metadata:
  artifact_id:
  status:
  phase:
  content_version:
  knowledge_dependencies: []
  schema_dependencies: []
```

If current Cursor parsing rejects or ignores required governance fields, maintain the product frontmatter and place governance metadata in a validated adjacent manifest rather than breaking skill discovery.

## Placeholder safety

A planned skill must not contain valid active skill frontmatter until it is intentionally entering controlled runtime testing.

Safe placeholder options:

- omit the product frontmatter entirely;
- use a non-`SKILL.md` planning filename;
- keep the current scaffold format that explains the future skill without becoming discoverable.

Do not rely only on descriptive text saying “placeholder” if Cursor can still discover and invoke the skill.

## Required `SKILL.md` sections

Every active skill contains the following sections unless the skill-authoring standard explicitly allows an exception.

### Purpose

One paragraph defining the bounded capability and value.

### Use when

Testable invocation conditions.

Example:

```markdown
## Use when

- the user asks which KPIs should support a defined P&R decision;
- an existing metric needs a complete definition;
- numerator, denominator, population, time logic, or aggregation is unclear.
```

### Do not use when

Explicit exclusions.

Example:

```markdown
## Do not use when

- the user only needs visual formatting of an already approved metric;
- the request is solely about DAX syntax and the metric definition is complete;
- no business question or decision can be identified.
```

### Required inputs

List minimum inputs and their source.

Distinguish:

- mandatory;
- optional;
- inferable;
- externally researchable;
- user decision required.

### Missing-information behaviour

Define when to:

- proceed with a labelled assumption;
- ask one focused question;
- inspect repository files;
- conduct research;
- stop because the risk is too high.

### Method

Provide the ordered procedure, including decision points and branches.

### Selection rules

State how to choose between valid techniques or outputs.

### Knowledge and schema references

Link to authoritative knowledge, schemas, templates, and scripts.

### Output contract

Identify:

- schema;
- required sections or fields;
- allowed variants;
- assumptions and limitations;
- validation required.

### Quality checks

Specify checks performed before returning the result.

### Anti-patterns

List common misuse and failure modes.

### Examples

Include compact examples or link to approved repository examples. Do not embed large example libraries in the main skill file.

### Handoff

Where the output feeds another stage, identify:

- downstream skill or artifact;
- fields that must be persisted;
- unresolved decisions;
- next action.

## Optional sections

Use when relevant:

- jurisdiction and regulatory boundary;
- privacy and confidentiality;
- Power BI feasibility;
- accessibility;
- script usage;
- source freshness;
- performance considerations;
- manual invocation instructions;
- failure recovery;
- release compatibility.

## Description-writing rules

The description is the primary routing summary. It must contain both capability and trigger conditions.

### Good description pattern

```text
Design complete KPI definitions for Performance & Reward dashboards, including formula, population, time logic, aggregation, comparator, direction, limitations, and governance. Use when creating, reviewing, or resolving ambiguity in dashboard measures.
```

### Weak description

```text
Expert KPI designer.
```

### Requirements

A good description:

- starts with an action or capability;
- names the primary objects or domain;
- states when to use the skill;
- distinguishes it from adjacent skills;
- avoids generic claims such as “best practice” or “expert”;
- avoids keywords for unrelated domains merely to increase discovery;
- remains concise enough to reduce context overhead.

### Description test

A reviewer should be able to answer:

- what task does this skill perform?
- when should it be selected?
- when should an adjacent skill be selected instead?

## Invocation modes

### Automatic

Use when:

- the skill is broadly safe;
- the trigger conditions are precise;
- automatic selection is necessary for trustworthy output;
- the skill does not launch an expensive or disruptive workflow;
- false positives are unlikely to materially confuse the task.

### Explicit but model-visible

Use when the skill should normally be user-selected but may still be suggested by the agent.

### Manual-only

Use `disable-model-invocation: true` only after current behaviour is verified.

Candidates:

- prolonged grilling;
- repository-wide restructuring;
- comprehensive release evaluation;
- migration or generation workflows affecting many files;
- actions requiring explicit user authority.

Because product behaviour can vary by delivery mechanism and Cursor version, manual invocation must be tested in the actual package profile before release.

## Path scoping

Use `paths` only when file location materially determines relevance.

Appropriate:

- a skill for editing Power BI theme JSON files;
- schema validation limited to `schemas/**`;
- release packaging limited to manifest and release directories.

Inappropriate:

- audience framing;
- P&R domain analysis;
- consulting storyline;
- chart selection based on business questions rather than file path.

Path scoping supplements the description; it does not replace clear invocation rules.

## Inputs and decision ownership

Classify every important input:

| Type | Behaviour |
|---|---|
| Repository fact | inspect the authoritative file |
| Current external fact | research using authoritative sources |
| Reversible assumption | proceed and label |
| Material design decision | recommend and ask the user |
| Organisation policy | use supplied approved policy or request it |
| High-risk unresolved input | stop until resolved |

A skill must not convert a recommendation into a user decision silently.

## Method-writing rules

The method should:

- use ordered steps;
- include branch conditions;
- name required upstream outputs;
- identify stop conditions;
- keep stable concepts in references rather than repeating them;
- define what is persisted;
- avoid hidden subjective leaps.

Weak:

```text
Choose the best chart and make it executive-friendly.
```

Strong:

```text
1. Identify the analytical relationship.
2. Determine required precision.
3. Resolve audience and reading mode.
4. Compare candidate encodings.
5. Apply accessibility and Power BI constraints.
6. Record the selected chart and rejected alternatives.
```

## Knowledge references

A skill references shared knowledge when the content:

- is used by several skills;
- defines domain terminology or KPI logic;
- has its own evidence and refresh cycle;
- is too large for the main skill file;
- requires independent subject-matter review.

Skill-local references are limited to execution aids unique to the skill.

Do not copy:

- audience archetypes into every skill;
- KPI definitions into visual skills;
- Power BI limitations into every chart skill;
- consulting-method evidence into every storyline workflow.

## Scripts

Use a skill-local script when:

- the operation is deterministic;
- reproducibility matters;
- validation is safer than prose;
- the script can be tested independently;
- it does not make unapproved business decisions.

A script must define:

- inputs and outputs;
- read and write behaviour;
- dependencies;
- exit codes;
- error handling;
- tests;
- safety boundaries.

The skill explains when to call the script and how to interpret its result.

## Output contracts

A skill producing a governed artifact must reference a schema.

Example:

```markdown
## Output contract

Produce `SCHEMA-CORE-003 — KPI definition` using `templates/kpi-definition.md`.
```

The skill may add method-specific guidance but cannot redefine schema field meaning.

When no schema exists yet, use a clearly labelled draft field contract and create a Phase 2 schema dependency.

## Quality checks

Each skill defines proportional checks.

Common checks:

- audience and decision are explicit;
- domain and population are correct;
- assumptions are visible;
- evidence is cited;
- outputs satisfy schema fields;
- calculations are internally consistent;
- selected techniques fit the decision;
- Power BI feasibility is not overstated;
- privacy and accessibility risks are identified;
- downstream handoff is complete.

Do not invoke the complete assurance suite during every early draft.

## Status lifecycle

### Placeholder

- not discoverable as an active skill;
- scope and required work documented;
- no release inclusion.

### Draft

- active only in controlled testing;
- dependencies may remain draft;
- limitations visible;
- representative tests running.

### In review

- metadata verified against current Cursor;
- required benchmark routes pass;
- knowledge and schema dependencies stable enough for review;
- no unresolved critical finding.

### Approved

- release-compatible;
- mandatory dependencies approved;
- automatic and explicit invocation tested;
- privacy, evidence, and output checks passed;
- included in release manifest.

### Superseded

- no longer selected for new routes;
- replacement identified;
- migration documented.

## Versioning

Use repository `content_version` unless a separate runtime skill version is proven necessary.

A major version change includes:

- incompatible output contract;
- materially changed invocation semantics;
- renamed or removed capability;
- incompatible dependency change.

A minor version adds backward-compatible capability. A patch corrects behaviour without changing the contract.

## Compatibility

An active skill should eventually record:

- minimum tested Cursor version;
- skill-format assumptions;
- required scripts or runtimes;
- required schema versions;
- required knowledge versions where compatibility matters;
- package profile inclusion.

Current product support is reverified before release.

## Canonical skill template

```markdown
---
name: skill-name
description: >-
  Perform X for Y. Use when Z.
disable-model-invocation: false
metadata:
  artifact_id: SKILL-DOMAIN-001
  status: DRAFT
  content_version: 0.1.0
---

# Skill title

## Purpose

## Use when

## Do not use when

## Required inputs

## Missing-information behaviour

## Method

## Selection rules

## Knowledge and schema references

## Output contract

## Quality checks

## Anti-patterns

## Examples

## Handoff
```

Optional sections are inserted only when relevant.

## Valid example outline

`kpi-measure-design` is valid when it:

- distinguishes KPI design from DAX implementation;
- requires business question, population, grain, and time logic;
- references the KPI schema;
- loads domain knowledge selectively;
- produces formula, comparator, limitations, and governance;
- invokes metric QA proportionally;
- excludes visual-only formatting requests.

## Invalid example outline

`dashboard-expert` is invalid when it:

- covers discovery, KPIs, visual design, DAX, and review in one skill;
- uses a vague description;
- contains copied domain knowledge;
- has no non-invocation conditions;
- returns an unstructured narrative;
- claims organisation-specific policy without inputs;
- has no benchmark tests.

## Activation checklist

Before a placeholder becomes an active draft skill:

- [ ] artifact ID assigned and registered;
- [ ] folder and `name` match;
- [ ] current product frontmatter verified;
- [ ] description passes routing review;
- [ ] use and non-use conditions are testable;
- [ ] required inputs and missing-information behaviour defined;
- [ ] method and selection rules complete;
- [ ] knowledge and schema dependencies declared;
- [ ] output contract identified;
- [ ] anti-patterns and quality checks present;
- [ ] privacy and evidence risks addressed;
- [ ] at least one positive and one negative routing case exists;
- [ ] placeholder safety removed intentionally;
- [ ] CI and skill validator pass.

Before approval:

- [ ] automatic invocation tested where enabled;
- [ ] explicit invocation tested;
- [ ] two or more benchmark scenarios pass;
- [ ] false-positive and false-negative routing reviewed;
- [ ] context load is acceptable;
- [ ] mandatory dependencies approved;
- [ ] release package resolves all assets and references;
- [ ] no critical or major review finding remains.

## Validation requirements

The future skill validator must check:

- exact `SKILL.md` filename;
- folder and `name` agreement;
- allowed name characters;
- required product metadata;
- valid status and artifact ID;
- description presence and length bounds;
- declared knowledge and schema dependencies;
- referenced paths exist;
- placeholder versus active discovery safety;
- required sections;
- duplicate skill names;
- manual-only configuration consistency;
- release manifest inclusion rules.

Judgement-based checks such as description quality, domain overlap, or method sufficiency remain benchmark and review tasks.

## Testing requirements

Each skill has:

- at least two positive invocation cases;
- at least two non-invocation cases;
- one ambiguous case;
- one missing-input case;
- one output-contract validation case;
- one interaction with an adjacent skill;
- one context-load review;
- domain-specific critical failure cases.

Phase 12 runs the full integrated skill suite.

## Anti-patterns

- One giant skill replacing the architecture.
- A skill named after a broad persona.
- Vague descriptions designed to trigger everywhere.
- No `Do not use when` section.
- Copying shared knowledge into each skill.
- Defining new KPI formulas in an example.
- Using a subagent where a skill is sufficient.
- Using a skill where a deterministic script is sufficient.
- Automatic invocation for disruptive workflows.
- Activating all 49 scaffold skills before foundational routing is tested.
- Treating manual invocation as proof that automatic routing works.
- Shipping draft dependencies as approved runtime content.

## Draft acceptance assessment

This draft defines:

- location and naming;
- provisional frontmatter contract;
- required and optional sections;
- description and invocation rules;
- knowledge, script, and output boundaries;
- lifecycle and compatibility;
- canonical template;
- activation and approval checklists;
- validation and testing requirements;
- valid and invalid skill patterns.

Before the artifact leaves `PLACEHOLDER`, it must be trialled against at least:

- `audience-decision-framing`;
- `kpi-measure-design`;
- `chart-selection`;
- one manual-only review or grilling skill;
- the active skill validator;
- current Cursor discovery and slash invocation.

## Sources

[^cursor-skills]: Cursor, “Subagents, Skills, and Image Generation,” release 2.4, 2026, retrieved 2026-07-17, https://cursor.com/changelog/2-4. Central source ID: `cursor-2-4-subagents-skills`.

[^cursor-practices]: Cursor, “Best practices for coding with agents,” 2026, retrieved 2026-07-17, https://cursor.com/blog/agent-best-practices. Central source ID: `cursor-agent-best-practices`.
