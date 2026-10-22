# R7 — Cross-Agent Portability for Architect

> **Terminology correction (2026-10-22):** The project is the **Power BI / Fabric Architect**. **Wayfinder** is Matt Pocock's planning skill used during research, not the project name. Original issue/PR titles may retain historical wording. The evidence and technical conclusions are unchanged. References to private standards describe the repository's earlier visibility; it became public on 2026-10-22.

**Issue:** [#14 — R7](https://github.com/GitKlink/performance-reward-dashboard-architect/issues/14)  
**Research snapshot:** 2026-10-19  
**Status:** research / provisional recommendation. **Not** the final target-architecture decision or a feature-parity commitment.  
**Required inputs:** [R1](01-cursor-primitives.md), [R3](03-reference-repo-benchmark.md). Additional context: [R2](02-harness-agent-skill-plugin.md), [R4 (review PR #23)](https://github.com/GitKlink/performance-reward-dashboard-architect/pull/23), [ADR-0001](../../docs/decisions/0001-canonical-standards-home.md).

## 1. Scope and target runtimes

**Question:** How can a Cursor-first Power BI/Fabric analytical architect run useful, governed workflows in other coding agents without either (a) rebuilding every native Cursor feature, or (b) duplicating canonical engineering standards and business definitions into prompts, rules and plugins?

**Priority hosts:**
1. **Cursor IDE/CLI** — primary interactive authoring host and first deployment target.
2. **OpenAI Codex** — secondary coding agent with AGENTS.md and Agent Skills support.
3. **Claude Code** — secondary host with its own memory, Skills, tool permissions, hooks and plugins.
4. **GitHub Copilot** — secondary/possible future check, not a launch-parity target.
5. **Other agents** — may participate where they support Agent Skills or plain Markdown and basic tools; not automatically considered compatible.

"Portable" is not a boolean. R7 evaluates these separately:

- **Content portability:** can the same policy, business definition or procedure be read without changing its meaning?
- **Discovery portability:** can a host locate the correct instruction/skill at the right time?
- **Execution portability:** can its local tools actually inspect a PBIP model, run scripts, access sources and emit results?
- **Enforcement portability:** can the *same observable checks* independently verify conformance?
- **Deployment portability:** can a project resolve pinned private dependencies in the supported environment?
- **Workflow portability:** can a repeatable task yield semantically equivalent results, despite different tools?

**Out of scope:** build a full adapter system, install toolchains, certify agents on a live PBIP project, guarantee model output equivalence, port all native Cursor hooks/subagents or choose a final plugin format.

### Existing Architect authority constraints

- **Architect/Architect:** workflow routing and orchestration; not the agent runtime.
- **Canonical policy:** private [GitKlink/power-bi-fabric-standards](https://github.com/GitKlink/power-bi-fabric-standards), already established by [ADR-0001](../../docs/decisions/0001-canonical-standards-home.md). There are 11 original semantic-model standard files, preserved byte-for-byte.
- **Reusable implementation:** [GitKlink/dax-m-query-library](https://github.com/GitKlink/dax-m-query-library) for executable DAX/M/Python/Deneb patterns, not business truth.
- **Domain pack:** Performance & Reward controls business/KPI meaning, populations, eligibility, dates and contracts. Its physical separation from semantic-model domain extensions remains [#6](https://github.com/GitKlink/performance-reward-dashboard-architect/issues/6).
- **PBIP project:** owns its actual local code, model, reports, tests and adopted pinned dependency revisions.
- **Microsoft Power BI/Fabric skills:** prefer upstream maintained platform capability; adapt/delegate rather than fork by default.

**Evidence labels used below:** **DOCUMENTED** = current official documentation or open specification; **OBSERVED** = R1/R3 reference implementation; **INFERENCE** = proposed design consequence; **UNTESTED** = needs host/environment verification. No installed Cursor, Claude or Codex runtime was exercised as part of this R7 research.

## 2. Portable primitives

### 2.1 Ordinary Markdown, schemas, tests and scripts

**DOCUMENTED/OBSERVED:** The lowest-friction portable layer is plain version-controlled documentation, metadata, schemas, datasets and deterministic scripts. R3's Spec Kit, Matt Pocock, Addy Osmani and Microsoft examples keep reusable content separate from installed host-specific adapters.

**Recommendation:** keep all normative engineering standards as canonical repository documents. Treat domain contracts and test fixtures similarly, at their proper domain/asset authority. Scripts must declare their runtime/tool requirements; a Python/DAX/Tabular tooling dependency does **not** magically become available because the Markdown travels to a new agent.

This is content portability, not automatic instruction loading. A host requires an explicit resolver, approved revision and sufficient permissions.

### 2.2 AGENTS.md as compact instruction bridge

**DOCUMENTED:**
- Cursor supports root and nested AGENTS.md in current Rules documentation: [Cursor Rules](https://cursor.com/docs/rules).
- Codex walks its instruction hierarchy from global scope through repo root to the working directory; AGENTS.override.md, fallback filenames and size limits are Codex-specific: [Codex AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md).
- **Important October 2026 update:** Claude Code supports AGENTS.md natively starting with its recent built-in support (**v2.1.277+**). By default, it reads AGENTS.md **only when no CLAUDE.md (or CLAUDE.local.md) is present at the working directory or above it**. An explicit user/managed setting can elect to read both. Older versions lack native support; a CLAUDE.md with an `@AGENTS.md` import remains a compatibility adapter. [Claude Code memory/AGENTS.md](https://code.claude.com/docs/en/memory#agentsmd).

**INFERENCE:** one concise **canonical project-level AGENTS.md**, in the **project repository that will be opened by the agent**, is the leading portable *router*. It may say: identify project write root; resolve pinned standards revision; load required standards/glossary/domain meaning; never write to reference repos without explicit authorization; record evidence.

**Not a substitute** for the large standard. Do not embed all DAX/semantic-model conventions in AGENTS.md, assume all hosts honour nested files identically, or rely on AGENTS.md as permission enforcement.

**Claude-specific caution:** avoid generating both a verbose CLAUDE.md and a full copied AGENTS.md. If the host must have a CLAUDE.md, import/reference the shared AGENTS.md once; check configuration and installed version. Direct AGENTS.md loading has differences in hooks and added-directory handling documented by Anthropic.

### 2.3 Agent Skills / SKILL.md

**DOCUMENTED:** [Agent Skills open specification](https://agentskills.io/specification) defines a directory with SKILL.md YAML frontmatter including required `name` and `description`, Markdown workflow, and optional scripts/references/assets. Cursor and Codex both document project Agent Skill locations, especially `.agents/skills/<name>/SKILL.md`. Claude Code has its own project skill discovery under `.claude/skills/`, including skills from additional directories. [Cursor Skills](https://cursor.com/help/customization/skills), [Codex skills](https://learn.chatgpt.com/docs/build-skills), [Claude Code skills](https://code.claude.com/docs/en/skills).

**INFERENCE:** a **canonical skill source** (for example, "review-semantic-model-measures") can use only the open-spec essentials so the main instructions are portable. The skill tells an agent *how* to load relevant standards and inspect a model; it does **not** duplicate the canonical standards.

**Crucial limitation:** common SKILL.md syntax ≠ guaranteed identical discovery paths, automatic selection, tool permission, host context or trigger behaviour. Host-specific frontmatter such as path-scoping, invocation flags and model/tool bindings require adapters or capability checks; do not silently claim portable semantics for unknown fields.

### 2.4 MCP as tool-capability boundary

**DOCUMENTED:** Cursor, Codex and Claude Code support MCP integrations, while MCP itself defines a protocol separate from a host's UX/configuration. [Cursor MCP](https://cursor.com/docs/mcp), [Codex MCP](https://developers.openai.com/codex/mcp), [Claude Code MCP](https://code.claude.com/docs/en/mcp), [MCP specification](https://modelcontextprotocol.io/specification/).

**INFERENCE:** standards-resolution tools, model-inspection tools and existing Microsoft/Fabric integrations can sometimes expose a portable **protocol contract**. This does not mean identical installation, prompts, scopes, authentication, tool approval or data handling. Prefer deterministic local scripts for conformance where possible, with MCP adapters when live access is required.

### 2.5 Portable validations

**INFERENCE:** deterministic conformance checks (for measure naming, metadata completeness, repository authority/versions, prohibited writes, declared semantic basis) are the strongest cross-host contract. Run the same validator and golden fixtures when different hosts propose a PBIP change. A model stating that it followed a rule is not evidence of passing.

## 3. Cursor-specific primitives

**DOCUMENTED / R1:** Cursor Project Rules under `.cursor/rules/*.mdc` have their own activation modes and globs; Cursor-specific hooks, agents/subagents, commands, MCP configuration and plugin packaging provide extra ergonomics and control. Cursor also supports both its own `.cursor-plugin/plugin.json` format and the portable **Agent Plugins** root `plugin.json` format for skills/MCP; the latter is a smaller common surface, **not** a universal guarantee that every other host installs it without adaptation. [Cursor Rules](https://cursor.com/docs/rules), [Cursor Plugins](https://cursor.com/docs/plugins), [Cursor Plugin reference](https://prod.cursor.com/docs/reference/plugins).

**Design:** keep a Cursor adapter that can:
- expose a small relevance trigger or Project Rule referring to the **pinned canonical standard**;
- install/select the portable skill in a path Cursor discovers;
- register permitted tools/MCP and apply optional Cursor-native UX such as commands;
- surface source revision, write root and validation commands before a change;
- enforce whatever restrictions a deterministic validator/tool permission can actually enforce.

**Important R4 limitation:** multi-root is useful **locally** to expose sibling Git repos to Cursor Agent, but official Cursor docs say **Cloud Agents do not support multi-root workspaces**. File-pattern Rules also require actual file/context activation. A cross-root accessible standard is not proof that Agent used it. See [R4 review PR #23](https://github.com/GitKlink/performance-reward-dashboard-architect/pull/23), [Cursor search](https://cursor.com/docs/agent/tools/search).

**Not portable by syntax:** `.mdc` frontmatter, globs/activation, Cursor-specific plugin variables, hook event names and any orchestration assumptions about multi-root. A converter must **interpret desired behaviour**, not merely rename a file to CLAUDE.md.

## 4. Other-agent-specific primitives

### Codex

**DOCUMENTED:**
- `AGENTS.md` / `AGENTS.override.md` are instruction-discovery files; Codex reads a scoped chain at start. [Codex AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md).
- `.agents/skills/` exposes SKILL.md workflows, with project and user/admin skill discovery. [Codex skills](https://learn.chatgpt.com/docs/build-skills).
- MCP is a common tool integration pattern. [Codex MCP](https://developers.openai.com/codex/mcp).

**INFERENCE:** no Codex-only clone of canonical standards should exist. Keep Codex path/skill registration, permissions, tool config and invocation documentation in a thin adapter. Native product plugin conventions and agent runtime permissions must be tested against the actual Codex environment being targeted; they are **not** simply Cursor's `.cursor-plugin` contract.

### Claude Code

**DOCUMENTED:**
- Project instructions normally use `CLAUDE.md`; recent versions can read `AGENTS.md` subject to the fallback/config/version rules above. [Claude memory](https://code.claude.com/docs/en/memory).
- Project skills use `.claude/skills/`; subagents live under Claude's agent conventions, while tool hooks and permissions have their **own** structured settings/event contracts. [Claude skills](https://code.claude.com/docs/en/skills), [subagents](https://code.claude.com/docs/en/sub-agents), [hooks](https://code.claude.com/docs/en/hooks).
- Claude Code plugins and marketplaces use `.claude-plugin`-specific installation structure and semantics. [Claude plugins](https://code.claude.com/docs/en/plugins).
- A `CLAUDE.md` `@AGENTS.md` import **expands into context**; it is not a zero-token pointer. External imports can require consent.

**INFERENCE:** rely first on direct AGENTS.md when tested on a supported Claude version; use a **small generated CLAUDE.md adapter** only where an existing CLAUDE.md or older host forces it. Keep optional Claude-specific hooks/subagents isolated in `.claude/`. Their absence in Codex or Cursor must not make the core semantic-model review impossible.

### GitHub Copilot (secondary check)

**DOCUMENTED:** GitHub documents repository instructions, AGENTS.md support for some surfaces, Agent Skills and separate GitHub-specific custom agents/paths/hooks. Support differs by Copilot feature (cloud agent vs review vs IDE). [Support matrix](https://docs.github.com/en/copilot/reference/custom-instructions-support); [skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills).

**INFERENCE:** treat Copilot as a host-specific adapter target after the first three pass. Do not imply that its code-review runner and IDE agent load every skill/instruction the same way.

## 5. Canonical-source vs generated-adapter model

### Proposed division

| Content | Canonical source | Runtime exposure | Copy policy |
|---|---|---|---|
| Semantic-model/DAX/M engineering **policy** | **Standards repo** | Resolved, version-pinned Markdown/reference reads | Do **not** hand-maintain second normative copies |
| Performance & Reward **business meaning** | Domain authority/contract | Domain-selected reference files/contracts | No redefinition in generic engineering rules |
| Reusable DAX/M/Python/Deneb | **Implementation library** | Versioned asset IDs/functions/templates and tests | Reuse executable assets with attribution/version |
| Project identity, write root, requested behaviour | **PBIP project** | Small AGENTS.md/project contract | Project-local facts, not global standards |
| Cross-host procedural SKILL.md | One reviewed canonical skill source in Architect or governed capability package | Resolved/installed into per-host skill path | Generated/materialised **read-only, tagged** projections allowed |
| Host hooks/rules/commands/plugin manifests | Host adapter templates | Generated into host-specific paths if installed | Only adapter owns host syntax; never duplicate core policy |
| Validation/test fixtures | Correct standards/domain/library owner by test type | Standalone validator + evidence report | Reference pinned test suite/version |

**Provisional source tree (conceptual only, not an instruction to restructure repositories now):**

~~~text
Architect (architect authority)
  contracts/               # proposed project/dependency and capability descriptors
  capabilities/            # proposed canonical procedural SKILL.md packages
  adapters/
    cursor/                 # .mdc, plugin and hook templates (native-only)
    codex/                  # registration/tool/config adapter
    claude/                 # optional CLAUDE.md, hooks/agents templates
    copilot/                # possible future bridge
  bootstrap/               # R5 to choose whether this is needed
  evaluations/             # cross-host golden tasks

power-bi-fabric-standards (engineering-policy authority)
  semantic-model/...       # already migrated; remain canonical
  dax/...                  # future standards, not invented as existing content

dax-m-query-library (reusable implementation authority)
  library/dax ...
  library/m ...

PBIP project (product implementation authority)
  AGENTS.md                # concise approved host-neutral project guidance
  <project dependency pin/lock — schema TBD by R5/R8>
  <PBIP/TMDL files>
~~~

**Generator/installer contract — proposed for R5 to refine:**

1. **Source selection:** resolve authoritative repo + exact approved release/SHA and verify private-repo access, integrity and license/scope.
2. **Capability check:** detect target host/version/platform and supported instruction, Skill, MCP, plugin and hook features. Do not equate capability by filename alone.
3. **Materialisation:** place **only required** portable skills and thin host adapters under correct host-specific roots. Preserve a manifest with source ID, content digest, generator version and target.
4. **Conflict detection:** before touching files, identify local user modifications and duplicate capability installations. Avoid overwriting unrelated `AGENTS.md`, `CLAUDE.md`, `.cursor/rules` or any private application settings.
5. **Activation smoke test:** prove the host discovers the router, can resolve the approved standard, reads the target domain rule and can invoke required tools.
6. **Conformance test:** run a host-independent validator on a small PBIP fixture. Store evidence: project revision, standards/domain/library versions, host version, files inspected, rules applied and test outputs.
7. **Lifecycle:** upgrades and removals touch only *managed* projections with matching recorded digests; changed local files require a merge/override path. A failed dependency update must not silently fall back to latest.
8. **Default safety:** dependency/reference repos read-only in an ordinary PBIP change; no copying private full standards into a public repo; credentials never embedded in generated manifests.

This mechanism is a **recommendation**, not implemented or adopted. R5 chooses whether to build a CLI/bootstrapper, use plugin-manager-native workflows, or phase them.

### Example canonical project router — illustrative, not installed

~~~markdown
# AGENTS.md

This repository owns the PBIP analytical product. All substantive edits belong here
unless the task explicitly names another repository as its write owner.

For semantic model or DAX work:
1. Resolve the project's pinned versions of engineering standards, domain contracts
   and implementation-library assets. Never assume the latest default branch.
2. Read the canonical semantic-model standard and business glossary at that revision,
   then the relevant domain representation and domain business definitions.
3. Inspect actual model metadata and dependencies before proposing changes.
4. Run the named deterministic checks and record both results and input revisions.
5. Fail with a clear missing-dependency/permission error rather than guessing.

Do not copy entire private standards into this repository.
~~~

Host adapters can add the trigger/discovery needed by Cursor or Claude without making this project router the source of normative DAX definitions.

## 6. Installation/distribution considerations

| Distribution pattern | Portable content? | Host discovery? | Security/update implications | R7 assessment |
|---|---|---|---|---|
| Plain Git clone + small AGENTS.md | Strong | Mixed: host/version depends | Independent access/version checks | Good common baseline, insufficient automation |
| One canonical `SKILL.md` tree + host paths | Strong | Good where path supported | Installer must manage paths and source provenance | **Preferred workflow content design** |
| Cursor Plugin `.cursor-plugin` | Host-specific | Cursor-native | Cursor version/marketplace trust | Optional Cursor enhancement |
| Root Agent Plugin `plugin.json` | Portable **format subset**: skills/MCP | Cursor documents support; others must be checked | Config/variable differences remain | Worth testing, **not** assumed universal |
| Claude `.claude-plugin` | Host-specific | Claude-native | Different runtime/install/marketplace | Optional Claude enhancement |
| Codex-native registration/plugin/config | Host-specific | Codex-native | Host-specific auth/approval | Thin adapter only |
| Manually copied SKILL.md files | Content is transferable | Maybe | Divergence/duplicate capability risk | Suitable prototype, not long-term authority |
| Immutable dependency manifest + managed materialisation | Host-neutral contract possible | Requires adapters/resolver | Best potential provenance, private access and rollback | **Recommended design direction** |
| Vendored full normative standards | Files readable everywhere | High local visibility | Private leak and authority drift | **Reject by default** |

R4 [PR #23](https://github.com/GitKlink/performance-reward-dashboard-architect/pull/23) adds an essential deployment caveat: local Cursor multi-root discovery is **not** the same as a single-root Cloud Agent runtime or a Codex/Claude session. Installation should make source inputs available through the host's actual supported environment and then verify *effective* loading. A portable AGENTS.md file is **not** itself a cross-repo source fetcher.

## 7. Comparison matrix — portable vs host-specific

Legend: **P** = portable content/contract with host test; **N** = native syntax/behaviour; **A** = requires adapter/configuration; **U** = untested for this project. These labels **do not** assert successful end-to-end execution.

| Concern | Cursor | Codex | Claude Code | Portable core recommendation |
|---|---|---|---|---|
| Ordinary Markdown canonical standards | P with accessible checkout | P with access | P with access | Yes: versioned references, not duplicated prompts |
| `AGENTS.md` project router | P (current docs) | P (native) | P **conditional** (version/config/fallback) | Yes, short/invariant only |
| Full host-specific rule files | **N** `.cursor/rules/*.mdc` | **A** AGENTS/custom instructions | **N** `.claude/rules/*.md` | No full-rule parity; generate thin adapters |
| Open-spec Agent Skills `SKILL.md` | P in supported dirs | P in supported dirs | P in Claude-compatible paths | Yes: canonical procedures with minimal required metadata |
| Skill auto-selection and scoping | N/U | N/U | N/U | Test route accuracy per host |
| Custom subagents | N | N/U | N | Not required for minimum viable task |
| Hooks/lifecycle controls | N | N/U | N | Avoid behavioral assumptions; external validator for required controls |
| MCP protocol tools | P at protocol level, A config | P/A | P/A | Portable tool contract with host adapters/auth |
| Plugin manifests/distribution | N plus Agent Plugin subset | N/A | N | Separate from canonical policy and skill content |
| Multi-root editor workspace | N (local; Cloud unsupported) | Not a common installation contract | Not a common installation contract | Use resolved dependency/source contract instead |
| Immutable dependency pin + source verification | P if externally implemented | P if externally implemented | P if externally implemented | Yes: **design candidate**, needs R5 |
| Deterministic model/naming validator | P if runtime dependencies available | P if dependencies available | P if dependencies available | Yes: strongest common acceptance layer |
| PBIP live inspection / execution | Depends on available tools | Depends on available tools | Depends on available tools | Tool capability checks, not inferred from instructions |

**Interpretation:** common **information architecture** and **task acceptance criteria** can be portable. Native lifecycle events, host context assembly and installation are not automatically portable even when file formats look alike.

## 8. Recommended portability boundary

### R7 recommendation, subject to R8 synthesis

Adopt **portable core + thin host adapters + host-independent acceptance tests**, with Cursor as the highest-fidelity initial adapter.

- **Canonical shared core:** approved standards, P&R domain contracts, stable implementation-asset IDs, open-format procedural SKILL.md, brief AGENTS.md project instructions, versioned dependency declarations, test fixtures/validators.
- **Native adaptation:** Cursor Rules, commands, plugins, subagents and hooks where they improve first-host experience; Claude/Codex equivalent adaptations only when a tested need exists.
- **No weakest-host veto:** do not remove a good Cursor-native capability because another host cannot use it. Instead give that other host a feature-gated fallback or mark the capability unsupported.
- **No duplicate source of truth:** generated adapters may include pointers, invocation wrappers and platform settings; they must not become a second hand-maintained standards manual.
- **No enforcement-by-prompt:** cross-host claims must be checked by validated outputs and source provenance, not an agent self-report.
- **Narrow initial proof:** one Power BI semantic measure review operation across Cursor and Codex, optionally Claude, against identical model and standards/domain revisions.

### Non-negotiable support tiers (proposal)

**Tier 1 — Supported:** host can resolve pinned inputs, inspect target PBIP/TMDL, run required validator, and reproduce expected evidence with no manual reconstruction.

**Tier 2 — Compatible/manual:** host can read the same standards and follow the skill but some tool/installer features require human setup; conformance is only claimed when deterministic checks actually ran.

**Tier 3 — Unsupported:** only generic natural-language advice; no conformance/portability claims.

Do not market every `SKILL.md`-capable host as Tier 1 without a documented pilot and installed dependency path.

## 9. Implications for the Power BI Architect

### Example: Variable Reward measures in a real PBIP repo

A user requests a measure naming/metadata refactor in a Performance & Reward model.

**Host-neutral task contract:**

1. Identify PBIP project root and enumerate measures with actual DAX, folders, descriptions, format strings and dependencies.
2. Confirm pinned standards source `GitKlink/power-bi-fabric-standards` and reference the core semantic-model standard, glossary, Variable Reward representation guidance.
3. Confirm domain-owned definitions of the target Opportunity, Payout and IPM measures. Do not infer business semantics from names.
4. Propose model-local changes: root-first business measure names and family relationships, controlled `Change` versus `Variance`, appropriate hidden/support prefixes and display-folder treatment.
5. Preserve business meaning and existing dependency links; compare model outputs before/after where a calculation or relationship is changed.
6. Run a deterministic conformance check for naming, descriptions, visibility, folder ownership, collision avoidance, DAX parse/model compile and numerical reconciliation where relevant.
7. Emit structured evidence recording **source revisions**, host/runtime, standards/skill IDs, measures checked, pass/fail and unresolved exceptions.
8. Edit only the PBIP project unless a separate explicitly authorised standards/library PR is necessary.

**Cursor experience:** native Project Rule or Skill prompts to load relevant standard; use multi-root checkout if local. **Codex experience:** project AGENTS.md and Agent Skill with the same task contract, plus tool adapter. **Claude experience:** supported AGENTS.md or minimal CLAUDE.md import, with Claude-specific skills/tool config. Results are **equivalent only if test evidence agrees**.

This avoids making a second DAX refactoring standard in the skill. It also preserves separate P&R analytical meaning from the generic semantic/model naming grammar.

### Portability-specific evaluation suite — proposed

| Test | Setup | Pass criterion | Why |
|---|---|---|---|
| P1 | Three hosts; same approved SKILL.md | Each discovers correct skill after install; explicit invoke works | Discovery |
| P2 | AGENTS.md plus existing CLAUDE.md | Claude reads project router **once** with supported host configuration | No silent omission/duplication |
| P3 | Pinned private standards repo inaccessible | Resolver fails closed and reports missing auth | Security/integrity |
| P4 | Dependency version drift | All hosts report approved vs actual SHA mismatch | Reproducibility |
| P5 | Same PBIP fixture, naming violation | Same deterministic validator failure in Cursor/Codex/Claude | Behavioural equivalence |
| P6 | Domain semantic conflict | Host defers to domain authority, never edits generic standards | Ownership |
| P7 | Agent attempts to edit standards dependency | Fails/asks or detects forbidden write, no silent mutation | Write boundary |
| P8 | New standards version released | Project still uses pinned old revision until reviewed change | Update policy |
| P9 | Skill supporting reference omitted by selective install | Activation reports missing file; no guessed substitute | Packaging |
| P10 | Cursor rule / Claude hook / Codex command absent | Core test still runs or host is honestly marked Tier 2/3 | Graceful degradation |
| P11 | Public PBIP repo + private standards dependency | Private full text not added to public commits, diff, logs or generated docs | Confidentiality |
| P12 | Change accepted on one host | Re-run independent validator outside any agent | Deterministic acceptance |

Tests remain **UNTESTED**; R5/R8 should select an executable smoke-test harness and fixture before promising compatibility.

## 10. Unresolved questions and handoffs

### R5 — installation/bootstrap (#15)

- Choose a **single portable project manifest/lock format** and whether CLI/bootstrap is necessary in phase 1.
- Decide managed vs editable skill installation and what to do when both are present.
- Detect actual Cursor, Codex, Claude versions and supported skill paths without breaking user customisations.
- Define private repo auth, reproducible checkout, rollback, provenance and no-credential-in-manifest rules.
- Provide **separate local multi-root Cursor and single-root cloud/CI materialisation** plans.
- Prevent mismatch between installed adapters and the canonical skill version.
- Determine what the installer **will not** own (standards authorship, domain semantics, the host's model/tools/runtime).

### R6 — standards/library packaging (#16)

- Choose canonical skill package metadata, stable IDs, standards index/entrypoint/versioning and generated manifest boundary.
- Decide how supporting references survive selective installation; no hard-coded sibling paths.
- Evaluate independent versions of standards, skill, reusable asset and adapter; a single global version cannot cover all.

### R8 — target architecture synthesis (#17)

- Decide composition: Cursor-first native adapter with portable core, release/distribution mechanism, dependency resolver and test contract.
- Preserve the actual constraints of the embedded P&R analytics team.
- Explicitly state feature support tiers and failure modes for Cursor Cloud, Codex and Claude.
- Determine if an installable plugin is warranted **after** proving the core workflow.

### Domain authority (#6)

- Refactor domain extensions **only after** the business concept vs semantic-model representation boundary is approved. Migration/source preservation is complete; refactor remains a separate change.

### Documentation/version risks

- Claude's native AGENTS.md support is a recent change with version and default-config caveats. Lock documentation and installed versions for any published compatibility claim.
- Cursor and Codex may accept the same SKILL.md but select it under different routing rules.
- Agent Plugins is a promising portable *subset* for skills/MCP, not an all-host universal plugin installer.
- Cross-agent tool permissions, private dependency fetching, hook enforcement and cost/context behaviour remain runtime-specific.

## Sources and evidence register

**Repository research / decisions:**
- [R1 — Cursor native primitives](01-cursor-primitives.md) — first-party activation, Rules/Skills/commands/subagents/hooks/MCP/Plugins.
- [R3 — fixed six-repository benchmark](03-reference-repo-benchmark.md) — Microsoft skill composition, Matt Pocock single skill source, Addy Osmani host adapters, Spec Kit generated integration.
- [R2 — harness vs agent vs skill/plugin](02-harness-agent-skill-plugin.md) — roles vs packaging.
- [R4 PR #23 — cross-repository composition](https://github.com/GitKlink/performance-reward-dashboard-architect/pull/23) — local Cursor multi-root vs cloud/CI/single-root limitations. **Not merged at snapshot.**
- [ADR-0001 — standards authority](../../docs/decisions/0001-canonical-standards-home.md) — decision accepted and migrated.
- [#14 R7 research ticket](https://github.com/GitKlink/performance-reward-dashboard-architect/issues/14).

**Current first-party / open specifications checked 19 October 2026:**
- [Agent Skills specification](https://agentskills.io/specification) — SKILL.md required fields and portable content contract.
- [Cursor Rules](https://cursor.com/docs/rules), [Cursor Skills](https://cursor.com/help/customization/skills), [Cursor Plugins](https://cursor.com/docs/plugins), [Cursor Plugin reference](https://prod.cursor.com/docs/reference/plugins) — native and open/plugin subset.
- [Codex project instruction hierarchy](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [Codex skills](https://learn.chatgpt.com/docs/build-skills), [Codex MCP](https://developers.openai.com/codex/mcp).
- [Claude Code memory and AGENTS.md](https://code.claude.com/docs/en/memory), [Claude Code Skills](https://code.claude.com/docs/en/skills), [subagents](https://code.claude.com/docs/en/sub-agents), [hooks](https://code.claude.com/docs/en/hooks), [plugins](https://code.claude.com/docs/en/plugins), [MCP](https://code.claude.com/docs/en/mcp).
- [MCP spec](https://modelcontextprotocol.io/specification/) — shared protocol layer, not shared host installation.
- [GitHub Copilot support matrix](https://docs.github.com/en/copilot/reference/custom-instructions-support), [Copilot Agent Skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills) — optional fourth-host evidence.

**Research integrity:** current feature support is backed by first-party docs; the proposed Architect adapter arrangement and support tiers are **design recommendations**. No Codex/Cursor/Claude installation, live multi-host execution, PBIP model validation, private authentication test or plugin packaging integration test was performed. Do not turn this R7 report into an implementation-complete claim.
