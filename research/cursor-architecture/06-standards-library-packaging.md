# Research R6 — Standards and reusable-library packaging

**Research ticket:** R6  
**Evidence snapshot:** 2026-09-16; **Power BI domain-fit review:** 2026-10-22  
**Status:** Research recommendation; not yet a normative implementation standard. October review narrows JS/npm claims to applicable runtime components; see the mandatory §20 correction.  
**Question:** How should standards and reusable libraries be packaged and consumed?

## 1. Executive summary

The ORIGINAL candidate architecture was **registry-first, content-aware, and ESM-first**; **for Wayfinder's actual DAX/M/Python/Deneb-first library, this is not the universal recommendation**. The domain-specific correction in §20 supersedes the executable-package and public-registry generalisation below:

> **Canonical standards remain canonical content; reusable executable assets become conventional packages; Cursor receives only a thin discovery/routing layer.**

This preserves the settled distinction from the earlier Cursor research between **canonical knowledge** and the **mechanism that discovers, routes, or activates that knowledge**. R6 therefore does not move standards into persistent Cursor Rules, agent prompts, or skill bodies merely for distribution convenience.

The baseline packaging model should distinguish four artifact classes:

| Artifact class | Recommended packaging | Runtime contract |
|---|---|---|
| Engineering standards | Versioned content package containing Markdown, schemas, manifests, and examples | No runtime required; optional tiny resolver API |
| Reusable implementations | **Native DAX, M, Python, and Deneb source assets** with indexed metadata; JS/TS package only for independently reusable JS/TS components | Native artifact + tests/compatibility metadata; ESM + .d.ts only for JS/TS modules (see §20) |
| Shared contracts | Separate package only where schemas/types are independently consumed | Types/schema only as required |
| Cursor integration | Thin Plugin/Skill/bootstrap/router layer | Discovers installed canonical packages; does not duplicate them |

For executable packages, use explicit `"type": "module"`, a deliberately narrow `"exports"` map, generated TypeScript declarations, a `"files"` allow-list, minimal runtime dependencies, and pure modules wherever practical. Node positions `"exports"` as the modern package public-surface mechanism and allows it to prevent arbitrary undeclared deep imports. TypeScript recommends shipping declarations with typed packages.

> **October 2026 scope override:** do not interpret the JS/TS build, npm registry or bundler material in §§5–11 as general requirements for DAX measures/UDFs, M functions, Python or Deneb. They apply only if a consumer-facing JS/TS executable package is justified. Our existing implementation library is not a JS/TS application package.

### Recommended format baseline

- **ESM:** yes **for JS/TS packages only**; not the default format for DAX/M/Python/Deneb.
- **TypeScript declarations:** yes **for typed JS/TS APIs**; irrelevant to native DAX/M/Python/Deneb artifacts.
- **CommonJS:** only when an audited consumer still requires `require()`.
- **UMD/IIFE:** not part of the baseline; add only for a demonstrated classic-browser script use case.
- **Raw assets:** yes where consumers need native DAX/M/JSON/Markdown/schema content rather than JavaScript wrappers.

### Recommended distribution baseline

- **npm:** a candidate registry **for public JS/TS packages only**, not the canonical distribution path for native Power BI assets or private engineering standards.
- **GitHub Packages:** use for genuinely private/internal packages where access should follow GitHub permissions.
- **CDN:** optional derivative delivery from a published npm version; never a separate authority/version stream.
- **Git URLs:** preview/escape hatch only; not the stable release interface.
- **Submodules/subtrees:** source composition only; not normal released-library consumption.

