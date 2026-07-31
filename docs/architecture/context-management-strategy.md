---
artifact_id: ARCH-CORE-002
status: PLACEHOLDER
phase: 1
priority: critical
depends_on:
  - artifact_id: ARCH-CORE-001
    path: agent-architecture.md
  - artifact_id: STD-CORE-001
    path: ../standards/naming-standard.md
  - artifact_id: STD-CORE-002
    path: ../standards/research-standard.md
  - artifact_id: EX-CORE-001
    path: ../../knowledge/research-register/trials/cursor-rules-and-skills-trial.md
blocks:
  - ARCH-CORE-003
  - Cursor rules
  - subagent handoffs
content_version: 0.1.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Context-management strategy

## Document state

This is the first substantive draft. The lifecycle status remains `PLACEHOLDER` until the Phase 1 architecture set is reconciled as a whole.

## Purpose

Define how the Cursor agent keeps the active context focused while preserving durable knowledge, decisions, evidence, assumptions, and implementation state in the repository.

The strategy must support long-running dashboard-design work without relying on one ever-growing chat transcript.

## Core principle

```text
Conversation is working memory.
Repository artifacts are durable memory.
Rules coordinate.
Skills execute methods.
Knowledge packs provide governed subject matter.
Subagents isolate context-heavy work.
Handoffs preserve state between sessions.
```

Cursor rules are persistent prompt-level context.[^cursor-rules] Agent Skills are dynamically selected packages intended for specialised knowledge and procedures, which makes them more suitable than always-on rules for large modular capability sets.[^cursor-skills][^cursor-practices]

## Objectives

The strategy must:

- keep persistent context small;
- load only relevant capabilities;
- prevent duplicated authorities;
- preserve decisions outside chat history;
- isolate deep research and verification;
- make session transitions deliberate rather than accidental;
- allow a fresh agent to resume work from repository artifacts;
- detect context degradation before it damages output quality;
- avoid importing confidential or irrelevant material.

## Context layers

### Layer 1 — Persistent operating context

**Mechanism**

- project rules;
- minimal repository-wide instructions.

**Contains**

- mission and product boundary;
- decision-first routing principle;
- source-of-truth hierarchy;
- status and placeholder safety;
- evidence and privacy obligations;
- requirement to use schemas and quality checks;
- instruction to maintain assumptions and open questions.

**Does not contain**

- complete P&R domain knowledge;
- chart catalogues;
- consulting-method detail;
- Power BI implementation documentation;
- large examples;
- project-specific working history.

### Layer 2 — Active task context

**Mechanism**

- current Cursor conversation;
- files currently being edited;
- explicit user-provided artifacts.

**Contains**

- current request;
- agreed audience and decision;
- active assumptions;
- selected workflow stage;
- relevant constraints;
- current draft outputs;
- concise subagent returns;
- unresolved decisions requiring user input.

This is disposable working memory. Anything required after the session must be written to a governed artifact or handoff.

### Layer 3 — Dynamically loaded capability context

**Mechanism**

- Agent Skills;
- skill references and assets.

**Contains**

- method instructions;
- selection rules;
- bounded domain procedures;
- output contract references;
- anti-patterns;
- local examples required for the task.

Only selected skills should load. Skills that are broadly related but unnecessary remain unloaded.

### Layer 4 — Governed knowledge context

**Mechanism**

- files under `knowledge/`;
- source register and claims matrices.

**Contains**

- audience archetypes;
- P&R value-driver and domain definitions;
- KPI and diagnostic knowledge;
- consulting and visual evidence;
- Power BI product evidence;
- governance and risk information.

Knowledge is loaded by reference and section rather than as whole-directory context.

### Layer 5 — Isolated subagent context

**Mechanism**

- research, critique, or verification subagents.

**Contains**

- one bounded task;
- relevant source paths;
- known constraints;
- explicit output schema;
- maximum useful detail;
- required evidence standard.

The parent should not pass the full conversation when a concise task brief is sufficient.

### Layer 6 — Durable project state

**Mechanism**

- dashboard brief;
- decision log;
- KPI definitions;
- page specifications;
- design-review records;
- implementation handoff;
- status and artifact register;
- phase handoffs.

This layer enables continuation from a new session without reconstructing prior reasoning from chat.

## Context ownership table

| Information | Owning location | Active context treatment |
|---|---|---|
| Mission and orchestration rules | project rule | always available, concise |
| Reusable method | skill | load when selected |
| P&R definition or KPI concept | knowledge pack | load relevant sections |
| Output field definition | schema | load when producing or validating artifact |
| Current user decision | decision log or brief | keep active and persist |
| Temporary reasoning | conversation | discard after result is recorded |
| Deep research trail | research record | subagent returns concise synthesis |
| Worked pattern | example | load only when closely matched |
| Current implementation state | handoff and repository files | load at session start |
| Review findings | review artifact or issue | load unresolved findings only |

## Working-context budget

The repository does not assume one fixed model context size because Cursor model options and product behaviour change.

