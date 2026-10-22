# R8 — Target Architecture Synthesis for the Power BI/Fabric Architect

> **Terminology correction (2026-10-22):** The project is the **Power BI / Fabric Architect**. **Wayfinder** is Matt Pocock's planning skill used during research, not the project name. Original issue/PR titles may retain historical wording. The evidence and technical conclusions are unchanged. References to private standards describe the repository's earlier visibility; it became public on 2026-10-22.

**Research ticket:** [#17 — R8 synthesis](https://github.com/GitKlink/performance-reward-dashboard-architect/issues/17)  
**Synthesis date:** 2026-10-22  
**Status:** **PROPOSED TARGET DESIGN FOR REVIEW**. Not yet an approved architecture ADR, not proof of an installed product, and not a mandate to merge/ship every proposed component.  
**Inputs:** [R1](01-cursor-primitives.md) · [R2](02-harness-agent-skill-plugin.md) · [R3](03-reference-repo-benchmark.md) · [R4](04-cross-repo-composition.md) · [R5](05-installation-bootstrap.md) · [R6](06-standards-library-packaging.md) · [R7](07-cross-agent-portability.md).

**Prior normative decision that this report must not reopen:** [ADR-0001](../../docs/decisions/0001-canonical-standards-home.md) establishes `GitKlink/power-bi-fabric-standards` as the canonical engineering-policy home. [Architect Issue #5](https://github.com/GitKlink/performance-reward-dashboard-architect/issues/5) has already been closed. This R8 paper proposes the *implementation/composition* architecture that consumes that authority, not another home for standards.

The statements below use:
- **ESTABLISHED:** already accepted Architect authority boundary or a material documented product constraint.
- **RESEARCH-SUPPORTED:** recommended by a named R1–R7 research artifact but not adopted as production architecture.
- **PROPOSED:** concrete R8 design selection awaiting review/ADR.
- **UNVALIDATED:** requires a real tool, user-workstation, CI or PBIP test.

---

## 1. Executive architecture summary

### Decision proposed

**Build Architect as a Cursor-first, Power BI-focused, cross-repository *composed capability system*, hosted by an existing coding-agent runtime.** Do **not** build a new independent LLM/agent harness at this stage. Do **not** put all knowledge in one always-loaded prompt, or treat a Cursor Plugin as the complete architecture.

**First useful product slice:** a standards-aware **Power BI semantic-model measure review**, operating on a real PBIP/TMDL repository. It should read the approved naming standard and relevant domain/asset context, inspect existing measures, propose a safe refactor, and produce independent validation evidence. This is the acceptance test for the architecture, not a side demonstration.

### Core components

| Component | Job | Initial concrete approach | Why |
|---|---|---|---|
| **Architect / router** | Identify task, audience, domain, required standards, relevant skills and write destination | Concise host-neutral `AGENTS.md` plus small Cursor-specific routing Rule where needed | R1/R2/R7: keep permanent context and duplicated instructions small |
| **Procedural capabilities** | Steps for model discovery, semantic design, DAX review, M transformation, report UX and QA | Focused `SKILL.md` with progressive reference retrieval | R1/R3/R7: skill is a good reusable procedure, not full normative content |
| **Canonical engineering standards** | Rules and policy: naming, folders, DAX/M engineering, modelling, UX, conformance | **Private standards repo** at approved pinned revision | ADR-0001 and R6 correction |
| **Domain authority** | What Performance & Reward entities, populations and KPIs actually mean | Domain pack, initially co-located with Architect if practical | ADR-0001 / #6: business semantics separate from generic naming |
| **Reusable implementations** | DAX, M, Python, Deneb native patterns/functions/templates | Existing `dax-m-query-library`, indexed by stable IDs and pinned revisions | R6 correction: not obligatorily wrapped in JS/npm |
| **Platform execution** | Power BI/Fabric operations and compatible model checks | Prefer **Microsoft-maintained skills and existing tools**, augment with our policy | #4/R3 delegate first, fork only if needed |
| **Product execution** | Real analytical output, model and report code | PBIP repository owns edits, tests, local config and result | R4 write authority |
| **Dependency/installer layer** | Get approved source versions and host adapters into a supported environment | Phase-0 manual local composition; small Python `doctor/plan/apply/verify` candidate after pilot | R4/R5: local multi-root useful; installed dependency lock independent of workspace |
| **Evidence and validation** | Prove what was read and whether output conforms | Deterministic checks and traceable source revisions, with model/reconciliation tests where feasible | R2/R4/R5/R7: agent assertion is not enforcement |

### What R8 recommends *not* building yet

- A custom autonomous harness, model router or chat runtime.
- A full Cursor/Claude/Codex plugin marketplace, or a general-purpose enterprise analytics platform.
- npm packages containing every DAX measure/M function/Deneb template.
- An always-loaded copy of the complete engineering standard or P&R business glossary.
- A single monorepo that merges independent authority repositories.
- A production Cloud Agent deployment before private access and single-root checks succeed.
- Auto-editing an EOY/pay/HR report without domain reconciliation and explicit change approval.

### Launchable milestone

The **smallest end-to-end pilot** must, on a fixture PBIP repo with synthetic data:
1. resolve a specific approved revision of standards and library;
2. load the measure-standard core, glossary and the applicable domain-specific representation;
3. obtain the actual domain meaning from an approved domain contract;
4. inspect measure names, descriptions, format strings, folders, DAX and dependencies;
5. propose changes **only in PBIP** (do not automatically modify the canonical references);
6. independently check naming, metadata completeness and mathematical equivalence where relevant;
7. emit the exact source versions, findings and pass/fail evidence.

**Milestone acceptance is conditional:** no demo or command has been executed as part of this R8 research.

## 2. Research findings consumed

| Research source | Durable finding used | R8 consequence | Caveat |
|---|---|---|---|
| [R1 — Cursor primitives](01-cursor-primitives.md), §§2, 4–13 | Instructions, Skills, agents, hooks, MCP, plugins and ordinary docs have different loading/roles; full standards do not belong in persistent Rules | Small routing instructions + progressively loaded Skills + canonical reference docs | Exact discovery and precedence need installed-build tests |
| [R2 — architecture classification](02-harness-agent-skill-plugin.md), executive finding / vocabulary / recommendation | Architect is an orchestration role; Cursor owns core agent execution loop; plugin is distribution, not runtime | Compose capabilities in existing host, do not build custom harness | Future needs could change this |
| [R3 — reference benchmark](03-reference-repo-benchmark.md), §§14–20 | Spec Kit shows managed bootstrap lifecycle; Matt distinguishes managed/editable; Addy uses host adapters; Microsoft composes skills/MCP | Single canonical source, thin host adapters, careful managed state | Reference repositories are examples, not a complete Architect installer |
| [R4 — repo composition](04-cross-repo-composition.md), §§3–10 | Side-by-side independent clones + Cursor multi-root are good locally; Cloud Agent multi-root unsupported; dependency pins separate from editor view | Local multi-root **pilot** and explicit single-root cloud path | Multi-root Rule activation and private auth must be tested |
| [R5 — bootstrap](05-installation-bootstrap.md), §§2–10 | Manual pilot before a lightweight pinned resolver; clear ownership, idempotence, rollback and no silent updates | Phase-0 runbook; Python-based `doctor/plan/apply/verify` implementation candidate | No actual installer exists yet |
| [R6 — standards/library packaging](06-standards-library-packaging.md), §§1, 18, **20** | One canonical source; stable asset IDs; **native DAX/M/Python/Deneb** first; npm/ESM only when a genuine JS/TS API exists | Git-pinned standards and native library retrieval with catalogue/compatibility metadata | September npm-first executive claims are superseded by October domain-fit correction |
| [R7 — cross-agent portability](07-cross-agent-portability.md), §§2–9 | Portable docs, compact `AGENTS.md`, open `SKILL.md` and host-neutral evidence can coexist with native host adapters | Cursor first; Codex/Claude adapters later; supported capability tiers | Format portability does not guarantee discovery, tools or results |

**Synthesis discipline:** R8 consumes the seven artifacts as **research**; nothing in this table upgrades their candidate implementation choices into existing code or an approved normative standard. This report identifies the package of decisions that a subsequent review/ADR should accept, revise or reject.

## 3. Target component model

### Logical, not physical, architecture

~~~text
USER / ANALYTICAL QUESTION / PBIP PROJECT
                  |
                  v
     HOST RUNTIME (Cursor first)
     | Agent loop + tool permissions
     | rules / AGENTS.md / skills
                  |
                  v
      WAYFINDER ARCHITECT ROUTER
     /   Task + write-root discovery
    /    Dependency/version resolution
   /     Skill and domain selection
  v
+------------------+     +----------------------------+
| Procedure Skill  |---->| MS POWER BI / FABRIC SKILLS|
| (bounded workflow|     | platform execution/review  |
|  & references)   |     +----------------------------+
+---------+--------+
          |
          v
+-------------------------------+
| PINNED CANONICAL REFERENCES   |
| Standards  +  Domain pack     |
| Library asset catalogue      |
+-------------------------------+
          |
          v
       PBIP/TMDL
    project-local edits
          |
          v
   VALIDATOR + QA EVIDENCE
          |
          v
  REVIEW / HUMAN APPROVAL / PR
~~~

The diagram does **not** imply that Architect is a new external process orchestrating every host. The first orchestration layer may live as the coding agent's active skill plus project instructions, with deterministic scripts and tools around it. R2 specifically distinguishes that from owning an agent harness.

### Ownership boundaries and their enforcement implications

| Authority | What it decides | What it may generate/execute | What it **must not** overwrite silently |
|---|---|---|---|
| Architect | Workflow choices, loading route, acceptance contract, recommended tools | Small host adapters, candidate project plan, validation orchestration | Normative engineering standards, P&R KPI truth |
| Engineering standards | Generic Power BI-focused policy; schema/metadata conventions | Conformance specifications and examples | Business definition or specific project data |
| P&R domain pack | KPI definition, grain, eligibility, reporting periods, meaning, interpretations, reconciliations | Domain checks/contracts/fixtures | Generic technical engineering grammar |
| DAX/M library | Reusable native executable implementations, dependencies and examples | Approved patterns/UDFs/M functions/scripts, tests | Generic standards or product-specific KPI ownership |
| PBIP project | Actual model/report content, local accepted exceptions | Project-side change, test output, documentation, PR | Upstream authorities |
| Microsoft capabilities | Platform-specific tool-supported operations and QA mechanics | Inspections, model changes where authorised, technical validations | Business semantics or Architect-specific governance |

**Conflict handling:** domain meaning overrides a *guess* made from folder names. A true conflict between domain contract and generic policy becomes an explicit exception or upstream issue. An installer cannot settle it by copying one source over another.

### Capability roles (proposed initial set)

- **semantic-model-review** — inspect model/TMDL and measure navigation, naming, descriptions, format strings, visibility, dependencies, required contextual docs.
- **dax-engineering** — evaluate expression/UDF correctness, performance and compatible library patterns, preserving business meaning.
- **power-query-engineering** — identify source/staging transformations, M logic, refresh/grain/dataflow assumptions.
- **domain-analysis** — choose P&R analytical contract, eligible population, date basis and reconciliation tests.
- **report-experience-review** — audience-specific Power BI report information design and presentation.
- **quality-evidence** — run deterministic checks and produce source-linked acceptance record.

Only the first and quality-evidence subset are required for the initial pilot. Microsoft skills should perform supported generic tasks; avoid creating duplicate platform-expert instructions merely to fill this list.

## 4. Asset-placement map

**Proposed physical files/directories** are illustrative implementation targets **after R8 review**; their creation is not claimed.

| Asset | Proposed physical home | Activation/use | Owns |
|---|---|---|---|
| Accepted repo authority ADR | Architect `docs/decisions/0001-canonical-standards-home.md` (**exists**) | Referenced by architect docs | Physical standards home |
| Thin project router | PBIP `AGENTS.md` (generated/adapted only with approval) | Host project instructions | Project write-scope, dependency route |
| Core architect instructions | Architect `AGENTS.md` / ordinary architecture docs | Host instruction when relevant | General orchestration invariants only |
| Cursor-specific project rule | Architect or PBIP `.cursor/rules/semantic-model-review.mdc` | Scoped/intelligent routing | Trigger and pointer, not copied standard |
| Portable semantic review Skill | Architect `.agents/skills/semantic-model-review/SKILL.md` | On-demand discovery/explicit invocation | Procedure, required evidence and missing-input failure |
| Supporting skill references/scripts | Beside SKILL.md under `references/`, `scripts/` | Loaded on demand | Workflow support only |
| Power BI engineering standard | Private standards repo `semantic-model/semantic_measure_standard.md` (**exists**) | Pinned, explicit read | Normative model/measure conventions |
| Glossary and domain representation | Private standards repo `semantic-model/business_glossary.md`, `semantic-model/domains/…` (**exist**) | Task-selected references | Current migrated representation content, pending ownership classification |
| P&R KPI / lifecycle contracts | Architect domain pack initially, `domains/performance-reward/` candidate | Domain-selected read | Business meaning and test expectations |
| Native DAX/M/Python/Deneb patterns | `dax-m-query-library/library/{dax,m,python,deneb}/` (**exist**) | Versioned source or catalogue reference | Reusable implementation |
| Asset metadata catalogue | Library; e.g. `catalogue/` or generated index (new; TBD) | Query by asset ID, language, compatibility | Find real source; no executable wrapper required |
| Project dependency lock | PBIP repo `power-bi-architect.lock.json` candidate | Deterministic resolver/doctor | Approved revisions for this product |
| Bootstrap tool | Architect `tools/bootstrap/` or script package, TBD | Explicit `doctor/plan/apply/verify` | Reversible local composition |
| Eval fixture/validators | Architect `evaluations/` + owner-specific tests | Without model prompt where possible | Independent evidence against source revisions |
| Generated workspace | User-local `*.code-workspace` | Cursor local IDE | View over separate repos; not source authority |
| Host adapters | Architect `adapters/cursor/`, then `adapters/codex/`, `adapters/claude/` | Installed only where host supports them | Host-specific syntax/permissions |

**Avoid premature empty folders:** create these assets only as part of a scoped first pilot and approved follow-on tickets. Do not transplant the entire existing semantic standards pack into Architect.

## 5. Repository/topology model

### Accepted repositories today

~~~text
GitKlink/
  performance-reward-dashboard-architect/  [Architect; public; source of orchestration/research]
  power-bi-fabric-standards/                [engineering policy; PRIVATE]
  dax-m-query-library/                     [public native implementation asset library]
  <real-product>.pbip                       [example *consumer*; do not assume exists]
~~~

Current `main` includes [R1–R7](README.md); the seven R-research files are evidence rather than installation assets. Standards README/core/glossary/domain extension originals were copied into the standards authority without semantic edits; do not rewrite them during bootstrap.

**Important access constraint:** a public Architect repo and private standards repo may be viewed by different identities and CI runners. A link in a public file does not grant access; a private source file must not be imported into a public package, Actions log or tool trace without authorisation.

### Local developer composition proposal

~~~text
analytics-work/                             (user-selected parent; conceptual)
  my-analytical-product/                    (primary write owner)
  performance-reward-dashboard-architect/  (reference unless explicitly developing it)
  power-bi-fabric-standards/                (private canonical policy)
  dax-m-query-library/                     (approved implementation assets)
  product-local.code-workspace              (generated editor view)
  .power-bi-architect-state/                         (local, ignored, generated provenance)
~~~

**Why sibling repositories:** preserve independent Git history, private access control, PR workflow and product-specific revisions. **Why multi-root:** direct local Cursor visibility without vendoring source. **Limitations:** Cursor Cloud Agents do not currently consume multi-root workspaces, and some Cursor worktree behaviour is disabled for multi-root sessions (R4). A workspace file is **not** proof of version pinning or standards application.

**Git submodules and vendoring:** remain conditional alternatives for a demonstrated single-root/offline/build constraint; do not make them default. A public checked-in subtree containing private standards is unacceptable.

### Project contract and versioning candidate

Separate three things:

1. **Logical dependency declaration** — IDs/owners/classes and how to resolve them.
2. **Approved immutable revision lock** — which exact Git SHA/artifact revision the product must use.
3. **Observed local install state** — what files and host adapters were actually materialised, their hashes and whether modified.

**Schema v0 sketch (illustrative, not yet accepted):**

~~~json
{
  "schemaVersion": "power-bi-architect-proposal-0",
  "productId": "sample-reward-pbip",
  "writeRoot": ".",
  "dependencies": [
    {
      "id": "engineering-standards",
      "repo": "GitKlink/power-bi-fabric-standards",
      "revision": "<exact-approved-40-character-sha>",
      "source": "semantic-model/README.md",
      "authority": "engineering-policy",
      "writePolicy": "reference"
    },
    {
      "id": "architect",
      "repo": "GitKlink/performance-reward-dashboard-architect",
      "revision": "<exact-approved-40-character-sha>",
      "authority": "orchestration",
      "writePolicy": "reference"
    },
    {
      "id": "reusable-assets",
      "repo": "GitKlink/dax-m-query-library",
      "revision": "<exact-approved-40-character-sha>",
      "authority": "implementation-library",
      "writePolicy": "reference"
    }
  ]
}
~~~

The above contains **placeholders, not valid runnable SHAs**, and must not be committed as a working lock without resolved values. Do not put tokens, user machine paths, secret URLs, employee data or private content in a checked-in manifest.

A domain contract entry must be added once the #6 authority split and domain pack packaging are approved. The initial pilot can treat its domain definition as an explicit approved input rather than inventing a domain location.

## 6. Runtime/context-loading flow

### Proposed request resolution procedure

1. **Identify task and target:** Which PBIP repository, which model/report, which business domain, and which repo is allowed to receive edits?
2. **Resolve source IDs and revisions:** Check manifest/approved pins. Confirm the exact standards and library SHA actually accessible in this environment. Private auth failure halts task, not "best effort" generic advice labelled compliant.
3. **Load minimal always-on context:** Compact project AGENTS.md or host router. Do not inject all standard/domain/reference files.
4. **Select capability:** Use the semantic-model-review Skill for a measure refactor; delegate generic platform tasks to installed Microsoft-maintained Power BI/Fabric Skill(s) where capability is available; explain unsupported operations.
5. **Load normative context on demand:** Canonical measure standard, glossary, relevant domain representation and *separate domain-owned KPI contract*. Record exact path/revision used. Do not treat the backlog as an approved standard.
6. **Inspect live target:** For PBIP/TMDL inspect actual source/metadata. If model is only accessible via Desktop or live XMLA, use available authorised tools. Never assume model metadata from a screenshot or measure name alone.
7. **Plan changes:** Distinguish cosmetic metadata/naming changes from semantic/expression changes; preserve dependencies and business basis. Mark proposed edits, risks, and required human decisions.
8. **Execute within write owner:** Apply only approved changes to the PBIP project. Changes to canonical upstream policy or library require their own PRs.
9. **Run independent checks:** Static naming/metadata/visibility/folder checks; model/parse tests if available; numerical before/after reconciliation for expression or business-logic changes.
10. **Report evidence:** Source revision, asset ID, domain contract, input model revision, validator version, pass/fail, exceptions and any unresolved checks. A conversational claim that the rule was obeyed is insufficient.

### Context-economics decision

| When | Load | Do **not** load |
|---|---|---|
| Agent starts a generic task | Thin project instructions / capability descriptions | Full salary/rating/variable-pay standards |
| Semantic-model task selected | Relevant Skill plus pinned core standard entrypoint | Every unused technical or domain standard |
| Domain determined | Only its needed meaning/representation files | Other domain packs |
| Implementation pattern required | Relevant native library asset, dependencies and tests | Whole implementation library |
| Validation | Necessary checks/fixtures and bounded evidence | Entire repository in one prompt |

R1's distinction between model context, filesystem/search and MCP/tool payload still applies. Model-supported reading is not a deterministic access-control or version validation mechanism.

### Discovery contracts

**Suggested minimum normative-standard record** (schema to be approved): stable `standard_id`, authority, status (normative/guidance/backlog), applicability, version/source SHA, entrypoint path, owner and declared dependencies.

**Suggested reusable asset record:** stable `asset_id`, language/native format, source SHA/path, intended grain/context, parameters, required model/engine compatibility, dependencies, examples, tests and licence.

**Critical distinction:** the catalogue helps find and verify source; it does not replace source or automatically transform a DAX measure into a portable npm module.

## 7. Installation/bootstrap flow

### Phase 0 — pilot without installer (first gate)

The first product slice can be run with documented independent Git checkouts and a hand-authored .code-workspace. Capture exact source SHAs and prove the measure-review workflow **before** designing a general installer.

**Minimum tests:** a local Cursor session opens the correct standard, reads the correct domain contract and source, limits writes to PBIP and yields deterministic pass/fail. Negative tests remove private standards access or put a wrong SHA in the manifest.

### Phase 1 — proposed small Python bootstrapper

A *candidate* lightweight tool, not a finished CLI:

~~~text
power-bi-architect doctor           # check Git/Python/host, repo visibility/access, permissions, project
power-bi-architect plan             # show desired vs observed source versions and proposed managed writes
power-bi-architect apply            # resolve exact approved refs and generate local workspace/adapters safely
power-bi-architect verify           # compare SHA/digests, validate entrypoints and fixture test
power-bi-architect update --check   # report options; do not update implicitly
power-bi-architect uninstall        # remove only hash-verified installer-managed artifacts
~~~

Required constraints:

- No automatic switching to default-branch HEAD when an approved SHA is unavailable.
- No silent installation of hooks, MCP servers, unknown third-party executables or user-global config.
- No overwrite of modified AGENTS.md/CLAUDE.md or user's PBIP/project work.
- Managed installation and editable contributor checkouts must not claim to own the same capability simultaneously.
- Explicit auth preflight for private standards; credentials must stay outside project manifests/logs.
- A rerun with unchanged approved inputs must create **no diff**.
- Store local state/hashes separately from project-declared desired versions.
- Support atomic or journaled file creation and rollback for managed paths.
- Run deterministic tests without requiring an AI prompt.

This is a **post-pilot implementation candidate**, not a decision that all teammates must install Python packages or GitHub CLI immediately.

### Phase 2 — repeatable teams and cross-agent adapters

Deliver a validated managed consumer mode distinct from editable development. Host adapters for Cursor first; Codex and Claude only as test-driven follow-ons. Capture capability registry, install-source provenance, duplicate installation detection, and versioned assets/skill references. Do not copy private normative content into public project scaffolding.

### Phase 3 — Cloud/CI

Choose a **single-root** or authenticated read-through source mechanism independent of Cursor multi-root. The source must be pinned and accessible with narrowly scoped credentials. GitHub's normal checkout token is repo-scoped; reading another private repo in CI requires dedicated permission. Cloud/CI pass only if leakage, resolution, model inspection and validation tests pass. **Unvalidated:** the chosen Cloud Agent private-repo mechanism.

### Phase exit gates

| Gate | Outcome | Key evidence |
|---|---|---|
| G0 | Real local PBIP fixture reviewed via pinned standards | References read, diff scope, validator outputs and unresolved defects |
| G1 | Reproducible local bootstrap | Idempotent plan/apply, wrong SHA/auth fail closed, rollback, user-edit preservation |
| G2 | Multi-project/team consumption | Per-component managed/editable state, controlled upgrades, no duplicate skills |
| G3 | Remote/CI support | Exact source resolution, scoped secrets, no private leaks, matching conformance evidence |
| G4 | Optional packaged plugin | Demonstrated user/deployment benefit beyond skills/CLI; host validation |

No G0–G4 acceptance gate has been executed as part of R8.

## 8. Version/update model

### Source and state identities

Do not collapse all of these into one version:

- Architect orchestrator and its approved Skill revision.
- Canonical engineering standard revision/approval state.
- P&R domain contract revision.
- Native implementation asset/library revision.
- Bootstrap/host adapter generator version.
- Host runtime/tool version.
- PBIP project commit and current dirty state.
- Test/evaluation revision and last validated result.

**Initial policy:** Git full SHA **pin for a PBIP project's declared authoritative dependencies**. Human-friendly tags and SemVer are optional later if they improve release/adoption; especially for standards, normative compatibility is not identical to source diff or API signature compatibility (R6).

### Adoption and update

1. Source owner creates/reviews its change in its **own repository**.
2. New revision is available; **no downstream project automatically adopts it**.
3. A consumer opens a **dependency update PR** changing its project lock/approved revision, with expected semantic impact described.
4. Resolver materialises new dependency in a staging context, verifies hashes and manifests; test suite runs against the PBIP project.
5. Approve on evidence; record new last-validated source set. Rollback means returning to the prior approved lock + managed state.
6. If a standards change makes existing models nonconformant, document it as a breaking adoption event even if no executable package changed.

**Anti-patterns:** floating default branches in production conformance runs, runtime substituting newer library code without audit, a plugin reinstall silently upgrading authoritative standards, treating a syntax-valid DAX function as business correct, or running private source publishing through an unreviewed public release automation.

### Concrete evidence record sketch

~~~json
{
  "schemaVersion": "power-bi-architect-evidence-proposal-0",
  "projectCommit": "<actual-project-commit>",
  "projectDirty": false,
  "standardsRevision": "<approved-git-commit>",
  "domainRevision": "<approved-domain-commit>",
  "implementationLibraryRevision": "<approved-library-commit>",
  "capabilityId": "semantic-model-review",
  "validatorVersion": "<test-suite-version>",
  "checks": [
    {"id": "naming", "status": "pass"},
    {"id": "business-reconciliation", "status": "not-run", "reason": "no numerical change"}
  ],
  "outcome": "incomplete-until-required-gates-pass"
}
~~~

This is an illustrative report shape, not yet a committed JSON Schema. A rejected/missing private source must produce a hard failure and no false completed verdict.

## 9. Cross-agent portability model

**Policy:** preserve a **portable core with native host adapters**, not lowest-common-denominator capability.

| Capability | Cursor-first | Codex | Claude Code | Portability status |
|---|---|---|---|---|
| Canonical Markdown standards (pinned read) | Repo source/tool | Repo source/tool | Repo source/tool | Content portable; access still environment-specific |
| Compact AGENTS.md router | Native project instructions | Native project instructions | Recent native support subject to version/config/CLAUDE.md precedence | Shared intent; activation needs host test |
| Portable SKILL.md procedure | Project Skill | Project Skill | Host Skill path or adapter | Shared workflow body; triggers/tool permissions host-specific |
| Model inspection | Microsoft/native tools where available | Tool adapter required | Tool adapter required | Must test actually accessible tools |
| Cursor .mdc Rules/globs | Native | No equivalent syntax guarantee | No equivalent syntax guarantee | Host-only convenience |
| Hook/subagent lifecycle | Native Cursor capabilities | Host-specific | Host-specific | Optional; no hard common dependency |
| MCP protocol | Host-supported tools/services | Host-supported with config | Host-supported with config | Protocol portable, install/auth not guaranteed |
| Source/validation contract | Git SHA, catalogue, independent tests | Same | Same | Primary conformance contract |

**Minimum supported surface:** one semantic-model measure review with the same approved source/contract and *independent validation output*; require installed host permissions and valid model access. Mark unsupported features rather than replacing them with unverifiable generic advice.

**Default rollout:**
1. Cursor local (Tier 1 only when G0/G1 tests pass).
2. Codex with same docs and Skill, test actual tool capabilities and outputs.
3. Claude Code, respecting its AGENTS/CLAUDE precedence and project Skill loading.
4. GitHub Copilot/others only when there is a concrete consumer need.

A Cursor-only subagent or hook should not be deleted solely to make the other hosts identical, but **critical correctness checks** must not depend only on that feature. They belong in independent validators or approval gates.

## 10. Example end-to-end task flow — Variable Reward measure review

**Scenario:** review a Power BI year-end Variable Reward semantic model for naming, description, folders, metadata and meaning, without changing calculation outcomes.

### Inputs and permissions

- PBIP project checkout with synthetic fixture or authorised real dataset.
- Read permission to pinned private engineering standards.
- Read permission to approved P&R domain definitions/contract.
- Read permission to optional reusable DAX assets in library.
- Write permission to **PBIP only** for the actual refactor.
- Model inspection/validation tool access; if absent, report that limitation rather than hallucinating results.

### Execution trace

| Step | Architect/action | Expected evidence |
|---|---|---|
| 1 — Identify work | Determine project/semantic-model root, write-owner repo and task scope | PBIP path, Git commit/dirty state |
| 2 — Resolve authorities | Load approved SHA for standards, domain and optional library | SHA/path/access check results |
| 3 — Read generic standards | Retrieve `semantic_model` measure naming, metadata, glossary rules | Exact file references and normative status |
| 4 — Read domain meaning | Read the P&R contract for VR target opportunity, payout, overall rating and IPM basis | Domain-defined grain, eligibility, effective dates, currency/rating meaning |
| 5 — Inspect model | Enumerate measures, DAX, dependencies, formatting, descriptions, hidden state and folders | Actual extracted metadata table, not inferred labels |
| 6 — Classify gaps | Flag inconsistent root-first naming, technical prefixes, missing description, unsupported measures and ambiguous family placement | Deterministic rule references and affected measures |
| 7 — Propose refactor | Produce before→after names/folders/descriptions and impact on references; separate semantic changes | Previewable diff and dependency impact |
| 8 — Human control | Approve proposed edits, especially domain meaning, visibility and ambiguous renamed measures | Approval/review record, not implicit consent from a tool running |
| 9 — Apply/validate | Update PBIP/TMDL project, compile/reload if possible, run before/after numerical comparisons where applicable | Validator/test outputs with version provenance |
| 10 — Deliver | PBIP-only PR and concise conform/nonconform report | Changed paths, test results, unresolved exceptions |

**Metric example:** `Variable Reward Payout`, `Variable Reward Payout Average` and `Variable Reward Payout Change %` are only *illustrative naming forms*, **not approved business definitions** or a claim that any actual production model uses them. The domain contract must define whether "payout" refers to an employee amount, plan spend, or another grain and whether the relevant percentages represent IPM, opportunity or spend-to-target. The generic standard cannot determine that meaning by itself.

### Acceptance checks for first pilot

- Detect a deliberate naming violation and show the correct applicable standard/version.
- Reject an attempted edit to the standards/library read-only roots.
- Preserve reference integrity after an approved measure rename.
- Report a business-contract ambiguity rather than invent a KPI definition.
- Catch a standards SHA mismatch and private-repo access loss.
- Run a non-AI conformance checker and preserve machine-readable evidence.
- Ensure synthetic pay/rating fixtures do not disclose actual workforce information.
- Confirm the PBIP model actually loads/validates before claiming deployment-ready.

## 11. Risks and trade-offs

| Risk/trade-off | Why it matters | Mitigation / decision gate |
|---|---|---|
| Multi-root good locally, not cloud | Cursor Cloud Agents cannot use the same workspace | G3 separate single-root/authenticated resolver |
| Canonical repository is private, Architect public | CI and agent tools can see different sources; leakage risk | Access preflight, scoped permissions, no copied full standards in public outputs |
| Rules/Skills are nondeterministic in application | File exists but model may not load correct content | Mandatory source read evidence + independent checks |
| Monorepo simplicity vs authority | Collapsing repos blurs business/engineering/code ownership | Keep repos separate; manifest identifies source |
| Packaging overreach | npm/ESM unfit as universal wrapper for native DAX/M/Deneb | Follow R6 §20 native-first correction |
| Bespoke installer complexity | Rollback, idempotence, paths, auth and team tooling cost | Pilot first, small Python scope, explicit delivery gate |
| Copying private standards into plugin | Marketplace/update ease at price of confidentiality/drift | Thin adapters referencing canonical pinned text only |
| Existing domain standards contain business semantics | Duplicate meaning could drift with domain pack | Resolve #6 before general domain refactor; preserve original migration |
| Tool/version drift | TMDL/model format, UDF support, API rights vary | Compatibility metadata, parse/load tests, runtime matrix |
| Regression in pay outcomes | Incorrect population/rating/IPM can have material consequences | Domain reconciliation, synthetic fixtures, review approval |
| Excess context | Large standards/glossary packs consume tokens and distract model | Progressive core + selected domain retrieval |
| Weak provenance | "AI followed standard" is not auditable | Evidence contract records exact SHA, tests, model revision |
| R6 research reversal | September JS/npm baseline conflicts with native library | Explicit R6 §20 supersession; do not mechanically reapply original advice |
| Premature cross-agent parity | Codex/Claude have differing hooks, permissions, tool access | Support tiers, adapters and host-specific tests |
| Overdesign | Building multiple agents/plugins before one accepted analytic product | Single vertical slice and measurable exit gates |

**Cost rationale:** For a small embedded Power BI team using Python, Dataflows and Cursor, the lightest sufficient runtime is the existing host plus a small number of Skills and deterministic checks. A separate runtime, package registry and full installer are costly before the first product workflow proves value.

## 12. Decisions ready for Architect #5 / follow-on ADR

### Clarification: #5 is **already settled**

At ticket creation, #17 was expected to feed a still-open standards-home decision #5. As of this synthesis, **#5 is closed** and ADR-0001 has already established the separate canonical standards repository. **Do not reopen that physical-home decision.**

R8's next normative work is an **implementation/target-architecture ADR in Architect**, not a change to existing standards authority. The following choices are ready for review:

| ID | Proposed implementation choice | Basis | Status |
|---|---|---|---|
| A1 | Composed Cursor-first capability system hosted by Cursor, not bespoke harness | R1/R2/R3 | **Proposed** |
| A2 | Focused skills + thin instructions, canonical reference loading on demand | R1/R3/R7 | **Proposed** |
| A3 | Independent authority repos, PBIP primary write target | ADR-0001/R4 | **Proposed implementation of established authority** |
| A4 | Local sibling clones + multi-root **as phase-0 developer UX** | R4/R5 | **Proposed, requires pilot** |
| A5 | Immutable per-project dependency pins and separate installed-state provenance | R4/R5/R6/R7 | **Proposed** |
| A6 | Native DAX/M/Python/Deneb catalogue; no mandatory JS wrapper/npm | R6 §20 + actual repos | **Proposed correction to R6's earlier default** |
| A7 | Small Python doctor/plan/apply/verify **only after G0 pilot** | R5 | **Proposed conditional** |
| A8 | Cursor-specific convenience adapters, host-independent validation and later Codex/Claude | R7 | **Proposed** |
| A9 | Delegate generic Power BI/Fabric platform mechanics to Microsoft skills when suitable | #4/R3 | **Already agreed principle; implementation untested** |
| A10 | Single-root Cloud/CI is a separate later test/deployment design | R4/R5 | **Required constraint; implementation undecided** |

### Recommended decision sequence

1. Review/merge the R8 *research* PR. Do not conflate this with approving every row A1–A10.
2. Write a **target-architecture ADR** explicitly accepting/revising the proposed choices, with any required risk/security sign-off.
3. Resolve or narrow [#6](https://github.com/GitKlink/performance-reward-dashboard-architect/issues/6) domain/semantic-representation authority for the first Variable Reward pilot.
4. Open a **small bounded G0 pilot implementation ticket**; only then create Skills/adapters/fixtures and perform actual Cursor/PBIP evaluation.
5. Let measured pilot failure modes dictate whether the first bootstrap tool is justified.

The canonical standards home and 11-file migration are already completed; do not block the G0 pilot on redoing them.

### Candidate implementation backlog **after architecture approval**

| Order | Proposed ticket | Definition of done | Depends on |
|---|---|---|---|
| I1 | Pilot product/fixture and conformance-contract selection | Synthetic PBIP/TMDL fixture, naming/domain violations, expected model outputs and tests documented | ADR scope + domain minimum |
| I2 | Pinned source manifest prototype and source resolver | Correct access/SHAs reported; missing private access or wrong SHA fail closed | I1 |
| I3 | Portable semantic-model-review Skill and thin Cursor router | Loads actual pinned standard/glossary/domain context; no normative duplication | I1–I2 |
| I4 | Independent naming/metadata validator and evidence report | Expected violations detected and post-change conformance measured | I1–I3 |
| I5 | End-to-end Cursor PBIP pilot | PBIP-only diff, model reload/compile, reconciled outcomes, no source leaks | I1–I4 |
| I6 | Reversible Python bootstrap prototype | Idempotent, safe managed writes, drift reporting, rollback test | I5 + R5 gate |
| I7 | Codex/Claude adaptation and cloud/CI option assessment | Same fixture/validation evidence; host tier stated; private auth approved | I5 or I6 |
| I8 | Release/catalogue governance | Native asset IDs, versioning and deprecation policy reviewed | I5 + R6 and #6 |

**These are backlog proposals, not existing GitHub issues and not implemented deliverables.** Ticket creation should follow review of the R8 ADR.

## 13. Remaining unknowns, future research and handoffs

### Must be tested before a production support claim

1. Installed Cursor version: multi-root Skill/Rule discovery, file-pattern triggers, multi-root git/worktree interaction.
2. Private standards authentication for the actual team workstation(s), each target coding agent, Cursor Cloud and CI.
3. Which Microsoft-maintained Power BI/Fabric Skills can inspect/validate the model under our permissions/tool environment, and which gaps genuinely require local skill/script code.
4. Minimum model-inspection route for PBIP/TMDL, DAX UDFs, XMLA/live models and Power Query M, including compatible Desktop/model versions.
5. Whether a Python installer is permitted by workplace device policy and whether users value it over a one-page manual runbook.
6. What test fixture may be committed publicly; never use actual employee, performance or reward data.
7. The domain authority split in #6, especially how approved Variable Reward eligibility, IPM, payout and KPI contracts are stored.
8. Whether the native asset library needs a curated manifest, explicit released bundles, per-asset versions or tooling such as a Python package — avoid designing a universal npm registry from a JavaScript-focused sample.
9. Standards normative-version/change-control process and any organisation-specific review approvals.
10. Cross-agent capability/discovery/permission parity only as far as supported by test evidence, not file extension.
11. End-to-end error recovery, auth/credential expiry, logs and privacy controls for remote execution.
12. Deterministic validation limits: some semantic correctness/reconciliation checks require the Power BI engine or authorised live dataset access; a text-only parser cannot prove all behaviour.

### Follow-on handoffs

- **[Issue #6](https://github.com/GitKlink/performance-reward-dashboard-architect/issues/6):** map domain meaning versus semantic-model representation before changing migrated domain extensions.
- **[Issue #7](https://github.com/GitKlink/performance-reward-dashboard-architect/issues/7):** generic semantic taxonomy/extension rules when designing standard identifiers and novel domains.
- **[Issue #8](https://github.com/GitKlink/performance-reward-dashboard-architect/issues/8):** independently recover Power Query/M governance before an M-focused standards-enforcement capability.
- **R8 follow-on ADR:** accept the target implementation choices without changing ADR-0001.
- **G0 pilot:** produce real, repeatable evidence for one native PBIP measure workflow.
- **Microsoft platform recheck:** verify live platform capabilities and security restrictions before tool integration.

### Research-to-decision traceability and non-goals

| Future implementation question | Research evidence | Proposed review outcome |
|---|---|---|
| New harness or composed system? | R1, R2, R3 | Existing-host composed system |
| Which assets are Rules/Skills/docs? | R1, R3, R7 | Small router + selected Skills + canonical ordinary docs |
| Repo topology and local UX? | ADR-0001, R4 | Separate owners; sibling clones/local multi-root pilot |
| Standards/library loading and asset format? | R4, R6 §20, R7 | Immutable source pin + selected native-asset retrieval |
| Installer/lifecycle? | R3, R5 | Phase-0 pilot then small managed Python bootstrap candidate |
| Cloud/CI? | R4, R5 | Explicit separate single-root/authenticated plan and tests |
| Cursor vs Codex/Claude? | R1, R7 | Portable core, thin native adapters and capability tiers |
| Business interpretation vs semantic layout? | #6, R6, ADR-0001 | Split business authority from representation rules |

**Final research conclusion:** implement the **smallest useful composed Power BI workflow** using the already-owned repositories before investing in a broad agent/plugin/installer framework. Keep engineering policy canonical, P&R business meaning domain-owned, reusable native implementation assets independent, PBIP changes local and validation observable. The R8 artifact is a synthesis proposal ready for design review, not a claim that the architecture has already been deployed.

---

## Sources

**Primary in-repository evidence:**

- [R1 — Cursor native architecture primitives](01-cursor-primitives.md)
- [R2 — Harness vs agent vs skill vs plugin](02-harness-agent-skill-plugin.md)
- [R3 — Six reference implementation benchmark](03-reference-repo-benchmark.md)
- [R4 — Cross-repository composition](04-cross-repo-composition.md)
- [R5 — Installation/bootstrap architecture](05-installation-bootstrap.md)
- [R6 — Standards and reusable-library packaging](06-standards-library-packaging.md), including **§20 native Power BI correction**
- [R7 — Cross-agent portability](07-cross-agent-portability.md)
- [ADR-0001 — Canonical standards home](../../docs/decisions/0001-canonical-standards-home.md)

**Relevant platform references:**

- [Microsoft PBIP projects](https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-overview)
- [Power BI semantic-model project files](https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-dataset/)
- [Microsoft DAX UDF support and constraints](https://learn.microsoft.com/en-us/dax/best-practices/dax-user-defined-functions)
- [TMDL View](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-tmdl-view)
- [Cursor Rules](https://cursor.com/docs/rules), [Skills](https://cursor.com/docs/skills), [Search / multi-root constraints](https://cursor.com/docs/agent/tools/search)
- [Agent Skills specification](https://agentskills.io/specification)
- [GitHub Spec Kit](https://github.com/github/spec-kit) — managed/bootstrap pattern reference, not a required dependency.

**Research integrity statement:** repository state and documentation were checked; this document did **not** build/test a new Architect runtime, Python installer, PBIP model/refactor, distributed agent Skill, Cloud Agent private-repo flow, or Power BI service integration. Every item described as a gate remains UNVALIDATED until executed and evidenced in an implementation ticket.
