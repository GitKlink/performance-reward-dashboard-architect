# R1 — Cursor Native Architecture Primitives

**Research ticket:** #10 — Research R1: Cursor native architecture primitives  
**Evidence snapshot:** 2026-09-16  
**Status:** Evidence-gathering research only. This report does **not** decide the final Power BI/Fabric Architect architecture.

This report uses the following labels:

- **FACT** — behaviour explicitly documented by Cursor or the relevant open specification.
- **OBSERVATION** — implementation evidence visible in official/reference repositories.
- **INFERENCE** — an architectural implication derived from the evidence; not documented product behaviour.

---

## 1. Research question and scope

The research question is: **what are Cursor's current native architecture primitives, how do they load and interact, and what constraints do they impose on architecture choices?**

The primitives covered are:

1. `AGENTS.md` / project instructions
2. Rules
3. Skills
4. Commands
5. Agents / subagents
6. Hooks
7. MCP servers
8. Plugins
9. Ordinary Markdown documentation and reference files

For each primitive this report examines definition, location, discovery, loading, invocation, scope, interactions, conflicts, intended use, anti-patterns, portability, context economics, suitability for engineering standards, suitability for orchestration, and suitability for executable implementation assets.

The source order is:

1. current official Cursor documentation;
2. official Cursor GitHub repositories;
3. official changelog/announcement material;
4. implementation evidence from current repositories;
5. community material only where official material is incomplete.

The principal official sources used are Cursor's current documentation for Rules, Skills, Subagents, Hooks, MCP, Plugins, prompting/context, plugin reference and customisation, plus Cursor's official `plugin-template` and `plugins` repositories. See **§20 Sources**.

---

## 2. Executive findings