Use proportional and behavioural controls.

### Target operating range

- Keep the active main context focused on one major workflow stage.
- Prefer fewer than five concurrently active skills unless the workflow genuinely requires more.
- Load only the necessary sections of large knowledge packs.
- Keep subagent returns concise enough to review without importing their full working history.
- Start a new session at major concept changes rather than extending a degraded conversation indefinitely.

### Warning signals

Treat the context as overloaded when one or more occur:

- the agent repeats settled questions;
- earlier decisions are contradicted without explanation;
- irrelevant skills or knowledge are referenced;
- output becomes generic despite detailed inputs;
- the agent confuses audiences, metrics, pages, or domains;
- files already containing the answer are repeatedly re-read in full;
- the same definitions appear in multiple working artifacts;
- the current task changes to a new major concept;
- the conversation contains large research transcripts that are no longer needed;
- the user or agent must repeatedly restate the plan.

### Required response to overload

1. Stop adding new conceptual scope.
2. Persist decisions, assumptions, current outputs, and open questions.
3. Create or update a handoff artifact.
4. Start a fresh session for the next major concept.
5. Load only the handoff and authoritative dependencies.

## Progressive loading algorithm

### Step 1 — Load repository controls

Read only the minimum required controls:

- `STATUS.md`;
- current artifact frontmatter;
- `BUILD-ORDER.md` section for the active phase;
- relevant architecture or standard.

Do not reload all controls on every turn.

### Step 2 — Resolve the task

Classify:

- audience;
- decision mode;
- P&R domain;
- consumption mode;
- workflow stage;
- requested output.

### Step 3 — Select capabilities

Choose the minimum skills and subagents required.

### Step 4 — Load authoritative references

For each selected skill, load:

- required knowledge sections;
- schema;
- one or two closely matched examples where needed;
- current project artifacts.

### Step 5 — Exclude irrelevant context

Do not load:

- unrelated P&R domains;
- every audience archetype;
- all visual patterns;
- entire research records when a reviewed synthesis exists;
- previous examples from materially different decisions;
- superseded artifacts.

### Step 6 — Persist the result

Write durable decisions and outputs to the repository before moving to another major stage.

## Session state model

A long-running dashboard project should maintain a concise state artifact:

```yaml
project:
current_phase:
current_workflow_stage:
primary_audience:
secondary_audiences:
decision_owner:
decision:
actions_supported:
performance_reward_domains:
consumption_mode:
confirmed_constraints:
assumptions:
decisions_made:
open_questions:
active_artifacts:
selected_skills:
subagent_findings:
risks:
next_action:
```

The schema will be finalised in Phase 2. Until then, the structure is a draft field contract.

## Major-session boundaries

Start a fresh session when moving between:

- repository governance and architecture;
- architecture and schemas;
- audience foundation and P&R domain modelling;
- one major P&R domain and another where contexts are large;
- analysis and page-design production;
- design and Power BI implementation;
- implementation and independent review;
- one complete dashboard project and another.

A fresh session is not required for every small file or iteration.

## Handoff protocol

### When a handoff is required

- context-warning signals appear;
- the next task is a new major concept;
- work pauses before completion;
- responsibility passes to another agent or contributor;
- a subagent performs long-running work;
- the implementation phase begins from a completed design.

### Handoff input

```yaml
task:
scope:
audience:
decision:
known_constraints:
active_artifacts:
required_sources:
assumptions:
open_questions:
required_output:
maximum_detail:
```

### Handoff return

```yaml
executive_summary:
work_completed:
decisions_made:
findings:
recommended_application:
artifacts_created_or_changed:
risks:
validation_status:
sources:
open_questions:
next_action:
```

### Handoff quality rules

- reference authoritative files instead of duplicating them;
- distinguish decisions from recommendations;
- include unresolved dependencies;
- record validation completed and still required;
- exclude private reasoning transcripts;
- avoid broad narrative when structured fields are sufficient.

## Subagent isolation rules

### Research synthesiser

Receives:

- research question;
- decision supported;
- source requirements;
- jurisdiction and freshness;
- relevant existing knowledge;
- output contract.

Returns:

- concise synthesis;
- claim and source mapping;
- selection rules;
- conflicts and gaps;
- repository changes recommended.

The parent loads the synthesis, not the full search trail, unless a source needs inspection.

### Dashboard design critic

Receives:

- audience and decision profile;
- dashboard brief;
- page or visual specification;
- relevant quality rubric;
- explicit review questions.

Returns:

- severity-ranked findings;
- evidence and rationale;
- recommended corrections;
- unresolved design trade-offs.

It does not rewrite the design before findings are recorded.

### Power BI verifier

Receives:

- implementation handoff;
- model and grain assumptions;
- measure definitions;
- interaction design;
- security and export requirements.

Returns:

- feasibility findings;
- model and DAX risks;
- interaction limitations;
- security, accessibility, performance, and export issues;
- required implementation tests.

## Example-selection rules

Use an example only when it matches at least three of:

- audience;
- decision mode;
- P&R domain;
- consumption mode;
- workflow stage;
- output type.

Do not use an executive static example as the default pattern for a Business Partner diagnostic dashboard merely because both concern fixed reward.

When examples conflict with a standard or schema, the standard or schema wins.

## Research compression

After research is reviewed:

```text
raw search trail
→ source records
→ claim matrix
→ synthesis and selection rules
→ knowledge artifact
→ skill reference
```

The active agent should normally load the knowledge artifact or skill reference, not the raw search trail.

Retain the source register so claims can be reconstructed and refreshed.

## Decision persistence

Persist decisions when they affect:

- audience priority;
- metric definition;
- comparator or threshold;
- page architecture;
- interaction behaviour;
- security or privacy;
- implementation scope;
- release compatibility.

A decision record should include:

```yaml
decision:
status:
date:
owner:
context:
options_considered:
selected_option:
rationale:
consequences:
revisit_triggers:
```

Do not rely on the chat transcript as the only record.

## Re-entry protocol

At the start of a fresh session:

1. Read `STATUS.md`.
2. Read the handoff or current project-state artifact.
3. Read only the direct dependencies of the active artifact.
4. Confirm the next action and unresolved decisions.
5. Select skills from the current task, not from the previous conversation.
6. Reopen additional knowledge only when required.

The new session should be able to answer:

- What are we building?
- For whom?
- What decision does it support?
- What has been decided?
- What remains unresolved?
- Which files are authoritative?
- What is the next action?

## Recovery when context has degraded

If no reliable handoff exists:

1. stop substantive edits;
2. inspect current repository status and changed files;
3. identify authoritative artifacts from the register;
4. reconstruct confirmed decisions from files and issue history;
5. label uncertainty rather than guessing;
6. create a recovery handoff;
7. resume in a fresh session.

Do not use a plausible reconstruction as if it were a confirmed user decision.

## Context-risk checklist

Before a major output, confirm:

- [ ] primary audience and decision are still consistent;
- [ ] active skills are necessary;
- [ ] loaded knowledge is relevant and current;
- [ ] no superseded artifact is being used;
- [ ] user decisions are distinguished from recommendations;
- [ ] metric definitions have one owner;
- [ ] subagent findings are concise and cited;
- [ ] assumptions are visible;
- [ ] durable decisions have been persisted;
- [ ] a fresh session is not required before the next major concept.

## Metrics for later evaluation

Phase 12 should measure or assess:

- number of skills loaded per benchmark task;
- irrelevant skill-invocation rate;
- repeated-question rate;
- contradiction rate across long workflows;
- handoff completeness;
- percentage of decisions persisted outside chat;
- subagent return length and usefulness;
- ability of a fresh session to continue without clarification;
- duplicate content across rules, skills, and knowledge;
- context-related benchmark failures.

No hard thresholds are approved yet. Phase 12 will establish acceptable levels from benchmark results.

## Anti-patterns

- Treating the main chat as the project database.
- Loading every knowledge pack “just in case.”
- Embedding full research output in a persistent rule.
- Passing the entire chat to every subagent.
- Returning long subagent transcripts instead of findings.
- Starting a new session without a handoff.
- Creating handoffs that duplicate full repository artifacts.
- Continuing after repeated contradictions or lost decisions.
- Using old examples because they are familiar rather than relevant.
- Saving only final outputs and losing decisions or assumptions needed to revise them.
- Using context-size numbers as permanent product facts.

## Representative trials required before status change

Before this artifact leaves `PLACEHOLDER`, test:

### Multi-page dashboard project

- discovery;
- audience and decision framing;
- KPI architecture;
- three-page design;
- implementation handoff;
- session transition between design and implementation.

### Deep-research task

- delegate research;
- return concise evidence synthesis;
- update source and knowledge artifacts;
- resume main design work without loading the full research trail.

### Fresh-session recovery

- provide only status, handoff, and direct dependencies;
- confirm the new session can continue the correct next action without reconstructing the entire conversation.

## Draft acceptance assessment

This draft defines:

- six context layers;
- ownership and loading rules;
- overload signals and recovery;
- session-state and handoff contracts;
- subagent isolation;
- example selection;
- research compression;
- decision persistence;
- re-entry protocol;
- evaluation metrics.

It must be reconciled with the skill-routing model, skill-authoring standard, subagent schemas, and Phase 2 handoff schemas before status changes.

## Sources

[^cursor-rules]: Cursor, “Rules,” updated date not stated, retrieved 2026-07-17, https://docs.cursor.com/context/rules. Central source ID: `cursor-rules`.

[^cursor-skills]: Cursor, “Subagents, Skills, and Image Generation,” release 2.4, 2026, retrieved 2026-07-17, https://cursor.com/changelog/2-4. Central source ID: `cursor-2-4-subagents-skills`.

[^cursor-practices]: Cursor, “Best practices for coding with agents,” 2026, retrieved 2026-07-17, https://cursor.com/blog/agent-best-practices. Central source ID: `cursor-agent-best-practices`.
