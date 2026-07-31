---
artifact_id: STD-CORE-001
status: DRAFT
phase: 0
priority: critical
depends_on:
  - artifact_id: CTRL-CORE-001
    path: ../../BUILD-ORDER.md
  - artifact_id: CTRL-CORE-002
    path: ../../DEPENDENCIES.md
blocks:
  - STD-CORE-002
  - STD-CORE-003
  - STD-CORE-004
  - all named governed artifacts
content_version: 0.2.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Naming standard

## Purpose

This standard establishes stable and predictable names for repository paths, Cursor components, artifact identifiers, metadata, branches, commits, versions, and Performance & Reward terminology.

Consistent naming matters because Cursor discovers some components from reserved paths and filenames, while contributors and validators need names that remain interpretable without conversation history. Cursor documents project rules under `.cursor/rules`; its Agent Skills use `SKILL.md` packages.[^cursor-rules][^cursor-skills]

## Scope

This standard applies to:

- directories and files;
- Cursor rules, skills, subagents, and future commands;
- artifact identifiers and frontmatter keys;
- schemas, templates, examples, evaluations, infrastructure, tests, and scripts;
- branches, commits, releases, and tags;
- headings, abbreviations, dates, and controlled status values.

Power BI semantic-model naming will be defined in the Power BI knowledge and skill layers.

## Governing principles

1. Names describe durable purpose rather than temporary implementation.
2. One concept has one canonical name.
3. Paths are interfaces and approved paths change only through a migration.
4. Names must be readable by people and deterministic for validators.
5. Public names must not expose confidential organisations, people, systems, or projects.
6. Product-reserved paths and filenames override general conventions.
7. Artifact IDs remain stable when paths or titles change.

## Paths and filenames

### Default convention

Use lowercase kebab-case for ordinary directories and filenames:

```text
fixed-reward-analysis
market-competitiveness.md
power-bi-feasibility
executive-fixed-reward-summary.md
```

Ordinary paths may contain:

```text
a-z 0-9 hyphen period
```

Do not use spaces, underscores, camelCase, PascalCase, repeated hyphens, or trailing hyphens in ordinary paths.

### Reserved filenames

The following names retain their required or conventional casing:

```text
README.md
AGENTS.md
SKILL.md
LICENSE
CHANGELOG.md
CONTRIBUTING.md
BUILD-ORDER.md
DEPENDENCIES.md
STATUS.md
ARTIFACT-REGISTER.yaml
```

Root-level machine-readable controls may use uppercase descriptive names only when this standard explicitly reserves them.

Cursor project rules use `.mdc` files under `.cursor/rules`.[^cursor-rules] Cursor Agent Skills use the exact filename `SKILL.md`.[^cursor-skills] Product-sensitive details must be reverified before activation.

### Directory names

Directory names identify a durable capability, domain, audience, artifact class, or workflow.

Preferred:

```text
performance-reward
visual-design
consulting-techniques
business-partner
benchmark-scenarios
```

Avoid:

```text
misc
other
new
final
old
stuff
temp2
```

Use singular names for one bounded concept and plural names for collections.

### File names

A filename must identify its subject without relying entirely on the parent directory.

Preferred:

```text
holistic-value-driver-tree.md
research-standard.md
executive-storytelling.md
validate-skill-frontmatter.py
```

Do not encode lifecycle status or informal version labels in filenames.

### Acronyms

Use lowercase acronyms in paths:

```text
ibcs-standard.md
dax-patterns.md
kpi-definition.schema.yaml
```

Use `power-bi`, not `powerbi` or `pbi`, in public paths unless a formal identifier requires the shorter code.

Use `performance-reward`, not `pr`, in paths where `pr` could mean pull request.

### Required scaffold migration

Rename:

```text
.cursor/skills/performance-reward/holistic-pr-value-drivers/
```

to:

```text
.cursor/skills/performance-reward/holistic-performance-reward-value-drivers/
```

before Phase 4. Update all references in the same pull request.

## Cursor component names

### Rules

Path:

```text
.cursor/rules/<rule-name>.mdc
```

Rules use lower-kebab-case, describe one bounded concern, and do not add `rule` to the name unless needed for clarity.

Examples:

```text
performance-reward-dashboard-architect.mdc
evidence-and-source-standard.mdc
quality-gates.mdc
```

### Skills

Path:

```text
.cursor/skills/<capability-group>/<skill-name>/SKILL.md
```

The active skill `name` must match `<skill-name>` exactly. Skill names:

- use lowercase letters, numbers, and hyphens;
- describe a reusable capability or workflow;
- distinguish analysis, design, review, and implementation where material;
- avoid vague persona labels.

Preferred patterns:

```text
<domain>-analysis
<object>-design
<object>-review
<decision>-framing
<relationship>-visualisation
```

Only fields verified against current official Cursor documentation may be activated.

### Subagents

Path:

```text
.cursor/agents/<role-name>.md
```

Use a role or verification responsibility:

```text
research-synthesiser.md
dashboard-design-critic.md
power-bi-verifier.md
```

Do not use personal names, model names, or inflated seniority labels.

### Commands

When commands are added, use:

```text
.cursor/commands/<imperative-workflow>.md
```

Examples:

```text
review-dashboard.md
create-dashboard-brief.md
run-evaluations.md
```

Commands represent explicit workflows; skills represent reusable capabilities that may be selected dynamically.

## Artifact identifiers

Every substantive governed artifact receives an immutable ID:

```text
<TYPE>-<DOMAIN>-<NNN>
```

Examples:

```text
STD-CORE-001
ARCH-CORE-001
KNOW-FIXED-001
SKILL-VIZ-003
EVAL-EXEC-001
TEST-QA-001
INFRA-CORE-001
```

### Type codes

| Code | Artifact type |
|---|---|
| `CTRL` | Repository control |
| `ARCH` | Architecture decision or specification |
| `STD` | Standard |
| `PLAN` | Plan or roadmap |
| `RULE` | Cursor rule |
| `AGENT` | Cursor subagent |
| `SKILL` | Cursor skill |
| `KNOW` | Governed knowledge artifact |
| `SCHEMA` | Machine-readable schema |
| `TPL` | Output template |
| `EX` | Worked example or evidence trial |
| `EVAL` | Evaluation scenario, result, or review record |
| `SCRIPT` | Validation or generation script and its runtime dependency manifest |
| `TEST` | Automated test module or fixture set |
| `INFRA` | CI workflow or repository automation infrastructure |

### Domain codes

| Code | Domain |
|---|---|
| `CORE` | Repository-wide |
| `AUD` | Audience and decision framing |
| `PR` | Cross-domain Performance & Reward |
| `PERF` | Performance management |
| `FIXED` | Fixed reward |
| `VAR` | Variable reward |
| `MARKET` | Market competitiveness |
| `JOB` | Job architecture |
| `EQUITY` | Pay equity and fairness |
| `TALENT` | Attraction, retention, and talent |
| `TOTAL` | Benefits, recognition, and total rewards |
| `GOV` | Governance and controls |
| `CONSULT` | Consulting communication |
| `VIS` | Visual design |
| `VIZ` | Data visualisation |
| `UX` | Dashboard experience |
| `PBI` | Power BI implementation |
| `QA` | Assurance, testing, and quality |
| `EXEC` | Executive benchmark or example |
| `BP` | Business Partner benchmark or example |
| `MGR` | Manager benchmark or example |

New codes require an update to this standard. Existing IDs are never renumbered.

## Metadata keys

Use lowercase snake_case for machine-oriented metadata.

Required governed-artifact keys:

```yaml
artifact_id:
status:
phase:
priority:
depends_on:
blocks:
content_version:
last_reviewed:
next_review:
```

Canonical dependencies use objects:

```yaml
depends_on:
  - artifact_id: STD-CORE-001
    path: docs/standards/naming-standard.md
```

Optional keys use the same convention:

```yaml
owner:
reviewers:
source_as_of:
applicable_jurisdictions:
superseded_by:
```

Dates use ISO 8601 calendar format:

```text
YYYY-MM-DD
```

Use YAML lists rather than comma-separated strings.

## Lifecycle and priority values

Allowed statuses:

```text
PLACEHOLDER
RESEARCH IN PROGRESS
DRAFT
IN REVIEW
APPROVED
SUPERSEDED
```

