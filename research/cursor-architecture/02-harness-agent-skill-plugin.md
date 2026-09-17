# Research R2 — Harness vs agent vs skill vs plugin architecture

**Research ticket:** GitHub issue #12 — *Research R2: Harness vs agent vs skill vs plugin architecture*  
**Programme:** Wayfinder architecture — Power BI / Fabric analytical-product architect ecosystem  
**Evidence snapshot:** 16 September 2026  
**Durable target:** `research/cursor-architecture/02-harness-agent-skill-plugin.md`  
**Status:** Architectural research and classification. **Not the final target-architecture decision.**

## Executive finding

The precise answer to **“Are we building a harness, an agent, skills, a plugin — or all of them?”** is:

> **We are designing a layered analytical-product orchestration ecosystem that runs on an existing agent harness, presents an Architect as an agent-like orchestrator, composes specialist capabilities primarily as skills and selectively as subagents/tools, keeps domain and engineering authority in separate canonical repositories or knowledge packs, and may be distributed as one or more plugins plus an optional bootstrap/installer layer.**

These labels are **not competing alternatives at one architectural level**.

The most important separation is:

| Question | R2 classification |
|---|---|
| **What is the overall system?** | An **analytical-product orchestration system/ecosystem** layered on a host agent runtime/harness |
| **What is the Architect?** | A **manager/orchestrator role** operating through the host agent, not necessarily a new standalone agent runtime |
| **What performs specialist repeatable work?** | Primarily **skills**; **subagents** where isolated context, independent reasoning or parallelism is valuable |
| **Where do engineering policies live?** | A **standards authority/repository**, consumed on demand rather than duplicated into prompts |
| **Where does business meaning live?** | **Domain packs** combining domain knowledge/reference with domain-specific capabilities |
| **Where does executable reuse live?** | A normal **implementation library**, surfaced to agents through skills/scripts/tools where useful |
| **How do live external capabilities enter?** | **Tools/MCP**, with local scripts for simpler repository-local execution |
| **How are hard controls enforced?** | **Hooks/validators**, not natural-language instructions alone |
| **How are common interactive entry points exposed?** | Skills and, where appropriate, **commands/workflows** |
| **How is the system shipped?** | Potentially a **plugin/bundle** |
| **How is it materialised across projects/hosts?** | Potentially an **installer/bootstrap layer** |
| **What provides the underlying agent loop?** | Initially **Cursor's harness**, not a Wayfinder-built replacement |

This directly extends rather than reopens R1. R1 already concluded that Cursor separates instruction, capability, delegated cognition, deterministic control, external capability and distribution, and explicitly warned R2 not to treat “plugin”, “skill”, “subagent”, “harness” and related terms as choices at one abstraction level. fileciteturn15file0L2-L2 fileciteturn17file0L2-L2

There is, however, an important evidence-state problem. Issue #12 declares both R1 and R3 as required inputs. fileciteturn13file0L3-L6 R1 is complete on the open `research/r1-cursor-primitives` branch/PR #18 rather than `main`; its completion comment records its major findings. fileciteturn8file0L4-L5 At research time, `research/cursor-architecture/` on `main` exposed only `README.md`, not either completed report. fileciteturn2file0L2-L10 More importantly, I could not locate the required `03-reference-repo-benchmark.md`; issue #11 still appeared open with no comments in the accessible repository state. fileciteturn7file0L3-L6 fileciteturn7file0L33-L38

**That is a repository-state contradiction with the premise that R3 is already a completed durable input.** I have therefore **not pretended to have read R3**. To make R2 useful despite that gap, I inspected the relevant architecture evidence directly in the mandatory R3 reference corpus. This should be reconciled against the real R3 artifact if/when it becomes available before R2 is treated as final research evidence.

## Architectural vocabulary and boundaries

The terms become much less ambiguous when classified by the problem each one solves.

