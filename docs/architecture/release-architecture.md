---
artifact_id: ARCH-CORE-005
status: PLACEHOLDER
phase: 1
priority: high
depends_on:
  - artifact_id: ARCH-CORE-001
    path: agent-architecture.md
  - artifact_id: ARCH-CORE-004
    path: information-architecture.md
  - artifact_id: EX-CORE-002
    path: ../../knowledge/research-register/trials/internal-source-of-truth-decision-trial.md
blocks:
  - PLAN-CORE-003
  - package validation
content_version: 0.1.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Release architecture

## Document state

This is the first substantive draft. The lifecycle status remains `PLACEHOLDER` until package manifests, current Cursor compatibility, and release validation are implemented.

## Purpose

Define how the maintained source repository produces a stable, reproducible, reviewable, and safe release of the Performance & Reward Dashboard Architect.

## Release principles

1. The source repository remains authoritative.
2. A release is derived from a tagged source commit.
3. The runtime package contains only required approved dependencies.
4. Development evidence and incomplete content are excluded unless the package profile explicitly includes them.
5. Package contents are declared in a manifest rather than inferred from folder names alone.
6. Version and compatibility are visible to consumers.
7. No release relies on conversation history.
8. Privacy, confidentiality, copyright, licensing, and supply-chain checks are release gates.
9. Rollback is possible using previous tagged releases.
10. A release candidate must pass the integrated Phase 12 evaluation suite.

## Release products

The repository may produce three package profiles.

### Minimal runtime package

For users who want the agent capabilities with the smallest practical footprint.

Expected contents:

```text
.cursor/
├── rules/
├── agents/
└── skills/
knowledge/               # only files required by packaged skills
schemas/                 # runtime output contracts
 templates/              # templates required by packaged skills
README.md
LICENSE
RELEASE-MANIFEST.yaml
```

This profile excludes development tests, research trials, internal reviews, planning files, and unused examples.

### Standard runtime package

For users who want runtime capabilities plus useful examples and explanatory documentation.

Expected additions:

```text
examples/                # selected approved examples
CHANGELOG.md
MIGRATION.md              # when required
docs/runtime/             # concise user-facing guidance if created
```

### Contributor source package

The tagged source repository itself.

Contains:

- runtime components;
- complete knowledge and evidence trail;
- schemas and templates;
- examples and evaluations;
- tests and scripts;
- architecture, standards, plans, and review records.

The contributor package is not equivalent to the minimal runtime package.

## Release channels

### Development branch

Contains active draft work. It is not a consumer release.

### Release candidate

Tag or branch convention to be defined in the release plan.

A release candidate:

- has a frozen manifest;
- includes only intended release content;
- has passed automated validation;
- is undergoing Phase 12 integrated review;
- may change only through tracked corrections.

### Stable release

A Semantic Versioning tag such as:

```text
v0.1.0
v0.2.0
v1.0.0
```

A stable release contains approved runtime components and mandatory dependencies.

### Hotfix release

A patch release for a critical defect that does not introduce incompatible behaviour.

## Source-to-package boundary

### Normally included

- approved runtime project rules;
- approved packaged skills;
- approved packaged subagents;
- required skill assets and local scripts;
- required knowledge files;
- required schemas and templates;
- consumer README and licence;
- release manifest;
- changelog or release notes appropriate to the profile.

### Normally excluded

- `PLACEHOLDER` artifacts;
- research in progress;
- internal pre-review records;
- raw research trials unless required for provenance;
- unselected knowledge packs;
- development plans;
- test fixtures;
- repository-only CI workflows;
- temporary migration scripts;
- private or local configuration;
- credentials and environment secrets;
- organisation-specific confidential material;
- licensed source content not authorised for distribution.

### Selectively included

- approved examples;
- deterministic runtime scripts;
- contributor documentation;
- source register excerpts required for attribution;
- evaluation assets for development distributions;
- commands or hooks where adopted and supported.

## Dependency-closure rule

The package builder starts from declared runtime entry points and computes their dependency closure.

```text
runtime rule
→ selected skills and subagents
→ required knowledge
→ required schemas and templates
→ required assets and scripts
→ consumer documentation and licence
```

A file is included when:

- it is an approved runtime entry point; or
- an included artifact declares it as a mandatory runtime dependency; or
- the release manifest includes it for consumer use.

A file is excluded when:

- its status prohibits release;
- it is development-only;
- it is not in the dependency closure or explicit inclusion list;
- its licence or confidentiality prevents distribution.

The builder must fail rather than silently omit an unresolved mandatory dependency.

## Release manifest

The package contains `RELEASE-MANIFEST.yaml`.

Draft field contract:

```yaml
release:
  name:
  version:
  source_repository:
  source_commit:
  created_at:
  package_profile:
  licence:
  minimum_cursor_version:
  tested_cursor_versions:
  compatibility_notes:

entry_points:
  rules: []
  skills: []
  subagents: []
  commands: []
  hooks: []

included_artifacts:
  - artifact_id:
    path:
    content_version:
    sha256:
    role:

excluded_capabilities: []
known_limitations: []
required_configuration: []
migration_from: []
validation:
  ci_commit_status:
  benchmark_result:
  independent_review:
  privacy_review:
  licence_review:
```

The Phase 2 schema and Phase 11 runtime metadata will refine this contract.

## Versioning

### Repository release version

Use Semantic Versioning:

- major: incompatible runtime, schema, or package change;
- minor: backward-compatible capability addition;
- patch: backward-compatible correction.

Pre-`1.0.0` releases may introduce breaking changes in minor versions, but migration impact must still be documented.

### Artifact content version

Each governed artifact retains its own `content_version`.

The release manifest records the packaged artifact version so a runtime issue can be traced to the exact source content.

### Skill version

The skill-authoring standard will decide whether active skills expose a separate runtime version or rely on artifact content version plus release version.

Avoid maintaining two version fields without a clear compatibility purpose.

## Compatibility model

Compatibility must be explicit for:

- Cursor component support;
- active skill and subagent metadata;
- required command or hook features;
- repository schema versions;
- operating-system assumptions for packaged scripts;
- optional Python runtime dependencies;
- Power BI product assumptions in implementation guidance.

### Compatibility matrix

Draft structure:

| Release | Cursor baseline | Skill format | Subagent format | Schema version | Script runtime | Notes |
|---|---|---|---|---|---|---|
| `v0.1.0` | to be verified at release | to be verified | to be verified | initial | Python 3.11+ for dev validators | first public release |

Current product behaviour must be reverified immediately before a release candidate is frozen.

## Packaging workflow

### 1. Freeze source state

- select source commit;
- ensure working tree is clean;
- update artifact statuses and versions;
- freeze release-candidate manifest inputs.

### 2. Validate source repository

Run:

- unit tests;
- dependency validation;
- source-register validation;
- internal-link validation;
- schema validation;
- skill metadata validation;
- status and placeholder checks;
- package dependency-closure validation.

### 3. Build package profiles

- resolve entry points;
- compute dependency closure;
- copy permitted files into a clean staging directory;
- generate the manifest;
- calculate file hashes;
- verify no unexpected files are present.

### 4. Test staged packages

Test the package rather than only the source repository:

- load in a clean Cursor workspace;
- verify rule, skill, and subagent discovery;
- run explicit and automatic invocation scenarios;
- verify referenced knowledge, schemas, templates, assets, and scripts resolve;
- run representative workflows;
- check platform-specific script behaviour where included.

### 5. Review content safety

- scan for secrets and private URLs;
- review personal and organisational information;
- verify synthetic example data;
- verify licence and attribution requirements;
- check that proprietary market data or framework content is absent;
- inspect generated archives manually.

### 6. Complete release review

- resolve Phase 12 critical and major findings;
- record accepted residual risks;
- confirm migration and rollback instructions;
- approve runtime artifacts and mandatory dependencies.

### 7. Publish

- create signed or annotated tag where supported by the release process;
- publish release notes and package archives;
- record hashes;
- update status and changelog;
- retain the source commit and manifest.

## Package integrity

The package validator must confirm:

- manifest path list matches archive contents;
- every included artifact exists in the tagged source commit;
- artifact IDs and content versions match source metadata;
- file hashes match the manifest;
- mandatory dependency closure is complete;
- no prohibited status is included;
- no unregistered runtime file is included without an explicit manifest reason;
- required licences and notices are present;
- no symlink or path traversal escapes the package root;
- generated archives can be reproduced from the same source commit and tool version.

## Runtime approval gate

A runtime component may enter a stable release only when:

- its status is `APPROVED`;
- mandatory dependencies are approved;
- its metadata validates against current Cursor requirements;
- representative automatic and explicit invocation tests pass;
- no unresolved critical or major review finding applies;
- privacy, security, evidence, and licensing checks pass;
- package dependency closure includes all required support files.

Draft or `IN REVIEW` development artifacts may remain in the source repository but cannot enter the stable runtime package.

## Comprehensive release-quality gate

Phase 12 must complete:

- independent architecture review;
- full benchmark suite;
- routing false-positive and false-negative tests;
- context-load and handoff tests;
- cross-skill contradiction analysis;
- audience and consumption-mode scenarios;
- Performance & Reward metric review;
- Power BI feasibility, security, accessibility, performance, and export review;
- current-product verification;
- privacy, confidentiality, copyright, and licence review;
- regression testing after corrections.

Phase 13 verifies closure and publishes.

## Migration

A release includes migration notes when it changes:

