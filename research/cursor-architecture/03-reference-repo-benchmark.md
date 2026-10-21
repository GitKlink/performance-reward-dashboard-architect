# R3 — Reference Implementation Benchmark

> **Research ticket:** R3 — GitHub issue #11, `GitKlink/performance-reward-dashboard-architect`  
> **Research date:** 2026-09-16 (Pacific/Auckland)  
> **Durable target:** `research/cursor-architecture/03-reference-repo-benchmark.md`  
> **Status:** Research complete and persisted to the repository.  
> **Decision status:** Evidence benchmark only. This document does **not** select the final Power BI / Fabric Architect architecture; R8 remains the synthesis/decision point.

## 1. Research scope

This benchmark compares six fixed reference implementations to answer a cross-cutting architecture question: **how do strong, current agent-oriented repositories divide knowledge, workflow, execution, orchestration, packaging, persistence, installation, validation and portability without creating duplicated authority or loading everything into context?**

The mandatory corpus is exactly:

1. `cursor/plugins`
2. `cursor/plugin-template`
3. `microsoft/skills-for-fabric`
4. `mattpocock/skills`
5. `addyosmani/agent-skills`
6. `github/spec-kit`

No optional repository was required. Where a question remained unresolved by the six repositories, it is recorded in §30 rather than widening the corpus.

The benchmark is deliberately not a popularity comparison and not six README summaries. Repository internals were inspected at fixed Git commit references so that claims can be traced to a specific state.

**FACT —** The target repository's R3 ticket defines this work as evidence gathering, fixes the six-repository corpus, and reserves final architecture synthesis for later research.  
**RECOMMENDATION —** Treat every design implication below as a candidate lesson, not a target-architecture commitment.

## 2. Methodology

The research used a question-driven inspection method. For each repository, the investigation sampled the assets that actually implement its architecture: manifests, directory trees, `SKILL.md` files, agent definitions, rules, commands, hooks, MCP configuration, ordinary references, scripts, installers, generated-asset logic, tests/evals, release metadata, and root agent instructions.

The evidence vocabulary is:

- **FACT** — documented behaviour in the repository or its maintained documentation.
- **OBSERVATION** — a pattern directly visible in the inspected repository state.
- **INFERENCE** — an architectural implication derived from facts/observations.
- **RECOMMENDATION** — a provisional lesson for Wayfinder; not a final decision.

The benchmark snapshots were:

| Repository | Inspected ref | Why pin it |
|---|---|---|
| `cursor/plugins` | `c1c0a32802223f4be824112dd83d33ad29a8b26c` | Production Cursor plugin examples are changing rapidly; pinning prevents later marketplace changes from silently changing the evidence. |
| `cursor/plugin-template` | `46216072ac5750f782f95bb325b4d12b7c3ae9c9` | Captures the canonical simple/advanced plugin template and validator together. |
| `microsoft/skills-for-fabric` | `24cc0d296e5e8523cc6a92e1342bc1791d7deb85` | Captures the Fabric/Power BI skill decomposition, plugin bundle and MCP configuration used in this benchmark. |
| `mattpocock/skills` | `959a8e9f1edc3adbe2f7e3054bb6fbefa6696260` | Captures v1.2.3-era managed-plugin/editable-skill design and the canonical installation ADR. |
| `addyosmani/agent-skills` | `be4e44a9fbc5e8df0beaefadbb28bd22ee61cc39` | Captures the multi-agent adapters, hooks, shared references and three-tier eval system. |
| `github/spec-kit` | `1d5106f59e1b148ee23ab136638932dd790ff1b6` | Captures the current CLI/integration/upgrade architecture and runtime single-source-of-truth model. |

Inspection depth was intentionally uneven. More files were inspected where a repository is especially informative for a question: Cursor production plugins for native primitives; Microsoft for Power BI/Fabric decomposition; Matt Pocock and Addy Osmani for skill packaging/portability; Spec Kit for bootstrap, generated assets and lifecycle management.

**OBSERVATION —** Some documentation and validation rules do not perfectly align. The clearest example is `cursor/plugin-template`: prose describes command frontmatter as recommended, while its validator requires command `name` and `description`. The implementation/validator is therefore the stronger benchmark evidence for template conformance.

**LIMITATION —** A repository can show intended loading boundaries (for example, “read these references on demand”) but cannot by itself prove every host's exact internal token-loading implementation. Claims about context economics therefore distinguish repository design from host-runtime internals.

## 3. Reference corpus

### `cursor/plugins`

**Why selected.** Official production examples of Cursor plugins using real combinations of skills, agents, hooks, MCP and scripts.  
**Primary architectural value.** Shows what teams actually package after moving beyond a starter template: selective primitives, explicit state machines, subagent isolation, deterministic scripts and plugin-level composition.  
**Relevant assets.** Marketplace manifest, per-plugin manifests, skills, agents, rules, hooks, MCP configs, scripts, prompt fragments, schemas, tests and ordinary references.

Especially useful examples are:

- `orchestrate`: a task-scoped orchestration harness implemented primarily as an explicit skill plus scripts, prompts, schemas and tests.
- `thermos`: parallel specialist review agents, each grounded by a skill.
- `advisor`: checkpoint consultation using a skill, subagent, hook state and bounded stop-loop behaviour.
- `continual-learning`: hook → skill → memory-updater subagent pipeline that incrementally maintains compact `AGENTS.md` memory.
- `cursor-team-kit`: very small always-on rules rather than a monolithic handbook.
- `third_party/github`: a thin MCP-only integration plugin.

### `cursor/plugin-template`

**Why selected.** Canonical/minimal Cursor plugin starter and validator.  
**Primary architectural value.** Separates what a plugin *must* be from what it *can* contain; demonstrates simple versus advanced composition and conventional discovery.  
**Relevant assets.** `.cursor-plugin/plugin.json`, marketplace metadata, rules, skills, agents, commands, hooks, `mcp.json`, scripts, assets, docs and `validate-template.mjs`.

### `microsoft/skills-for-fabric`