| Architecture type | Precise architectural meaning | It owns | It does **not** inherently own | Wayfinder implication |
|---|---|---|---|---|
| **Agent** | A reasoning/acting unit: an LLM configured with instructions, capabilities and runtime behaviour | Decision-making for a task, tool selection, iterative reasoning | Distribution, canonical standards, an entire runtime platform | The Architect may **behave as** an agent role without Wayfinder implementing its own agent runtime |
| **Subagent** | A delegated specialist agent, normally with its own context and task boundary | Isolated specialist reasoning, parallel work, independent verification | General reusable knowledge storage or distribution | Use selectively for architecture analysis, independent validation, specialised long-running work |
| **Agent harness** | The runtime envelope in which an agent operates | Model + instructions/context + tools; commonly the loop/runtime machinery that drives execution | Domain standards or product packaging as such | **Cursor already provides this layer** initially |
| **Orchestration layer** | Logic/policy coordinating the sequence, routing and interaction of agents, capabilities, tools and artifacts | “What happens next?”, delegation, routing, workflow control | Necessarily the model runtime or package format | This is the strongest description of the **Architect's core responsibility** |
| **Skill** | A portable, progressively loaded capability package | Task-specific instructions plus optional scripts, references and assets | Full agent runtime; canonical ownership of every standard it cites | Preferred unit for modular analytical capabilities |
| **Skill library** | A curated collection/taxonomy of skills | Capability catalogue, reuse, discoverability, shared conventions | Central runtime or guaranteed end-to-end orchestration | Wayfinder will almost certainly contain or consume several |
| **Plugin** | An installable composition/distribution package | Bundling and installation of rules, skills, agents, hooks, MCP and other assets | The semantic role of those contained assets; an agent loop by itself | Likely a **shipping format**, not the answer to “what is Wayfinder?” |
| **Rules / instruction system** | Persistent or scoped behavioural guidance injected into agent operation | Invariants, policies, routing hints, behavioural constraints | Large canonical standards corpora; deterministic enforcement | Keep thin; use as guardrails/routes to authority |
| **Command / workflow system** | Named entry point for an explicit procedure | User-triggered workflow initiation and sequencing | General automatic expertise or hard runtime guarantees | Useful façade for high-value procedures, but richer workflows can be skills |
| **Knowledge / reference repository** | Passive canonical information retrieved when required | Facts, explanations, architecture references, examples and source material | Enforcement, reasoning loop, autonomous action | Appropriate for substantial knowledge that should remain outside persistent context |
| **Standards repository** | A knowledge repository with **normative authority** | Engineering policy, definitions, compliance expectations and governance | Agent runtime or reusable production code | Engineering standards should remain an authority distinct from both Architect and implementation library |
| **Tool / MCP capability** | A callable execution/data boundary connecting the agent to systems | Actions, live data and external services | Normative policy or orchestration strategy | Fabric/Power BI APIs, model inspection/editing and services belong here where suitable |
| **Installer / bootstrap layer** | A deterministic deployment/materialisation mechanism | Selecting, adapting, copying/linking and configuring runtime assets for a host/project | Reasoning or domain expertise | Useful if Wayfinder must support many project repos or multiple agent hosts |

### Agent and subagent

OpenAI's current Agents SDK describes an agent as an LLM configured with instructions, tools and optional behaviour such as handoffs, guardrails and structured outputs. The SDK separately provides a runner that manages turns, tools and handoffs, illustrating the difference between **the agent definition** and **the machinery running it**. citeturn8search1turn8search4

Cursor's subagents are specialised assistants delegated to by the parent agent; each has its own context window, can run independent multi-step work and can operate in parallel. Cursor explicitly contrasts this with skills: use subagents for context isolation, parallel work or substantial independent investigation; use skills for simpler repeatable capabilities where a separate context is unnecessary. citeturn7search1

Therefore:

```text
Agent     = actor / reasoning unit
Subagent  = delegated actor / reasoning unit with its own task/context boundary
```

A domain such as “DAX” is **not automatically a reason to create a DAX subagent**. If “write or review DAX according to these standards” can be executed efficiently within the current context, it fits a skill. A subagent becomes justified when the architecture requires **independent context, specialised model/tool configuration, extended investigation, parallel execution or independent verification**. This follows both Cursor's current guidance and R1. citeturn7search1 fileciteturn16file0L2-L2

### Agent harness

“Agent harness” is the most overloaded term in this ticket.

Cursor's own current learning material gives a particularly useful definition: an agent runs inside a **harness** made from its instructions, tools and model. citeturn11search0 Contemporary agent systems extend that practical envelope with execution-loop behaviour, workspace/environment management, state, tool mediation and agent coordination; for example, OpenAI explicitly calls its sandbox runtime an “execution harness” that wires together filesystem tools, shell access, sandbox lifecycle and snapshots around the normal agent/runner model. citeturn8search9turn8search5

That yields a useful R2 test:

> **If Wayfinder supplies content and configuration to Cursor but Cursor still owns model invocation, the agent loop, core tool execution, context machinery, runtime and execution environment, Wayfinder is not an independent agent harness.**

Wayfinder may **extend or configure a harness**. It may add orchestration, hooks, instructions, MCP tools and capabilities around that harness. But calling the whole repository “the agent harness” would imply more runtime ownership than the current model warrants. Cursor itself explicitly speaks of ongoing “Cursor Harness Improvements”, reinforcing that Cursor regards the harness as part of its product runtime. citeturn10search0

This distinction is strategically important. A future Wayfinder runtime that directly owns model calls, state transitions, context assembly, tool execution, retries, sandbox lifecycle and cross-agent scheduling **could** properly be called its own harness. R2 does not provide evidence that such a replacement runtime is currently required.

### Orchestration layer

Orchestration answers a different question from harnessing: **how should work be decomposed, routed and coordinated?**

OpenAI's orchestration guidance distinguishes manager-style orchestration—where one agent invokes specialists as tools—from handoff-style orchestration, where control is transferred between agents. The important architectural point is that orchestration is about **the flow among actors/capabilities**, and may be driven by an LLM, code or a mixture. citeturn8search0

This is almost exactly the role already assigned to the project-level **ARCHITECT** in the ticket context: interpret the problem, select applicable standards/capabilities, coordinate the path from business question to analytical product, and delegate rather than own all engineering expertise.

Thus the strongest R2 classification is:

> **Architect = orchestration role.**

That role might be implemented largely inside the main Cursor Agent through an orchestration skill, augmented by subagents, commands and deterministic scripts/hooks. It does **not** require the orchestrator to become a second agent runtime.