1. **FACT — Cursor separates instruction, capability, delegated cognition, deterministic control, external tools, and distribution.** Rules and `AGENTS.md` are instruction primitives; Skills are capability packages; Subagents provide separate delegated contexts; Hooks provide lifecycle/event control; MCP exposes external capabilities; Plugins package/distribute other primitives. Sources: [Rules](https://cursor.com/docs/rules), [Skills](https://cursor.com/docs/skills), [Subagents](https://cursor.com/docs/subagents), [Hooks](https://cursor.com/docs/hooks), [MCP](https://cursor.com/docs/mcp), [Plugins](https://cursor.com/docs/plugins).

2. **FACT — context economics vary materially by primitive.** Applied Rules and applicable project instructions become prompt-bearing context. Skill descriptions are available for discovery while full Skill content is loaded only when activated, with supporting files progressively retrieved. Subagents use separate context windows. MCP exposes tool/catalogue information and adds tool results only when invoked. Cursor explicitly lists Rules, Skill descriptions, MCP instructions/catalogue, Subagent documentation, conversation history and tool results as context consumers. Source: [Prompting agents](https://cursor.com/docs/agent/prompting).

3. **INFERENCE — canonical knowledge storage and activation/routing should be treated as separate concerns.** A large engineering standard stored as an always-applied Rule has very different context cost from the same standard stored as ordinary documentation and retrieved through a Skill or file lookup. The architecture decision therefore needs to distinguish **where canonical knowledge lives** from **how Cursor is told when to use it**.

4. **FACT — Rules and Skills overlap but are not equivalent.** Cursor supports relevance-selected Rules and relevance-selected Skills, but Skills are explicitly designed for progressive capability packaging with supporting scripts/references/assets. Cursor's migration tooling can convert some intelligently-applied Rules and slash Commands into Skills, but current docs still treat Rules, Skills and Commands as separate primitives. Sources: [Rules](https://cursor.com/docs/rules), [Skills](https://cursor.com/docs/skills).

5. **FACT — Plugins are primarily a distribution/composition boundary, not an agent runtime.** A Cursor Plugin can contain Rules, Skills, Agents, Commands, Hooks and MCP configuration. Installing a Plugin does not imply that all contained content is loaded into model context; each contained primitive keeps its own activation semantics. Source: [Plugins](https://cursor.com/docs/plugins).

6. **OBSERVATION — Cursor's official plugin template confirms the composition model.** The advanced starter includes `agents/`, `commands/`, `hooks/`, `rules/`, `skills/`, `scripts/` and `mcp.json`. Source: [cursor/plugin-template](https://github.com/cursor/plugin-template).

7. **OBSERVATION — production plugins need not use every primitive.** Cursor's official `cursor/plugins` repository includes narrowly composed plugins, including orchestration capabilities packaged primarily as Skills with supporting prompts, references, schemas and scripts. Source: [cursor/plugins](https://github.com/cursor/plugins).

8. **FACT — Subagents are a native context-management mechanism.** Cursor explicitly positions them for separate context, parallel work, specialist tasks and delegated multi-step work. Source: [Subagents](https://cursor.com/docs/subagents).

9. **FACT — Hooks are the main native deterministic control surface around the agent loop.** They respond to lifecycle/tool events using structured data and can allow, ask, deny, transform or inject behaviour depending on event type. Source: [Hooks](https://cursor.com/docs/hooks).

10. **FACT — MCP is the native boundary for protocolised external capability.** MCP servers expose external tools/data/resources through the Model Context Protocol and can be selected by Agent when relevant. Source: [MCP](https://cursor.com/docs/mcp).

11. **FACT — `AGENTS.md` is a plain-Markdown project-instruction mechanism, not merely another filename for a Rule.** Cursor documents hierarchical/nested project instructions with more-specific nested guidance taking precedence. Source: [Rules — AGENTS.md section](https://cursor.com/docs/rules).

12. **INFERENCE — large standards should not automatically become Rules or Skills.** Cursor recommends focused Rules and supports references from Rules/Skills to canonical files. Large standards may remain ordinary version-controlled documentation while thin activation assets direct Agent to them.

---

## 3. Cursor architecture model

The following model is an **INFERENCE** from the documented roles of the primitives:

```text
                     CURSOR ENVIRONMENT

      Organisation / user / project configuration
      ┌─────────────────────────────────────────┐
      │ Team Rules                              │
      │ User Rules                              │
      │ Project Rules                           │
      │ AGENTS.md                               │
      │ Skills / Commands                       │
      │ Subagent definitions                    │
      │ Hooks                                   │
      │ MCP configuration                       │
      └────────────────────┬────────────────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │ Cursor Agent     │
                  │ host/runtime     │
                  └────────┬─────────┘
                           │
        ┌──────────────────┼───────────────────┐
        │                  │                   │
        ▼                  ▼                   ▼
 Instruction /       Delegated work       Runtime / external
 capability          separate context     capability
 discovery
 ┌──────────────┐    ┌───────────────┐    ┌───────────────┐
 │ Rules        │    │ Subagents     │    │ MCP servers   │
 │ AGENTS.md    │    └───────────────┘    │ Hook scripts  │
 │ Skill meta   │                         │ Local scripts │
 │ Commands     │                         └───────────────┘
 └──────┬───────┘
        │
        ▼
 On-demand knowledge / implementation
 ┌──────────────────────────┐
 │ Skill references         │
 │ Ordinary docs            │
 │ Templates / schemas      │
 │ Source / examples        │
 └──────────────────────────┘

             DISTRIBUTION / COMPOSITION
       ┌─────────────────────────────────┐
       │ Cursor Plugin / Agent Plugin    │
       │ packages selected assets above │
       └─────────────────────────────────┘
```

Two distinctions matter:

- **FACT:** the main Cursor Agent is the host runtime. Custom Subagent definitions are delegated specialist roles operating within Cursor's agent system rather than independent application runtimes. Source: [Subagents](https://cursor.com/docs/subagents).
- **FACT:** Plugins sit across the other categories as packaging/distribution units. A Plugin can contribute multiple primitive types. Source: [Plugins](https://cursor.com/docs/plugins).

---

## 4. AGENTS.md / project instructions

### What it is

**FACT:** Cursor supports `AGENTS.md` as a plain-Markdown project-instruction mechanism and presents it as a simpler alternative to structured Project Rules where Rule metadata and activation modes are unnecessary. Source: [Rules](https://cursor.com/docs/rules).

### Where it lives

**FACT:** Cursor supports a repository-root `AGENTS.md` and nested `AGENTS.md` files in subdirectories. Source: [Rules](https://cursor.com/docs/rules).

### Discovery and loading

**FACT:** Root and nested `AGENTS.md` files are discovered by filename/location. Nested instructions become relevant for files/directories beneath their location. Parent and child instructions are combined, and more-specific child instructions win when they conflict. Source: [Rules](https://cursor.com/docs/rules).

**INFERENCE:** Applicable `AGENTS.md` content is prompt-bearing context rather than passive documentation. It therefore creates a context cost wherever its scope applies.

### Invocation

- **Model automatic:** yes, through project/directory applicability.
- **User explicit:** not as a slash-command style primitive; the user can influence relevance by working in the relevant directory or explicitly referring to the file.
- **Activation metadata:** no Rule-style frontmatter modes such as always/manual/intelligent/globs.

Source: [Rules](https://cursor.com/docs/rules).

### Scope

- repository root;
- nested subtree scope through directory placement.

### Interaction and precedence

**FACT:** nested `AGENTS.md` files override less-specific parent guidance on conflict. Source: [Rules](https://cursor.com/docs/rules).

**UNRESOLVED:** current Cursor documentation does not publish a universal precedence rule for a direct conflict between `AGENTS.md` and Project/Team/User Rules.

### Intended use

**INFERENCE:** best fit is concise, durable repository or subtree invariants where automatic application is desired without Rule metadata.

### What should not go in it

**INFERENCE:** avoid very large standards corpora, occasional specialist procedures, executable code, and complicated orchestration logic. Those would create persistent context cost or conflate documentation with execution.

### Portability

**FACT:** `AGENTS.md` is broader than Cursor and is promoted as an open convention for coding-agent instructions. Source: [agentsmd/agents.md](https://github.com/agentsmd/agents.md).

### Suitability

- Large engineering standards: **low–medium**; suitable as a concise routing/invariant layer, not ideal as the full corpus.
- Orchestration logic: **low**.
- Reusable executable implementation assets: **no**.

---

## 5. Rules

### What they are

**FACT:** Rules are instruction assets that influence Cursor Agent behaviour. Cursor documents Project, User and Team Rules, with Project Rules stored in the repository and User/Team Rules managed at broader scopes. Source: [Rules](https://cursor.com/docs/rules).

### Where they live

**FACT:** Project Rules live under:

```text
.cursor/rules/
```

and current Project Rule files use `.mdc`. Cursor states that a plain `.md` placed there is not treated as a Project Rule. Source: [Rules](https://cursor.com/docs/rules).

### Discovery and loading modes

Cursor documents four Project Rule activation modes. Source: [Rules](https://cursor.com/docs/rules).

| Mode | Behaviour |
|---|---|
| Always Apply | Full Rule applies every Agent chat in scope |
| Apply Intelligently | Agent uses Rule metadata/description to decide relevance, then loads the Rule |
| Apply to Specific Files | Rule applies when matching files are relevant/in context |
| Apply Manually | Rule applies only when explicitly referenced, such as `@rule` |

### Context economics

**FACT:** applied Rules are included in model context. Therefore an Always Rule creates persistent context cost. Intelligent/manual/file-scoped Rules defer the full body until activation. Source: [Rules](https://cursor.com/docs/rules).

**UNRESOLVED:** Cursor does not document exact inactive metadata token accounting for every Rule mode.

### Invocation

- Model automatic: yes for Always, Intelligent and file-scoped Rules.
- User explicit: yes for Manual Rules via explicit reference.

### Scope and precedence

**FACT:** Cursor documents Rule scope precedence as:

```text
Team Rules → Project Rules → User Rules
```

When applicable guidance conflicts, earlier/higher-precedence sources win. Source: [Rules](https://cursor.com/docs/rules).

### Interaction with files

**FACT:** Cursor recommends referencing canonical repository files from Rules rather than copying large bodies of guidance into the Rule. Source: [Rules](https://cursor.com/docs/rules).

### Intended use

Persistent or conditionally applied behavioural/project guidance, especially invariants and constraints that should reliably influence Agent.

### What should not go in Rules

**FACT:** Cursor recommends keeping Rules focused/actionable and generally under roughly 500 lines, splitting large Rules and avoiding wholesale duplication of large guides, every command, rare edge cases or material already present in the repository. Source: [Rules](https://cursor.com/docs/rules).

### Portability

Cursor Project Rules (`.cursor/rules/*.mdc`) are **Cursor-specific**.

### Suitability

- Large engineering standards: **low if embedded; medium as thin routers to canonical docs**.
- Orchestration logic: **medium for behavioural/procedural guidance; not deterministic**.
- Reusable executable implementation assets: **low**; Rules may direct use of scripts/tools, but should not be the implementation library.

---

## 6. Skills

### What they are

**FACT:** Cursor Agent Skills implement the Agent Skills convention: reusable capability packages containing instructions plus optional scripts, references, assets and other support material. Source: [Cursor Skills](https://cursor.com/docs/skills), [Agent Skills specification](https://agentskills.io/).

### Where they live

Current Cursor documentation supports project and user Skill roots including:

```text
.agents/skills/
.cursor/skills/

~/.agents/skills/
~/.cursor/skills/
```

Cursor also recognises compatibility locations associated with adjacent agent ecosystems, including Claude/Codex locations. Source: [Cursor Skills](https://cursor.com/docs/skills).

### Discovery

**FACT:** each Skill is a directory containing `SKILL.md`. Cursor discovers Skills recursively and uses Skill metadata — especially `name` and `description` — for relevance. Current Skill metadata can also include path scoping. Source: [Cursor Skills](https://cursor.com/docs/skills).

### Progressive loading

**FACT:** Skills are designed for progressive disclosure. The model can see lightweight Skill metadata for discovery; when a Skill is activated, Cursor loads `SKILL.md`; supporting references/scripts/assets can then be accessed only when needed. Sources: [Cursor Skills](https://cursor.com/docs/skills), [Agent Skills specification](https://agentskills.io/).

```text
normal turn
  ↓
Skill name + description available for discovery
  ↓ relevance match / explicit selection
SKILL.md loaded
  ↓ only if needed
references / scripts / assets / templates
```

### Invocation

- **Model automatic:** yes, by relevance unless disabled.
- **User explicit:** yes, with `/skill-name`.
- **Explicit-only mode:** a Skill can disable model invocation and require explicit use.
- **Session persistence:** Cursor Custom Modes can keep selected capabilities active for a session.

Source: [Cursor Skills](https://cursor.com/docs/skills).

### Supporting files

**FACT:** Skills support supporting documentation and executable helpers, commonly structured as `references/`, `scripts/` and `assets/`. Source: [Cursor Skills](https://cursor.com/docs/skills).

**OBSERVATION:** Cursor's official plugins repository contains Skills that separate `SKILL.md` from supporting prompts/references/schemas/scripts rather than embedding everything into one Markdown file. Source: [cursor/plugins](https://github.com/cursor/plugins).

### Skills vs Rules

**FACT:** both can be model-selected, but Skills are capability packages with progressive disclosure and supporting resources, whereas Rules are instruction assets with persistent/intelligent/file/manual activation modes. Cursor's migration tooling explicitly supports moving some intelligently-applied Rules into Skills. Sources: [Rules](https://cursor.com/docs/rules), [Skills](https://cursor.com/docs/skills).

### Skills vs Commands

**FACT:** Skills can be invoked explicitly with `/...`, creating overlap with Commands, but Skills add model selection, supporting resources and portable Agent Skills semantics. Cursor migration tooling can convert slash Commands into explicit-only Skills. Source: [Cursor Skills](https://cursor.com/docs/skills).

### Skills vs Subagents

**FACT:** Cursor explicitly distinguishes them: use Skills for repeatable capabilities/instructions; use Subagents when independent context, delegated multi-step work or parallel work matters. Source: [Subagents](https://cursor.com/docs/subagents).

### Portability

**FACT:** Skills are one of the strongest portable primitives because Cursor implements the Agent Skills convention and recognises cross-tool compatibility locations. Sources: [Cursor Skills](https://cursor.com/docs/skills), [Agent Skills specification](https://agentskills.io/).

### Suitability

- Large engineering standards: **high as progressively loaded supporting references; not necessarily as the canonical Skill body**.
- Orchestration logic: **medium–high for model-mediated procedures**.
- Reusable executable implementation assets: **high as a wrapper/package around scripts/templates**.

---

## 7. Commands

### What they are

**FACT:** Cursor Commands are reusable prompts/workflows invoked through `/` in Agent chat. Source: [Customise Cursor](https://cursor.com/docs/customize-cursor).

### Where they live

**FACT:** repository Commands can live under:

```text
.cursor/commands/
```

Source: [Cursor deeplinks/reference](https://cursor.com/docs/reference/deeplinks).

**OBSERVATION:** Cursor's official plugin template also has a top-level `commands/` component for Plugin-packaged commands. Source: [cursor/plugin-template](https://github.com/cursor/plugin-template).

### Discovery and invocation

**FACT:** the primary documented interaction is explicit user invocation through `/command`. Source: [Customise Cursor](https://cursor.com/docs/customize-cursor).

**UNRESOLVED:** current primary documentation does not clearly specify a contract under which standalone Commands are autonomously relevance-selected by Agent from command metadata. This report therefore does not assume automatic model invocation.

### Current status vs Skills

**FACT:** Commands remain present in current Cursor customisation and plugin documentation. Cursor also offers migration of slash Commands to explicit-only Skills, showing overlap without proving Commands are deprecated. Sources: [Customise Cursor](https://cursor.com/docs/customize-cursor), [Cursor Skills](https://cursor.com/docs/skills), [Plugin reference](https://cursor.com/docs/reference/plugins).

### Intended use

Short, explicit, repeatable user-triggered workflows such as `/test`, `/deploy`, `/review` or other named procedures.

### What should not go in Commands

**INFERENCE:** avoid large standards corpora, large execution libraries, or behaviour that must happen deterministically without a user explicitly starting the command.

### Portability

Cursor's Command directory/interface is primarily **Cursor-specific**.

### Suitability

- Large engineering standards: **low**.
- Orchestration logic: **medium for explicit short workflows**.
- Reusable executable implementation assets: **low–medium**; a Command can direct tools/scripts but should not be the implementation itself.

---

## 8. Agents and subagents

### What they are

**FACT:** Cursor Subagents are specialised assistants that the main Cursor Agent can delegate tasks to. Each operates in its own context window. Source: [Subagents](https://cursor.com/docs/subagents).

### Discovery and invocation

**FACT:** Cursor Agent can automatically choose a Subagent based on task fit/description, and the user can explicitly request delegated work. Source: [Subagents](https://cursor.com/docs/subagents).

### Context isolation

**FACT:** Subagents operate with independent context rather than simply expanding the current parent prompt. Cursor recommends them where context isolation, specialist investigation, parallel work or independent verification is useful. Source: [Subagents](https://cursor.com/docs/subagents).

### Agent vs Subagent

**INFERENCE:** for architecture vocabulary, the main Cursor Agent is the host runtime; custom Subagent definitions are specialist delegated roles within that runtime. A Subagent definition is not equivalent to a standalone agent application/harness.

### Scope and same-name resolution

**FACT:** current Cursor documentation supports project/user custom-agent locations and compatibility with other agent ecosystems. Cursor documents project-local precedence over user definitions and native-location precedence over compatibility locations for same-name custom agents. Source: [Subagents](https://cursor.com/docs/subagents).

### Nested delegation

**FACT:** current Subagent behaviour includes child/nested delegation subject to documented restrictions. This is version-sensitive and newer than the initial Subagent model. Source: [Subagents](https://cursor.com/docs/subagents).

### Parallelism and editing risk

**FACT:** Subagents consume their own model tokens and parallel editing can conflict if multiple agents modify the same checkout. Cursor documents isolation/worktree patterns for parallel work. Source: [Subagents](https://cursor.com/docs/subagents).

### What should not go in Subagents

**INFERENCE:** do not duplicate a very large standards corpus into every Subagent prompt. That weakens the context-isolation benefit; concise role instructions plus on-demand references are more compatible with the primitive's purpose.

### Portability

**Medium.** Cursor supports compatibility paths and related conventions, but runtime semantics, tools and delegation behaviour can differ across products.

### Suitability

- Large engineering standards: **low in the Subagent prompt; potentially high when retrieved on demand**.
- Orchestration logic: **high for delegated cognitive work and parallelism**.
- Reusable executable implementation assets: **medium via tools/scripts; Subagent definitions themselves are not libraries**.

---

## 9. Hooks

### What they are

**FACT:** Hooks are scripts or handlers connected to Cursor Agent lifecycle/tool events. They receive structured event data and can observe, control, transform or block aspects of Agent execution. Source: [Hooks](https://cursor.com/docs/hooks).

### Where they live

Cursor documents project/user hook configuration, including:

```text
.cursor/hooks.json
~/.cursor/hooks.json
```

and broader managed/team/enterprise surfaces. Plugins can also contribute hooks. Sources: [Hooks](https://cursor.com/docs/hooks), [Plugins](https://cursor.com/docs/plugins).

### Discovery and invocation

**FACT:** Hooks are event-driven. They do not rely on the model deciding that a hook is semantically relevant; Cursor executes matching configured hooks at lifecycle/tool events. Source: [Hooks](https://cursor.com/docs/hooks).

### Conflict/merge behaviour

**FACT:** multiple matching hooks can execute. Permission outcomes have explicit decision precedence, including deny over ask over allow, while other fields have event-specific merge/ordering behaviour. Cursor documents source processing across enterprise/team/project/user layers. Source: [Hooks](https://cursor.com/docs/hooks).

### Context economics

**FACT:** hook scripts/configuration generally execute outside ordinary model prompt context. Hook responses may inject additional context, and some hook forms may themselves invoke models. Source: [Hooks](https://cursor.com/docs/hooks).

### Hooks vs Rules/Commands

**INFERENCE:** Rules and Commands are model-mediated instructions; Hooks are stronger where policy/validation must run at a lifecycle boundary regardless of whether the model remembers to follow prose.

### Local vs Cloud parity

**FACT:** hook support has had environment/version differences, particularly across local/Cloud/managed surfaces. Any architecture that depends on Hooks should validate the exact target Cursor release/environment rather than assume perfect parity. Source: [Hooks](https://cursor.com/docs/hooks).

### What should not go in Hooks

**INFERENCE:** long engineering guidance, domain explanations and reference documentation should not live in Hook configuration. Hooks should call reusable scripts/validators or return concise control/context information.

### Portability

Cursor Hook schemas/events are **product-specific** even if scripts themselves are portable.

### Suitability

- Large engineering standards: **no**.
- Orchestration logic: **high for deterministic lifecycle/control orchestration**.
- Reusable executable implementation assets: **high for validators/checkers/scripts, preferably modular rather than inline**.

---

## 10. MCP servers

### What they are

**FACT:** Model Context Protocol servers expose external capabilities to Agent through MCP. Cursor supports MCP tools/resources/prompts and common MCP transports. Sources: [Cursor MCP](https://cursor.com/docs/mcp), [Model Context Protocol](https://modelcontextprotocol.io/).

### Where configuration lives

Cursor documents project and user configuration including:

```text
.cursor/mcp.json
~/.cursor/mcp.json
```

Plugins and managed configuration can also contribute MCP capability. Sources: [MCP](https://cursor.com/docs/mcp), [Plugins](https://cursor.com/docs/plugins).

### Discovery and invocation

**FACT:** connected/enabled MCP servers expose their capabilities to Agent. Agent can automatically select relevant MCP tools, and users can ask for a specific server/tool. Source: [MCP](https://cursor.com/docs/mcp).

### Context economics

**FACT:** Cursor's prompting/context documentation identifies MCP catalogue/instruction information as context-bearing. Remote data/tool results enter conversation context when calls are made. Sources: [Prompting agents](https://cursor.com/docs/agent/prompting), [MCP](https://cursor.com/docs/mcp).

**INFERENCE:** MCP keeps remote execution/data behind a tool boundary, but a very large enabled MCP tool catalogue still has discovery/context cost.

### MCP vs local scripts/tools

**INFERENCE:** MCP is strongest where a capability is genuinely external, shared, authenticated or benefits from interoperable protocol discovery. Small repository-local helpers often have lower overhead as normal scripts called by Skills/Hooks/Agent.

### Portability

**FACT:** MCP is an open protocol with clients/servers beyond Cursor. Source: [Model Context Protocol](https://modelcontextprotocol.io/).

### Suitability

- Large engineering standards: **low as the primitive itself; potentially useful as a remote retrieval interface**.
- Orchestration logic: **high for external/service interaction**.
- Reusable executable implementation assets: **high when exposed as MCP tools/services**.

---

## 11. Plugins

### What they are

**FACT:** Cursor Plugins are installable packages that can bundle Rules, Skills, Agents/Subagents, Commands, Hooks and MCP configuration. Source: [Plugins](https://cursor.com/docs/plugins).

### Manifest and structure

**FACT:** Cursor Plugin packages use a manifest under `.cursor-plugin/` and conventional component paths such as:

```text
skills/
rules/
agents/
commands/
hooks/
mcp.json
```

Source: [Plugin reference](https://cursor.com/docs/reference/plugins).

**OBSERVATION:** Cursor's official `plugin-template` advanced starter includes these primitive families and supporting scripts. Source: [cursor/plugin-template](https://github.com/cursor/plugin-template).

### Installation scope

**FACT:** Cursor supports project/workspace and user installation scopes, plus organisational marketplace/policy mechanisms. Source: [Plugins](https://cursor.com/docs/plugins).

### Loading behaviour

**INFERENCE:** a Plugin has no single context-loading behaviour. Its contents retain their native semantics: an Always Rule may be persistent, Skill content progressive, MCP external, Hooks event-driven, and Subagents isolated.

### Cursor Plugin vs Agent Plugin

**FACT:** Cursor documents a broader Agent Plugin approach alongside Cursor-specific Plugin capabilities. Portable components such as Skills/MCP fit better with the cross-agent model, whereas Cursor Plugins can add product-specific Rules, Commands, Agents and Hooks. Source: [Plugins](https://cursor.com/docs/plugins).

### Intended use

Distribution, installation and composition of a cohesive set of customisations/capabilities.

### What should not go in Plugins

**INFERENCE:** do not treat “Plugin” as the answer to runtime/orchestration design. A Plugin is a packaging boundary; architecture still needs to decide what should be a Rule, Skill, Subagent, Hook, MCP capability, ordinary file, etc.

### Suitability

- Large engineering standards: **neutral — depends on contained primitive**.
- Orchestration logic: **high as packaging/distribution, not orchestration by itself**.
- Reusable executable implementation assets: **high for distributing them with the right runtime wrapper**.

---

## 12. Ordinary documentation and references

### What they are

**FACT:** ordinary Markdown/reference/source files do not automatically become Cursor instructions merely because they exist. Cursor reserves automatic behaviour for recognised mechanisms such as `AGENTS.md`, Rules, Skills, Commands, Subagents, Hooks and MCP. Sources: [Rules](https://cursor.com/docs/rules), [Skills](https://cursor.com/docs/skills), [Prompting agents](https://cursor.com/docs/agent/prompting).

### Discovery and loading

Ordinary files remain outside active prompt context until Agent reads/searches them or the user explicitly references/attaches them.

**INFERENCE:** this gives ordinary documentation the lowest persistent context cost, but there is a reliability trade-off: existence alone does not guarantee that Agent will retrieve or obey the right standard.

### Interaction with Rules/Skills

**FACT:** Rules can reference canonical repository files, and Skills can keep deeper material in supporting references rather than duplicating it in the primary instruction body. Sources: [Rules](https://cursor.com/docs/rules), [Skills](https://cursor.com/docs/skills).

### Intended use

**INFERENCE:** ordinary version-controlled documentation is a strong canonical home for substantial standards, architecture references, examples, specifications and human-readable governance material, especially where multiple tools/agents should consume the same source.

### Suitability

- Large engineering standards: **high**.
- Orchestration logic: **low**.
- Reusable executable implementation assets: **high for ordinary source/script files; Markdown itself remains passive**.

---

## 13. Discovery, scope and precedence

### Scope and discovery comparison

| Primitive | Typical scope/location | Discovery | Model can select automatically? | User can explicitly invoke? |
|---|---|---|---:|---:|
| `AGENTS.md` | Root/nested project directories | Filename + hierarchy | Yes, by applicability | Indirectly |
| Project Rule | `.cursor/rules/*.mdc` | Rule metadata/mode | Yes, depending on mode | Yes for manual Rules |
| User Rule | User Customise scope | Global configuration | Yes | User config/toggle |
| Team Rule | Team/admin scope | Managed configuration | Yes | Depends on admin policy |
| Skill | Project/user/plugin Skill roots | Recursive discovery + description/path relevance | Yes unless disabled | Yes, `/skill-name` |
| Command | `.cursor/commands`, plugin `commands/` | Slash-command catalogue | Not clearly documented | Yes, `/command` |
| Subagent | Project/user/plugin custom-agent definitions | Role/description | Yes | Yes, explicit delegation |
| Hook | Project/user/team/enterprise/plugin config | Event registration | Event-driven, not semantic selection | Config-driven |
| MCP | Project/user/plugin/managed config | Connected server capability catalogue | Yes for relevant tools | Yes, named request |
| Plugin | User/project/org installation | Marketplace/manifest | N/A — contained primitives decide | User/admin installs |
| Ordinary docs | Anywhere | File/search/reference tools | Agent may search/read | Yes, explicit file reference |

Primary sources: [Rules](https://cursor.com/docs/rules), [Skills](https://cursor.com/docs/skills), [Customise Cursor](https://cursor.com/docs/customize-cursor), [Subagents](https://cursor.com/docs/subagents), [Hooks](https://cursor.com/docs/hooks), [MCP](https://cursor.com/docs/mcp), [Plugins](https://cursor.com/docs/plugins).

### Documented conflict behaviour

Cursor does **not** publish one universal precedence ladder covering every primitive.

| Conflict | Documented behaviour |
|---|---|
| Team vs Project vs User Rule | Team → Project → User; applicable Rules merge; higher-precedence source wins conflicting guidance. Source: [Rules](https://cursor.com/docs/rules) |
| Parent vs nested `AGENTS.md` | Combined; more-specific nested instruction wins. Source: [Rules](https://cursor.com/docs/rules) |
| Multiple Hooks | Matching Hooks can all execute; decision results use event-specific merge semantics such as deny > ask > allow for permission decisions. Source: [Hooks](https://cursor.com/docs/hooks) |
| Project vs user Subagent same name | Project-local definition takes precedence; Cursor-native locations take precedence over documented compatibility locations. Source: [Subagents](https://cursor.com/docs/subagents) |
| Local-development Plugin vs installed marketplace Plugin same identity | Marketplace-installed version takes precedence. Source: [Plugins](https://cursor.com/docs/plugins) |
| `AGENTS.md` vs Project Rule | **Not explicitly documented** |
| Plugin Rule vs native Project/User/Team Rule | **Not explicitly documented as a complete cross-origin precedence table** |
| Same Skill name across all supported roots/scopes | **Not fully documented** |
| Same Command name across project/user/plugin scopes | **Not fully documented** |
| Same MCP server identifier across scopes | **Not fully documented** |

**INFERENCE:** architectures should avoid depending on undocumented same-name shadowing or cross-primitive conflict resolution. Use unique names and explicit ownership until behaviour is documented/tested.

---

## 14. Context-loading behaviour

| Primitive | Before use | On activation/applicability | Context risk |
|---|---|---|---|
| Always Rule | Full Rule is applied | Already present | **High persistent cost** |
| Intelligent Rule | Discovery metadata/description | Full Rule when selected | **Low–medium discovery cost; episodic body cost** |
| File-scoped Rule | Matching metadata/pattern machinery | Full Rule when matching context applies | **Scoped episodic cost** |
| Manual Rule | Discoverable identity | Full Rule after explicit reference | **Low until invoked** |
| Applicable `AGENTS.md` | Applicable project instructions | Full applicable text | **Persistent within matching scope** |
| Skill | Name/description discovery metadata | `SKILL.md`; then supporting references/assets progressively | **Strong context economy for specialist depth** |
| Skill kept active in Custom Mode | Explicitly active Skill | Remains available during session | **Higher persistent session cost by design** |
| Command | Command catalogue (exact accounting undocumented) | Prompt/workflow on `/` invocation | **Generally episodic** |
| Subagent | Role/description metadata in parent | Separate child context receives delegated task | **Good parent isolation; extra child-token cost** |
| Hook | Config/script outside ordinary prompt | Event input/output; optional context injection | **Low ordinary prompt cost** |
| MCP | Tool/server catalogue/instructions | Arguments/results/resources when called | **Catalogue cost + episodic tool-result cost** |
| Plugin | No single context mode | Depends on contained primitives | **Composition-dependent** |
| Ordinary docs | Nothing automatically prompt-persistent | File/chunks when retrieved | **Lowest persistent cost; retrieval not guaranteed** |

Source for the overall context model: [Prompting agents](https://cursor.com/docs/agent/prompting).

### Context-economics model

**INFERENCE:** Cursor context can be thought of as three budgets:

```text
Persistent / discovery budget
  Rules + applicable AGENTS.md
  Skill descriptions
  MCP catalogues
  Subagent descriptions

Activation budget
  selected Rule bodies
  selected SKILL.md
  invoked Commands
  requested reference files

Execution / result budget
  tool output
  MCP results
  file reads
  conversation
  Subagent return summaries
```

The architectural objective is not to minimise all context. It is to spend context on material that has high value for the current task.

### Likely flooding patterns

**INFERENCE:** common high-context patterns include giant Always Rules, giant root `AGENTS.md`, too many permanently enabled MCP tools, broad Custom Modes with unnecessary Skill content, and copying the same standards into multiple prompt-bearing assets.

### Progressive patterns

**INFERENCE:** context-efficient patterns include:

```text
concise Skill description
  → focused SKILL.md
  → task-specific references/scripts

thin Rule
  → canonical repository standard

Subagent delegation
  → isolated exploration
  → concise result returned to parent
```

---

## 15. Asset-selection matrix

This table is based only on Cursor primitive semantics. It is **not** the final Power BI/Fabric Architect design.

| Need | Best-fitting primitive | Why | Avoid using |
|---|---|---|---|
| Persistent organisation-wide invariant | Team Rule | Organisation scope, enforcement, highest documented Rule precedence | Per-project copy/paste |
| Persistent repository invariant | Project Rule or root `AGENTS.md` | Automatic project guidance; Rule adds activation metadata, `AGENTS.md` favours simplicity | Optional Command for mandatory behaviour |
| Subtree-specific invariant | Nested `AGENTS.md` or file-scoped Rule | Native directory/glob scoping | Giant global instruction |
| Large engineering standard | Ordinary version-controlled docs/references, reached through thin Rule/Skill where needed | Keeps canonical content outside persistent prompt and reduces duplication | Giant Always Rule / giant root `AGENTS.md` |
| Model-selected specialist capability | Skill | Description-based discovery, progressive resources, scripts/references | Always Rule for rarely needed expertise |
| User-triggered simple repeatable workflow | Command | Explicit `/` workflow semantics | Persistent Rule |
| User-triggered rich workflow with scripts/references | Explicit-only Skill | Keeps explicit invocation while retaining Skill packaging/resources | Oversized single Command |
| Context-isolated specialist investigation | Subagent | Separate context and delegated execution | Skill alone when isolation is the requirement |
| Parallel independent work | Subagents | Native delegation/concurrency boundary | Multiple Skills in one context as a concurrency substitute |
| Deterministic lifecycle enforcement | Hook | Event-driven script/control semantics | Natural-language Rule as a hard control |
| External API/service/tool | MCP server | Standardised external capability boundary | Embedding network integration in prompt prose |
| Small repository-local executable helper | Normal script called by Skill/Hook/Agent | Lower protocol overhead than MCP for local-only helpers | MCP when interoperability is unnecessary |
| Distribute cohesive Cursor customisations | Plugin | Native package for Rules/Skills/Agents/Commands/Hooks/MCP | Manual copying across repositories |
| Cross-agent portable capability | Agent Skill, MCP, portable `AGENTS.md` convention | Open/cross-tool conventions | Cursor-specific Rules/Hooks where portability is mandatory |
| Canonical reusable implementation | Normal source/scripts/library + appropriate wrapper | Keeps implementation testable and independent from prompt packaging | Duplicating production code inside Rules/Commands |

### Suitability summary

| Primitive | Large standards | Orchestration logic | Reusable executable assets |
|---|---|---|---|
| `AGENTS.md` | Low–medium | Low | No |
| Rules | Low embedded; medium as router | Medium, model-mediated | Low |
| Skills | High for progressive references | Medium–high | High as wrapper/package |
| Commands | Low | Medium, explicit workflows | Low–medium |
| Subagents | Low in prompt; can retrieve standards | High | Medium via tools |
| Hooks | No | High deterministic lifecycle control | High |
| MCP | Low as static store | High external capability integration | High service/tool boundary |
| Plugins | Depends on contents | Packaging only by itself | High distribution capacity |
| Ordinary docs/source | High | Low | High for ordinary source files |

---

## 16. Current vs legacy patterns

### `.cursorrules`

**FACT:** Cursor introduced the root `.cursorrules` convention in the 0.32-era product in April 2024. Source: [Cursor 0.32 changelog](https://cursor.com/changelog/0-32-x).

**FACT:** current Rule documentation presents `.cursor/rules/*.mdc` and `AGENTS.md` as the supported project-instruction mechanisms and does not present `.cursorrules` as the recommended current architecture. Source: [Rules](https://cursor.com/docs/rules).

**INFERENCE:** treat `.cursorrules` as a legacy historical pattern for new architecture work. Do not depend on undocumented compatibility behaviour.

### Current Project Rule format

**FACT:** current Project Rules use `.mdc`; a plain `.md` file in `.cursor/rules` is not treated as a Project Rule. Source: [Rules](https://cursor.com/docs/rules).

### Skills are recent and strategically important

**FACT:** Cursor 2.4-era changes significantly expanded Skill/Subagent support and current docs include migration tooling from some Rules/Commands to Skills. Source: [Cursor Skills](https://cursor.com/docs/skills).

### Rules are not obsolete

**FACT:** Always/file/manual/intelligent Rules remain first-class in current docs. Migration tooling does not collapse all Rule semantics into Skills. Source: [Rules](https://cursor.com/docs/rules).

### Commands are not currently documented as deprecated

**FACT:** Commands remain exposed in current customisation and plugin documentation even though migration to explicit-only Skills is supported. Sources: [Customise Cursor](https://cursor.com/docs/customize-cursor), [Plugin reference](https://cursor.com/docs/reference/plugins), [Cursor Skills](https://cursor.com/docs/skills).

### Skill metadata has evolved

**FACT:** current Skill guidance uses current path-scoping conventions while retaining compatibility with older metadata patterns. Source: [Cursor Skills](https://cursor.com/docs/skills).

### Subagents are evolving

**FACT:** current Subagent semantics include automatic delegation, separate contexts, parallelism and nested child behaviour subject to restrictions. Older material that describes only static custom prompts is incomplete. Source: [Subagents](https://cursor.com/docs/subagents).

### Plugins are richer than prompt bundles

**FACT:** current Plugins can package multiple primitive types and have manifest/install/marketplace semantics. Source: [Plugins](https://cursor.com/docs/plugins).

### Hooks remain environment/version-sensitive

**FACT:** support details have evolved across local, Cloud and managed environments. Source: [Hooks](https://cursor.com/docs/hooks).

---

## 17. Implications for the Power BI/Fabric Architect research programme

These are **research constraints/questions only**, not final architecture decisions.

### R2 — harness vs agent vs skill vs plugin

**INFERENCE:** R2 should not treat these labels as alternatives at one abstraction layer.

- Plugin = distribution/composition boundary.
- Skill = discoverable capability package.
- Subagent = delegated context/execution unit.
- Main Cursor Agent = host runtime.
- Hook = deterministic lifecycle control.
- MCP = external capability boundary.
- “Harness” = broader architecture pattern, not itself one Cursor primitive.

R2 therefore needs to compare **compositions**, not merely choose one noun.

A useful decomposition is:

```text
procedural orchestration          → Skill / Command
delegated cognitive orchestration → Subagent
deterministic lifecycle control   → Hook
external capability integration   → MCP
distribution/composition          → Plugin
```

### R3 — reference implementation benchmark

R3 should inspect more than whether a repository “uses Skills.” It should record:

- canonical source of truth;
- persistent context;
- discovery metadata;
- progressive/on-demand content;
- executable assets;
- delegated contexts;
- distribution/install mechanism;
- duplication between primitives.

**OBSERVATION:** Cursor's own official repositories already demonstrate Skills with supporting references/scripts inside Plugins rather than a monolithic prompt approach. Sources: [cursor/plugin-template](https://github.com/cursor/plugin-template), [cursor/plugins](https://github.com/cursor/plugins).

### R4 — cross-repository composition

**FACT:** native Project Rules/Skills/`AGENTS.md` are project-local concepts; Cursor's documented repository-scale distribution mechanism is Plugin-oriented rather than arbitrary remote Rule import. Sources: [Rules](https://cursor.com/docs/rules), [Skills](https://cursor.com/docs/skills), [Plugins](https://cursor.com/docs/plugins).

R4 therefore needs to test:

- Plugin installation;
- vendoring/syncing;
- checked-out dependencies/submodules;
- shared packages;
- MCP/service exposure;
- whether canonical standards are duplicated or referenced.

### R6 — standards/library packaging

R6 should explicitly separate:

```text
canonical normative standard
≠ automatic invariant/trigger
≠ procedural Skill
≠ executable implementation
≠ distribution package
```

The key test is whether a proposed packaging method preserves one source of truth without turning the whole standards corpus into persistent context.

For Power BI/Fabric this matters because standards and executable assets are different things:

- standards: DAX, M, semantic model, visualisation, governance, Fabric patterns;
- executable assets: DAX snippets/functions, M functions, Python utilities, Deneb templates/specifications, validation scripts.

Cursor primitives do not require these to share the same canonical container.

### R7 — cross-agent portability

Portability is uneven:

| Primitive | Portability outlook |
|---|---|
| Agent Skills | Strong — open Agent Skills convention |
| MCP | Strong — open protocol |
| `AGENTS.md` | Strong–medium — open/shared convention, but client semantics may differ |
| Agent Plugin format | Potentially stronger than Cursor-specific Plugin components |
| `.cursor/rules` | Cursor-specific |
| Cursor Commands | Cursor-specific convention/interface |
| Cursor Subagent definitions | Medium — compatibility exists, runtime semantics may differ |
| Cursor Hooks | Lower — event/schema/runtime semantics are product-specific |
| Cursor Plugin | Cursor-specific envelope around potentially portable contents |
| Ordinary Markdown/source | Very strong as passive content; automatic behaviour not portable by itself |

R7 should distinguish:

1. **same files work unchanged**;
2. **same canonical content with thin adapters**;
3. **same concept recreated separately**.

Those are materially different portability targets.

### Programme-wide context constraint

The eventual Power BI/Fabric standards corpus may be large. Later architecture tickets should measure candidate designs against:

```text
1. persistent instruction tokens
2. discovery metadata tokens
3. activation-time capability tokens
4. reference-retrieval tokens
5. tool/result tokens
6. subagent token duplication
```

Source for the categories of context pressure: [Prompting agents](https://cursor.com/docs/agent/prompting).

---

## 18. Recommendations for subsequent research

1. **R2:** require each candidate architecture to draw an explicit concern map covering persistent invariants, specialist procedures, canonical knowledge, executable assets, deterministic controls, external capabilities, delegated cognition and distribution.

2. **R3:** benchmark context behaviour, not just folder structure. Record what is loaded persistently, exposed as metadata, retrieved on activation, executed outside context and returned as results.

3. **R4:** perform an empirical cross-repository installation/composition experiment with at least three repositories: standards, domain pack and consumer PBIP project.

4. **R6:** benchmark a realistically large engineering standard using at least four packaging approaches:
   - Always Rule;
   - conditional/intelligent Rules;
   - Skill with supporting references;
   - ordinary docs routed by a thin Rule/Skill.

5. **R6:** test whether implementation assets can remain normal testable source while Skills/Rules act as discovery/routing wrappers.

6. **R7:** take one representative capability and test the same Skill/AGENTS/MCP assets in Cursor and selected adjacent agents, recording unchanged-file compatibility versus adapter requirements.

7. **Empirical context test:** measure actual token/context footprint for large Rule sets, Skill catalogues and MCP catalogues because official documentation explains semantics but not exact per-feature token accounting.

---

## 19. Unresolved / undocumented questions

| Question | Why it matters |
|---|---|
| What is the exact precedence between `AGENTS.md` and an applicable Project Rule when they directly contradict? | Both can represent project instructions; docs publish separate precedence models but not a unified one. |
| How are Plugin-provided Rules ordered relative to native Project/User/Team Rules? | Required before relying on Plugins for governance overrides. |
| What is the complete same-name Skill precedence across `.cursor`, `.agents`, compatibility roots, user scope and Plugins? | Needed for deterministic multi-tool installation. |
| What is same-name Command precedence across project/user/plugin scopes? | Current primary docs do not provide a Rule-style precedence table. |
| Can standalone Commands ever be autonomously selected by Agent, or should they be treated as explicit-only? | Docs strongly emphasise `/` invocation but do not publish a formal negative guarantee. |
| What exact context tokens are consumed by inactive Intelligent Rule metadata? | Needed for large standards/catalogue sizing. |
| What exact discovery/context footprint does a very large MCP server impose before any tool call? | Relevant if future Fabric/Power BI tooling exposes many actions. |
| What are collision semantics for project and global MCP server IDs? | Needed for reproducible team configuration. |
| Is root `.cursorrules` still parsed for compatibility in every current Cursor channel? | Historical introduction is clear; current design guidance has moved on. |
| What is current local-vs-Cloud parity for every Hook event and hook type? | Core control logic must be environment-safe. |
| How do large Plugin installations affect aggregate discovery metadata context? | Plugins can add many Skills, Rules, Subagents and MCP tools. |
| How reliably will Agent retrieve an ordinary standard without a Rule/Skill routing hint? | Determines the trade-off between context economy and governance reliability. |
| How are Skill/Plugin versions pinned and updated in team/project deployments? | R4/R6 require reproducibility, not just discoverability. |
| Which Power BI/Fabric workflows require local-only capabilities that Cloud Agents cannot reproduce? | Affects Hooks, credentials, local tools and Desktop/PBIP integration. |

---

## 20. Sources

### Primary official Cursor documentation

- Cursor Docs — Rules: <https://cursor.com/docs/rules>
- Cursor Docs — Agent Skills: <https://cursor.com/docs/skills>
- Cursor Docs — Prompting agents/context: <https://cursor.com/docs/agent/prompting>
- Cursor Docs — Subagents: <https://cursor.com/docs/subagents>
- Cursor Docs — Hooks: <https://cursor.com/docs/hooks>
- Cursor Docs — Model Context Protocol: <https://cursor.com/docs/mcp>
- Cursor Docs — Plugins: <https://cursor.com/docs/plugins>
- Cursor Docs — Customise Cursor / Commands: <https://cursor.com/docs/customize-cursor>
- Cursor Docs — Plugin reference: <https://cursor.com/docs/reference/plugins>
- Cursor Docs — Deeplinks / command creation reference: <https://cursor.com/docs/reference/deeplinks>
- Cursor historical changelog — 0.32 `.cursorrules`: <https://cursor.com/changelog/0-32-x>

### Portable/open conventions

- Agent Skills specification: <https://agentskills.io/>
- AGENTS.md open convention: <https://github.com/agentsmd/agents.md>
- Model Context Protocol: <https://modelcontextprotocol.io/>

### Official Cursor repository evidence

- Cursor Plugin Template: <https://github.com/cursor/plugin-template>
- Cursor official Plugins repository: <https://github.com/cursor/plugins>

---

## Research state

R1 establishes a sufficiently differentiated primitive vocabulary for later architecture work:

- what each Cursor primitive does;
- where its main context costs sit;
- where documented precedence exists;
- where behaviour is still undocumented/version-sensitive;
- which primitives are Cursor-specific versus portable/open conventions.

It deliberately does **not** decide the Power BI/Fabric Architect topology. Those decisions belong to subsequent Wayfinder tickets.