**Why selected.** Closest functional analogue to Wayfinder: Fabric, semantic-model and Power BI knowledge packaged for agents.  
**Primary architectural value.** Demonstrates platform-specialist skill decomposition, large on-demand reference sets, cross-skill routing, MCP/tool fallback, Power BI planning/design/authoring separation, and cross-agent distribution.  
**Relevant assets.** `skills/**/SKILL.md`, large `references/` trees, shared `common` materials, Fabric agents, `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, plugin marketplace metadata, MCP declarations, APM install instructions, package/release metadata.

### `mattpocock/skills`

**Why selected.** Deliberately skill-centric architecture with an explicit philosophy against over-owning process.  
**Primary architectural value.** Clean distinction between user-invoked orchestration skills and model-invoked reusable discipline, strong canonical-source thinking, managed versus editable installation, and a documented refusal to create duplicate skill sources merely to satisfy a platform manifest.  
**Relevant assets.** Bucketed skill tree, `.agents/` ADRs and maintenance docs, Claude plugin manifest, setup skill, project `docs/agents` routing pattern, Changesets/release automation.

### `addyosmani/agent-skills`

**Why selected.** Broad multi-asset, multi-agent skill distribution with explicit quality/evaluation machinery and many host adapters.  
**Primary architectural value.** Separates skills, personas, commands, hooks, references, scripts and evals; documents cross-agent mappings; exposes a concrete failure mode when a single skill depends on repository-level shared references.  
**Relevant assets.** `skills/`, `agents/`, `commands/`, `.claude/`, `.codex-plugin/`, other host adapters, `hooks/`, root `references/`, `evals/`, scripts, `AGENTS.md`, `CLAUDE.md`.

### `github/spec-kit`

**Why selected.** Strongest harness/bootstrap architecture in the corpus.  
**Primary architectural value.** Demonstrates an installed CLI that generates and manages agent-specific project assets while preserving user-owned specs/work products, with manifest-aware upgrades, templates, extensions/presets and a live project constitution as authority.  
**Relevant assets.** Python CLI, integration registry/adapters, command templates, spec/plan/tasks templates, `.specify` memory, extensions/presets, generated integration manifests, upgrade logic and extensive tests.

## 4. High-level findings

The most important cross-repository result is that **the primitives are not competing labels for the same thing**. Strong implementations tend to give each primitive a narrow architectural job:

1. **Plugins are primarily distribution/composition containers.** A Cursor plugin may contain architecture, but “plugin” itself is not the architecture. The corpus includes both rich plugins and an MCP-only plugin.
2. **Skills are the dominant reusable capability unit.** They combine discovery metadata with a bounded workflow/discipline and route to deeper references or tools as needed.
3. **Persistent rules/root instructions work best when small.** Cursor production rules are tiny; Addy explicitly tells Cursor users not to paste full skills into rules; Matt's setup pattern writes a small router to deeper project docs. Microsoft's larger `AGENTS.md` is useful counter-evidence showing the portability benefit but also the context/duplication cost of a broad persistent file.
4. **Commands are explicit workflow entry points, not substitutes for skills.** Addy and Spec Kit use commands/command-like invocations to enter lifecycle stages, while deeper capability lives in skills and persistent artifacts.
5. **Agents/subagents earn their cost through context ownership/isolation.** Microsoft uses a cross-workload agent that delegates endpoint depth to skills; Cursor Thermos and Matt's code-review skill use separate contexts to prevent one review perspective from contaminating another.
6. **Deterministic enforcement moves out of prose.** Cursor hooks invoke scripts on objective events; Microsoft Power BI skills call validators/CLIs; Addy and Spec Kit test structures and execution. Prompt instructions are not treated as the only quality mechanism.
7. **The recurring context pattern is progressive disclosure:** small router/invariant → relevant skill → relevant reference → relevant executable/tool. Microsoft explicitly says not to load all semantic-model references at once; Cursor Orchestrate routes roles to references and keeps state in executable code.
8. **Canonical-source discipline is a first-class architecture concern.** Spec Kit stopped propagating constitution text into templates because it duplicated authority; Matt rejects duplicate promoted-skill copies for Codex; Addy centralises reusable skill content but exposes the danger of root-shared references on partial installs.

The meaningful disagreements are equally important:

- **Managed versus editable distribution.** Matt presents these as two different philosophies; Spec Kit provides managed generated files with local-change detection; universal skill CLIs copy editable files.
- **How much belongs in persistent instructions.** Microsoft carries substantial platform routing/standards in root instructions; Cursor/Matt/Addy generally push deeper knowledge behind selective routing.
- **Where orchestration lives.** Cursor Orchestrate puts a mini-harness inside a skill/plugin; Spec Kit externalises the harness into a CLI and generated project lifecycle; Microsoft uses an explicit orchestrating agent for cross-workload work; Matt often uses a skill to spawn subagents.
- **How portability is achieved.** Matt refuses a native platform package when the platform's manifest would require duplicate content; Addy maintains many thin adapters around shared skills; Spec Kit generates target-specific integration assets; Microsoft carries several root instruction forms plus package/install tooling.

**INFERENCE —** Wayfinder should not start by asking “plugin or agent or skill?” The better question is “which responsibilities need persistent context, discoverable knowledge, explicit workflow, isolated reasoning, deterministic execution, external capability, packaging, or project-owned state?” R2/R8 can then map those responsibilities to primitives.

## 5. Rules

### What strong implementations put in rules

Cursor's production `cursor-team-kit` rules are narrow always-on invariants. `no-inline-imports.mdc`, for example, is a few hundred bytes and states one coding rule. The advanced plugin template similarly demonstrates a short `coding-standards.mdc` rather than a full engineering handbook.

Addy's Cursor instructions explicitly recommend putting workflow skills under `.cursor/skills/` and **short policies** under `.cursor/rules/*.mdc`, with a warning not to paste full skills into rules.

Matt's project setup skill takes a similar route without depending on Cursor rules specifically: a small root `AGENTS.md`/`CLAUDE.md` block points to `docs/agents/issue-tracker.md`, `docs/agents/domain.md` and optional triage configuration.

**OBSERVATION —** The common shape is “persistent invariant/router”, not “persistent encyclopedia”.

### What is deliberately not placed in rules

The detailed workflow lives elsewhere:

- Cursor Orchestrate keeps orchestration detail in `SKILL.md`, role-specific references, prompts, JSON schemas and TypeScript.
- Microsoft's semantic-model skill keeps DAX performance patterns, modelling guidance and metadata discovery in separate references loaded by intent.
- Addy's lifecycle workflows live in skills; root rules/instructions route to them.
- Spec Kit's methodology lives in workflow assets/templates and project artifacts rather than a single persistent rules file.

**INFERENCE —** Rules are a poor home for standards that are large, frequently revised, domain-specific or only relevant to a subset of tasks. They are a better home for stable invariants such as “never hard-code secrets”, “read the project standard before editing X”, or “run validator Y when condition Z applies”.

### Persistent versus scoped

Cursor rule frontmatter supports an `alwaysApply` concept, and the production examples use it for narrow conventions. Skills/commands then provide scoped behaviour. Root `AGENTS.md`/`CLAUDE.md` files are also persistent at repository scope, so their size has the same context-economics concern even when the host syntax differs.

**RECOMMENDATION —** For future Wayfinder engineering standards, test a layered model rather than a monolithic rules file:

`small persistent rules/router → canonical standard index → relevant standard chapter/reference → validator/tool`

The persistent layer should identify authority and routing conditions; it should not reproduce the entire standard.

## 6. Skills

### Canonical structure

Across Cursor, Microsoft, Matt and Addy, the stable common denominator is a directory containing `SKILL.md` with YAML frontmatter that exposes at least a name and description. The description is not decorative: it is part of capability discovery/routing, and Addy's eval architecture explicitly tests whether descriptions route realistic prompts to the right skill.

Supporting files vary by need:

- **Microsoft:** often substantial `references/` trees and shared common reference material.
- **Cursor Orchestrate:** references, prompts, JSON schemas, scripts and tests co-located with one skill.
- **Matt:** many skills are self-contained instructions but can route to project-created ordinary docs or seed files in the skill directory.
- **Addy:** skill-local content plus repository-level shared references, scripts and evaluation fixtures.

**OBSERVATION —** `SKILL.md` is best treated as a capability contract/router, not necessarily as the entire knowledge base.

### `SKILL.md` responsibilities

The strongest `SKILL.md` files consistently do four things:

1. **Discovery:** precise trigger/scope description.
2. **Boundary:** state what the skill owns and what it deliberately hands off.
3. **Workflow:** the minimum ordered method, gates and exit conditions.
4. **Routing:** point to deeper references/tools only when the task requires them.

Microsoft's `powerbi-report-design` is especially clear: it owns design intent and a design contract, but does not write PBIR; it routes file mechanics to `powerbi-report-authoring`. `powerbi-report-authoring` in turn routes open-ended design and planning elsewhere.

### Progressive loading and large knowledge

Microsoft's semantic-model skill explicitly says to load reference files on demand and **not** to load all references at once. Its references include DAX guidance, DAX performance decision guides/pattern catalogues, TMDL/PBIP material, modelling guidelines, metadata discovery and connection binding. Some are tens of kilobytes, which makes the benefit of selective reading concrete rather than theoretical.

Cursor Orchestrate follows the same pattern at a workflow level: the root skill routes planners, workers, verifiers and handoff logic to dedicated reference documents and executable components.

Addy also externalises large checklists/patterns into `references/`, but its own README documents a portability flaw: installing one skill with the generic skills CLI copies only that skill directory, so links to repository-level shared references become unavailable.

**INFERENCE —** Deep knowledge should be selectively readable, but reference location must respect the intended installation boundary.

### Skill scope and granularity

Three successful decompositions appear:

- **Platform/endpoint specialist:** Microsoft skills such as semantic-model authoring, report design/authoring/management, Spark, warehouse and event workloads.
- **Workflow discipline:** Matt and Addy skills such as TDD, debugging, code review, specification and planning.
- **Task-scoped harness:** Cursor Orchestrate is a skill whose implementation includes a stateful executable orchestration engine.

These are compatible, not mutually exclusive. A library can contain both platform/domain skills and workflow skills, as long as boundaries are explicit.

### Where standards belong

The corpus supports a **combination**, not one location:

- Put **trigger, scope, mandatory workflow and routing rules** in `SKILL.md`.
- Put **large detailed standards, patterns, examples and decision tables** in references read on demand.
- Keep **organisation-wide canonical standards** outside a particular skill when multiple skills/repos must share the same authority; the skill should point to the canonical source rather than fork it.
- Put **mechanically enforceable standards** in validators/scripts/CI/hooks as well as documenting them.

**RECOMMENDATION —** Do not make a future DAX or semantic-model skill the canonical owner of all Wayfinder engineering standards merely because it can load them. Let the skill consume and route to authoritative standards.

## 7. Commands and workflows

Commands are most useful when the user needs an **explicit named transition into a deterministic or consequential workflow**.

Cursor's advanced template command `deploy-staging.md` demonstrates the basic form: an explicit user-invoked workflow with ordered steps. Addy takes this further: lifecycle commands such as `/spec`, `/plan`, `/build`, `/test`, `/review` and `/ship` are user-facing orchestration entry points that activate deeper skills. Spec Kit's `/speckit-*` invocations drive a project lifecycle that leaves durable specification, plan, task and verification artifacts.

There is, however, no absolute “command versus skill” boundary. Cursor production skills such as Orchestrate and Thermos use `disable-model-invocation: true`, making a **skill** explicit-only. Matt likewise has user-invoked skills whose job is orchestration and model-invoked skills that provide reusable discipline.

**INFERENCE —** The stronger distinction is architectural intent:

- **Command / explicit-only skill:** user chooses a named workflow, often with side effects, approvals, state transitions or persistent artifacts.
- **Auto-discoverable skill:** model can safely select a bounded reusable capability when the task matches.

**RECOMMENDATION —** Candidate Wayfinder workflows such as “architect a new analytical product”, “validate project conformance” or “prepare an approved report implementation brief” should be evaluated for explicit invocation if they are expensive, stateful or require approval gates. Narrow DAX/Power Query guidance is more naturally discoverable.

## 8. Agents and subagents

### Why the repositories introduce agents

Agents are used when a role needs **its own context, perspective, output contract or responsibility boundary**.

Microsoft's `FabricDataEngineer.agent.md` is a cross-workload orchestrator: it owns end-to-end decomposition and consistency across Spark, Warehouse, pipelines and related Fabric workloads, then delegates endpoint-specific implementation to skills.

Cursor Thermos uses separate security/correctness and code-quality subagents. The Thermos orchestration skill launches them in parallel and merges/deduplicates results. Each specialist agent loads the relevant skill and works in an isolated review context.

Matt's `code-review` skill creates two parallel fresh-context reviews — Standards and Spec — specifically so the two axes do not pollute one another. This shows that agent isolation can be an implementation technique *inside a skill* rather than requiring a permanent persona for every speciality.

Addy separates “who” (personas under `agents/`) from “how” (skills) and “when” (commands). Its repository guidance explicitly discourages router personas; user/command intent routing owns orchestration, while personas may use skills.

### Delegation direction

The observed direction is usually:

`orchestrator skill/command/agent → specialist agent/subagent → specialist skill/reference/tool`

or:

`skill → parallel subagents → aggregation`

There is little evidence for unconstrained recursive agent-to-agent delegation. Cursor Orchestrate is the exception only because it explicitly implements planner/subplanner recursion with structured scopes, state and handoffs.

### Context benefit versus coordination cost

Isolation prevents one specialist's reasoning from consuming or biasing another specialist's context. The cost is that state must be packaged into prompts/handoffs; sibling agents cannot assume shared working memory; aggregation has to resolve conflicts and duplicates. Cursor Orchestrate therefore uses explicit handoff schemas and persistent JSON state rather than relying on conversational memory.

### Implications for proposed Wayfinder specialists

These are **not final decisions**:

| Proposed capability | Benchmark implication |
|---|---|
| Semantic model architect | Microsoft treats semantic-model depth primarily as a skill/tool domain. An agent becomes more plausible only when the role must coordinate multiple skills, project constraints and architectural trade-offs over a sustained context. |
| DAX specialist | Evidence leans toward skill + references + executable/query tooling for bounded expertise. A subagent may still be valuable for isolated performance/review work. |
| Data architecture specialist | Microsoft provides the strongest precedent for an orchestrating agent when work crosses multiple Fabric endpoints and architectural layers. |
| Power BI design specialist | Microsoft represents report design as a skill with on-demand design references and a design-contract output. An isolated design-review subagent could still be useful, but the domain itself does not require a permanent agent persona. |

**RECOMMENDATION —** Require every proposed agent to justify the context it owns that a skill cannot. “Specialist subject matter” alone is not enough.

## 9. Hooks

Hooks in the corpus are used for **event-driven, deterministic interventions around agent behaviour**, not as another place to store prose knowledge.

Cursor's advanced template demonstrates:

- `afterFileEdit` → run a formatter script;
- `beforeShellExecution` with command matching → run a safety/validation script;
- `sessionEnd` → run an audit.

Cursor Advisor uses response/stop/subagent events plus bounded state to decide when to inject a consultation checkpoint. Continual Learning uses stop-event cadence and transcript state to trigger an explicit learning flow. Addy's hooks similarly call shell scripts at session start and for workflow caching/ignore behaviour, and the hook scripts themselves have tests.

**OBSERVATION —** Hooks are strongest when the trigger condition is objective and the action is deterministic or narrowly bounded.

Where hooks outperform prompt instructions:

- formatting or regeneration after a file changes;
- blocking/inspecting risky shell operations;
- invoking a validator whenever a relevant artifact is modified;
- recording/checking lifecycle state;
- triggering a bounded audit at session end or before completion.

Where hooks are weaker:

- nuanced architectural judgment;
- open-ended domain reasoning;
- large standards bodies that still require contextual interpretation.

**RECOMMENDATION —** Future Power BI/Fabric conformance should investigate hooks as *triggers for validators*, not as the validators themselves. The normative rule should remain documented; the deterministic check should live in code/CLI; the hook should connect the event to that code.

## 10. MCP and tools

The corpus draws a useful line between **knowledge** and **capability**.

Microsoft's README and skills distinguish guidance/patterns in skills from live Fabric capability in MCP servers and CLIs. The semantic-model skill dynamically prefers Power BI Modeling MCP when available, falls back to local TMDL for appropriate operations, and stops rather than inventing unsupported behaviour when neither route is viable.

Cursor's `third_party/github` plugin demonstrates the thin extreme: the plugin is essentially a manifest plus `mcp.json` that exposes a remote GitHub MCP service. It does not need to copy the server's implementation or inject it into a skill.

Cursor's Orchestrate demonstrates the local-tool counterpart: deterministic state management, dispatch and validation belong in TypeScript scripts adjacent to the skill because they are part of the packaged workflow and do not require an external service.

**INFERENCE —** A reusable implementation can occupy at least three distinct layers:

1. **Knowledge/instructions** — “when and why to use this pattern” → skill/reference.
2. **Local executable implementation** — deterministic generation/transformation/validation → script/CLI/library.
3. **External/live capability** — access a service, workspace, semantic model or other stateful system → MCP/tool API.

This is directly relevant to the future DAX / Power Query M / Python / Deneb library. The benchmark does **not** support stuffing the implementation library into skill prose. Nor does it imply that every reusable function must become MCP. The packaging should follow the nature of the capability, to be decided in R6/R8.

## 11. Plugins and manifests

### What “plugin” means in current Cursor examples

The template and production corpus both support the conclusion that a Cursor plugin is primarily a **package/distribution and composition boundary**.

A plugin can bundle:

- rules;
- skills;
- agents/subagents;
- commands;
- hooks;
- MCP configuration;
- scripts/assets/references used by those components.

The production corpus proves that not every plugin should contain all of them:

- `third_party/github` is essentially MCP packaging.
- `orchestrate` is primarily one explicit skill plus deep executable/reference support.
- `thermos` packages an orchestrating skill and specialist agents.
- `advisor` packages a skill, subagent, hook state and scripts.
- `cursor-team-kit` contains small rules among other team utilities.

**INFERENCE —** “Plugin” answers “how does Cursor install/discover this package?” more directly than “where should the canonical architecture live?”

### Minimal and advanced plugin structure

In `cursor/plugin-template`, the simple plugin manifest is metadata-only while rules and skills are discovered by conventional directories. This demonstrates that the content directories are optional. In a multi-plugin marketplace repository, each plugin has `.cursor-plugin/plugin.json` and is registered by source in the root marketplace manifest. In a standalone/single-plugin repository, the plugin manifest can live at the repository root's `.cursor-plugin/plugin.json`; the marketplace file is not the architectural requirement for the plugin itself.

The advanced starter demonstrates all major component directories together: `rules/`, `skills/`, `agents/`, `commands/`, `hooks/`, `scripts/` and `mcp.json` plus assets.

The template validator recognises conventional component directories and also validates declared manifest paths. It checks frontmatter/JSON safety and marketplace-to-source mapping. A documentation/implementation mismatch exists for command frontmatter: the validator requires `name` and `description` even where prose describes frontmatter as recommended.

### How much architecture should live inside a plugin?

Production examples favour **self-contained package logic when it is package-specific**, but reuse external capabilities rather than copying them. Cursor Orchestrate, for example, depends on another `cursor-sdk` capability rather than re-embedding it. Large organisation-wide standards that multiple packages must share are therefore poor candidates to be privately duplicated inside every plugin.

**RECOMMENDATION —** Keep “distribution package” and “canonical knowledge authority” as two separate design decisions. A future Wayfinder Cursor plugin may assemble assets whose canonical sources live elsewhere.

## 12. AGENTS.md and persistent instructions

The repositories show three materially different uses of persistent root guidance.

### Compact router/configuration

Matt's setup skill writes a small `## Agent skills` block to whichever of `CLAUDE.md` or `AGENTS.md` already exists, then points to ordinary project docs for issue tracker, triage and domain-document configuration. It explicitly avoids creating both root instruction files when one already exists.

Addy's `AGENTS.md` opens with a strong scope boundary: it configures agents working **on the agent-skills repository itself** and is not reusable content to copy into downstream projects. The reusable assets are under `skills/`. The same file routes to deeper contributor documentation instead of restating it.

Cursor Continual Learning maintains only two learned sections in `AGENTS.md` — user preferences and workspace facts — and updates matching bullets incrementally rather than rewriting a large memory file.

### Larger portable platform guidance

Microsoft's `AGENTS.md` is substantially larger. It carries its hybrid `Agents → Skills → Common` model, authentication/setup guidance, workload routing, Power BI/Fabric patterns and Must/Avoid constraints. This makes it useful as a broad cross-agent fallback, but it also duplicates some routing/standards that exist in skills and other platform-specific root files (`CLAUDE.md`, `.cursorrules`, `.windsurfrules`).

**OBSERVATION —** The Microsoft model optimises portability/availability; the Cursor/Matt/Addy patterns optimise context economy and authority separation.

**RECOMMENDATION —** For Wayfinder, persistent project instructions should preferentially contain:

- project identity and immutable local facts;
- a tiny set of truly always-on invariants;
- capability/standards routing;
- pointers to deeper canonical documents;
- installation-generated local configuration where necessary.

They should not become another copy of the full engineering standards or domain knowledge base.

## 13. Documentation and reference architecture

Ordinary Markdown is not second-class in the strong implementations. It is the main mechanism for **large selectively loaded knowledge**.

Microsoft provides the clearest subject-router pattern. A skill's “Topic Files” or “load on demand” table maps intent to references such as DAX performance, modelling guidance, PBIP mechanics, chart selection, visual configuration, accessibility or layout. The root skill stays usable without loading every document.

Cursor Orchestrate similarly keeps planner, dispatcher, handoff and spawning details in dedicated reference files, with the skill acting as the router and TypeScript implementing stateful mechanics.

Matt's setup process deliberately creates ordinary project docs under `docs/agents/` and then installs only a short persistent pointer. This makes project configuration editable and discoverable without permanently injecting it.

Addy's root references show the benefits and the packaging hazard. Shared security, performance, testing and orchestration checklists avoid copying the same knowledge into every skill, but a single-skill copy can strand links if the package manager does not also materialise shared references.

**Architectural pattern:**

`router/index → identify relevant subject → selectively read supporting document → invoke implementation/tool`

not:

`load all standards and domain knowledge → hope the model attends to the right section`

**RECOMMENDATION —** Treat ordinary Markdown references as a deliberate tier in Wayfinder, with explicit indexes/routing metadata and installation-safe dependency paths.

## 14. Installation and bootstrap

The corpus contains four distinct installation models.

### Cursor plugin installation

Cursor plugin packaging installs a managed unit that can expose multiple native asset types. The plugin manifest is the package identity; marketplace metadata provides discovery/distribution. This is the lightest bootstrap model because it does not inherently need to generate project work artifacts.

### Matt Pocock: managed versus editable

Matt makes the distinction explicit:

- **Managed Claude plugin:** read-only/subscription-like bundle; updates follow the marketplace release path.
- **`skills.sh` install:** copies editable skill files into the user's project/agent; the user owns the copies and updates deliberately.

The repository warns that installing both produces duplicate capabilities and tells users to choose one.

### Addy Osmani / universal skills CLI

Addy uses the generic skills CLI as the widest cross-agent path, plus native integrations for several platforms. Whole-repository installs preserve shared materials; single-skill installs expose the root-reference dependency gap.

### Microsoft: bundle plus selective materialisation

Microsoft offers plugin bundles and APM-based skill installation. Its documented APM route materialises the package then activates selected skills, including rewriting/materialising links to shared references under package-managed storage. It warns against simply copying a subdirectory whose relative shared references would then dangle. MCP registration and agent deployment have their own bundle-level behaviour.

### Spec Kit: CLI/bootstrapper

Spec Kit is much heavier. The installed `specify` CLI owns project scaffolding, integration selection, scripts/templates, extension/preset registration and generated agent-specific integration assets. It also records what it created so later upgrades/uninstalls can distinguish managed files from user modifications.

**INFERENCE —** An installer should own **deployment topology and lifecycle metadata**, not become the canonical content author. The strongest bootstrapper in the corpus (Spec Kit) explicitly separates managed scaffolding from user-owned work.

**R5 evidence to carry forward:** managed versus editable mode needs to be explicit; duplicate installations need detection; dependencies need materialisation/rewrite or self-containment; local edits need hash/manifest protection; version pin/update and recovery are separate concerns.

## 15. Versioning and updating

### Cursor

Plugin manifests carry versions and marketplace/package metadata. The template validates package structure, while production plugins version their own package manifests. The corpus does not by itself fully answer enterprise/private marketplace update policy, so that remains an R5 question.

### Microsoft

The inspected Fabric package/marketplace state is versioned `0.3.16`. The project has retained deprecated plugin aliases after changing bundle identity so existing update flows do not break abruptly — a practical lesson in installation identity stability.

### Matt Pocock

`package.json` and `.claude-plugin/plugin.json` are version-synchronised; Changesets automation creates version PRs/tags. The repository's ADR notes an important operational nuance: the official Claude marketplace listing pins a source SHA, so an upstream tag/commit and what installed users receive can temporarily differ until the marketplace pin moves.

### Addy Osmani

Claude and Codex plugin adapters share the same observed `0.6.9` version around one canonical skill tree. Multiple platform manifests therefore version adapters without forking the core skill content.

### Spec Kit

Spec Kit distinguishes **CLI version** from **project-managed asset version/state**. `specify self upgrade` updates the CLI; `specify integration upgrade <key>` and extension updates refresh project-managed assets. The integration manifest records created files/hashes; upgrades block on locally modified managed files unless forced; stale managed files can be removed while user artifacts remain untouched.

**INFERENCE —** “Version the plugin” is not enough for Wayfinder if an installer also generates project assets. Package version, generated-asset provenance, external dependency version, project-owned artifact schema and rollback need separate lifecycle rules.

## 16. Testing and evaluation

The corpus shows a maturity spectrum rather than one standard.

### Structural and manifest validation

`cursor/plugin-template` validates JSON, safe paths, marketplace registration and frontmatter for rules, skills, agents and commands. This is the baseline: malformed packages should fail deterministically before an agent ever uses them.

### Executable workflow tests

Cursor Orchestrate ships substantial TypeScript plus unit tests around its dispatcher/stateful orchestration behaviour. Addy's hooks also include shell-level tests. Spec Kit has an extensive Python test tree covering integrations, extensions, hooks, contracts, migration/upgrade behaviour and adapter consistency.

### Routing/discovery evaluation

Addy is the strongest direct benchmark. Its three tiers are:

1. **Structural** — frontmatter, naming, required sections and command parity in CI.
2. **Trigger/routing** — realistic positive/negative prompts, ranking and description-collision checks in deterministic CI.
3. **Behavioural** — on-demand headless-agent runs against fixtures, graded against `expectations[]` including tool traces and pressure cases.

Every skill is expected to carry routing and behavioural eval material. This recognises that valid Markdown is not enough: descriptions can collide, fail to trigger, or trigger the wrong capability.

### Domain/output validation

Microsoft's Power BI skills embed validation into the work itself. `powerbi-report-authoring` requires PBIR validation after logical batches and rendered verification through Power BI Desktop reload/screenshot workflows. This is not the same as testing a skill's routing, but it is essential product-level conformance.

No equivalent repository-wide behavioural skill-eval harness was observed in the Microsoft or Matt snapshots. That is not evidence of poor quality; it is evidence that their QA emphasis is different.

**RECOMMENDATION —** Mature Wayfinder QA should eventually cover four layers:

- package/schema/frontmatter validity;
- capability discovery/routing and overlap;
- deterministic scripts/tools/installers;
- end-to-end agent behaviour and analytical-product output conformance, including PBIP/render validation where relevant.

## 17. Cross-agent portability

The corpus rejects the idea that portability requires all agents to use identical packaging.

### Matt Pocock

Canonical promoted skill content remains in the existing bucketed tree. Claude's manifest can explicitly list selected skill directories, so a native plugin is shipped. Codex's then-current plugin path constraint cannot express the same curated set; Matt explicitly rejects creating duplicate copies as a second source of truth and keeps the universal skills installer for Codex/other agents instead.

### Addy Osmani

One canonical `skills/` tree is surrounded by host-specific adapters: Claude and Codex plugin manifests, command wrappers, Gemini/OpenCode/etc. setup files and docs. The adapter layer varies by platform while reusable skill content remains shared.

### Spec Kit

Portability is generated. The CLI keeps a central integration registry and renders the same methodology into each agent's required directory/invocation format. Its integration documentation includes Claude, Codex, Cursor (`cursor-agent`), Copilot and many others. Integration state tracks the generated files.

### Microsoft

Microsoft provides canonical skills/common references plus multiple persistent instruction formats and package-manager targets. This reaches many agents, but the coexistence of `AGENTS.md`, `CLAUDE.md`, `.cursorrules` and other adapters illustrates the duplication pressure that portability can create.

**INFERENCE —** The strongest portability pattern is **canonical shared content + thin generated or mechanically checked adapters**, with platform-native enhancements where they add value. Do not reduce the canonical model to the lowest common denominator simply because some hosts lack hooks, agents or plugin manifests.

## 18. Context-loading and progressive disclosure

This question produces one of the clearest cross-repo patterns.

### Persistent context

Most likely persistent/context-adjacent assets are root instruction files and always-on rules. Therefore their size and authority matter. Cursor's tiny rules and Matt's short root router minimise this layer; Microsoft's broad root instructions deliberately place more platform guidance there.

### Discovery metadata

Skill name/description/frontmatter acts as a small routing surface. Addy's Tier-2 evals explicitly optimise this metadata for trigger accuracy and non-collision.

### On-demand content

Skill bodies and referenced Markdown are designed to be selected by intent. Microsoft explicitly tells the agent which reference to read for which task and not to load them all. Cursor Orchestrate does the same by role. Commands/explicit-only skills load only when invoked.

### Isolated context

Subagents provide another context-control mechanism. Thermos and Matt code review create fresh specialist contexts; the parent receives scoped outputs rather than sharing every token of every specialist's reasoning.

### Outside model context

Executable implementation and external systems stay outside prose context until represented by tool schemas/results. TypeScript/shell/Python code runs deterministically; MCP servers expose capabilities without requiring their implementation source to be read.

**Benchmark pattern:**

`small persistent router/invariants`  
`→ discovery metadata`  
`→ relevant skill`  
`→ relevant reference`  
`→ relevant script/CLI/MCP/library`  
`→ scoped result`

**RECOMMENDATION —** Make this progressive-disclosure chain an explicit evaluation criterion in R8. Any candidate design that requires loading all standards, all Microsoft guidance and all domain knowledge at session start should be treated as having a context-economics defect unless proven otherwise.

## 19. Harness vs skill-library patterns

A **skill library** provides reusable capabilities that the host/model composes. A **harness** owns more of the process: state, lifecycle, artifact generation, transitions, validation and recovery.

| Pattern | Strongest corpus examples | Characteristics |
|---|---|---|
| Skill library | Microsoft, Matt, Addy | Many discoverable bounded skills; user/model selects and composes; references/tooling support each skill. |
| Task-scoped mini-harness | Cursor Orchestrate | Explicit entry point; planner/worker/verifier roles; JSON state; executable dispatcher; structured handoffs; tests. Packaged inside a skill/plugin. |
| Project lifecycle harness | Spec Kit | Installed CLI; templates; persistent specs/plan/tasks; integration adapters; extensions/presets; upgrade manifests; project-owned state. |
| Hybrid agent-orchestration library | Microsoft | Cross-workload agent delegates endpoint depth to skills, without a separate project-generating harness. |

**INFERENCE —** “Harness versus skill” is not a packaging dichotomy. A harness can be distributed as a plugin and can expose its entry points as skills/commands. The distinction is how much lifecycle/state the component owns.

For Wayfinder, this benchmark supports carrying two questions into R2/R8 rather than choosing now:

- Does architecture/orchestration need durable lifecycle state and generated work artifacts? If yes, harness characteristics become important.
- Are specialist Fabric/domain capabilities independently reusable? If yes, a skill-library layer remains valuable even if a harness exists above it.

## 20. Canonical-source patterns

This is the strongest area of convergence.

### Spec Kit: runtime resolution instead of propagated copies

Spec Kit's upgrade documentation records an explicit architectural correction: `/constitution` no longer writes governance text into multiple templates. `plan`, `tasks` and `analyze` resolve the live `.specify/memory/constitution.md` at runtime; templates carry a pointer. The project explains the reason directly: propagation duplicated the single source of truth and conflicted with preset/override composition.

### Matt Pocock: canonical installation wording and no duplicate skill tree

`.agents/install-block.md` is declared the canonical install wording; README/change/docs consumers are expected to derive from it. More importantly, the plugin ADR rejects a flat duplicate copy of promoted skills merely to satisfy Codex's path-selection limitation because that would create a sync burden and second source of truth.

### Addy Osmani: canonical skills with thin host adapters

The same skill tree is exposed through different host manifests and wrappers. `AGENTS.md` explicitly says reusable content is the skills, not the root repository guidance. The weak point is shared root references: a canonical shared reference can still become an *unresolved dependency* when distribution copies only one skill.

### Microsoft: canonical skill/common content with package-aware materialisation

Microsoft centralises workload skills and shared common references, while APM materialises the package and rewrites shared links for selective installs. Plugin bundles then assemble selected skills/agents/MCP without needing to fork their bodies.

### Cursor: package-local authority and explicit dependency reuse

Production plugins are generally self-contained for plugin-specific material. Where a separate capability already exists, Orchestrate instructs the user/agent to use that capability rather than reimplementing it.

**Common pattern:** one canonical source for each normative concept; adapters, indexes and generated copies are acceptable only when their derivation/provenance is controlled.

**RECOMMENDATION —** For Wayfinder, evaluate every proposed duplication with three questions:

1. Which copy is authoritative?
2. How is another copy generated or checked against it?
3. What happens when only one package/repository is installed?

If those answers are unclear, the composition boundary is not ready.

## 21. Cross-repository comparison matrix

| Dimension | `cursor/plugins` | `cursor/plugin-template` | `microsoft/skills-for-fabric` | `mattpocock/skills` | `addyosmani/agent-skills` | `github/spec-kit` |
|---|---|---|---|---|---|---|
| **Primary architecture** | Production Cursor plugin ecosystem; selective combinations, including mini-harnesses | Canonical Cursor plugin package starter/validator | Fabric/Power BI skill library plus orchestrating agents and MCP | Small composable skill library | Full SDLC skill/persona/command library with adapters/evals | Project lifecycle/bootstrap harness |
| **Canonical source** | Per-plugin package contents | Template plugin directories + validator | `skills/`, agents and common refs in repo | Bucketed skill tree; `.agents` ADRs maintain policy | Canonical `skills/` plus shared refs; adapters around them | CLI/core templates/resolution stack + project constitution |
| **Rules** | Tiny always-on examples in team kit | Optional `rules/*.mdc`; starter examples | `.cursorrules` plus root guidance; substantial persistent policy | Not central; setup writes small root router | Cursor guidance says short policies only | Not a primary primitive; project constitution/templates govern methodology |
| **Skills** | Core primitive; can include refs/scripts/state harness | Optional conventional directory | Primary endpoint/domain capability unit | Primary architecture | Primary workflow capability unit | Current integrations often render workflow steps as skills |
| **Commands** | Used where explicit entry point helps; not required by every plugin | Optional `commands/` | Less central than skills | User-invoked skills often fill command role | Explicit lifecycle slash-command layer | Explicit `/speckit-*` lifecycle entry points, rendered per host |
| **Agents** | Specialist reviewers/updaters/advisors | Optional `agents/` | Cross-workload Fabric agents delegate to skills | Mostly subagents spawned from skills rather than packaged personas | Reusable specialist personas; no router-persona pattern | Agent-specific integrations rather than domain personas are central |
| **Hooks** | Production event automation in Advisor/Continual Learning | Optional hooks with formatter/safety/audit example | Not a central repo primitive | Not central | Session/workflow hooks plus tested shell scripts | Harness has hook support/tests, but lifecycle mostly CLI/assets |
| **MCP** | Thin MCP-only plugins and richer combos | Optional `mcp.json` | Multiple Fabric/Power BI MCP services bundled/configured | Not central | Used by relevant skills/platforms; not core package role | Integrations may use external agent/tool capabilities; not methodology authority |
| **Plugin** | Native package/distribution container | Canonical package format | GitHub Copilot/plugin bundles assemble skills/agents/MCP | Claude plugin is managed distribution only | Claude/Codex manifests adapt same library | Not fundamentally a Cursor-style plugin; CLI installs integrations |
| **References** | Skill-local role docs/prompts/schemas | Optional support inside skills/scripts | Large skill-local and shared common refs | Skill support + project docs produced by setup | Root shared checklists/patterns; known single-skill dependency gap | Templates/docs/project artifacts rather than skill reference libraries |
| **Installer** | Cursor plugin install/marketplace | Template documents marketplace/single-plugin package | Plugin marketplace + APM selective installation | Managed plugin or editable `skills.sh` | Universal skills CLI plus native host integrations | `specify` CLI/bootstrapper |
| **Generated assets** | Plugin runtime state for some plugins | None required | APM/package-manager materialisation | Setup skill creates project `docs/agents` config | Some host adapters copied/installed | Extensive project integrations, `.specify` assets, specs/plans/tasks |
| **Versioning** | Per-plugin manifests | Starter semver + validator | Package/bundle version; aliases preserve migration | Changesets; package/plugin sync | Shared adapter versions | CLI version + managed project asset state |
| **Evaluation** | Plugin-specific executable tests; real hooks/scripts | Structural validation | Product validation embedded in skills; limited repo-wide behavioural eval observed | Release/version checks; no comparable behavioural harness observed | Three-tier structural/routing/behavioural skill evals | Extensive CLI/integration/contract/upgrade tests |
| **Context strategy** | Small skill routers + refs/scripts; subagent isolation | Encourages separate asset types | Explicit on-demand refs; agent→skill→common routing | Small composable skills + project docs | Skill discovery + shared refs + personas; routing tested | Persistent artifacts; workflow step loads current relevant assets |
| **Cross-agent support** | Cursor-native by design | Cursor-native | Many agents/hosts through package/install targets and root adapters | Universal skills install; native plugin only where clean | Many explicit host adapters + universal skills CLI | Integration registry generates many host-specific layouts including Cursor/Codex/Claude |

## 22. Patterns worth adopting

These are candidate patterns for R8, not commitments.

### Small router, deep on demand

Persist only the minimum context required to route correctly. Make each skill name/description precise, then let the skill select references and tools by intent.

### Explicit capability boundaries

Microsoft's Power BI design → authoring handoff is a strong benchmark: design owns a structured design contract; authoring owns PBIR mechanics and validation. Similar contracts can prevent a future Wayfinder orchestrator, domain pack and platform skill from all claiming the same responsibility.

### Agent isolation only where it buys something

Use fresh subagent contexts for independent review axes, specialist audits or parallel bounded work. Require structured handoffs/aggregation when parallelism is introduced.

### Deterministic execution for deterministic obligations

Formatting, schema validation, package validation, generator logic and conformance checks should be executable and testable. Prompts should decide *when/why*; tools should prove *whether*.

### Manifest-aware installation

Track what the installer owns, hashes/provenance, dependency versions, managed versus editable mode and local modifications. Preserve project-owned work artifacts across upgrades.

### Canonical shared content plus thin adapters

Permit platform-specific manifests/invocation wrappers, but generate/check them from one canonical source where possible. Never create an independently edited second copy solely because one host's package format is awkward.

### Quality assurance beyond syntax

Adopt the Addy distinction between structural validity, trigger/routing quality and behavioural quality, then add analytical-product validation appropriate to PBIP/Fabric.

## 23. Patterns worth avoiding

### Monolithic persistent instruction files

They consume context on unrelated tasks and create a second standards authority. Microsoft's larger root guidance is useful portability evidence but should not be copied uncritically into a project that can route to skills/references selectively.

### Duplicating Microsoft-owned platform mechanics

Forking PBIR schema guidance, semantic-model tool mechanics or Fabric API behaviour into a Wayfinder-specific copy would create a maintenance race with the closest upstream authority.

### Making “plugin” the architecture

A plugin can be a one-file MCP wrapper or a full orchestration package. Selecting “plugin” does not answer capability boundaries, canonical source, context policy or project state.

### Agent-per-topic design

Speciality alone does not justify a persistent persona. Too many agents increase handoff and coordination cost. Use a skill for bounded expertise unless independent context/agency is required.

### Prompt-only conformance

If a rule can be checked mechanically, do not rely only on “remember to follow this”. Hooks/scripts/CLI/CI should enforce deterministic constraints.

### Shared-reference dependencies that installers do not carry

Addy's documented single-skill reference gap is directly relevant to cross-repository composition. Never assume a relative link survives when the consumer installs only one subdirectory.

### Manually maintained adapter copies

Platform-specific wrappers are acceptable; duplicated normative bodies are not. Matt's rejected Codex duplicate-tree option is the clearest warning.

### Updating generated assets without ownership boundaries

Spec Kit's hash-aware upgrade model exists because generated integration files can be locally edited. Blind overwrite is unsuitable for a development ecosystem expected to preserve project work.

## 24. Implications for Power BI/Fabric Architect

### Architect/orchestrator

Evidence supports treating orchestration as a responsibility above specialist skills, but does not decide whether the final form is a Cursor agent, explicit skill/command, plugin-contained mini-harness or external bootstrap harness.

A strong candidate boundary is: the architect owns decomposition, dependency ordering, project-wide decisions, handoffs and completion/conformance gates; specialist capabilities own bounded domain/platform work.

### Engineering standards

Standards should have a canonical ordinary-document authority. A small persistent rule/router can identify mandatory standards; skill references can load relevant chapters; deterministic validators should enforce machine-checkable parts. Avoid pasting the complete standards set into every skill or root instruction file.

### Domain packs

Performance & Reward domain material is conceptually different from Microsoft platform mechanics. Domain packs can provide semantics, design patterns, measures, terminology and domain-specific conformance while delegating PBIR/TMDL/Fabric mechanics to upstream Microsoft skills/tools where practical.

### Microsoft skills

There is substantial overlap with intended Wayfinder platform-specialist functionality: semantic model authoring, DAX guidance, Power BI planning/design/authoring/management, PBIP/TMDL references, Fabric workloads and validation tooling.

**RECOMMENDATION —** Treat Microsoft skills as an upstream capability dependency to integrate/delegate to before duplicating them. Wayfinder should add orchestration, organisation engineering standards, Performance & Reward knowledge, reusable internal implementations and stronger conformance where those are genuinely distinct.

### Reusable DAX / M / Python / Deneb library

Keep instruction and implementation separate. Skills can select/explain library components; scripts/CLIs can generate or validate deterministic assets; MCP is appropriate only where live/external capability is needed. The reusable source should remain inspectable/versionable independently of prompt text.

### PBIP projects

Spec Kit provides the strongest ownership analogy: generated methodology/integration scaffolding can be managed, while project artifacts remain project-owned and upgrade-safe. For PBIP work, design briefs, architecture decisions, specs and the PBIP itself should not be disposable cache owned by the installer.

Microsoft's report workflow adds a product-specific lesson: planning/design outputs can form explicit contracts that authoring consumes; authoring then validates PBIR and rendered output.

### Validation

Future conformance likely needs layers: standards routing, file/schema validation, DAX/model checks, PBIR validation, possibly Desktop/render verification, domain rules, and architecture-level checks. Hooks can trigger cheap deterministic checks; CI can run broader suites; agent behavioural evals can test whether the system routes and applies the checks correctly.

### Installer/bootstrap

R5 should benchmark against Spec Kit's managed-file manifest, Matt's managed-versus-editable distinction, Microsoft's shared-reference materialisation and Addy's partial-install failure mode. Required concerns include duplicate detection, pinning, dependency mapping, safe updates, local edits and rollback/recovery.

## 25. Inputs this provides to R2

R2 asks about **harness vs agent vs skill vs plugin**. R3 provides these evidence-backed distinctions:

- **Plugin:** distribution/composition boundary; can ship any of the other patterns.
- **Skill:** bounded reusable capability and progressive-disclosure router; can itself orchestrate subagents or scripts.
- **Agent:** context/role owner; justified by isolation, sustained cross-cutting responsibility or independent perspective.
- **Harness:** lifecycle/state/artifact owner; can be implemented inside a skill/plugin (Cursor Orchestrate) or as an external CLI/bootstrap system (Spec Kit).
- **Command:** explicit user-facing workflow entry point; orthogonal to the above.

R2 should therefore compare responsibility ownership, not only syntax/primitives.

## 26. Inputs this provides to R4

R4 cross-repository composition should investigate:

- how a consumer resolves a skill/reference/tool whose canonical source is another repository;
- whether dependencies are pinned by commit/version/lockfile;
- whether installation materialises shared references or leaves cross-repo links;
- whether adapters are generated rather than manually duplicated;
- how an orchestration package detects missing upstream Microsoft skills/tooling;
- what remains usable in an offline/local-only project;
- whether domain packs can depend on standards/library interfaces without taking ownership of those repositories.

The Addy single-skill shared-reference gap and Microsoft's package-aware materialisation are the clearest opposing benchmark examples.

## 27. Inputs this provides to R5

R5 installer/bootstrap research should carry forward these benchmark requirements:

- explicit **managed** versus **editable/development** modes;
- installation manifest/provenance and local-change detection;
- duplicate capability/install detection;
- dependency materialisation/path rewriting;
- version pinning and update channels;
- identity/alias migration without breaking existing installs;
- rollback/clean uninstall;
- safe preservation of user/project artifacts;
- multiple-agent integration without uncontrolled duplication;
- recovery path when generated assets predate the current manifest system.

Spec Kit is the primary harness benchmark; Matt provides the clearest user-facing managed/editable split.

## 28. Inputs this provides to R6

R6 standards/library packaging should test a four-layer hypothesis from this corpus:

1. **Canonical normative docs** — standards and domain/reference authority.
2. **Skills** — scope/workflow and selective routing into those docs.
3. **Executable library/tools** — reusable DAX/M/Python/Deneb implementations and deterministic validators/generators.
4. **Persistent rules/hooks** — small routing/invariants and event triggers, not duplicated knowledge.

R6 should specifically test how references stay valid when a skill is installed independently and how version compatibility between standards, skill and implementation library is expressed.

## 29. Inputs this provides to R7

R7 cross-agent portability should compare three proven strategies:

- **Universal copied skills + selective native package where clean** — Matt.
- **Canonical reusable tree + many thin platform adapters** — Addy.
- **Canonical methodology + generated integration-specific project assets** — Spec Kit.

Microsoft adds a fourth hybrid: canonical skills/common assets plus several persistent root adapters and package-manager targets.

Key R7 criterion: portability must not create a manually maintained second normative source. Cursor-native features such as hooks/subagents may remain platform-specific while domain/standards content stays portable.

## 30. Unresolved questions

The six repositories leave the following questions open or only partially answered:

1. **Cursor runtime loading semantics:** exactly how much skill/rule/plugin metadata and body content is counted in context before versus after capability selection in the current Cursor release. Repository design strongly signals progressive disclosure, but the repos do not fully specify runtime token accounting.
2. **Cursor managed-update semantics for private/internal plugins:** pinning, rollback and enterprise marketplace behaviour need deeper R5 evidence from current product documentation or testing.
3. **Cross-plugin dependencies in Cursor:** Orchestrate demonstrates a dependency on another capability, but the repository does not establish a general dependency/version manifest protocol for arbitrary internal plugins.
4. **Microsoft upstream dependency contract:** how Wayfinder should pin or track `skills-for-fabric` while still receiving platform fixes without unreviewed behaviour drift.
5. **Shared standards across repositories:** whether canonical Wayfinder standards are referenced remotely, vendored/materialised, packaged as a dependency, or resolved by an installer is intentionally left to R4/R5/R6.
6. **Domain-pack contract:** the exact interface between Performance & Reward domain semantics and platform skills/reusable implementations is not yet defined.
7. **Validator execution environment:** which Power BI/Fabric checks can run headlessly in CI versus requiring Power BI Desktop, authenticated MCP, Fabric workspace access or human/render review.
8. **Behavioural eval harness choice:** Addy's model is strong evidence for routing/behavioural evals, but the appropriate agent/model matrix, cost budget and deterministic acceptance thresholds for Wayfinder need separate design.
9. **Stateful orchestration boundary:** whether Wayfinder needs Spec-Kit-like project lifecycle state, Cursor-Orchestrate-like task state, or only lightweight skill composition is an R2/R8 decision.
10. **Generated adapter policy:** if multi-agent support requires generated Cursor/Codex/Claude assets, the canonical schema and regeneration/conformance mechanism remain to be designed in R7.

No additional repository was consulted to answer these; doing so would have expanded the mandatory corpus without being necessary for the R3 benchmark itself.

## 31. Sources

All repository links below are pinned to the inspected commit/ref where practical.

### R3 ticket / target repository

- https://github.com/GitKlink/performance-reward-dashboard-architect/issues/11
- https://github.com/GitKlink/performance-reward-dashboard-architect/blob/main/research/cursor-architecture/README.md

### `cursor/plugins`

- https://github.com/cursor/plugins/tree/c1c0a32802223f4be824112dd83d33ad29a8b26c
- https://github.com/cursor/plugins/blob/c1c0a32802223f4be824112dd83d33ad29a8b26c/.cursor-plugin/marketplace.json
- https://github.com/cursor/plugins/blob/c1c0a32802223f4be824112dd83d33ad29a8b26c/orchestrate/.cursor-plugin/plugin.json
- https://github.com/cursor/plugins/blob/c1c0a32802223f4be824112dd83d33ad29a8b26c/orchestrate/skills/orchestrate/SKILL.md
- https://github.com/cursor/plugins/blob/c1c0a32802223f4be824112dd83d33ad29a8b26c/thermos/skills/thermos/SKILL.md
- https://github.com/cursor/plugins/blob/c1c0a32802223f4be824112dd83d33ad29a8b26c/thermos/agents/thermo-nuclear-review-subagent.md
- https://github.com/cursor/plugins/blob/c1c0a32802223f4be824112dd83d33ad29a8b26c/advisor/hooks/hooks.json
- https://github.com/cursor/plugins/blob/c1c0a32802223f4be824112dd83d33ad29a8b26c/advisor/skills/advisor/SKILL.md
- https://github.com/cursor/plugins/blob/c1c0a32802223f4be824112dd83d33ad29a8b26c/continual-learning/README.md
- https://github.com/cursor/plugins/blob/c1c0a32802223f4be824112dd83d33ad29a8b26c/cursor-team-kit/rules/no-inline-imports.mdc
- https://github.com/cursor/plugins/blob/c1c0a32802223f4be824112dd83d33ad29a8b26c/third_party/github/mcp.json

### `cursor/plugin-template`

- https://github.com/cursor/plugin-template/tree/46216072ac5750f782f95bb325b4d12b7c3ae9c9
- https://github.com/cursor/plugin-template/blob/46216072ac5750f782f95bb325b4d12b7c3ae9c9/README.md
- https://github.com/cursor/plugin-template/blob/46216072ac5750f782f95bb325b4d12b7c3ae9c9/docs/add-a-plugin.md
- https://github.com/cursor/plugin-template/blob/46216072ac5750f782f95bb325b4d12b7c3ae9c9/plugins/starter-simple/.cursor-plugin/plugin.json
- https://github.com/cursor/plugin-template/blob/46216072ac5750f782f95bb325b4d12b7c3ae9c9/plugins/starter-advanced/.cursor-plugin/plugin.json
- https://github.com/cursor/plugin-template/blob/46216072ac5750f782f95bb325b4d12b7c3ae9c9/plugins/starter-advanced/skills/code-reviewer/SKILL.md
- https://github.com/cursor/plugin-template/blob/46216072ac5750f782f95bb325b4d12b7c3ae9c9/plugins/starter-advanced/rules/coding-standards.mdc
- https://github.com/cursor/plugin-template/blob/46216072ac5750f782f95bb325b4d12b7c3ae9c9/plugins/starter-advanced/agents/security-reviewer.md
- https://github.com/cursor/plugin-template/blob/46216072ac5750f782f95bb325b4d12b7c3ae9c9/plugins/starter-advanced/commands/deploy-staging.md
- https://github.com/cursor/plugin-template/blob/46216072ac5750f782f95bb325b4d12b7c3ae9c9/plugins/starter-advanced/hooks/hooks.json
- https://github.com/cursor/plugin-template/blob/46216072ac5750f782f95bb325b4d12b7c3ae9c9/plugins/starter-advanced/mcp.json
- https://github.com/cursor/plugin-template/blob/46216072ac5750f782f95bb325b4d12b7c3ae9c9/scripts/validate-template.mjs

### `microsoft/skills-for-fabric`

- https://github.com/microsoft/skills-for-fabric/tree/24cc0d296e5e8523cc6a92e1342bc1791d7deb85
- https://github.com/microsoft/skills-for-fabric/blob/24cc0d296e5e8523cc6a92e1342bc1791d7deb85/README.md
- https://github.com/microsoft/skills-for-fabric/blob/24cc0d296e5e8523cc6a92e1342bc1791d7deb85/AGENTS.md
- https://github.com/microsoft/skills-for-fabric/blob/24cc0d296e5e8523cc6a92e1342bc1791d7deb85/agents/FabricDataEngineer.agent.md
- https://github.com/microsoft/skills-for-fabric/blob/24cc0d296e5e8523cc6a92e1342bc1791d7deb85/skills/semantic-model-authoring/SKILL.md
- https://github.com/microsoft/skills-for-fabric/blob/24cc0d296e5e8523cc6a92e1342bc1791d7deb85/skills/powerbi-report-design/SKILL.md
- https://github.com/microsoft/skills-for-fabric/blob/24cc0d296e5e8523cc6a92e1342bc1791d7deb85/skills/powerbi-report-authoring/SKILL.md
- https://github.com/microsoft/skills-for-fabric/blob/24cc0d296e5e8523cc6a92e1342bc1791d7deb85/.github/plugin/marketplace.json
- https://github.com/microsoft/skills-for-fabric/blob/24cc0d296e5e8523cc6a92e1342bc1791d7deb85/package.json

### `mattpocock/skills`

- https://github.com/mattpocock/skills/tree/959a8e9f1edc3adbe2f7e3054bb6fbefa6696260
- https://github.com/mattpocock/skills/blob/959a8e9f1edc3adbe2f7e3054bb6fbefa6696260/README.md
- https://github.com/mattpocock/skills/blob/959a8e9f1edc3adbe2f7e3054bb6fbefa6696260/.agents/adr/0002-ship-as-a-claude-code-plugin.md
- https://github.com/mattpocock/skills/blob/959a8e9f1edc3adbe2f7e3054bb6fbefa6696260/.agents/install-block.md
- https://github.com/mattpocock/skills/blob/959a8e9f1edc3adbe2f7e3054bb6fbefa6696260/.claude-plugin/plugin.json
- https://github.com/mattpocock/skills/blob/959a8e9f1edc3adbe2f7e3054bb6fbefa6696260/skills/engineering/code-review/SKILL.md
- https://github.com/mattpocock/skills/blob/959a8e9f1edc3adbe2f7e3054bb6fbefa6696260/skills/engineering/setup-matt-pocock-skills/SKILL.md
- https://github.com/mattpocock/skills/blob/959a8e9f1edc3adbe2f7e3054bb6fbefa6696260/.github/workflows/release.yml
- https://github.com/mattpocock/skills/blob/959a8e9f1edc3adbe2f7e3054bb6fbefa6696260/package.json

### `addyosmani/agent-skills`

- https://github.com/addyosmani/agent-skills/tree/be4e44a9fbc5e8df0beaefadbb28bd22ee61cc39
- https://github.com/addyosmani/agent-skills/blob/be4e44a9fbc5e8df0beaefadbb28bd22ee61cc39/README.md
- https://github.com/addyosmani/agent-skills/blob/be4e44a9fbc5e8df0beaefadbb28bd22ee61cc39/AGENTS.md
- https://github.com/addyosmani/agent-skills/blob/be4e44a9fbc5e8df0beaefadbb28bd22ee61cc39/.claude-plugin/plugin.json
- https://github.com/addyosmani/agent-skills/blob/be4e44a9fbc5e8df0beaefadbb28bd22ee61cc39/.codex-plugin/plugin.json
- https://github.com/addyosmani/agent-skills/tree/be4e44a9fbc5e8df0beaefadbb28bd22ee61cc39/references
- https://github.com/addyosmani/agent-skills/tree/be4e44a9fbc5e8df0beaefadbb28bd22ee61cc39/agents
- https://github.com/addyosmani/agent-skills/tree/be4e44a9fbc5e8df0beaefadbb28bd22ee61cc39/hooks
- https://github.com/addyosmani/agent-skills/blob/be4e44a9fbc5e8df0beaefadbb28bd22ee61cc39/hooks/hooks.json
- https://github.com/addyosmani/agent-skills/tree/be4e44a9fbc5e8df0beaefadbb28bd22ee61cc39/commands
- https://github.com/addyosmani/agent-skills/blob/be4e44a9fbc5e8df0beaefadbb28bd22ee61cc39/evals/README.md

### `github/spec-kit`

- https://github.com/github/spec-kit/tree/1d5106f59e1b148ee23ab136638932dd790ff1b6
- https://github.com/github/spec-kit/blob/1d5106f59e1b148ee23ab136638932dd790ff1b6/README.md
- https://github.com/github/spec-kit/blob/1d5106f59e1b148ee23ab136638932dd790ff1b6/docs/upgrade.md
- https://github.com/github/spec-kit/blob/1d5106f59e1b148ee23ab136638932dd790ff1b6/docs/reference/integrations.md
- https://github.com/github/spec-kit/tree/1d5106f59e1b148ee23ab136638932dd790ff1b6/templates/commands
- https://github.com/github/spec-kit/tree/1d5106f59e1b148ee23ab136638932dd790ff1b6/templates
- https://github.com/github/spec-kit/blob/1d5106f59e1b148ee23ab136638932dd790ff1b6/src/specify_cli/commands/init.py
- https://github.com/github/spec-kit/blob/1d5106f59e1b148ee23ab136638932dd790ff1b6/src/specify_cli/_agent_config.py
- https://github.com/github/spec-kit/tree/1d5106f59e1b148ee23ab136638932dd790ff1b6/src/specify_cli/integrations
- https://github.com/github/spec-kit/tree/1d5106f59e1b148ee23ab136638932dd790ff1b6/tests
- https://github.com/github/spec-kit/blob/1d5106f59e1b148ee23ab136638932dd790ff1b6/.specify/memory/constitution.md