Cursor's own production `orchestrate` plugin is instructive. It distributes an orchestration capability principally as a **Skill plus scripts/assets**; its README says the skill fans a task out across Cursor cloud agents while scripts reconcile the task tree. fileciteturn26file0L2-L10 fileciteturn27file0L2-L6 This is concrete evidence that **“orchestration” is a functional role while “skill”, “script”, “agent” and “plugin” are implementation/distribution mechanisms around it**.

### Skill and skill library

The Agent Skills specification defines a skill as a folder centred on `SKILL.md`, with optional scripts, references and assets. Skills use progressive disclosure: only metadata is needed for initial discovery; the full skill loads when applicable; deeper supporting files are retrieved as required. citeturn8search2

That is a strong match for analytical architecture because Power BI/Fabric work contains many **specialist capabilities that are important sometimes but unnecessary most of the time**: semantic modelling, DAX, M, report design, Fabric architecture, testing, deployment and domain-specific reasoning. R1 had already identified this as one of the strongest reasons to use Skills rather than large permanently loaded rules. fileciteturn16file0L2-L2

A **skill library** is simply the governed collection of these capability packages. It has different semantics from an agent:

```text
Skill library
    semantic-model-design
    dax-engineering
    power-query-engineering
    report-design
    quality-validation
    domain-analysis
    ...

Agent / Architect
    selects and composes these capabilities for the current problem
```

The distinction matters because a skill library can remain highly portable even when the host agent changes.

### Plugin

Current Cursor Plugins package Rules, Skills, Agents, Commands, MCP servers and Hooks into installable bundles. Cursor now also distinguishes the more portable Agent Plugin model from Cursor-specific plugin capabilities. citeturn7search0

Therefore:

```text
Plugin ≠ Agent
Plugin ≠ Harness
Plugin ≠ Orchestrator
Plugin = packaging / composition / installation boundary
```

A plugin can **contain** the assets implementing an Architect. That does not make “plugin” the architectural identity of the Architect.

R1 reached the same conclusion, and Cursor's official plugin template and production plugins show the composition model directly. fileciteturn17file0L2-L2 fileciteturn18file0L2-L10

### Rules, commands, knowledge and standards

R1 established that Cursor Rules are prompt-bearing behavioural instructions, whereas ordinary documentation remains passive until retrieved. Large always-loaded standards therefore have materially different context economics from canonical documents reached through a thin rule or skill. fileciteturn15file0L2-L2 fileciteturn16file0L2-L2 Current Cursor Rules remain scoped/invocable project instructions under `.cursor/rules`. citeturn9search1

That creates a strong boundary:

```text
RULE
"Whenever modifying a semantic model, apply the canonical semantic-model standard."

STANDARD
Full normative specification of naming, relationships, measures,
calculation groups, metadata, validation, etc.
```

The first belongs in an instruction/routing layer. The second belongs in the standards authority.

This is also consistent with open issue #5, which explicitly treats semantic-model, DAX and Power Query standards as separate engineering authorities and rejects the reusable DAX/M implementation library as the standards authority. fileciteturn14file0L3-L6

A **knowledge repository** and a **standards repository** therefore differ primarily in authority:

```text
knowledge/reference repo
    descriptive / explanatory / evidentiary
    "this is how something works"

standards repo
    normative / governed
    "this is how our analytical products must be engineered"
```

Either can be consumed by skills. Neither becomes a skill merely because an agent reads it.

Commands occupy yet another boundary: R1 found them best suited to explicit repeatable user-triggered workflows. A command can start orchestration, but it should not become the canonical knowledge store or executable implementation library. fileciteturn16file0L2-L2

### Tools, MCP and bootstrap

MCP is currently an open standard for connecting AI applications to external systems, data sources, tools and workflows. Cursor supports MCP tools, prompts and resources. citeturn6search2turn9search3 The boundary is therefore primarily **capability access**, not architecture policy.

For Wayfinder:

```text
"Use star schema unless..."      → standard/rule
"How to design this schema"      → skill
"Inspect this live model"        → tool/MCP
"Change this model"              → tool/MCP/script
"Verify this model conforms"     → validator/tool/hook
```

An installer/bootstrap layer is different again: it deterministically materialises the right assets into a target project or agent environment. GitHub's Spec Kit illustrates this pattern clearly. Its CLI initialises a project for a selected coding-agent integration, after which the **external coding agent** runs the generated skills/workflows; Spec Kit describes itself as a toolkit providing processes, templates and documented outcomes, rather than as the agent runtime itself. fileciteturn23file0L2-L6

Microsoft's Fabric Skills repository demonstrates a similar separation at the platform-domain level: plugin bundles distribute sets of capabilities; APM can selectively deploy skills to different agent hosts and configure related MCP dependencies; the repository explicitly distinguishes skills, which provide guidance and patterns, from MCP servers, which provide live system/API access. fileciteturn19file0L2-L6

## Evidence from prior research and reference implementations

### What R1 has already settled

R1 should remain authoritative for Cursor-native primitive behaviour. Its major architectural implications for R2 are:

> **Instruction, capability, delegation, deterministic control, external integration and distribution are distinct concerns.** fileciteturn15file0L2-L2

> **Canonical knowledge storage and activation are different problems.** Putting a standard in a Rule is not equivalent to keeping the standard canonical and having a Rule/Skill retrieve it. fileciteturn15file0L2-L2

