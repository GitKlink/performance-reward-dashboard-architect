# R5 — Installation and Bootstrap Architecture for Architect

> **Terminology correction (2026-10-22):** The project is the **Power BI / Fabric Architect**. **Wayfinder** is Matt Pocock's planning skill used during research, not the project name. Original issue/PR titles may retain historical wording. The evidence and technical conclusions are unchanged. References to private standards describe the repository's earlier visibility; it became public on 2026-10-22.

**Research ticket:** [#15 — Installation and bootstrap](https://github.com/GitKlink/performance-reward-dashboard-architect/issues/15)  
**Research snapshot:** 19 October 2026  
**Status:** RESEARCH / IMPLEMENTATION RECOMMENDATION — **not** an approved R8 target architecture, a shipped installer, or evidence of an end-to-end Cursor/PBIP test.  
**Required prior work:** [R2](02-harness-agent-skill-plugin.md), [R4](04-cross-repo-composition.md), [R7](07-cross-agent-portability.md), [R3](03-reference-repo-benchmark.md).  
**Authority decision:** [Architect ADR-0001](../../docs/decisions/0001-canonical-standards-home.md).

This document distinguishes **DOCUMENTED** (current official specification/documentation), **OBSERVED** (existing implementation studied by R3 or official repository), **RECOMMENDATION** (R5 architecture judgment), and **UNTESTED** (proposed tests not yet run on actual developer or CI machines).

## 1. Installation problem and personas

Architect is a Power BI/Fabric-focused *orchestration* project: it must combine upstream Microsoft platform skills, the canonical engineering standards, domain authority, reusable DAX/M/Python/Deneb patterns, and a real analytical project without turning itself into a second content authority or a new AI agent runtime.

The source repositories are deliberately independent:

| Component | Existing authority | Content a setup tool may consume | Ownership constraint |
|---|---|---|---|
| Architect / workflow | [GitKlink/performance-reward-dashboard-architect](https://github.com/GitKlink/performance-reward-dashboard-architect) | Capability definitions, routing, future adapters, domain-pack interfaces | Orchestration, not full copies of standards |
| Engineering policy | **Private** [GitKlink/power-bi-fabric-standards](https://github.com/GitKlink/power-bi-fabric-standards) | `semantic-model/README.md`, core naming standard, glossary, seven original domain extensions | Canonical engineering-policy text; 11 original sources already migrated and parity-checked |
| Executable patterns | [GitKlink/dax-m-query-library](https://github.com/GitKlink/dax-m-query-library) | Versioned DAX, M, Python and Deneb assets | Code/patterns, not standards authority |
| Domain pack | P&R authority (not yet finally separated; see [#6](https://github.com/GitKlink/performance-reward-dashboard-architect/issues/6)) | KPI meaning, grain, eligibility, periods, calculation contracts, tests | Business truth must not be silently inferred from semantic-model folder layouts |
| Actual Power BI product | Its PBIP/product repository | PBIP, TMDL, report definitions, local project decisions | Primary **write target** for a report/model task |
| Platform capabilities | Microsoft-maintained Power BI/Fabric skills/tools | Already-supported upstream operations and validations | Delegate first; do not fork mechanically |

**Personas / supported execution modes to distinguish:**

1. **Architecture contributor:** edits Architect/standards/library in separate authorised PRs; needs *editable* checkouts and may work on any one authority explicitly.
2. **P&R/PBIP developer:** works primarily in **Cursor IDE** on a PBIP model; needs reference sources available but normally **read-only** by policy; minimal setup friction.
3. **Team consumer:** wants the approved skills and policies installed/updated without personally modifying them; needs a *managed* mode with provenance and safe upgrades.
4. **CI/conformance runner:** must be reproducible and deterministic without Cursor; works with pinned exact inputs, machine-readable evidence and short-lived credentials.
5. **Cursor Cloud Agent / other remote host:** cannot assume a multi-root desktop workspace; must be provisioned independently or fetch sources via an authorised tool.
6. **Codex / Claude Code user:** wants shared content where supported, with separate host adapters. Host feature parity is not a prerequisite for a supported common workflow.

**Problem to solve:** obtain exact permitted dependencies, make the minimum necessary sources and skills discoverable, preserve independent Git/write boundaries, and validate conformance/update state *without* requiring users to know the topology or trusting the model to remember what to load.

**Problem not to solve:** implement another runtime, create a full package marketplace, invent a second DAX policy repository, convert all standards to prompts, or replace an existing third-party installer unless a demonstrated gap warrants it.

## 2. Candidate installation models

| Candidate | Developer startup | Change isolation / reproducibility | User and CI portability | Lifecycle burden | R5 evaluation |
|---|---|---|---|---|---|
| **A — Documentation-only manual setup** | Clone repos and open workspace manually | Git boundaries good; revision drift unless manually recorded | Poor; environment-specific and easily missed steps | Very low code cost, high per-user error | Useful baseline and fallback, **not durable team default** |
| **B — Saved multi-root .code-workspace only** | Excellent once clones exist | **No** dependency lock or credentials supplied by workspace file | Cursor local only; Cloud Agents unsupported | Low | Development UX component, **not full installation** |
| **C — Submodules inside each PBIP project** | Single top-level checkout *if recursively initialised* | Gitlink pins exact commits | Standard Git/CI with private-auth complexity | Elevated nested-Git burden; detached HEAD pitfalls | Conditional exception, **not default** |
| **D — Subtree/vendor full dependencies** | Easiest single-root visibility | Snapshot can be pinned but becomes copied data | Technically broad | High update/authority/privacy cost | Reject by default for **private normative standards** |
| **E — Native Cursor Plugin / Agent Plugin** | Minimal install for supported host | Package version, but does not automatically lock sibling repos | Varies by host and private auth | Marketplace/release/adapter maintenance | Future distribution *option*, not full bootstrap |
| **F — Shared skills.sh / host-native skill installers** | Good at deploying selected skills | Copies may be user-editable; dependency provenance separate | Broad but paths/metadata differ | Duplicates and selective references must be managed | Suitable optional distribution layer |
| **G — Small pinned resolver + workspace/adapter generator** | One checked setup command after prerequisites | **Strong by design**, if refs/hashes and state enforced | Portable Python/CLI or CI, with host-specific renderers | Moderate implementation cost | **Recommended phased end state**, not yet built |
| **H — Full spec-kit-style scaffolding framework** | One polished CLI | Can be strong with a complete managed-file ledger | Extensible across hosts | Very high upfront test, trust and upgrade burden | **Too large for current Power BI slice** |

**R2/R3 alignment:** a plugin is a packaging boundary, a Skill is a capability boundary, a Rule/AGENTS.md is an instruction surface, and a bootstrapper is a deterministic materialisation/lifecycle boundary. Choosing an installer does **not** turn Architect into a harness.

**R4 alignment:** sibling clones plus a multi-root IDE workspace are the lowest-coupling **local development** path, but not a dependency resolver. Cursor officially supports local multi-root and says **Cloud Agents do not support multi-root**; some single-root Git features such as worktrees are disabled within multi-root. See [Cursor search FAQ](https://cursor.com/docs/agent/tools/search).

**R7 alignment:** host-neutral information and `SKILL.md` workflows may be shared; host-specific trigger/plugin/hook/tool configuration remains a thin adapter. An installer must not silently copy canonical standards into all hosts' prompt files.

### Decision-oriented synthesis

**RECOMMENDATION:** Start with a **documented manual bootstrap contract**, immediately turn it into a **small deterministic, Python-based setup/doctor utility** after one successful PBIP pilot, and **defer** a public plugin/marketplace product until the architecture is proven. This meets an embedded team where Python and Cursor are already present and avoids requiring Node/npm or enterprise deployment tooling at phase 1.

R8 must approve the final distribution and lockfile contracts. R5 should not declare the CLI already implemented.

## 3. Managed vs editable development mode

**OBSERVED (R3 + refreshed official code):** Matt Pocock distinguishes a **managed, read-only plugin** from **skills.sh copies that developers own/edit** and warns against installing both (duplicate capabilities). The current canonical installation guidance keeps these channels separate: [mattpocock/skills .agents/install-block.md](https://github.com/mattpocock/skills/blob/main/.agents/install-block.md).

**OBSERVED:** GitHub Spec Kit uses per-integration manifests with hashes, detects modified managed files, blocks upgrades that would overwrite them, and preserves user edits on normal uninstall. Its docs describe multi-install conflict handling, per-integration status reporting and rollback on failed installation: [Spec Kit integration commands](https://github.com/github/spec-kit/blob/main/docs/reference/integrations.md).

### Two explicit modes (proposed)

| Behaviour | `managed` — default for consumers | `editable` — contributor |
|---|---|---|
| Architect capability/adapter files | Installed from approved pinned revision; **owned by tool** | Source checkout in normal Git repo, intentionally editable |
| Standards/library reference files | Pinned, treated **read-only** except explicitly delegated authority task | Independent writable Git checkouts only when working on their own authority |
| PBIP project files | **User-owned**, never overwritten without explicit approval | User-owned |
| Update | Explicit new approved pin and managed-state diff; no silent HEAD | Normal Git pull/branch/PR controlled by contributor |
| Uninstall | Remove only unchanged files proven owned by installer | Do not delete contributor source checkouts |
| Local modification | Warn, block or preserve; never silently replace | Normal Git diff |
| Duplicate install | Fail with diagnostics if managed and editable same capability are active in one host | Fail or require explicit mode switch |

**Terminology caveat:** a Git clone in a normal writable folder is not an OS-enforced read-only sandbox. In phase 1, "read-only dependency" is an **intent and a validation rule**; genuine enforcement requires filesystem/tool permissions and validated no-write checks. Do not overclaim protection from a prompt.

A user may have **mixed roles across repositories**, e.g. Architect editable and standards managed. Mode should therefore be recorded **per installed component or capability**, not as one vague global toggle.

## 4. Dependency acquisition and preflight

### What setup must know

A project-specific dependency declaration should identify each required source by:

- stable logical ID (`engineering-standards`, `power-bi-architect`, `reusable-implementations`, optionally `domain-pr`);
- GitHub repository identity, expected access class, expected content entrypoint and role (`policy`, `domain`, `library`, `architect`);
- **immutable full commit SHA** or approved verified release resolved to a commit;
- intended write policy and host surfaces;
- artifact or adapter revision separately from the normative standard revision.

**Recommendation:** store **desired dependency pins** in a small checked-in project lock/manifest, and **observed install state** in a separate local state file. A workspace description cannot serve as either a dependency lock or a proof of installed version.

**Illustrative configuration, NOT an adopted schema:**

~~~json
{
  "schemaVersion": "research-only-v0",
  "product": "example-reward-pbip",
  "sources": [
    {
      "id": "engineering-standards",
      "repository": "GitKlink/power-bi-fabric-standards",
      "revision": "<approved-40-character-git-sha>",
      "entrypoint": "semantic-model/README.md",
      "role": "normative-policy",
      "editMode": "reference"
    },
    {
      "id": "power-bi-architect",
      "repository": "GitKlink/performance-reward-dashboard-architect",
      "revision": "<approved-40-character-git-sha>",
      "role": "orchestration",
      "editMode": "reference"
    },
    {
      "id": "implementations",
      "repository": "GitKlink/dax-m-query-library",
      "revision": "<approved-40-character-git-sha>",
      "role": "implementation-library",
      "editMode": "reference"
    }
  ]
}
~~~

**Boundary:** no project user name, machine-specific absolute path, GitHub PAT, SSH key, credential store location or private file contents should go into a public/project-checked manifest. Repo identity and commit SHA alone are generally not secret; full private source bytes may be.

### Preflight sequence (candidate)

1. Detect operating system, Python runtime, Git, Cursor (for local development), and target PBIP project path. **Report** unavailable optional tooling rather than silently installing it.
2. Verify GitHub source repository access via the machine's configured **Git Credential Manager, SSH agent, GitHub CLI or externally supplied short-lived credential**. Never request pasted PATs in logs, arguments or generated files. For private standards, fail closed on missing access.
3. Validate manifest schema and repository ID allow-list, full immutable ref, permitted paths and write-owner policy. Reject unapproved Git remotes, floating branches in reproducible mode, path traversal and symlink escapes.
4. Resolve/check out the exact approved revisions in a controlled local cache or sibling folder. Compare the **actual Git HEAD** and required entrypoint to the requested pins. Do not silently replace an unavailable SHA with latest/default branch.
5. Validate all required skill supporting references and import paths are available; R3 showed selected-skill installs can omit shared references.
6. Classify existing host skill/rule/plugin installations and detect duplicates before writing adapters.
7. Generate requested local workspace and **minimum** host-specific managed adapter files.
8. Invoke `doctor`/verification: installed revisions, file ownership, source accessibility, skill discovery smoke test and a deterministic validator (if available).
9. Record installation state only after success. On error, roll back managed changes and preserve user-owned PBIP files.

**Security-sensitive failures:** wrong GitHub owner/repo, failed private auth, unexpected Git SHA, wrong source classification, symlink/path escape, untrusted executable install script, duplicate conflicting adapter, unverified managed-file overwrite. These block further setup; there is no "best effort by guessing" fallback.

### Local vs CI credentials

**DOCUMENTED:** GitHub's `actions/checkout` notes the usual workflow `github.token` is scoped to the **current repository**; checking out a different **private** repository requires additional credentials with access (a properly scoped GitHub App installation token or fine-grained PAT, for example). See [actions/checkout README, multiple private repos](https://github.com/actions/checkout#checkout-multiple-repos-private). Do not assume a public Architect repo's CI token can read private standards.

**RECOMMENDATION:** prefer scoped, short-lived machine/CI auth where possible; never print secrets; mask output; restrict source paths; keep independent release/supply-chain controls. A CI job in a public project that reads private standards must not publish their bodies into artifacts, PR diffs or verbose logs. Do not equate access to a reusable private *action* with general arbitrary private-repo checkout: GitHub's action/workflow sharing has its own controls and information-leak warning ([GitHub private Actions sharing](https://docs.github.com/en/actions/how-tos/reuse-automations/share-across-private-repositories)).

## 5. Workspace and bootstrap generation

### Proposed phase-1 local layout

**Not a hardcoded filesystem requirement:** a chosen parent folder contains independent Git clones and a saved editor workspace file. Example:

~~~text
analytics-work/
  product-reward-pbip/                    # PRIMARY WRITE TARGET
  performance-reward-dashboard-architect/ # reference/orchestrator
  power-bi-fabric-standards/               # private policy authority
  dax-m-query-library/                     # reusable implementation authority
  reward-local.code-workspace              # generated LOCAL editor view
  .power-bi-architect-install/                      # ignored/local cache/state (conceptual)
~~~

A saved workspace may use relative paths:

~~~json
{
  "folders": [
    {"name": "Reward PBIP", "path": "product-reward-pbip"},
    {"name": "Architect", "path": "performance-reward-dashboard-architect"},
    {"name": "Engineering Standards", "path": "power-bi-fabric-standards"},
    {"name": "Implementation Library", "path": "dax-m-query-library"}
  ]
}
~~~

**DOCUMENTED:** [VS Code multi-root workspaces](https://code.visualstudio.com/docs/editing/workspaces/multi-root-workspaces) use `.code-workspace` with named folders/relative paths. **DOCUMENTED:** Cursor makes each folder available to the local agent, but Cloud Agents do not support multi-root. [Cursor Search FAQ](https://cursor.com/docs/agent/tools/search).

The workspace is an **editor view**. It cannot prove dependencies are pinned, hosts have permissions, the AI loaded standards or the model passed validation.

### Managed assets vs project-owned assets

**Installer may write/manage, by explicit user consent:**
- Local editor workspace file in a chosen output location.
- Its own state/manifest, cache directory and backup/transaction journal.
- Host-specific *generated adapter files* in bounded target directories, recording source, path and content SHA-256.
- An optional project-local **managed section** linking to an existing AGENTS.md when there is no collision, otherwise a proposed diff that the user approves.
- Smoke-test outputs and non-sensitive provenance, ideally stored outside tracked application directories.

**Installer must not silently:**
- Rewrite existing PBIP/TMDL files or model measures.
- Modify authoritative standards, P&R business definitions or reusable library source.
- Overwrite any existing AGENTS.md, CLAUDE.md, Rule, Skill, hook or editor configuration without seeing and respecting ownership.
- Install/enable arbitrary third-party packages, executable hooks or MCP servers merely because metadata references them.
- Commit private canonical standards text into a public PBIP or Architect repository.
- Modify user-wide Cursor/Codex/Claude configuration without a separate explicit opt-in and reversible install record.

### Path, idempotence and collisions

Define a stable **logical ID** for each generated capability, not just a matching filename. Two sources producing the same skill identity or "Always" Rule should be flagged before writing. A second identical setup run should yield **no changes**; a different desired revision produces a **previewable plan**. If a local managed file differs from its recorded hash, refuse automatic replacement or provide a reviewed three-way merge; normal `--force` should never mean "delete everything that is there."

An adapter's generated documentation may **point to** private standards and provide a resolver command, but should not embed their full content. On a different host, that pointer must first pass access and version checks.

### Single-root fallback for Cloud Agent and CI

**Not all four sibling clones can be passed as a local multi-root workspace to Cursor Cloud Agent.** Candidate non-mutating approaches:

1. Host-supported authenticated tools that fetch **pinned** canonical source files by identity, revision and path, returning only necessary content to the agent.
2. A provisioned ephemeral **single-root execution workspace** containing permitted pinned dependency material, with a clear private/public boundary. This is not a tracked vendor commit.
3. A separately packaged, versioned lightweight skill/adapter whose *references* are resolved at runtime from the authorised canonical sources.

Do **not** choose among these without measuring availability, private authentication, model context limits, tool permissions and log/artifact leakage in the actual runtime. R8 should select the cloud deployment approach; R5 identifies its requirements.

## 6. Version/update strategy

There are **distinct versions**, and conflating them creates false auditability:

| Version/state | Source of truth | Example |
|---|---|---|
| Architect orchestrator | Git commit/release of Architect | Architect integration behaviour |
| Canonical standards | Git revision/release of standards repo | Measure naming policy |
| Domain contract | Its independent approved revision | Variable Reward / eligibility meaning |
| Implementation library | Git revision or package/asset ID/release | Reusable DAX function |
| Host adapter/Skill | Canonical skill revision + generated adapter version | Cursor `.mdc` routing to standard |
| Installer/bootstrap tool | Its own signed/verified release | CLI behaviour |
| PBIP project | Project Git commit | Actual model/report state |
| Last validated evidence | Model/standards/domain/library revisions + test version | Exact conformance result |

**RECOMMENDATION — update policy:**
- Development `editable` mode may deliberately track working branches, but any **conformance result** must record actual SHA and uncommitted-file/dirtiness status.
- Consumer `managed`, Cloud and CI default to **immutable approved pins**; no floating default-branch input for reproducible checks.
- `update --check` should list available candidate revisions without changing effective inputs.
- `update --plan` should produce a diff of dependency pins, generated adapter changes, removed files and required new permissions.
- `update --apply` should be an explicit approved transaction, ideally with a PR for the *project lockfile*, followed by resolution/validation.
- No silent auto-update of canonical normative standards simply because the installer or plugin updates.
- Use distinct **source content digest**, **install-state hash** and **tested validation revision**. A package version string is insufficient evidence of which normative policy was actually loaded.
- Reverting lockfile + restoring managed-file snapshot should restore the previous valid local composition when upstream SHA is still accessible; otherwise report an unresolved availability problem rather than fake success.

**Note on R6:** [PR #19](https://github.com/GitKlink/performance-reward-dashboard-architect/pull/19) proposes content-first canonical standards, stable asset IDs, packages and SemVer semantics. R5 requires an **ID+revision+integrity contract** but **does not settle** npm vs GitHub Packages, public distribution, the exact schema, or any final release channel. R8 must reconcile them.

### Suggested CLI lifecycle (illustrative, not implemented)

~~~text
power-bi-architect doctor
power-bi-architect init --project <pbip-path> --host cursor --mode managed
power-bi-architect plan
power-bi-architect apply
power-bi-architect update --check
power-bi-architect update --plan
power-bi-architect update --apply
power-bi-architect uninstall --managed-only
~~~

These are **proposed command names**, not commands the user can run today. `doctor` must make its own results machine-readable and must not require an AI model call to check hashes, paths or credentials.

## 7. Failure handling and rollback

**OBSERVED:** [Spec Kit integration implementation](https://github.com/github/spec-kit/blob/main/docs/reference/integrations.md) and [integration design](https://github.com/github/spec-kit/blob/main/design/integration.md) go beyond a simple "copy files" operation: content hash tracking, status, modified-file preservation, transaction rollback, explicit trust boundaries and directory/ownership validation. **RECOMMENDATION:** borrow the *principles*, not the complete complex framework, for a small first-party Architect installer.

### Failure matrix

| Failure | Detection | Correct recovery action | Never do |
|---|---|---|---|
| Private GitHub repo inaccessible | Credentialed read preflight fails | Explain exact repo/permission required; stop | Fall back to public search or guessed standards |
| Dependency SHA unavailable | Remote has no requested commit or checkout mismatches | Preserve previous working install; ask for approved pin update | Check out HEAD silently |
| Half-generated workspace | Transaction journal incomplete | Restore previous hashes, remove **only newly created managed files** | Delete project folder wholesale |
| Existing AGENTS.md/CLAUDE.md | Target path exists and ownership hash absent | Display diff or leave untouched | Overwrite with template |
| User edited installed adapter | Current file digest differs from recorded generated digest | Preserve edit; show conflict and options | Destructive "upgrade" by default |
| Duplicate skill/plugin | Same logical capability registered twice | Identify both source IDs and select approved channel | Install third duplicate |
| Broken relative reference | Skill reference/path resolution fails | Block activation/test; materialise missing approved dependency | Rewrite path to arbitrary adjacent repo |
| Symlink/path escape | Resolved output path outside allowed base | Refuse write and report path | Follow link into home/other repo |
| Host feature unsupported | Host/version capabilities report gap | Mark supported tier accurately; fallback manual/skip optional adapter | Pretend a Cursor hook works in Claude |
| Test/validator failure | Machine-readable check nonzero | Preserve evidence, mark setup **not validated**; make repair plan | Report completed because agent answered |
| Public artifact includes private policy bytes | Data classification/precommit check | Block export, redact, re-run review | Publish source and hope repository ACLs protect it |
| Concurrent setup/upgrade | Install-state lock held or changed during plan | Abort/ask retry with fresh plan | Two writers race over managed files |

### Transactional implementation outline (future)

- **Plan (read-only):** determine target paths and source pins, validate credentials/hosts, compare desired vs actual digests, enumerate all writes/deletions and conflicts.
- **Apply:** obtain exclusive process/target lock, recheck preconditions, stage downloaded/validated source content and new generated files, journal only managed affected paths, then atomically replace files where supported.
- **Verify:** compare recorded hashes, refs, host discovery, and validator output; only then persist a successful install-state record.
- **Rollback:** restore *verified prior managed bytes* and remove newly created managed files and empty owned directories. Preserve pre-existing/user-modified files. If rollback itself fails, retain recovery snapshots and disclose their paths.
- **Uninstall:** remove only matching-hash managed files; warn for modified/unknown files. Never remove PBIP, standards or library Git checkouts without an explicit separate operation.

The real installer should use path canonicalisation, symlink checks, safe temporary files, file locks and Windows/macOS/Linux test cases. There is no evidence these have been implemented for Architect.

## 8. Security and trust considerations

### Boundaries that matter

1. **Source trust:** GitHub identity + immutable revision + allow-listed source/entrypoint; do not execute remote scripts on the strength of natural-language instructions.
2. **Credential trust:** prefer OS/Git managed authentication for developers, GitHub App or narrowly scoped ephemeral CI token for service automation; never embed secrets in a manifest, workspace file, installer log or issue.
3. **Private-content handling:** repository ACLs govern access to Git bytes but do not constrain what an AI model might subsequently include in chat/output. Reduce loaded content to only what is needed; inspect generated diffs/logs. Cursor documents that Agent content read from a search match may enter a model request ([Cursor Search](https://cursor.com/docs/agent/tools/search)).
4. **Cross-repository write policy:** project task writes to PBIP only by default; upgrades to normative policy or shared patterns require independent named authority, branch and PR.
5. **Supply chain:** verify versions and hashes; distinguish arbitrary upstream plugin download from source-controlled trusted content; obtain explicit consent before running hooks/scripts or registering live MCP services.
6. **User configuration:** installer-managed code must not take over all user-level agent settings; isolated per-project defaults are safer to reason about.
7. **Public/private composition:** Architect is public and engineering standards are currently private. A public GitHub Actions run or PR can reveal logs/artifacts even if only a restricted token can clone a private dependency; perform an explicit classification/review before enabling automated jobs.
8. **Capability degradation:** if a host lacks a private-repo or model-inspection tool, stop or mark that workflow unsupported; do not fabricate standards compliance.

**UNTESTED:** actual GitHub/enterprise sharing policy, selected Windows workstation auth, availability of a private dependency from Cursor Cloud Agents, runtime host plugin/skill distribution and data governance approvals. These are implementation gates.

## 9. Decision comparison matrix

Scores are **qualitative, not measured performance results**. "Strong" means supported *by the proposed design* if verified; it is not a claim of working software.

| Criterion | Manual A | Workspace-only B | Submodules C | Plugin-only E | Pinned resolver + generator G | Full framework H |
|---|---|---|---|---|---|---|
| Low first-use burden | Weak | Medium | Medium | Strong when available | Strong after implementation | Strong after high build cost |
| Source-of-truth boundaries | Medium | Strong | Strong | Medium (bundle drift risk) | **Strong** | Strong |
| Exact per-project pin / reproducibility | Weak | Weak | **Strong** | Partial; plugin version only | **Strong** | Strong |
| Private dependency authentication | Manual | Manual | Requires separate setup | Plugin dependent | Explicit/checked | Explicit/checked |
| Local Cursor multi-root | Manual | **Good** | Single nested root option | Not automatic | **Generated** | Generated |
| Single-root cloud/CI path | Manual | **Unsupported for Cursor Cloud** | Possible with auth | Not guaranteed | Candidate renderer/provider | Candidate renderer |
| Cross-agent portability | Weak | Cursor-only | Git portable; host routing missing | Adapter dependent | Host-neutral manifest + adapters | Rich but complex |
| Safe local modification/update | Manual | N/A | Git submodule update workflow | Platform lifecycle | **Managed-state hash + explicit plan** | Strong at high cost |
| No hidden duplicate skills | Manual check | Not managed | Not managed | Depends | Preflight logical-ID collision check | Managed |
| Initial build/maintenance cost | Low / recurring toil | Low | Low code / Git training | Marketplace burden | **Moderate** | **Very high** |
| Fit for embedded P&R team | Short-lived pilot | Good local UX | Conditional | Later | **Preferred evolution** | Premature |

**R5 recommendation:** B for the **local editor experience**, with G as the **underlying reproducibility and installation contract**. Build G in narrow phases with a Python CLI once manual local and project checks establish a concrete use case. E/F become optional distribution modes for managed capability packages after R6/R8, not substitutes for project dependency resolution.

## 10. Recommended phased installation architecture

### Phase 0 — baseline and proof (before CLI)

Deliver a **single reproducible manual runbook** and small PBIP test fixture:

- Use independent Git clones and a local Cursor multi-root workspace (B).
- Record exact Architect/standards/library SHA values in a *prototype checked project manifest*.
- Demonstrate ability to read a named measure standard, inspect a test PBIP/TMDL measure, propose a change only in PBIP and compare independent checks.
- Document the current manual auth requirements for the private standards repo.
- Record which parts of the proposed manifest/adapter contract are missing.

**Gate 0:** C1/C3/C5/C6/C9/C10/C11 from R4 and P3/P4/P5/P7/P11/P12 from R7 pass where executable; missing tests are explicit blockers, not silent successes. No source mutation in this research ticket.

### Phase 1 — minimal local bootstrap (first recommended implementation)

A small Python command-line utility, no always-running server and no required native plugin:

- `doctor`: check prerequisites, repo access, Git refs, project paths, conflicting installs and existing user-owned instructions.
- `init/plan`: read an approved manifest; fetch/resolve specified SHAs; calculate candidate changes; detect path, classification and duplicate conflicts.
- `apply`: safe, idempotent and transactionally tracked generation of an optional relative-path `.code-workspace`, minimal host routing assets and local install state.
- `verify`: compare installed SHA/hash to required SHA, verify references/permissions; run a small non-AI measure-metadata conformance fixture.
- `uninstall`: remove only unchanged managed projections and leave user work intact.

**Gate 1:** repeated apply is a no-op; wrong private permissions fail closed; locally modified managed files are preserved; induced failure rolls back; Windows path/encoding/checkout tests pass; source/target Git status shows no unexpected writes. Only after this gate may "local bootstrap supported" be claimed.

### Phase 2 — managed team consumption and upgrades

- Explicit **editable** (contributor) vs **managed** (consumer) install channels, per component.
- Reviewable **dependency upgrade PR**, separate installed-state and locked version; no silent standards updates.
- Generated adapters for Cursor first, then Codex/Claude based on validated R7 capability matrix.
- Optional host plugin and skill installer integration only after duplicate-channel protection and shared-reference tests.
- Release/compatibility policy aligned with R6 (standards revision, skill capability version, asset version and installer version independent).

**Gate 2:** upgrade/rollback preserves PBIP and user modifications, verifies the correct private standards revision and supports a second P&R product without hard-coded local paths.

### Phase 3 — single-root Cloud/CI and distribution

- Select **one tested** method for single-root/cloud: ephemeral pinned checkout or authenticated source resolver.
- CI auth via narrowly scoped credentials and explicit private repo access; confidentiality checks for logs/artifacts/PRs.
- Host-independent validation runner and evidence schema.
- Assess Cursor Plugin or other marketplaces *only if* team installation friction and support scale justify packaging.
- Full Agent/Cloud support claimed **only when** end-to-end approved private access, host discovery and PBIP validation tests pass.

**Gate 3:** same representative PBIP fixture and approved standards/asset revisions produce matching deterministic validation evidence locally and remotely, with no leakage in public outputs.

### Recommended first implementation ticket after R8

**"Prototype Architect bootstrap: doctor + pinned dependency manifest + Cursor local workspace"**. Scope intentionally excludes plugin marketplace, general package registry, remote cloud deployments, generated large AGENTS.md, auto-changing production PBIP models and DAX refactors.

Suggested acceptance criteria:
1. Accept an existing PBIP repo and an immutable standards/library/Architect SHA set.
2. Verify access to the private standards repo and required semantic-model README/measure-standard path.
3. Generate one relative-path workspace and identify the PBIP **write root**; no changes to the source repos.
4. Produce a machine-readable `doctor` report and installed-state manifest with content digests.
5. Refuse wrong SHA, missing auth, duplicate installation and path escape; never fall back to HEAD.
6. Demonstrate rerun idempotence, rollback of an injected failure and preserving manually edited files.
7. Supply one deterministic test against a small fixture and a privacy review of any public output.
8. Prove the exact test outputs under supported Windows environment (team default), not just Linux.

This prototype is **not started** by R5; it is a candidate for R8/implementation planning.

## 11. Unresolved questions and decision handoffs

### For R8 — final architecture synthesis (#17)

- Does Architect truly need a Python CLI in the initial release, or should documented manual phase 0 remain until two pilot consumers prove the pain? R5 **recommends** CLI, but this is a value/cost decision.
- Precisely where do the resolver and lifecycle state live: Architect repo tooling, a separately distributed package, or a minimal project-side bridge?
- How does the single-root Cursor Cloud Agent access pinned **private** normative policy without unsafe public materialisation?
- Which subset of Skills/Rules/AGENTS.md ships by default, and which native Cursor enhancements are optional?
- How much of managed materialisation is required before public/team release?
- Should generated local editor workspace files be ignored/user-local or versioned templates, given different checkout locations and access permissions?

### For R6 — standards and reusable-library packaging (#16; PR #19 open)

- Approve stable logical standard/asset IDs, index/entrypoint metadata and normative version compatibility policy.
- Select implementation library export/package format and when npm/GitHub Packages makes sense; the **Python installer is not a universal substitute** for executable library packaging.
- Define provenance for generated adapter/skill material and relationships among standards, domain, package, Skill and installer versions.
- Avoid "installing one skill" when its shared references and supporting assets were not included.

### For domain authority (#6)

- Decide which parts of the seven migrated semantic-model **domain extensions** are representation policy vs business semantic content before automatically generating domain-aware conventions.
- Keep the original files canonical during post-migration classification; no unsolicited rewrite in an installer.

### Real-environment unknowns

- The actual operating systems of all team members and policy limits around installing Git/Python/CLI/extension tools.
- Whether existing corporate GitHub/Cursor auth can read the private standards repo from supported remote hosts.
- Whether product repositories will be private/public and who can access their CI logs/artifacts.
- The minimum portable model-inspection capability for PBIP/TMDL and accepted deterministic validation toolset.
- Actual collision behaviour among Microsoft-maintained skills, Architect skills and a user's existing agent customisations.
- Whether a local `.code-workspace` can provide the right developer ergonomics without disabling a critical Cursor worktree workflow.

**Research conclusion:** Architect should treat bootstrap as a **small, reversible source-and-adapter provisioning utility**, not as the normative content author, plugin marketplace or an alternative model runtime. Begin with sibling checkouts and a local Cursor multi-root pilot; advance to a pinned, Python-based `doctor/plan/apply/verify` utility after validation. Support managed and editable modes explicitly, and use a separate, tested single-root path for cloud/CI. The final decision remains R8's.

## 12. Evidence register

**Stored Architect research and constraints:**

- [R2 — Harness, agent, skill, plugin classification](02-harness-agent-skill-plugin.md).
- [R3 — Benchmark of six reference repositories](03-reference-repo-benchmark.md), especially §§14–16: managed vs editable, Spec Kit, installer state and release/versioning.
- [R4 — Cross-repo composition](04-cross-repo-composition.md), merged from PR #23: local Cursor multi-root vs cloud/CI; pinned manifest candidate; no canonical duplication.
- [R7 — Cross-agent portability](07-cross-agent-portability.md), merged from PR #24: portable SKILL.md, compact AGENTS.md, generated host adapters, independent conformance checks.
- [ADR-0001](../../docs/decisions/0001-canonical-standards-home.md): canonical standards repository decision; accepted and migration complete.
- [R6 draft PR #19](https://github.com/GitKlink/performance-reward-dashboard-architect/pull/19): packaging research only; not an approved dependency/registry decision.

**Current first-party / reference documentation, checked 19 October 2026:**

- [Cursor Search FAQ](https://cursor.com/docs/agent/tools/search): multi-root local support and Cloud Agent limitation; file read/model context privacy distinction.
- [Cursor Plugins](https://cursor.com/docs/plugins): installable native distribution surface, not a cross-repository lock.
- [Cursor Rules](https://cursor.com/docs/rules) and [Skills](https://cursor.com/docs/skills): instructions vs progressively loaded capability.
- [VS Code multi-root](https://code.visualstudio.com/docs/editing/workspaces/multi-root-workspaces): relative-path `.code-workspace` format.
- [GitHub actions/checkout](https://github.com/actions/checkout#checkout-multiple-repos-private): private second repository requires specifically authorised token; native workflow token is scoped to triggering repository.
- [GitHub sharing private actions/workflows](https://docs.github.com/en/actions/how-tos/reuse-automations/share-across-private-repositories): warning that logs can expose information to outside collaborators.
- [GitHub Spec Kit integrations](https://github.com/github/spec-kit/blob/main/docs/reference/integrations.md): integration install, report/status, hash-aware upgrades, file preservation, rollback.
- [Spec Kit installation/ownership design](https://github.com/github/spec-kit/blob/main/design/integration.md): managed ownership, local trust boundaries, transaction lifecycle.
- [Matt Pocock canonical install guidance](https://github.com/mattpocock/skills/blob/main/.agents/install-block.md): managed/plugin vs editable skills installation, duplicate-installation warning.
- [Git Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules): gitlinks and explicit recursive dependency initialization.

**Research integrity:** this work reviewed official docs, the prior durable R1–R4/R7 research and reference implementation mechanisms. No Architect installer, manifest validator, multi-root setup script, private CI checkout, Cloud Agent launch, Codex/Claude installation, or real PBIP validation was executed. All installer commands and data schemas above are **illustrative recommendations** only.