- rule names or paths;
- skill names, metadata, or invocation behaviour;
- subagent interfaces;
- schema fields or versions;
- knowledge paths referenced by skills;
- required configuration;
- package layout;
- minimum Cursor version;
- command or hook behaviour.

Draft migration-note fields:

```yaml
from_version:
to_version:
breaking_changes:
automatic_steps:
manual_steps:
renamed_artifacts:
removed_capabilities:
configuration_changes:
validation_steps:
rollback_steps:
```

## Upgrade workflow

1. Read release and migration notes.
2. Back up local project-specific customisations.
3. Compare installed manifest with target manifest.
4. Apply automated migrations where approved.
5. Resolve local overrides explicitly.
6. Validate rule, skill, subagent, and schema discovery.
7. Run representative workflows.
8. Retain the previous package until acceptance is confirmed.

The release must not overwrite user-owned organisation-specific knowledge silently.

## Local customisation boundary

Consumers may need private organisation-specific additions.

Recommended separation:

```text
packaged agent repository or package
+ private organisation overlay
+ project-specific working artifacts
```

The release process must document:

- which files are safe to customise;
- which files are managed by the package;
- how overlays are loaded;
- how upgrades preserve local content;
- how private material remains outside the public repository.

The exact overlay mechanism is deferred to later architecture and testing.

## Rollback

Rollback uses a previously published package and manifest.

Required procedure:

1. identify the last known-good release;
2. back up project-specific changes;
3. reinstall or restore the previous package;
4. restore compatible configuration and overlays;
5. rerun discovery and benchmark smoke tests;
6. record the rollback reason and affected release;
7. open a defect or hotfix workflow.

A rollback must not require reconstructing files from an untagged branch.

## Superseded releases

A superseded release remains available where practical for traceability but is clearly marked:

- superseded by version;
- support status;
- known critical defects;
- security or compatibility warnings;
- recommended migration path.

A release containing exposed secrets, unlawful content, or critical unsafe behaviour may require removal or revocation rather than ordinary supersession.

## Distribution options

Initial supported distribution is expected to be:

- GitHub source release;
- downloadable package archive;
- clone or copy instructions for the relevant runtime profile.

Potential future distribution:

- Cursor plugin packaging;
- marketplace distribution;
- organisation-managed internal package;
- generated installer or update utility.

These remain deferred until the runtime architecture is stable and current Cursor distribution requirements are verified.

## Release security and privacy

Required checks:

- secret scanning;
- private URL and tenant-identifier scanning;
- employee and personal-information review;
- confidential organisation-name and system review;
- licence and attribution review;
- dependency and workflow-action review;
- archive path and symlink safety;
- malicious or executable-content review for packaged scripts;
- minimum-permission documentation.

Public examples must use synthetic data and cannot reveal real employee, company, client, or licensed market information.

## CI and supply-chain policy

The final release process must decide:

- whether third-party CI actions are pinned to full commit SHAs;
- how Python dependencies are pinned and verified;
- whether generated archives are built in CI or a controlled local environment;
- whether release artifacts are signed;
- how checksums are published;
- who may approve and publish releases.

Until then, CI validates development quality but is not itself the complete release-security control.

## Failure conditions

Release fails when:

- a runtime placeholder or draft is included;
- a mandatory dependency is missing;
- package and manifest differ;
- current Cursor compatibility is unverified;
- critical or major review findings remain unresolved;
- confidential, personal, proprietary, or unlicensed content is present;
- a schema or invocation change lacks required migration guidance;
- staged-package tests fail;
- the package cannot be reproduced from the source tag;
- rollback instructions are absent for a breaking release.

## Draft `v0.1.0` scope

Expected minimum capability set:

- one concise project orchestrator rule;
- three focused subagents;
- foundational audience, discovery, value-driver, KPI, storyline, visual hierarchy, chart selection, consumption-mode, and Power BI feasibility skills;
- required audience and holistic P&R knowledge;
- required schemas and templates;
- five benchmark scenarios;
- release manifest and validation scripts.

Specialist domain breadth may be narrower than the final catalogue if the included capabilities form a coherent and tested product.

## Draft acceptance assessment

This draft defines:

- package profiles;
- release channels;
- source and runtime boundaries;
- dependency closure;
- manifest fields;
- version and compatibility model;
- packaging workflow;
- integrity and approval gates;
- migration, upgrade, customisation, rollback, and supersession;
- distribution options;
- privacy, security, and supply-chain decisions;
- draft `v0.1.0` scope.

Before the artifact leaves `PLACEHOLDER`, it must be reconciled with:

- active runtime metadata;
- Phase 2 schemas;
- the release plan;
- package-builder and validator implementation;
- organisation-overlay design;
- current Cursor distribution and plugin requirements;
- Phase 12 evaluation and approval criteria.