> **Skills are capability packages; Subagents are context/delegation units; Hooks provide deterministic lifecycle control; MCP provides external capability; Plugins provide distribution/composition.** fileciteturn16file0L2-L2 fileciteturn17file0L2-L2

> **“Harness” is an architecture pattern above Cursor's individual customisation primitives.** R1 explicitly directed R2 to compare compositions rather than choose one noun. fileciteturn17file0L2-L2

No new evidence found materially contradicts those conclusions.

One R1 detail has evolved enough to note without reopening the broader conclusion: current Cursor Hook documentation now lists substantial project-hook support in Cloud Agents, although some lifecycle/MCP/IDE hooks remain unavailable there. The architectural conclusion—Hooks are deterministic control rather than knowledge storage—still stands. citeturn9search2

### What the reference implementations demonstrate

Because the durable R3 report was not accessible, these are direct observations from the R3 reference corpus rather than claims about R3's unpublished conclusions.

**Microsoft `skills-for-fabric` is the closest domain analogue.** It is emphatically compositional. Microsoft distributes Fabric and Power BI capabilities as skill/plugin bundles, includes agents and MCP integration, supports cross-host installation, and separates live MCP capability from skill guidance. fileciteturn19file0L2-L6 This argues strongly against modelling Wayfinder as one giant Power BI agent.

The especially important implication is:

> **Microsoft Skills should be treated as upstream capabilities the Architect can consume, not as evidence that Wayfinder must reproduce Microsoft's platform expertise.**

That aligns with the project's stated strategy of **delegate first, augment second, replace/fork only for genuine gaps**.

**`mattpocock/skills` demonstrates the skill-library-first pattern.** Its design explicitly favours small, adaptable, composable skills, distinguishes user-invoked orchestration skills from model-invoked reusable disciplines, and offers both managed plugin installation and editable per-project skill installation. fileciteturn21file0L2-L2

That design shows two important distinctions:

```text
capability architecture  !=  distribution strategy
managed subscription     !=  editable local ownership
```

It also demonstrates that orchestration itself can be encoded as a skill while supporting other skills or agents, rather than requiring a bespoke harness. fileciteturn21file0L2-L2

**`addyosmani/agent-skills` demonstrates a richer workflow façade over a skill library.** Named lifecycle commands lead into specialised skills, skills can auto-activate by relevance, cross-agent installation is supported, and its Cursor guidance explicitly advises keeping workflow skills in the skill system while using short Cursor Rules for policy rather than pasting full skills into rules. fileciteturn22file0L2-L2

That strongly validates the R1 pattern:

```text
thin persistent policy
        ↓
progressively selected capabilities
        ↓
deeper references / executable helpers
```

**GitHub Spec Kit demonstrates a true bootstrap/process layer.** It installs and adapts workflow assets for a chosen host agent, creates durable project artifacts, and uses agent skills as the interactive runtime entry points. fileciteturn23file0L2-L6 Its source also contains explicit integration/adaptation machinery for installing project assets into different agent conventions. fileciteturn24file0L2-L12 fileciteturn24file8L176-L187

Spec Kit is therefore useful evidence for what **a bootstrap/harness-like project framework looks like without itself being the LLM agent runtime**.

**Cursor's official plugin ecosystem confirms the separation between function and package.** The production repository contains a plugin literally named `orchestrate`, yet that plugin is implemented around a Skill, scripts and assets; the plugin is its packaging boundary, while orchestration is its behaviour. fileciteturn25file0L2-L2 fileciteturn26file0L2-L10 fileciteturn27file0L2-L6

Across the inspected reference implementations, the recurrent pattern is therefore **composition**, not one monolithic abstraction.

## Mapping the Wayfinder ecosystem

The project context maps cleanly once the system is divided into authority, reasoning, capability, execution and distribution planes.

```text
                         HOST RUNTIME / HARNESS
                    ┌──────────────────────────┐
                    │      Cursor Agent        │
                    │ model • loop • tools •   │
                    │ context • execution      │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ORCHESTRATION / ARCHITECT
              ┌──────────────────────────────────┐
              │ interpret → route → sequence →   │
              │ delegate → reconcile → validate  │
              └──────────────┬───────────────────┘
                             │
       ┌─────────────────────┼────────────────────────┐
       │                     │                        │
       ▼                     ▼                        ▼
 DOMAIN CAPABILITIES   ENGINEERING CAPABILITIES   UPSTREAM CAPABILITIES
 ┌───────────────┐     ┌──────────────────────┐   ┌────────────────────┐
 │ Domain packs  │     │ Skills              │   │ Microsoft Fabric / │
 │ knowledge     │     │ specialist subagents│   │ Power BI Skills    │
 │ terminology   │     │ commands/workflows  │   └────────────────────┘
 │ decision logic│     └──────────┬───────────┘
 └───────┬───────┘                │
         │                        │
         ▼                        ▼
 AUTHORITY / KNOWLEDGE       EXECUTION / TOOLS
 ┌──────────────────┐        ┌──────────────────────┐
 │ Domain references│        │ MCP                  │
 │ Standards repos  │        │ local scripts        │
 │ architecture docs│        │ validators           │
 └──────────────────┘        │ implementation libs  │
                             └──────────────────────┘

 CROSS-CUTTING CONTROL                  DISTRIBUTION
 ┌────────────────────────┐            ┌──────────────────────┐
 │ Rules / AGENTS.md      │            │ Plugin / bundle      │
 │ Hooks / quality gates  │            │ bootstrap / installer│
 └────────────────────────┘            └──────────────────────┘
```