`SUPERSEDED` requires `superseded_by` with an artifact ID and relative path.

Allowed priorities:

```text
critical
high
medium
low
```

## Versioning

Repository releases use Semantic Versioning tags:

```text
v0.1.0
v0.2.0
v1.0.0
```

Artifact versions omit the leading `v`:

```yaml
content_version: 0.2.0
```

Increment:

- major for incompatible scope, schema, or method changes;
- minor for meaningful backward-compatible additions;
- patch for corrections that preserve intended use.

## Branches

Format:

```text
<type>/<scope>-<short-description>
```

Allowed types:

```text
scaffold
research
docs
feat
fix
refactor
test
chore
release
```

`scaffold` is limited to pre-release repository-foundation work and should not be used after the initial foundation is merged.

Examples:

```text
scaffold/repository-foundation
docs/phase-0-standards
research/fixed-reward-value-drivers
feat/executive-storyline-skill
fix/dependency-validator
```

Keep names under 60 characters where practical.

## Commits and pull requests

Commit format:

```text
<type>: <imperative summary>
```

Preferred types:

```text
research
docs
feat
fix
refactor
test
chore
review
ci
```

Pull-request titles describe the delivered result rather than the activity or tool.

Preferred:

```text
Define Phase 0 research and citation standards
Add fixed reward knowledge and analysis skill
```

Avoid:

```text
Updates
More files
Cursor changes
Final version
```

## Prose and terminology

- Use sentence case for Markdown headings.
- Use `Performance & Reward` in prose.
- Define abbreviations on first use.
- Use `Business Partner` for the audience and `BP` only in controlled IDs.
- Use `people manager` unless a formal product name differs.
- Preserve accepted casing for `Power BI`, `Cursor`, `DAX`, `IBCS`, and `KPI`.
- Use Australian English, including `visualisation`, `organisation`, `labour`, and `colour`, except in quotations or product-defined fields.

## Public-repository restrictions

Names must not contain:

- employee names or identifiers;
- confidential organisational names, codes, or systems without approval;
- unreleased program names;
- credentials, tokens, tenant identifiers, or private URLs;
- client-specific terminology presented as universal practice.

Use neutral names and fictional values.

## Rename and deprecation procedure

For an approved artifact:

1. Record the reason.
2. Identify inbound and outbound references.
3. Rename the path and update references in one pull request.
4. Preserve the artifact ID.
5. Update the changelog.
6. Run link and dependency validation.
7. Add a redirect file only where useful and safe.

## Anti-patterns

- Encoding lifecycle status in filenames.
- Informal names such as `final-v2-new.md`.
- Reusing an artifact ID for another concept.
- Creating aliases without declaring an authority.
- Naming skills after broad personas rather than bounded capabilities.
- Using `PR` in ordinary paths where it is ambiguous.
- Renaming approved files only for aesthetics.
- Registering an active artifact type that is absent from this standard.

## Acceptance criteria

This standard can move to `IN REVIEW` when:

- all scaffold paths and registered artifact IDs have been checked;
- exceptions and required migrations are recorded;
- the artifact register includes every active Phase 0 artifact;
- validators can enforce the naming rules without unresolved ambiguity;
- Cursor-sensitive conventions have current official support;
- representative rule, skill, knowledge, schema, evaluation, test, infrastructure, and pull-request names have been trialled.

It can move to `APPROVED` after independent review and correction of all critical and major findings. The standard must be reviewed again after the first active Cursor skill and first formal schema are implemented; that review does not prevent initial Phase 0 approval.

## Sources

[^cursor-rules]: Cursor, “Rules,” updated date not stated, retrieved 2026-07-17, https://docs.cursor.com/context/rules. Central source ID: `cursor-rules`.

[^cursor-skills]: Cursor, “Subagents, Skills, and Image Generation,” release 2.4, 2026, retrieved 2026-07-17, https://cursor.com/changelog/2-4. Central source ID: `cursor-2-4-subagents-skills`.

## Review notes

Product-specific details must be reverified before activation because Cursor capabilities and metadata may change. The internal Phase 0 pre-review added `TEST` and `INFRA`, documented the initial `scaffold` branch exception, reserved `ARTIFACT-REGISTER.yaml`, and removed the previous approval dependency on later phases.