> **Actual repository fit (2026-10-22):** [GitKlink/dax-m-query-library](https://github.com/GitKlink/dax-m-query-library) currently contains native-asset families at `library/dax`, `library/m`, `library/python`, `library/deneb` and no published JavaScript package surface. [GitKlink/power-bi-fabric-standards](https://github.com/GitKlink/power-bi-fabric-standards) is private and stores authoritative Markdown standards. A mandatory public npm mirror would add needless wrapping and potential confidentiality exposure.

### Recommended repository model

Use a **workspace monorepo within a single authority boundary** where packages share ownership, CI, fixtures, and release governance. Do **not** collapse repositories whose authority boundaries were already established by the cross-repository research. Between authorities, compose with versioned packages and explicit dependency contracts.

### Recommended release model

Use SemVer with **independent package versions by default**, with Changesets or an equivalent release tool capturing patch/minor/major intent and changelog entries. Fixed/linked version groups should be exceptional and limited to packages that are operationally inseparable.

For standards, SemVer must describe **normative compatibility**, not merely file/API syntax. If a standards change makes previously conformant output non-conformant, that is normally a breaking change and should be treated as a major version.

### Recommended security model

Publish through **trusted publishing/OIDC** rather than long-lived registry write tokens where the registry supports it. Attach provenance/attestations to releases and verify package shape and provenance in CI.

The target architecture is therefore:

```text
authoritative source repository/repositories
        │
        ├── standards content ──────────────> @org/architect-standards
        │                                  Markdown / schemas / manifest
        │
        ├── reusable assets/code ──────────> @org/pbi-pattern-library
        │                                  ESM + types + raw assets
        │
        └── shared contracts ──────────────> @org/architect-contracts
                                           only if independently reusable
                         │
                         ▼
                   package registry
                         │
              ┌──────────┼───────────┐
              ▼          ▼           ▼
        Architect repo  PBIP repo   optional browser/CDN
              │          │
              └──── thin Cursor adapter/router ────┘
                     no copied standards
```

This best satisfies the required goals:

- **discoverability** → stable package names + stable asset IDs + machine-readable manifests;
- **stability** → SemVer + explicit public surfaces + deprecation policy;
- **ease of consumption** → normal package-manager installation and lockfiles;
- **cross-repo composition** → released versions + packed-package tests + explicit dependency contracts;
- **minimal runtime overhead** → content-first standards, ESM-first executable code, minimal dependencies, no automatic copying of standards into consumers.

---

## 2. Scope and settled context

R6 answers only the remaining packaging/consumption question. It does **not** reopen earlier architectural decisions unless contradictory evidence appears.

The following prior findings are treated as settled inputs:

1. **Cursor primitives have different context and authority characteristics.** Rules, AGENTS instructions, Skills, Agents/subagents, Hooks, MCP, Plugins, and ordinary repository files are not interchangeable.
2. **Canonical knowledge does not need to live in the primitive that routes to it.** A small Cursor-facing discovery layer can point to larger canonical standards or implementation assets.
3. **Plugins are distribution/composition units rather than the sole runtime model.** Packaging strategy should not assume “put everything in a plugin” is equivalent to a sound information architecture.
4. **Cross-repository boundaries should follow authority and lifecycle, not convenience.** Repositories with distinct authority, ownership, release cadence, or security boundaries should remain separable and compose through contracts.
5. **Progressive loading is preferred.** Installing a package must not imply injecting its full content into persistent model context.

No new evidence found in R6 contradicts those findings.

---

## 3. Design goals and decision tests

The packaging design should be judged against five goals.

| Goal | Required packaging property | Concrete success test |
|---|---|---|
| Discoverability | Stable package names, stable asset IDs, machine-readable manifests | Consumer finds an asset without knowing repository layout |
| Stability | Explicit public surface, SemVer, deprecation policy | Compatible upgrade preserves declared behavior |
| Ease of consumption | Conventional install/update flow | No bespoke clone or sibling-repo requirement |
| Cross-repo composition | Registry versions, lockfiles, package-level contracts | Consumer works without producer source checkout |
| Minimal runtime overhead | Content-first standards; minimal executable dependencies | Standards impose no application runtime cost |

A major architectural point follows:

> **The logical public API should be the package manifest and stable asset identifiers, not the repository’s physical directory tree.**

A standards consumer should be able to request `semantic-model.naming` without knowing that the document currently lives at `standards/semantic-model/naming.md`.

Example manifest:

```json
{
  "schemaVersion": "1",
  "packageVersion": "1.4.0",
  "standards": [
    {
      "id": "semantic-model.naming",
      "kind": "normative",
      "path": "standards/semantic-model/naming.md",
      "title": "Semantic model naming",
      "tags": ["semantic-model", "naming"]
    }
  ]
}
```

The manifest is part of the package contract. Stable IDs and schema semantics therefore require compatibility governance just like exported functions.

---

## 4. Package boundaries

Package boundaries should follow **authority, compatibility, ownership, and consumption**, not folders.

Recommended initial logical boundaries:

| Package | Intended contents | Runtime |
|---|---|---|
| `@org/architect-standards` | Canonical Markdown, schemas, examples, metadata, manifest | None required |
| `@org/pbi-pattern-library` | DAX/M/Python/Deneb assets, metadata, optional resolver/search API | ESM |
| `@org/architect-contracts` | Shared schemas/types used by more than one independently released package | Types/schema oriented |
| Internal build/test/config helpers | CI utilities, fixtures, validators, build configuration | Private; not published |

A new package should exist only when there is a clear reason for **independent ownership, consumption, compatibility, or versioning**. Package-per-folder designs create release and dependency complexity without useful isolation.

### 4.1 Standards should be content-first

Standards are primarily knowledge artifacts. Wrapping every Markdown file in JavaScript would add code surface without increasing authority or clarity.

The standards package should therefore publish:

- native Markdown;
- JSON/YAML manifests;
- JSON Schema or equivalent contracts;
- examples and fixtures where useful;
- optional generated catalog/index files;
- an optional tiny resolver API for consumers that want functions such as `resolveStandard(id)`.

The resolver is an index into the content. It is **not** the authority itself.

A standards package should ideally have **zero runtime dependencies**.

### 4.2 Reusable implementation libraries should be native-package first

Reusable executable assets should use conventional package semantics so ordinary developer tooling can reason about them.

A reasonable ESM-first package shape is:

```json
{
  "name": "@org/pbi-pattern-library",
  "version": "1.0.0",
  "type": "module",
  "types": "./dist/index.d.ts",
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "default": "./dist/index.js"
    },
    "./manifest": {
      "types": "./dist/manifest.d.ts",
      "default": "./dist/manifest.js"
    }
  },
  "files": [
    "dist",
    "assets",
    "README.md",
    "LICENSE"
  ],
  "sideEffects": false
}
```

The contract is not this exact JSON. The important properties are:

- explicit module type;
- narrow documented entry points;
- generated declarations for typed entry points;
- an allow-listed publication artifact;
- no reliance on consumers importing internal build paths.

### 4.3 Do not make repository layout part of the public API

Avoid supported imports such as:

```text
@org/pbi-pattern-library/dist/internal/dax/security/headcount.js
```

Instead expose stable public entry points or stable asset IDs.

Introducing an `exports` map into an existing package can itself be breaking if consumers already use undeclared deep paths. Before tightening an existing package, inventory real consumers.

---

## 5. Module-format decision

### 5.1 ESM should be the baseline

ES modules are the modern JavaScript module standard and are supported directly by current Node releases and modern browser tooling.

Benefits for this architecture:

- simpler baseline than dual-format publishing;
- aligns with modern Node and TypeScript tooling;
- supports static analysis and tree shaking;
- avoids maintaining two module identities by default;
- clean fit for small resolver/search utilities around non-JS assets.

### 5.2 CommonJS should be evidence-driven

Support both ESM and CommonJS only where a real consumer cannot reasonably migrate.

Dual publishing increases the compatibility matrix:

- two runtime module forms;
- conditional export logic;
- matching declaration behavior;
- duplicate integration tests;
- greater risk of dual-package hazards and divergent behavior.

Therefore new packages should begin ESM-only and add CJS only after consumer inventory demonstrates need.

### 5.3 UMD/IIFE should not be baseline output

UMD/IIFE is justified only for a real legacy or classic `<script>` browser integration.

For modern browsers, ESM with import maps is a cleaner route where direct browser delivery is needed.

---

## 6. Build-tool recommendation

Use **the minimum transformation required by the declared runtime contract**.

| Tool | Correct role | Recommendation |
|---|---|---|
| `tsc` | Type checking and declaration generation; possibly direct ESM emission | Baseline |
| Rollup | Multi-format builds, controlled bundles, browser/UMD artifacts | Preferred optional bundler |
| esbuild | Fast application/CLI/browser bundles | Strong optional choice; pair with `tsc` for declarations |
| Babel | Syntax transformation for explicit runtime targets | Conditional only |
| tsup | Convenience bundler wrapper | Do not adopt as new baseline |

`tsup` should not be selected for a new long-lived architecture because its upstream project currently states that it is no longer actively maintained and recommends migration to `tsdown`.

For an ESM-first package, begin with a simple pipeline:

```text
tsc --noEmit
      ↓
tsc build / declaration emit
      ↓
unit + contract tests
      ↓
package lint
      ↓
npm pack
      ↓
install packed tarball into clean consumers
```

Only add Rollup/esbuild where an actual required artifact—such as CJS, a browser bundle, or a single-file executable—justifies it.

---

## 7. Dependency policy

Dependency classes should be explicit.

- build tools, compilers, test frameworks, documentation generators → `devDependencies`;
- real runtime implementation requirements → `dependencies`;
- host/framework compatibility supplied by the consumer → `peerDependencies`;
- genuinely optional peers → `peerDependenciesMeta`;
- bundled dependencies → avoid except for explicit offline/vendor scenarios.

The standards package should target **zero runtime dependencies**.

The implementation library should target **zero or very few runtime dependencies**.

Bundled dependencies deserve particular scrutiny because they become part of the distributed artifact’s direct size, patching, and licensing responsibility.

---

## 8. Distribution strategy

### 8.1 npm as the canonical public registry

For public packages, npm should be the canonical released identity:

```text
package name + version
```

A registry gives consumers:

- immutable released versions;
- standard install/update workflows;
- integrity metadata;
- lockfile integration;
- dependency graph tooling;
- established release/provenance support.

### 8.2 GitHub Packages for private/internal access control

Use GitHub Packages when a package is genuinely private or when access should align to GitHub organization/repository permissions.

Do not mirror every public package into two canonical registries by default. Multiple authorities create divergence and configuration cost.

### 8.3 CDN as derivative delivery only

If browser delivery becomes useful, CDN URLs should derive from the same published package version.

Do not create a separate CDN release/version stream.

Pin production browser consumption to explicit versions rather than implicitly tracking `latest`.

### 8.4 Git dependencies are previews, not stable releases

Git URLs can be useful for preview testing, but they should not be the normal stable interface.

If a Git dependency is temporarily required, pin a commit SHA rather than a moving branch.

### 8.5 Submodules/subtrees are source composition, not library distribution

Submodules remain valid where source-level composition is intentional, but consumers should not need a submodule merely to use a stable released standard or implementation library.

---

## 9. Monorepo versus multi-repo

The answer is **not one or the other universally**.

### 9.1 Use a workspace monorepo inside one authority

A monorepo is preferred where packages share:

- ownership;
- governance;
- CI and fixtures;
- release tooling;
- security boundary;
- coordinated development.

Example:

```text
repository/
  packages/
    architect-standards/
    pbi-pattern-library/
    architect-contracts/
  fixtures/
  .changeset/
  shared-ci/
```

npm workspaces or an equivalent workspace mechanism simplify local linking and shared package development.

### 9.2 Preserve separate repositories across authority boundaries

Where prior cross-repository research established distinct authorities, preserve those repositories.

Versioned packages become the bridge:

```text
standards repo ──> @org/architect-standards ─┐
                                               ├──> Architect / PBIP consumers
library repo ───> @org/pbi-pattern-library ──┘
```

This preserves governance separation without forcing consumers to clone or understand producer repositories.

---

## 10. Versioning and release governance

### 10.1 Independent versions by default

Standards and implementation packages are likely to evolve on different cadences. Lockstep repository-wide versioning therefore creates unnecessary churn.

Use independent versions unless packages are operationally inseparable.

Changesets is a strong fit because it is designed for multi-package versioning, changelogs, dependency updates, and fixed/linked groups when needed.

### 10.2 SemVer for standards must model semantic compatibility

For standards, compatibility is not merely API syntax.

Suggested interpretation:

| Standards change | Version impact |
|---|---|
| Typo/format/link correction with no semantic effect | Patch |
| Clarification with unchanged requirement | Patch |
| New optional guidance/example | Minor |
| New independent domain/standard | Minor |
| New normative requirement that invalidates previously conformant output | **Major** |
| Removal/rename of stable standard ID | **Major** |
| Breaking manifest/schema change | **Major** |
| Behavior-changing correction to an existing normative rule | Normally **major** |

The claim “it is only documentation” must not allow compatibility-breaking normative changes into minor versions. In this architecture, normative documents influence validation and agent decisions and are therefore observable contract surface.

### 10.3 Deprecation policy

A public symbol, export path, standard ID, or manifest field should:

1. be marked deprecated;
2. document its replacement;
3. remain functional for the current major line;
4. be removed only at the next major, except for security/safety reasons.

Stable standard IDs should never be reassigned to a different concept.

---

## 11. Consumption model

Supported consumption methods should have a clear hierarchy.

### 11.1 Primary: registry installation

```text
npm install @org/architect-standards
npm install @org/pbi-pattern-library
```

Consumers commit their lockfile and use their normal dependency workflow.

### 11.2 Development: workspace/local linking

Local paths/workspaces are appropriate while producer and consumer change together locally.

They are **not** the release architecture.

### 11.3 Pre-release verification: packed tarballs

Cross-repo tests should install the actual tarball generated by `npm pack`, for example:

```text
@org/pbi-pattern-library-1.3.0.tgz
```

This catches failures that workspace/source imports can hide:

- missing generated files;
- invalid export maps;
- undeclared runtime dependencies;
- accidental dependence on unpublished source;
- wrong package contents.

### 11.4 Browser: CDN/import map only when required

If browser ESM becomes a supported use case, map bare module names to explicit versioned URLs with import maps or a bundler.

Do not add UMD speculatively.

### 11.5 Cursor consumption: explicit discovery, not persistent injection

Package installation solves **identity and reproducibility**. It should not automatically inject all standards into Cursor context.

Preferred flow:

```text
npm install @org/architect-standards
        ↓
explicit architect bootstrap/discovery
        ↓
small local dependency manifest
(package + version + selected IDs)
        ↓
Cursor router resolves canonical content on demand
```

Avoid:

```text
npm install
        ↓
postinstall copies all standards into ./docs/standards
```

The latter creates duplicate apparent authorities and obscures update state.

---

## 12. Discoverability contract

Discoverability should be machine-readable and stable.

Each package should expose:

- package name and version;
- schema version;
- stable asset IDs;
- artifact kind (`normative`, `guidance`, `example`, `implementation`, etc.);
- title/summary;
- tags/domains;
- path or resolver target;
- optional dependency relationships;
- deprecation metadata;
- optional compatibility metadata.

Example:

```json
{
  "schemaVersion": "1",
  "packageVersion": "1.4.0",
  "assets": [
    {
      "id": "dax.security.suppress-small-n",
      "kind": "implementation",
      "language": "dax",
      "path": "assets/dax/security/suppress-small-n.dax",
      "tags": ["security", "privacy", "matrix"]
    }
  ]
}
```

Consumers should reference `dax.security.suppress-small-n`, not a brittle internal folder path.

---

## 13. Testing and compatibility gates

Package shape should be a first-class CI artifact.

Recommended test matrix:

| Test | Purpose |
|---|---|
| Unit tests | Validate executable behavior |
| Standards validation | Unique IDs, valid links, manifest/schema correctness |
| `npm pack --dry-run` | Verify exactly what will ship |
| Packed ESM fixture | Validate actual `import` consumption |
| Packed CJS fixture | Only where CJS is supported |
| Packed TypeScript fixture | Compile real public declarations |
| Cross-repo integration | Install package into representative Architect/PBIP consumer |
| Upgrade test | Validate N → N+1 compatible upgrade |
| Tree-shaking test | Confirm narrow imports do not execute/include unrelated code |
| Package benchmark | Tarball size, installed size, runtime dependency count |
| Runtime benchmark | Import/startup cost where runtime code exists |
| Browser test | Only if browser is a supported target |
| Release security smoke test | Verify provenance/signatures after publication |

`publint` is a suitable package-shape gate for package metadata/export compatibility. For mature public TypeScript APIs, API Extractor or an equivalent API-diff tool can make accidental API changes reviewable.

### Release pipeline

```text
PR change
   ↓
changeset: patch / minor / major
   ↓
typecheck + unit + schema/manifest validation
   ↓
build
   ↓
publint + npm pack --dry-run + content/size checks
   ↓
install packed tarball into clean fixtures
   ↓
cross-repo composition tests
   ↓
protected merge
   ↓
release PR / version update
   ↓
trusted publish + provenance
   ↓
tag + release notes + migration docs
   ↓
post-release install/provenance smoke test
```

---

## 14. Documentation contract

Documentation is part of discoverability and compatibility.

Each published package should include a registry-visible README covering:

- purpose and non-goals;
- installation;
- supported runtimes;
- public entry points;
- manifest/discovery usage;
- versioning and deprecation rules;
- examples;
- changelog;
- migration guidance;
- security reporting;
- licensing.

Examples should be executable in CI wherever practical rather than remaining untested prose.

For standards packages, metadata and documentation must make the distinction between:

- **normative requirement**;
- **guidance**;
- **example**;
- **implementation**.

Cursor and other tools should not infer authority from filenames or directory placement.

---

## 15. Supply-chain security and provenance

Where supported, prefer trusted publishing/OIDC over long-lived registry write tokens.

Recommended controls:

- protected release workflow;
- short-lived OIDC publishing credentials;
- provenance/attestation generation;
- registry integrity/signature verification;
- artifact/package-content checks before publish;
- branch protections for release source;
- explicit license metadata and license files;
- dependency and license review for bundled/vendored content.

GitHub artifact attestations are useful for separately downloadable artifacts. They supplement, rather than replace, registry-native provenance.

An attestation proves origin/build provenance; it does not prove that code is intrinsically safe or correct.

---

## 16. Failure modes and mitigations

### Failure mode 1 — copied standards become a second authority

**Symptom:** consumer repositories contain copied standards that drift from the canonical source.

**Mitigation:** install versioned package; store only package/version/selected-ID references locally; resolve canonical content on demand.

### Failure mode 2 — physical paths become permanent public API

**Symptom:** consumers depend on repository or `dist/internal/...` paths.

**Mitigation:** stable IDs + explicit exports + manifest-driven resolution.

### Failure mode 3 — compatibility surface explodes

**Symptom:** new library publishes ESM, CJS, UMD, several registries, and several CDN variants before any consumer requires them.

**Mitigation:** start ESM-first and add compatibility outputs only from evidence.

### Failure mode 4 — workspace tests hide broken packages

**Symptom:** producer/consumer tests pass locally but released tarball fails.

**Mitigation:** pack the real package and install it into clean fixture consumers.

### Failure mode 5 — standards changes bypass SemVer because “it is documentation”

**Symptom:** a minor version introduces a new mandatory rule that invalidates previously valid output.

**Mitigation:** define normative compatibility explicitly; breaking normative changes are major.

### Failure mode 6 — release automation becomes release authority

**Symptom:** tool automatically publishes breaking or high-impact standards without deliberate review.

**Mitigation:** automate build/version/provenance, but preserve explicit approval for major/high-impact normative releases.

### Failure mode 7 — multiple registries create ambiguity

**Symptom:** npm and GitHub Packages both claim to be canonical for the same public artifact.

**Mitigation:** one canonical registry per package class; use secondary channels only for a specific private/access need.

### Failure mode 8 — runtime package becomes the standards authority

**Symptom:** standards exist only as generated JS objects or embedded prompt text.

**Mitigation:** keep canonical native Markdown/schema content; resolver code remains a convenience layer.

---

## 17. Migration strategy

Change **consumption boundaries first**. Do not begin by moving repositories around.

Move existing consumers from:

```text
copied standards
sibling-repo path imports
deep dist imports
Git branch dependencies
ad-hoc submodule consumption
```

Toward:

```text
stable package name
        +
version range / lockfile
        +
documented exports or stable asset IDs
        +
thin local Cursor discovery manifest
```

This allows source authority to remain stable while the distribution contract becomes deterministic.

### Short-term pilot

1. Inventory real consumers: Node version, package manager, ESM/CJS, browser use, deep imports, local paths, Git/submodule dependencies.
2. Confirm the initial package boundaries: standards, implementation library, optional contracts.
3. Define stable standards/asset IDs and manifest schema.
4. Add explicit package metadata: `type`, `exports`, `files`, `engines`, license, repository.
5. Implement ESM-first builds with `tsc`.
6. Add package-shape checks, `npm pack --dry-run`, packed fixture tests, and package-size measurement.
7. Add one real cross-repository consumer test.
8. Introduce Changesets or equivalent release-intent tooling.
9. Configure trusted publishing/OIDC.
10. Migrate one representative downstream repository and remove copied/path-coupled assets from that consumer.

**Completion check:** a separate repository can install the package, discover a standard through a stable ID, consume the public implementation API, and pass tests without access to sibling source repositories.

### Medium term

- migrate remaining active consumers;
- establish supported runtime/package-manager matrix;
- add API-diff checks for public typed APIs;
- test compatible upgrades automatically;
- publish migration guides for old deep imports and file paths;
- generate standards/catalog documentation from manifests;
- add CJS only if real consumers require it;
- define package-size/runtime budgets from measured baselines;
- add GitHub Packages only for genuinely private artifacts.

### Long term, evidence-triggered

Potential additions:

- CDN/import-map browser delivery;
- UMD only for an actual legacy global-script consumer;
- stronger SBOM/attestation policy where governance requires it;
- shared reusable release workflows across repositories;
- downstream canary tests against release candidates;
- compatibility/adoption dashboards;
- codemods for major API migrations;
- a standards-baseline approval mechanism distinguishing a dependency update from acceptance of new normative obligations.

---

## 18. Recommended architecture decision for later ADR/design work

R6 is research, not the final target-architecture ADR. **Revised after repository/domain-fit audit on 22 October 2026:**

> **Keep canonical standards content-first in their private Git authority. Keep DAX, M, Python and Deneb implementations in their native formats with discoverable stable asset IDs, required dependencies and independently tested examples. Consume approved immutable source revisions initially; decide whether and when release bundles, Python packages, JS/TS packages, or an agent plugin are valuable separately, by asset type. ESM + TypeScript declarations and npm distribution are suitable for an actual JS/TS module API only, not a mandatory baseline for these analytical assets.**

Before declaring a stable `1.0` package contract, explicitly decide:

- public/private status and package namespace;
- target Node/runtime support matrix;
- supported package managers;
- whether browser use is first-class;
- whether any real CJS consumer exists;
- maximum package/bundle sizes;
- offline/air-gapped requirements;
- licensing of standards versus implementation code;
- whether consumers require raw-file access;
- governance for accepting normative standards upgrades.

---

## 19. Evidence and references

Primary external references used for R6:

- Node.js package documentation — package `type`, `exports`, conditional exports, package boundaries: https://nodejs.org/api/packages.html
- Node.js release status: https://nodejs.org/en/about/previous-releases
- npm `package.json` / dependency / files / workspace behavior: https://docs.npmjs.com/cli/v12/configuring-npm/package-json/
- npm publish behavior: https://docs.npmjs.com/cli/v12/commands/npm-publish/
- npm Trusted Publishing / OIDC: https://docs.npmjs.com/trusted-publishers/
- npm registry signatures: https://docs.npmjs.com/about-registry-signatures/
- npm signature verification: https://docs.npmjs.com/verifying-registry-signatures/
- TypeScript declaration publishing: https://www.typescriptlang.org/docs/handbook/declaration-files/publishing.html
- TypeScript ESM/CJS declaration behavior: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-7.html
- Semantic Versioning 2.0.0: https://semver.org/
- Changesets: https://github.com/changesets/changesets
- Changesets configuration: https://github.com/changesets/changesets/blob/main/docs/config-file-options.md
- Rollup: https://rollupjs.org/introduction/
- esbuild: https://esbuild.github.io/
- Babel preset-env: https://babeljs.io/docs/babel-preset-env
- tsup maintenance status: https://github.com/egoist/tsup
- GitHub Packages npm registry: https://docs.github.com/packages/working-with-a-github-packages-registry/working-with-the-npm-registry
- GitHub artifact attestations: https://docs.github.com/en/actions/concepts/security/artifact-attestations
- MDN JavaScript modules/import maps: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules
- jsDelivr documentation: https://www.jsdelivr.com/documentation
- UNPKG: https://unpkg.com/
- publint: https://github.com/publint/publint
- API Extractor: https://api-extractor.com/
- Git submodules documentation: https://git-scm.com/book/en/v2/Git-Tools-Submodules

### Prior internal research inputs

R6 is intended to consume, not supersede, the earlier Cursor architecture research:

- `research/cursor-architecture/01-cursor-primitives.md`
- `research/cursor-architecture/03-reference-repo-benchmark.md`
- `research/cursor-architecture/04-cross-repo-composition.md`

Those artifacts remain the source of settled findings about Cursor primitives, reference-repository patterns, authority boundaries, and cross-repository composition. R6 narrows its contribution to packaging, distribution, versioning, discoverability, and consumption contracts.


## 20. Domain-fit correction — native Power BI/Fabric assets (2026-10-22)

**Status:** research correction that **supersedes** generic JS/npm packaging claims elsewhere in §§1, 4–11, 17–18 wherever those claims are presented as the default for all implementation assets. The original JS package evaluation remains useful for a future JS/TS tool or browser-facing companion application; it does not govern the current DAX/M/Python/Deneb library.

### 20.1 Why the correction is necessary

The **real implementation repository** is [GitKlink/dax-m-query-library](https://github.com/GitKlink/dax-m-query-library), with explicit first-class families at `library/dax`, `library/m`, `library/python` and `library/deneb`. Its README says reusable assets are native patterns, functions, scripts, templates, visuals and examples. It currently has no general Node/ESM package tree or export map to constrain. Wrapping each DAX measure or M function into ESM would impose build and runtime concerns unrelated to Power BI's model/query execution semantics.

The **real standards repository**, [GitKlink/power-bi-fabric-standards](https://github.com/GitKlink/power-bi-fabric-standards), is currently **private**. Normative markdown lives there, with no public npm distribution decision. A package registry does not inherently guarantee private source access, model discovery, applicability or safe AI retrieval.

First-party technology confirms the native surfaces:

- [Microsoft PBIP documentation](https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-overview): PBIP projects use text-based reports and semantic-model files.
- [Microsoft semantic-model project structure](https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-dataset/): native TMDL, model definitions and DAX/TMDL scripts.
- [Microsoft DAX UDF guidance](https://learn.microsoft.com/en-us/dax/best-practices/dax-user-defined-functions): DAX functions are model objects, generally available as of June 2026, subject to compatibility level and specific limitations. A DAX UDF is **not** an ESM export.
- [Microsoft Power Query custom functions](https://learn.microsoft.com/en-us/power-query/custom-function): native M function reuse.
- [Vega-Lite spec](https://vega.github.io/vega-lite/docs/spec.html): JSON declarative visual specifications (relevant to Deneb templates).

These references justify asset-type-specific packaging; they do **not** demonstrate an off-the-shelf package registry that can install arbitrary DAX/M/Deneb assets into a semantic model.

### 20.2 Corrected packaging matrix

| Artifact | Canonical home / source format | Initial consumption | Possible later distribution | Validation contract |
|---|---|---|---|---|
| Semantic-model/DAX/M engineering standards | Private standards repo; Markdown, supporting structured metadata | Read *pinned approved Git revision* using a thin router/skill | Versioned standards bundle/index if a proven need | Provenance, scope, normative status, version, conformance tests |
| DAX measures and calculation patterns | `library/dax`; native DAX/TMDL examples/scripts | Explicit asset ID + versioned source read + adapt to project model | Signed/catalogued native snippet or TMDL asset package | Syntax/model compatibility, dependencies, output invariants, golden examples |
| DAX UDFs | `library/dax`; native DAX model function definitions | Approved native source + target model compatibility gate | Native UDF template bundle | Compatibility level, dependency resolution, TMDL/model load and tests |
| Power Query M functions/patterns | `library/m`; native M | Approved text/function with parameters, connectors, privacy/test metadata | Native M template/catalogue | M parsing, refresh/privacy compatibility, representative input/output tests |
| Python helpers | `library/python`; Python source/modules | Git source at pinned SHA with recorded Python dependency versions | Normal `pyproject.toml`/wheel package **if** imports/release consumers justify | Python interpreter/dependency matrix and unit tests |
| Deneb / Vega / Vega-Lite | `library/deneb`; JSON specs/templates | Pinned JSON template + declared data role/schema assumptions | Native JSON/asset bundle | Vega/Vega-Lite schema, data shape and render/visual checks |
| JS/TS adapter, UI or tool | Separate true JS/TS module(s), **if created** | Source or versioned JS package | ESM, typed exports, npm as appropriate | Package exports, build, runtime and dependency tests |
| Wayfinder Skill/adapter | Canonical procedural SKILL.md and host adapter | Host-compatible, progressively loaded from pinned source | Agent Plugin/host packaging if installation value demonstrated | Host discovery + exact authoritative source/version read + validation evidence |

**Research conclusion:** native artifacts require a **catalogue/manifest and compatibility contract**, not necessarily a JavaScript package. A stable logical `asset_id` / `asset_version`, description, language/format, entrypoint, owner, dependencies, model compatibility, required parameters, examples, licence and validation references is a better *candidate* common layer; the schema is not yet approved.

### 20.3 Native-first progressive discovery, not mandatory conversion

Prototype retrieval should follow:

1. The PBIP project declares or resolves **approved immutable source revisions** for standards and library.
2. A small router/Skill identifies task, affected semantic area and required domains; it reads only applicable canonical files.
3. An asset index returns matching reusable DAX/M/Python/Deneb records, preserving their **original native source format**.
4. Wayfinder/host tools inspect the actual model/project, resolve real dependencies and produce a target-local plan, not a blind copy.
5. Execute host-independent validators where possible; compare measure outputs/reconciliations when business meaning or DAX changes are involved.
6. Log resolved SHAs, asset IDs, domain/standards authority, unsupported assumptions and results.

Avoid hardcoded absolute paths and context-heavy duplication. An index is **generated or reviewed metadata pointing to canonical source**, not a competing standards manual.

### 20.4 Version and security implications

- Initial source pin: exact Git SHA is both implementable and sufficient for reproducible R5 pilot tests. Tags, semantic releases and normative SemVer may be added after governance decides review and adoption rules.
- **Native asset revisions are not automatically coupled:** standards release, DAX snippet revision, UDF compatibility, M function and Python package may all have different lifecycles.
- **Private Git must remain private:** do not automatically push normative content into a public npm registry. A private package registry is an *option*, not an access-control replacement.
- If the language-specific native format has no central executable package manager, an indexed Git source with immutable pins may be preferable to a package solely for the appearance of uniformity.
- Public `dax-m-query-library` examples must remain synthetic, especially for employee/pay/reward concepts.
- npm OIDC/provenance, ESM exports, Changesets, publint and packed-tarball tests from the original paper remain **valid scoped advice for JS/TS packages**. They are not release gates for the current native implementation library.
- No filesystem, Cursor or PBIP pilot was executed as part of this correction; R8 must preserve the experimental gates from R4/R5/R7.

### 20.5 Explicit reconciliation with R4, R5, R7 and the R8 decision

- **R4:** sibling Git clones + local multi-root workspace is a development candidate, not a production dependency manager.
- **R5:** thin Python `doctor / plan / apply / verify` candidate resolves private source and approved commit IDs; a Node/npm installation is **not** a phase-1 prerequisite.
- **R7:** shared procedural SKILL.md and AGENTS.md may be routed by host adapters; native standards content stays outside those prompts.
- **R8:** decide a minimal interoperable asset-catalogue schema, Pin/Manifest v0, installer owner and validation evidence. Test a native DAX/M or semantic-model use case before considering package-registry distribution.

**For R8:** treat the content/ownership/discovery principles of R6 as strong evidence and treat the original mandatory npm/ESM proposal as a **rejected universal default**, while retaining it as an optional JS/TS-specific pattern.