This diagram is an **architectural classification**, not a physical repository topology recommendation.

### Architect

The **Architect should conceptually be an orchestrator**, with an agent-like user-facing identity.

Its responsibilities are:

```text
understand intent
→ establish domain context
→ determine required analytical stages
→ select standards and capabilities
→ delegate platform-specialist work
→ maintain coherence across outputs
→ trigger validation
→ reconcile results into the analytical product
```

Those are orchestration responsibilities, not reasons to embed DAX, M, semantic modelling, Fabric architecture and UX standards directly into a giant Architect prompt.

The best initial implementation hypothesis is therefore a **thin orchestration capability operating through Cursor's main Agent**, potentially expressed as one or several orchestration Skills and supported by specialist Subagents where context isolation genuinely helps. Cursor can already delegate to subagents automatically and gives each one a clean context window. citeturn7search1

The Architect may consequently be described informally as “the Wayfinder agent”, but architecturally that statement should be qualified:

> **It is an agent role/persona hosted by Cursor, not evidence that Wayfinder owns an independent agent runtime.**

### Domain packs

Domain Packs are neither general Plugins nor just Rules.

They contain an **authority component** and potentially **capability components**:

```text
Performance & Reward domain pack
    canonical domain knowledge
    terminology / ontology
    metric semantics
    decision questions
    domain-specific patterns
    domain-specific validation
    optional domain skills
```

A pack should therefore be classified as a **modular domain knowledge/capability package**.

The separation is important because Performance & Reward must be removable/additive relative to future Health & Safety or other domains. Making its business meaning part of the core Architect prompt would create the wrong dependency direction.

Conceptually:

```text
Architect core
     ↓ selects
Domain interface
     ↓ resolves to
Performance & Reward pack
or Health & Safety pack
or another domain
```

That keeps **orchestration stable while domain meaning varies**.

### Engineering standards

Engineering standards should remain a **canonical standards authority** independent of the Architect.

This follows both R1's context findings and issue #5's governance question. Issue #5 already distinguishes Semantic Model standards, DAX engineering and Power Query/M engineering, and explicitly says the implementation library must not become their standards authority. fileciteturn14file0L3-L6

The runtime pattern should therefore be:

```text
thin rule / skill says:
    "This task requires Semantic Model Standards."

                ↓ retrieves

canonical standard says:
    full normative policy

                ↓ skill applies

capability performs:
    modelling / review / remediation

                ↓ validator tests

conformance result
```

This makes the same standard usable by Cursor, another coding agent, a validator, documentation tooling and humans without maintaining multiple “agent versions” of the policy.

### Reusable implementation library

The reusable DAX/M/Python/Deneb library is an **implementation asset library**, not an instruction system or standards authority.

Its artifacts may be:

- referenced from Skills;
- invoked by scripts;
- queried/retrieved as examples;
- exposed through a tool;
- installed into a project;
- validated against engineering standards.

But the semantic boundary remains:

```text
standard
    "what must / should be true"

skill
    "how the agent performs this kind of work"

implementation library
    "reusable code/patterns that can actually be used"

tool/MCP
    "callable access to execution or live systems"
```

R1 had already recommended normal source/scripts/libraries as the canonical home for reusable implementation rather than encoding production code inside Rules or Commands. fileciteturn17file0L2-L2

### Microsoft Fabric and Power BI Skills

Microsoft's Skills are best classified as an **upstream platform capability library**, potentially delivered through plugin/skill mechanisms and supplemented with MCP. Microsoft itself distinguishes skill guidance from MCP's live API/system access. fileciteturn19file0L2-L6

Wayfinder therefore should not conceptually claim ownership of a capability merely because its orchestrator invokes it.

For example:

```text
Architect decides:
    "We now need Power BI semantic-model authoring."

             ↓ delegate-first

Microsoft capability
    performs supported platform-specific authoring

             ↓

Wayfinder augmentation
    adds company/domain engineering requirements

             ↓

Wayfinder validation
    tests result against canonical standards
```

This is an important architectural inversion:

> Wayfinder's value is not “knowing every Fabric command better than Microsoft”. Its differentiated value is **turning business ambiguity into a governed analytical product by composing platform capability, domain meaning and engineering authority**.

### Project repositories

Project repos are the **working/product boundary**, not the home for every upstream standard.

They should contain the PBIP/Fabric/project implementation and the minimum local configuration/instructions necessary to make the architecture work for that project.

A project may consume:

```text
Architect/orchestration
Domain pack
Engineering standards
Microsoft platform skills
Implementation library
Tools/MCP
```

without becoming canonical for any of them.

That distinction is critical for avoiding copied standards that silently diverge.

## Candidate architecture patterns

The evidence supports several genuine alternatives, but they are not equally good fits.

