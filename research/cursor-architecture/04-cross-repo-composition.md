# R4 — Cross-Repository Composition for Cursor

**Ticket:** [Wayfinder #13](https://github.com/GitKlink/performance-reward-dashboard-architect/issues/13)  
**Evidence reviewed:** 19 October 2026  
**Status:** RESEARCH / RECOMMENDATION — not an approved target-architecture ADR  
**Prerequisites:** [R1 Cursor primitives](01-cursor-primitives.md), [R3 reference-repo benchmark](03-reference-repo-benchmark.md); [R2](02-harness-agent-skill-plugin.md) consulted for classification.

## 1. Problem definition

Wayfinder must coordinate four independently governed concerns without making a specific business project, the orchestrator or a reusable code library into an accidental second standards authority:

1. **Architect/Wayfinder:** workflow selection, orchestration, integration with Microsoft-maintained Power BI/Fabric capabilities.
2. **Engineering standards:** canonical rules for semantic models, DAX, Power Query/M, reporting UX and source-to-dashboard analytical engineering.
3. **Reusable implementation library:** DAX, M, Python and Deneb executable assets/patterns/tests.
4. **Analytical project:** a PBIP/PBIX-supporting project repository where the actual model, reports and project decisions are changed.
5. **Domain knowledge:** Performance & Reward initially; it defines what the concepts mean rather than generic engineering conventions. It may be co-located with Wayfinder initially; physical packaging is not settled here.

The **physical standards home is no longer an open question**: [Wayfinder ADR-0001](../../docs/decisions/0001-canonical-standards-home.md) and the completed migration place the canonical standards in the **private** repository [GitKlink/power-bi-fabric-standards](https://github.com/GitKlink/power-bi-fabric-standards). Its semantic-model folder contains 11 original, parity-checked Markdown files. The implementation library remains [GitKlink/dax-m-query-library](https://github.com/GitKlink/dax-m-query-library). This changes the original wording of #13 but not its remaining composition question.

**Question:** How can a Cursor user/agent discover and consume the correct files and reusable assets, edit the correct repository, and repeat the result later, locally or in automation, without dependency drift or governance duplication?

**Non-goals:** no installer code, no repository restructuring, no live PBIP pilot, no assumption that a Cursor plugin, npm package or submodule has already been adopted. R5, R6 and R8 consume this research.

## 2. Evidence method and constraints

This document distinguishes:

- **DOCUMENTED:** behaviour stated by official Cursor, VS Code, Git or GitHub material;
- **SUPPORT-REPORTED:** a Cursor forum support answer; useful current behaviour but less durable than formal specification;
- **INFERRED:** engineering judgement drawn from evidence and current project constraints;
- **UNTESTED:** requires a controlled Cursor/PBIP environment test before enforcement or final adoption.

The main pre-existing inputs are [R1](01-cursor-primitives.md) and [R3](03-reference-repo-benchmark.md), not a fresh selection of another reference corpus. Their enduring conclusions are preserved: Rules and AGENTS.md instruct, Skills progressively load procedural capability, plugins distribute other primitives, MCP accesses services, and ordinary Markdown is a valid canonical knowledge store. A plugin is not by itself an orchestrator; a standards document does not become a skill because an agent reads it.

**Actual project constraints:**

- Power BI-oriented vertical slice, not a universal enterprise AI platform.
- Embedded analytical team has Python, Excel, SharePoint, Dataflows, Power BI and Cursor; no assumed enterprise SQL/ETL estate.
- One owner for each authoritative concept; no independent hand-maintained copied standards.
- Private standards repository must be accessible to the person, process or agent that reads it; URL visibility does not confer permission.
- Production edits/PRs must stay in the repository that owns the resulting asset.
- Do not accidentally publish private material into the public Wayfinder or reusable-library repositories.

## 3. Evidence that materially changes the comparison

### 3.1 Multi-root is real, but not a universal agent runtime

**DOCUMENTED:** VS Code stores named multi-root folder sets in a .code-workspace file; paths may be relative and folders retain their own Git identity/settings. Cursor explicitly supports multi-root workspaces: each folder is available to Agent. [VS Code multi-root](https://code.visualstudio.com/docs/editing/workspaces/multi-root-workspaces); [Cursor Search FAQ](https://cursor.com/docs/agent/tools/search).

**DOCUMENTED LIMITATION, important:** Cursor says **Cloud Agents do not support multi-root workspaces**, and single-Git-root features **such as worktrees are disabled** within multi-root workspaces. Therefore multi-root is a **local IDE development affordance**, not a sufficient installer, cloud or production distribution design. [Cursor Search FAQ](https://cursor.com/docs/agent/tools/search).

**SUPPORT-REPORTED:** an April 2026 Cursor support response says Rules/Skills/Commands can be discovered from all included roots. Rules using file globs are scoped to their corresponding root; Commands may be visible across roots; duplicate always-on Rules consume context multiple times. [Cursor forum, 21 Apr 2026](https://forum.cursor.com/t/cursor-folders-in-multi-root-workspaces/158433).

**SUPPORT-REPORTED RULE TRAP:** an August 2026 Cursor support response clarifies that file-pattern Rules attach **when a matching file is actually in context**. Merely planning to create/edit a matching file does not guarantee that Rule activation happened. Explicitly opening or referencing the target first is a safer trigger, but that still does not prove model compliance. Always Apply rules may apply across the whole multi-root workspace rather than staying confined to one root. [Cursor forum, 13 Aug 2026](https://forum.cursor.com/t/apply-to-specific-files-rules-are-not-reliably-included-for-matching-files-in-multi-root-workspaces/168224/7).

**UNTESTED:** whether our exact Cursor build picks the correct rule, skill and authoritative standard for a mixed PBIP + private-standards + library session. Do not label automatic cross-root standards compliance as validated.

### 3.2 Search changed; old indexing assumptions need rechecking

**DOCUMENTED (current):** Cursor now describes **Instant Grep** as local search, not remotely hosted embeddings; reading matched files can still transmit their content as model context. Its official Search page also expressly acknowledges multi-root. [Cursor Search](https://cursor.com/docs/agent/tools/search). Older R1/Cursor changelog language about indexing all folders describes an earlier implementation. Treat **file reachability and targeted read tests** as the acceptance metric, not an assumption about vector-index synchronisation.

**INFERRED:** including more repositories in a workspace increases what search can encounter, not what is reliably attended to or obeyed. Thin explicit routing, unambiguous IDs and verification are still necessary.

### 3.3 Cursor instruction and packaging behaviour

**DOCUMENTED:** Project Rules live in .cursor/rules as .mdc and can be Always, context/file-scoped, intelligently selected or manual; referencing a file from a Rule does **not** inline the referenced document. Cursor recommends short Rules pointing to canonical files. [Cursor Rules](https://cursor.com/docs/rules).

**DOCUMENTED:** Skills are discovered from skill directories and supporting references load on demand. [Cursor Skills](https://cursor.com/docs/skills). Plugins are installable at a user or project scope, packaging selected primitive types rather than automatically importing the contents of every repository. [Cursor Plugins](https://cursor.com/docs/plugins). This agrees with R1 and R3.

**INFERRED:** the only robust promise of a composed workflow is a reproducible sequence **resolve source → verify version and access → read applicable standard → implement or review → validate**. Successful invocation of an agent does not by itself establish conformance.

### 3.4 Git dependency guarantees

**DOCUMENTED:** A Git submodule records a specific commit (gitlink) of another repository and usually requires explicit recursive initialisation/updates; branch/head and detached checkout can surprise novice users. [Git Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules); [git-submodule reference](https://git-scm.com/docs/git-submodule).

**DOCUMENTED:** Git subtree imports files/history into another repository; initial clone includes the files without separate submodule bootstrap, but upstream contribution and synchronization require a special workflow. [Atlassian git-subtree guide](https://www.atlassian.com/git/tutorials/git-subtree/).

**DOCUMENTED:** Git worktrees are **multiple checkouts of the same repository**, not a dependency mechanism spanning independent standards/architect/library repositories. [Git worktree](https://git-scm.com/docs/git-worktree).

**INFERRED:** checking out default-branch HEAD for a dependency is convenient while researching, but does not make a PBIP project build or conformance claim reproducible. Record tested commit IDs/tags in a manifest or lockfile; pinning policy itself remains for R5/R8.

## 4. Composition options (consistent assessment)

| Option | Git authority integrity | Local Cursor visibility | Reproducible dependency pin | Initial ergonomics | Cloud/CI suitability | Main risk |
|---|---|---|---|---|---|---|
| **A. Side-by-side independent clones, single repo opened** | Strong | Cross-repo not automatic; explicit paths/tools | Requires external lock | Simple per-repo work | Potential with controlled checkout | Agent cannot see sibling just because it exists |
| **B. Side-by-side clones + saved multi-root workspace** | Strong | High, local IDE (documented) | Requires external lock | Strong for developers | **Not supported in Cursor Cloud Agent** | Cross-root Rules scope and cross-repo context errors |
| **C. PBIP repo with Git submodules** | Strong Git commit boundary | High when initialized inside opened tree | Strong: gitlinks | Extra Git burden | Good only when nested private access and bootstrap configured | Missing/stale submodules, detached HEAD, credential failure |
| **D. Git subtree / committed vendor copies** | Canonical upstream exists; copies can drift | High | Strong as committed files | Easy downstream clone, hard upstream updates | High if redistribution permitted | Private standard leaks, duplicate authority, merge conflicts |
| **E. Symlinks to peer checkout** | Original unchanged | Inconsistent/UNTESTED across hosts | Requires out-of-band lock | Fast local hack | Poor portability | Broken Windows/CI path; scanning/permissions/duplication |
| **F. Plugin/skills/package distribution** | Strong if generated from upstream releases | Discovery through plugin/skill | Release version/pin possible | Good once mature | Depends on host support/installation | Package is not a live source authority; private content and update lag |
| **G. Repo-local dependency manifest + provisioner** | Strong | Depends on what provisioner materialises | Strong by design if immutable refs checked | More up-front implementation | Strong *candidate* for portable CLI/CI/cloud | Bootstrap complexity, manifest/installed-state drift |

**Interpretation:** the matrix is a qualitative design comparison, not an empirical benchmark or a score of Cursor model reasoning quality. A+B and G are complementary: B changes the developer's editor view; G defines the dependency contract. A plugin can later distribute thin integration capabilities; it is not a substitute for a source lock and access check.

### A — Independent sibling clones

Maintain separate checkouts outside a single project's Git tree, each with independent upstream and PR workflow. The editor may open only PBIP at first and explicitly reference other directories with tooling.

- **Good:** easy to understand source ownership; no nested Git surprises; no copy of normative standards.
- **Weak:** absolute sibling paths vary; Cursor cannot be assumed to discover folders outside an opened workspace; permissions and ref drift are implicit.
- **Use:** basic local checkout arrangement, especially when composing B or G.

### B — Local multi-root workspace over sibling clones

Illustrative, **not an installation product**:

~~~json
{
  "folders": [
    { "name": "PBIP Product", "path": "../example-pbip-project" },
    { "name": "Wayfinder", "path": "../performance-reward-dashboard-architect" },
    { "name": "Engineering Standards", "path": "../power-bi-fabric-standards" },
    { "name": "Implementation Library", "path": "../dax-m-query-library" }
  ]
}
~~~

Save beside peer folders and use relative paths for portability. Repositories remain independent and should have independent Git operations. Refer explicitly to the **project file and canonical standard file** when asking Cursor to evaluate naming or metadata.

- **Good:** first-class local inspection/editing; no standards copies; easy to compare an actual DAX measure with domain-specific instructions.
- **Weak:** multi-root does not equal cloud support, cross-repo atomic Git commits, guaranteed Rule precedence or deterministic conformance.
- **Guardrail:** identify the **write owner** at task start; default reference roots (standards/library) to *no writes without explicit scope*. A retrieved library pattern is not permission to alter its source.

### C — Submodules

Submodules fit an **explicit version-pinned embedded dependency** when the consumer needs a reproducible tree, has access to private dependencies, and accepts nested Git.

- **Good:** exact dependent SHA encoded in the superproject commit.
- **Weak:** extra initialisation step; a repo checkout without submodules is incomplete; updating a submodule is a **separate intentional version bump**, not automatic HEAD tracking; nested modifications and detached HEAD are frequent operator mistakes.
- **Important:** do not blindly add a **private** standards repo to a **public** Wayfinder or PBIP repo; URLs, CI availability and read permissions are separate risks. GitHub Actions permissions for private cross-repo access require deliberate configuration and should not be assumed from repository ownership.
- **Current judgment:** do **not** use as the universal default. Reconsider if the single-root Cursor Cloud/CI path proves more reliable with pinned submodules than other materialisation options.

### D — Subtree/vendor

Files become real tracked files in the consumer, providing convenient single-root search. That is attractive for offline/cloud use but violates our **no independently maintained standards copies** principle unless they are strictly **generated, read-only, version-stamped vendor snapshots** with a verified upstream and controlled refresh.

- **Current judgment:** not for canonical normative standards. Potential exceptional deployment artifact only after licensing, private-data and provenance review.
- **Hard failure:** public repo accidentally commits private standards content.

### E — Symlinks

Symlinks avoid byte duplication on one developer machine, but file traversal, code search, filesystem path resolution and privilege behaviour vary. They do not identify a source revision.

- **Current judgment:** personal experiment only, not supported distribution or reproducible CI pattern.

### F — Plugin/package

Per R1/R3, a Cursor plugin may distribute small Rules/Skills/Commands/agents/hooks/MCP integration; a generic package may distribute a typed reusable executable asset.

- **Good:** ergonomic project/user installation when policies and packages are versioned.
- **Weak:** installation scope, private distribution, host portability, policy authority and dependency access remain independent concerns.
- **Current judgment:** viable distribution *candidate* for a thin Wayfinder capability layer, **not** the canonical standards store. R6 analyzes packaging in detail and R8 decides whether plugin distribution is warranted.

### G — Manifest/lockfile and provisioner

A checked-in **declarative contract** in the PBIP product declares the semantic-model standards, Wayfinder and library dependencies by immutable Git commit, release or digest; a provisioner resolves them into workspace roots or local read-only dependency directories and checks permissions.

**Illustrative schema, not an adopted format:**

~~~json
{
  "schemaVersion": "research-example-only",
  "product": "example-pbip-product",
  "sources": [
    {
      "id": "engineering-standards",
      "repository": "GitKlink/power-bi-fabric-standards",
      "revision": "<approved-full-commit-sha>",
      "entrypoint": "semantic-model/README.md",
      "role": "normative-reference",
      "writePolicy": "read-only"
    },
    {
      "id": "wayfinder",
      "repository": "GitKlink/performance-reward-dashboard-architect",
      "revision": "<approved-full-commit-sha>",
      "role": "orchestration"
    },
    {
      "id": "implementations",
      "repository": "GitKlink/dax-m-query-library",
      "revision": "<approved-full-commit-sha>",
      "role": "reusable-implementation"
    }
  ]
}
~~~

Missing/unauthorized revision **fails closed**; it does not silently fall back to the public web or a stale cached copy. Explicitly distinguish the **source revision required by the project** from the **local revision currently present**. This would give CI, local tooling and future agent hosts a shared dependency contract while the actual installation mechanism can differ.

- **Current judgment:** strongest **portable design direction**, not built or validated. R5 must decide schema/CLI, lock update, authentication and rollback; R8 must decide whether it belongs in Wayfinder core, a companion bootstrap tool or a plugin.

## 5. Cursor discoverability and context implications

### Availability is not application

A file being present in an open root means it **can** be read/searchable. It does not establish that the right standard is applied to a response. Minimum intended flow:

~~~text
PBIP task / measure review
  -> identify product and intended write repo
  -> resolve pinned standards revision and access
  -> load core semantic measure standard + glossary
  -> load relevant domain extension (e.g. Variable Reward)
  -> inspect model and measure metadata
  -> use implementation library only when relevant
  -> make project-local proposal/change
  -> run deterministic checks + capture evidence
~~~

Keep canonical standards as ordinary documents. A *thin* AGENTS.md, Rule or Skill routes to the pinned canonical docs; do not paste full standard text into an Always Rule. Domain semantics must come from the domain authority, not guessed from engineering policy. Where standards say, for example, that measure names cluster root-first, the actual definition of Variable Reward is domain-owned.

### Key risks and mitigations

| Risk | Failure mode | Proposed mitigation |
|---|---|---|
| Unread source | Agent answers based on generic knowledge despite having a standards folder | Require explicit file-read evidence and resolved revision in QA output |
| Wrong standard version | Sibling clone updated to HEAD unnoticed | Pin commit/tag; compare resolved local SHA with lock |
| Root-crossing write | Agent edits library or standards instead of PBIP | Declare target write root, read-only dependency roots and pre-commit path checks |
| Rule not activated | Cursor glob Rule never enters context | Read/open target file before editing; for high-stakes policy explicitly call standards Skill/reference |
| Duplicate always-on instructions | Multiple roots inject same policy | Keep Always instructions minimal; do not copy the same Always Rule across all roots |
| Misleading discovery | Agent retrieves an irrelevant same-named measure/example | Use fully qualified repo/path/asset IDs and cite exact source |
| Unauthorized private repo | Cloud/CI lacks private standards access | Auth preflight; fail closed with clear missing permission |
| Confidentiality | Private standards content copied into public artifact/PR/agent logs | Classification check and prohibited cross-repo copying; redact test fixtures |
| Packaging staleness | Plugin includes older bundled standards | Separate canonical version from generated adapter/version; verify lock |
| Context overflow | Loads all domain standards irrespective of task | Progressive, domain-appropriate retrieval; keep evidence concise |

**Security caveat:** private GitHub access means the caller can read the repository; it does not guarantee contents never enter an agent prompt, logs, generated report or another repo. Verify the host's data-handling settings and destination before using sensitive material.

## 6. Git and version/update model

**Research direction:**

1. A specific PBIP product should record which **approved standards revision** and which reusable library revision it was validated against.
2. Standards can evolve independently; a standards release does not silently rewrite products. A *dependency update* should be reviewable as an explicit PR/change.
3. Distinguish source revision, materialised local revision and validation revision in machine-readable evidence.
4. Use content digest/revision identity to detect drift and accidental forks. File paths alone do not declare authority.
5. Version changes may affect meaning even when code still runs (e.g. changing a measure naming/description requirement). R6/R8 must decide normative SemVer semantics.
6. Maintain independent Git histories and PRs: standards correction PR in standards repo, pattern implementation PR in library repo, model/report change PR in PBIP repo. Where changes coordinate, cross-link PRs and order releases instead of pretending there is one atomic cross-repo commit.

**Not decided here:** whether a tag, release manifest, pinned full SHA, dependency-bundle digest or semantic version should be the canonical production dependency identifier. Immutable SHA is a safe **prototype** reference; release policy belongs to R5/R6/R8.

## 7. Developer ergonomics and deployment paths

### Local interactive engineering

**Recommended pilot:** independent side-by-side clones + saved multi-root .code-workspace + explicit per-repository authority and written/pinned dependency resolution. The project PBIP checkout is the primary write target. Other roots are reference inputs by default. The workspace file may be developer-local until its path layout is portable.

Success means opening a real PBIP project in Cursor, finding the standard, locating a reusable implementation and preparing a change **only** inside the PBIP repo without ambiguity.

### Cursor Cloud Agent

**Important documented constraint:** a multi-root workspace cannot be sent unchanged to Cloud Agents. They require a supported single-repository entry point. Candidate bridge: managed **single-root materialisation** of pinned dependencies into an ephemeral workspace, installed small skills/plugin assets, or authenticated tools that fetch permitted source content. Choose only after pilot and access check. Never quietly vendor a private standards body into a public repo.

### CI / repeatable validation

Prefer a deterministic resolver that obtains exact approved source revisions and emits provenance, followed by machine-checkable conformance tests. The UI workspace file is neither a dependency lock nor a CI guarantee. Relevant verification should still work when Cursor is absent.

### Team/distribution

A thin installable capability or starter template can improve ergonomics later. Do not publish a universal setup requiring a private repo without documenting required permissions and fallbacks. R5 owns installer and project-scaffold details.

## 8. Comparison by delivery phase

| Phase | First candidate | Reason | Explicit boundary |
|---|---|---|---|
| **R4 local proof** | Sibling clones + multi-root workspace | Lowest coupling with strong interactive visibility | No production guarantee or Cloud support |
| **Development with repeatability** | Above + experimental pinned manifest | Trace source standards/library versions | Schema/version lifecycle deferred |
| **Product/CI repeatability** | Pinned dependency resolution / provisioner | One project-specific lock, audit trail, fail-closed behaviour | R5 design and validation required |
| **Cloud Agent** | Single-root materialised dependencies or authenticated remote retrieval | Multi-root is unavailable | Validate access/privacy and context before selecting |
| **Team distribution** | Thin plugin/skills or generated adapter if justified | Deploy small capabilities, not the standards corpus | R6/R8 determine mechanism |
| **Emergency portability** | Explicit URLs + commit IDs + verified downloads | Can work without plugin ecosystem | Manual effort; not enforcement |

**Provisional recommendation:** use **B for local development**, investigate **G for portable/CI composition**, and keep **F as a later distribution option**. Do not default to submodules or vendored standards without a concrete single-root/CI constraint that justifies their cost.

## 9. Implications for Wayfinder and the PBI Architect

The architect should become a **consumer/orchestrator**, not a repo that must contain every dependency:

~~~text
      [PBIP project / project-local decisions]
                     |
                     | declared and verified dependencies
                     v
       [Wayfinder composition / routing]
            /          |          \
           v           v           v
 [Standards repo] [Domain authority] [DAX/M Library]
        |                               |
  normative rules                 reusable assets
            \          |          /
              [Microsoft Fabric skills]
                  platform capability
~~~

The diagram is about **authority and references**, not physical runtime file locations. The architecture must retain the ability to replace the P&R domain pack with another without changing the generic engineering-standard files.

**Example — salary/reward measures in a PBIP model:**

- For a requested measure refactor, load the pinned semantic-model core naming standard, glossary and appropriate Fixed/Variable Reward domain representation guidance.
- Load the domain definition and calculation contract separately from P&R authority.
- Inspect the project's actual measure names, DAX, format strings, descriptions, folders, dependencies and hidden state.
- Propose business-safe changes to the **PBIP project**; do not edit a library asset merely because its implementation was reused.
- Validate name, description, visibility, semantic basis and numerical reconciliation; record which standards revision was used.
- Escalate genuine conflicts by linking a domain-authority or standards-authority issue rather than silently overriding one in the other repository.

This provides a practical early test of our DAX naming standard while keeping architectural composition a separate decision.

## 10. Acceptance / experiment matrix for follow-on implementation

These are **planned tests**, not tests executed during R4. Run them in the installed version of Cursor before asserting reliability.

| ID | Setup | Action | Observable pass | Failure meaning |
|---|---|---|---|---|
| C1 | Four sibling clones, saved multi-root workspace | Ask Agent to locate a named measure naming rule | Opens correct path in standards root | Availability/discovery not reliable |
| C2 | Current PBIP open with target .tmdl file | Ask Agent to refactor measure with file-pattern rule | Rule listed as applied and standards file explicitly read | Glob/activation gap |
| C3 | PBIP task plus same-named example in library | Ask Agent to choose canonical source | Identifies standard vs reusable asset, writes only PBIP | Authority confusion |
| C4 | Multi-root includes duplicate Always Rules | Inspect applied Rules / token behaviour | Detect duplicate and remove/re-scope | Hidden context inflation |
| C5 | Pin standards to previous approved revision | Update local clone to newer HEAD | Resolver reports drift, does not use HEAD silently | No reproducibility |
| C6 | Remove permission to private standards | Run bootstrap/validation | Explicit access failure, no public-web fallback | Privacy/integrity flaw |
| C7 | Run equivalent task in Cursor Cloud Agent | Try multi-root workspace directly | Explicitly unsupported; evaluate single-root bridge | Non-portable local design |
| C8 | Add a second domain pack or generic sample | Apply same semantic naming rules | Generic standards reused; no P&R hardcode | Domain coupling |
| C9 | Propose source edit from within PBIP session | Verify Git status across roots | Only intended owner repo changed | Cross-repo write leakage |
| C10 | Disable Cursor | Run dependency/source-validation check | Deterministic machine-readable pass/fail | Overdependence on AI prompt |
| C11 | Project is public; standards repo is private | Attempt standard handling/export | No private full text in public commit/log/artifact | Confidentiality failure |
| C12 | Cross-root reusable UDF referenced | Validate expected implementation revision | Correct implementation ID and tested version | Code drift |

**Exit from pilot:** C1, C2, C3, C5, C6, C9, C10 and C11 pass or their failure is documented with a selected safe alternate. Do not accept "Agent said it followed the standard" as verification.

## 11. Unresolved questions / handoffs

**R5 — Installation/bootstrap (#15):**
- Who materialises the roots/skills: a CLI, Cursor plugin or local workspace generator?
- How does a private standards repository authenticate in Windows, CI, remote and Cloud Agent execution?
- What is the lockfile schema, upgrade procedure, rollback and error handling?
- Do we provide a single-root fallback? Should it use authenticated content retrieval, a read-only cache, or submodules?
- How do we expose both a fast local developer mode and a reproducible project deployment mode?

**R6 — Standards/library packaging (#16):**
- What makes a standard version normative/compatible, and how are catalogue/entrypoint identifiers declared?
- How is a library implementation exported, discovered and reused without copying unrelated standards?
- What is the release/artifact distribution model (research PR #19 is open; not an approved decision)?

**R7 — Cross-agent portability (#14):**
- Which dependency manifest and references are host-neutral?
- Which thin adapters are required for Cursor, Codex, Claude and other environments?
- Can the same conformance evidence be produced across hosts?

**R8 — Target architecture synthesis (#17):**
- Adopt/modify/reject B + G + optional F after experimental results and R5/R6/R7.
- Define an authority-aware, versioned source resolver contract.
- Resolve cloud single-root path explicitly; do not assume multi-root works there.

**Issue #6 — Domain boundary:**
- Classify semantic-model-specific domain extension content vs canonical P&R business meaning; no duplicated authorities after the original preservation migration.

## 12. Source and traceability register

**Prior project inputs (repository-local):**
- [R1 — Cursor native primitives](01-cursor-primitives.md): activation, scoped Rules, Skills, Plugins, context cost.
- [R3 — six-repository benchmark](03-reference-repo-benchmark.md): official Cursor plugin patterns, Microsoft skills, skill distribution, bootstrap examples, cross-host considerations.
- [R2 — architecture classification](02-harness-agent-skill-plugin.md): architecture role versus distribution/runtime role.
- [Wayfinder ADR-0001](../../docs/decisions/0001-canonical-standards-home.md): physical normative standards authority, already approved.
- [Standards migration record](https://github.com/GitKlink/power-bi-fabric-standards/blob/main/docs/migration/2026-10-16-semantic-model.md): preservation parity, private access required.

**Current primary documentation (checked 19 October 2026):**
- [Cursor Search / Instant Grep / multi-root limits](https://cursor.com/docs/agent/tools/search) — Cloud Agent multi-root incompatibility, worktree limitation, current search behaviour.
- [Cursor Rules](https://cursor.com/docs/rules) — .mdc activation and canonical file references.
- [Cursor Skills](https://cursor.com/docs/skills) — progressive loading and discovery.
- [Cursor Plugins](https://cursor.com/docs/plugins) — installation scopes and packaging.
- [VS Code multi-root workspaces](https://code.visualstudio.com/docs/editing/workspaces/multi-root-workspaces) — workspace format and path portability.
- [Git submodule](https://git-scm.com/docs/git-submodule) and [Git Book Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) — commit pins and update pitfalls.
- [Git worktree](https://git-scm.com/docs/git-worktree) — alternate checkout of one repo, not a cross-repo dependency.
- [Git sparse-checkout](https://git-scm.com/docs/sparse-checkout) — checkout footprint optimisation only, not cross-repo composition.
- [Atlassian subtree explanation](https://www.atlassian.com/git/tutorials/git-subtree/) — vendored-files alternative and merge burden.

**Cursor support reports (lower authority / verify in installed build):**
- [April 2026 multi-root rule/skill behaviour](https://forum.cursor.com/t/cursor-folders-in-multi-root-workspaces/158433).
- [August 2026 rule activation and always-on scope](https://forum.cursor.com/t/apply-to-specific-files-rules-are-not-reliably-included-for-matching-files-in-multi-root-workspaces/168224/7).
- [July 2026 Instant Grep clarification](https://forum.cursor.com/t/what-do-you-think-about-cursor-removing-the-codebase-indexing-settings/165899/10).

**Evidence integrity:** this report is a documentation/repository-architecture benchmark. No local Cursor product experiment, PBIP compilation, Git submodule workflow, CLI bootstrap or cloud deployment was performed. Recommendations are conditional on follow-on acceptance tests.