| Candidate | Description | Strengths | Structural problems | R2 assessment |
|---|---|---|---|---|
| **Monolithic Architect agent** | One custom agent prompt owns orchestration, domain knowledge and engineering expertise | Simple mental model; one visible persona | Context growth, duplicated authority, coupling of domains/standards/runtime, poor composability | **Poor fit** |
| **Independent Wayfinder agent harness** | Build own model loop/runtime/tools/state/orchestration | Maximum runtime control, host independence | Rebuilds capability already supplied by Cursor; large engineering/ops burden; prematurely binds architecture to runtime decisions | **Not justified by current evidence** |
| **Skill library only** | Everything decomposed into independently selected skills | Modular, portable, context-efficient, easy reuse | Weak system-level coordination; users/agent must reconstruct end-to-end analytical process | **Necessary component, insufficient whole** |
| **Plugin-first architecture** | Treat “Wayfinder plugin” as the main product abstraction | Cohesive installation/update experience | Confuses packaging with semantics; risks Cursor lock-in and hides authority boundaries | **Good packaging option, bad system definition** |
| **Bootstrap/process framework** | Spec-Kit-style installer materialises workflows/artifacts into each target project | Multi-host adaptation, persistent process artifacts, deterministic setup | Adds installer/versioning complexity; still requires host runtime/capabilities | **Potential supporting layer** |
| **Layered hosted orchestration ecosystem** | Cursor provides harness; Architect coordinates modular skills/subagents; standards/domain/reuse remain independent authorities; plugin/bootstrap handles distribution | Strong separation of concerns, progressive context, delegate-first platform use, portable core assets, replaceable domains | More interfaces and version contracts to govern | **Best-supported conceptual classification** |

### Why not a monolithic agent

A monolithic agent initially appears attractive because the user wants a single experience: “build me the right analytical product”.

But **single experience does not require single component**.

Cursor's own agent architecture already supports capability discovery and subagent delegation; Agent Skills exist specifically to defer specialist instructions/resources until they become relevant. citeturn7search1turn8search2 R1 also found that permanently loading large standards has materially worse context economics than thin routing to on-demand content. fileciteturn17file0L2-L2

The desired UX can therefore remain:

```text
User
  ↓
"Help me answer whether our new-hire salaries are creating compression."
  ↓
Architect
```

while the internal architecture becomes:

```text
Architect
  ├─ domain interpretation capability
  ├─ relevant P&R knowledge
  ├─ source/data architecture capability
  ├─ Microsoft Fabric capability
  ├─ semantic modelling skill
  ├─ semantic model standard
  ├─ DAX skill + DAX standard
  ├─ report-design capability
  └─ validation capability
```

That is **one product experience over many architectural components**.

### Why not build our own harness now

Building a Wayfinder harness becomes rational when requirements demand control the existing host cannot provide—for example, if the project must directly own cross-host model execution, durable run state, custom retry/approval semantics, sandbox scheduling or agent-loop behaviour.

The current evidence instead shows that Cursor already provides the host agent, context management, subagents, tools, MCP, hooks and plugin surfaces. citeturn7search0turn7search1turn9search2turn9search3

Creating another harness now would therefore mix two separate architecture decisions:

```text
decision A
What analytical-product reasoning system do we need?

decision B
Do we need to build our own model/runtime platform?
```

Nothing in R2 demonstrates that B is required to solve A.

### Why skills alone are not enough

The opposite extreme—“Wayfinder is just a skill collection”—also loses something important.

The project has an explicit system-level flow:

```text
ambiguous business question
→ domain interpretation
→ source/data architecture
→ transformation
→ analytical modelling
→ semantic model
→ DAX
→ report/UX
→ validation
→ finished analytical product
```

Individual skills can implement the stages. But the system still requires a capability responsible for **maintaining intent and coherence across them**, deciding which stages apply, handling feedback loops and resolving conflicts between domain needs and engineering constraints.

That is orchestration.

Matt Pocock's reference architecture illustrates this distinction well: it has reusable model-invoked discipline skills but also user-facing orchestration skills that compose those capabilities. fileciteturn21file0L2-L2

### Why plugin is not the answer either

A plugin could be the best Cursor installation vehicle and still tell us almost nothing about the underlying architecture.

Cursor's Plugin system can package Rules, Skills, Agents, Commands, MCP and Hooks together. citeturn7search0 The official `orchestrate` plugin demonstrates this directly: its architectural job is orchestration, its principal agent-facing implementation is a skill, scripts perform deterministic work, Cursor cloud agents execute delegated tasks, and the plugin packages the capability. fileciteturn27file0L2-L6

Therefore the statement:

> “Wayfinder should be a Cursor Plugin”

can eventually be a valid **distribution decision**, but it is not a sufficient architecture decision.

## Recommended R2 classification

The evidence supports a **compositional, layered classification** rather than choosing one label.

### The system is an orchestration ecosystem

The most accurate durable description is:

> **Wayfinder is an AI-assisted analytical-product architecture and orchestration ecosystem that composes domain authority, engineering standards, platform capabilities, reusable implementation assets and validation around a host coding-agent runtime.**

This says what the system **does and owns** without prematurely fixing how every component must be packaged.

A shorter working label would be:

> **Analytical-product orchestration layer**

“Agent harness” should **not** be the primary name at this stage, because the initial system relies on the Cursor harness rather than owning the whole execution loop. citeturn11search0

“Skill library” is too narrow because Wayfinder also needs cross-capability orchestration, standards authority, domain authority, tools and validation.

“Plugin” is too low-level because it answers distribution rather than system identity.

“Agent” captures the user-facing interaction model but overstates the architectural unity of the underlying knowledge/capability system.

### The Architect is an orchestrator hosted by an agent

The **Power BI/Fabric Architect** should conceptually be treated as the **manager/orchestrator role**.

Its implementation can initially exploit the **existing Cursor Agent** as the reasoning runtime rather than instantiate a completely independent agent.

Likely decomposition:

```text
Cursor Agent
    ↓
Architect orchestration skill/instructions
    ├─ capability routing
    ├─ domain selection
    ├─ standards selection
    ├─ workflow sequencing
    ├─ delegation
    ├─ state/artifact reconciliation
    └─ validation routing
```

Subagents should be added **by workload property, not by organisational chart**:

```text
Use Skill when:
    reusable capability
    task fits current context
    progressive knowledge/resources sufficient

Use Subagent when:
    independent context is valuable
    investigation is large
    parallelism is useful
    independent verification matters
    specialist model/tools genuinely differ
```

That boundary follows Cursor's own current distinction. citeturn7search1

### Individual capabilities should use the narrowest fitting primitive

The core implementation rule should be:

> **Choose primitives by responsibility, not by branding.**

| Responsibility | Preferred conceptual primitive |
|---|---|
| Overall analytical-product coordination | Orchestration layer |
| User-facing manager identity | Host Agent + Architect role |
| Repeatable specialist reasoning/procedure | Skill |
| Large independent specialist investigation | Subagent |
| Parallel independent review | Subagent |
| Stable behavioural invariant | Rule / concise project instruction |
| Explicit workflow entry point | Skill or Command |
| Hard event/control gate | Hook / validator |
| Canonical engineering policy | Standards repository |
| Canonical business/domain meaning | Domain knowledge pack |
| Reusable production implementation | Implementation library |
| Live external operation/data | Tool/MCP |
| Local deterministic helper | Script/tool |
| Cursor installation bundle | Plugin |
| Cross-project/host materialisation | Installer/bootstrap |
| Project implementation | Project repository |

### Packaging should remain a separate decision axis

The same conceptual architecture could be shipped several ways:

```text
Architecture
    Architect orchestration
    Skills
    Standards interfaces
    Domain interfaces
    Tool contracts
    Validators

Packaging option A
    Cursor Plugin

Packaging option B
    Agent Plugin + portable Skills/MCP

Packaging option C
    installer/bootstrap targeting several agents

Packaging option D
    combination of managed bundle + external canonical repos
```

Cursor currently supports both Cursor-specific Plugins and a broader Agent Plugin model, while Agent Skills and MCP themselves are designed for reuse across hosts. citeturn7search0turn8search2turn6search2

R2 therefore should **deliberately avoid collapsing portable architecture into Cursor package layout**. That is a later topology/distribution decision.

### The likely layered system

The most useful working model for later tickets is:

```text
LAYER: Host / harness
    Cursor initially
    potentially other compatible hosts later

LAYER: Architect / orchestration
    analytical-product reasoning
    routing
    sequencing
    delegation
    reconciliation

LAYER: Capability
    Wayfinder skills
    Microsoft Fabric / Power BI skills
    selected subagents
    workflows

LAYER: Authority
    domain packs
    engineering standards
    architecture knowledge

LAYER: Implementation
    DAX / M / Python / Deneb libraries
    templates
    validators
    schemas

LAYER: Tooling
    MCP
    APIs
    scripts
    project/file tools

LAYER: Control
    rules
    hooks
    deterministic conformance checks

LAYER: Distribution
    plugin / agent plugin
    versioned bundles

LAYER: Bootstrap
    optional installer / project adapter

LAYER: Product workspace
    PBIP / Fabric / analytical-project repository
```

This model preserves the project's intended authority boundaries while allowing Cursor-native capabilities to do the jobs for which they were designed.

## Risks, unresolved questions and durable-research status

### Architectural risks

**Misnaming the system as a harness.** This risks gradually rebuilding model/runtime infrastructure simply because the project adopted the term “harness”. The operational test should be runtime ownership: until Wayfinder actually owns the model/agent execution loop rather than configuring Cursor's, classify it as an orchestration layer **on** a harness. citeturn11search0turn8search9

**Misnaming the system as a plugin.** This risks letting Cursor's packaging layout dictate conceptual boundaries. Cursor itself treats Plugins as containers for multiple primitive families. citeturn7search0

**Making the Architect a knowledge monolith.** Embedding domain knowledge and engineering standards directly into the Architect would undermine replaceable domains, create duplicated authority and increase prompt/context cost. R1's evidence directly argues for separating canonical knowledge from activation/routing. fileciteturn15file0L2-L2

**Treating every expertise area as a subagent.** This would add separate-context startup/token overhead to capabilities that could be handled by lightweight skills. Cursor explicitly documents this trade-off. citeturn7search1

**Treating every procedure as a Skill.** Some controls should not depend on an LLM remembering to invoke instructions. Cursor Hooks exist specifically to observe, block or modify agent-loop behaviour at defined events, including tool and subagent use. citeturn9search2

**Duplicating Microsoft capabilities.** Microsoft's current Fabric repository already combines platform skills, agents, MCP integration and Power BI-specific authoring bundles. fileciteturn19file0L2-L6 Wayfinder should preserve the planned delegate-first boundary so that platform evolution does not become an internal maintenance burden without a demonstrated gap.

**Confusing standards with reusable implementation.** Issue #5 has already identified this as a governance problem and explicitly prohibits making the DAX/M implementation library the standards authority. fileciteturn14file0L3-L6

**Installer drift.** If a future bootstrap layer generates or copies standards and skills into project repos, those copies can become shadow authorities. A bootstrap system should preferably materialise versioned consumers/adapters rather than create independently editable copies of canonical policy. GitHub Spec Kit and Microsoft APM show why installation/versioning is its own architectural concern. fileciteturn23file0L2-L6 fileciteturn19file0L2-L6

### Questions that should deliberately remain open after R2

R2 should not prematurely settle:

**Physical repository topology.** Issue #5 has not yet selected the canonical standards home. fileciteturn14file0L3-L6 This R2 classification says what the standards authority *is*, not which repository must contain it.

**Exact packaging topology.** One plugin versus several plugins, Agent Plugin versus Cursor Plugin, managed installation versus bootstrap, and project versus user scope are distribution decisions rather than answers to the classification question.

**Cross-repository consumption mechanism.** Whether canonical standards/domain packs are installed, vendored, linked, fetched through tools, retrieved through MCP, packaged into releases or otherwise consumed needs separate evaluation.

**How much Architect state should be durable.** A long analytical-product journey may need decision/state artifacts that outlive a single agent context. Spec Kit demonstrates one pattern—persistent repository artifacts—but R2 does not establish that its exact method is right for Wayfinder. fileciteturn23file0L2-L6

**Where model-driven orchestration ends and deterministic workflow begins.** Some transitions may remain agent-selected; critical conformance gates may deserve executable state machines, scripts or Hooks. OpenAI's orchestration model explicitly allows both model-driven and programmatic coordination, while Cursor provides hooks around its loop. citeturn8search0turn9search2

**Which specialist roles deserve subagents.** The answer should follow empirical context isolation, quality and parallelism needs, not simply map every capability group to an agent.

**How Microsoft Skills are versioned and augmented.** The intended principle—delegate first, augment second—is architecturally sound, but the exact extension, version-pinning and fallback contracts remain to be designed.

### Evidence gap requiring repository reconciliation

The largest research-process risk is the missing R3 durable artifact.

Issue #11 defines a mandatory benchmark corpus and says its durable output must be `research/cursor-architecture/03-reference-repo-benchmark.md`. fileciteturn7file0L3-L6 That file was not discoverable in the accessible repository state during this research, while issue #11 remained open. This R2 report therefore used direct evidence from the mandatory repositories rather than claiming R3 conclusions that could not be inspected.

That should be treated as an explicit **research dependency gap**:

```text
R1                  read directly from its research branch
R3                  durable artifact not found
R3 reference repos  sampled directly for the R2 questions
R2 conclusions       supported, but must be reconciled with R3 when available
```

No direct evidence gathered from those reference repositories contradicted R1. Instead, Microsoft Fabric Skills, the two independent skill collections, Spec Kit and Cursor's own plugin ecosystem all reinforce R1's central finding that **runtime, orchestration, capability, authority and distribution are separable architectural concerns**. fileciteturn19file0L2-L6 fileciteturn21file0L2-L2 fileciteturn22file0L2-L2 fileciteturn23file0L2-L6 fileciteturn26file0L2-L10

### R2 conclusion for downstream research

The durable architectural answer that R5, R6 and R8 should consume is:

> **Wayfinder should not be classified as exclusively a harness, agent, skill library or plugin. These terms belong to different architectural dimensions.**
>
> **The system itself is best classified as a layered analytical-product orchestration ecosystem.**
>
> **The Architect is its manager/orchestrator role, initially hosted by Cursor's existing Agent/harness rather than replacing it.**
>
> **Specialist capabilities should primarily be modular Skills, with Subagents reserved for work that benefits from separate context, specialist execution or parallel independence.**
>
> **Domain Packs and Engineering Standards remain independent authorities consumed by the Architect and capabilities rather than embedded wholesale into them.**
>
> **Reusable implementation remains an implementation library. MCP/tools provide live execution boundaries; Rules provide concise persistent instructions; Hooks/validators provide deterministic controls.**
>
> **A Cursor Plugin or portable Agent Plugin can package and distribute these components, while a separate bootstrap/installer may eventually materialise them across projects and agent hosts. Packaging is not the architecture itself.**
>
> **Therefore: we are building several of these things together—but in distinct layers, with distinct ownership.**

That conclusion answers issue #12 without deciding the later physical repository topology or committing Wayfinder to a bespoke runtime before evidence shows one is needed. It is also consistent with issue #12's stated non-goal of avoiding premature installation/topology decisions. fileciteturn13file0L3-L6

**Repository persistence state:** this research is structured for `research/cursor-architecture/02-harness-agent-skill-plugin.md`, but the GitHub connector available in this session exposed repository read/search operations and no create/update-file or commit operation. Consequently, the report could not be made durable in GitHub from this session. Until it is committed there—and reconciled with the missing R3 artifact—the repository does **not yet contain this R2 result as its long-term source of truth**.