---
artifact_id: STD-CORE-001
status: DRAFT
phase: 0
priority: critical
depends_on:
  - BUILD-ORDER.md
  - DEPENDENCIES.md
blocks:
  - docs/standards/research-standard.md
  - docs/standards/citation-standard.md
  - docs/standards/skill-authoring-standard.md
  - all named repository artifacts
content_version: 0.1.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Naming Standard

## Purpose

This standard establishes stable, predictable names for repository paths, Cursor components, artifact identifiers, metadata fields, branches, commits, versions, and Performance & Reward terminology.

Consistent naming is required because Cursor discovers some components from specific paths and filenames, while humans and validation scripts need names that remain interpretable without relying on conversation history.

## Scope

This standard applies to:

- directories and files;
- Cursor rules, skills, subagents, and future commands;
- artifact identifiers and frontmatter keys;
- schemas, templates, examples, evaluations, and scripts;
- branches, commits, releases, and tags;
- headings, abbreviations, dates, and status values.

It does not prescribe Power BI semantic-model naming. That will be defined in the Power BI knowledge and skill layers.

## Governing principles

1. **Names describe purpose, not temporary implementation.**
2. **One concept has one canonical name.** Aliases may be recorded, but duplicate names must not create competing authorities.
3. **Paths are stable interfaces.** Rename an approved path only with a documented migration.
4. **Names are readable by humans and deterministic for scripts.**
5. **Public-repository names must not expose confidential organisation, employee, client, or project information.**
6. **Product-specific reserved filenames and locations take precedence over general project conventions.**

## Character and case rules

### Default path convention

Use lowercase kebab-case for ordinary directories and files:

```text
fixed-reward-analysis
market-competitiveness.md
power-bi-feasibility
executive-fixed-reward-summary.md
```

Allowed characters are:

```text
a-z 0-9 hyphen period
```

Do not use spaces, underscores, camelCase, PascalCase, repeated hyphens, or trailing hyphens in ordinary paths.

### Reserved filenames

The following names retain their conventional casing:

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
```

Cursor project rules use the `.mdc` extension. Cursor project skills use the exact filename `SKILL.md`. Cursor project rules are stored under `.cursor/rules`, and skills are loaded dynamically rather than being persistent rules. The final implementation must be checked against current Cursor documentation before activation.

## Directory names

Directory names must identify a durable capability, domain, audience, artifact class, or workflow.

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

Use singular names for a single bounded concept and plural names for collections:

```text
knowledge/audiences/
knowledge/performance-reward/fixed-reward.md
schemas/
templates/
```

## File names

A filename must identify the artifact subject without requiring its parent folder for basic interpretation.

Preferred:

```text
holistic-value-driver-tree.md
research-standard.md
executive-storytelling.md
validate-skill-frontmatter.py
```

Avoid date prefixes unless the artifact is inherently time-bound. Use metadata for review dates and versions rather than filenames such as `final-v2-new.md`.

### Acronyms in filenames

Use lowercase acronyms within kebab-case:

```text
ibcs-standard.md
dax-patterns.md
kpi-definition.schema.yaml
```

Use `power-bi`, not `powerbi` or `pbi`, in public path names unless the shorter code is part of a formal artifact identifier.

Use `performance-reward`, not `pr`, in names where `pr` could be confused with pull request.

### Required migration

The scaffold path:

```text
.cursor/skills/performance-reward/holistic-pr-value-drivers/
```

must be renamed during Phase 4 to:

```text
.cursor/skills/performance-reward/holistic-performance-reward-value-drivers/
```

The rename must update all references in the same pull request.

## Cursor component naming

### Rules

Path:

```text
.cursor/rules/<rule-name>.mdc
```

Convention:

- lower-kebab-case;
- noun phrase or bounded standard;
- name describes what the rule governs;
- one concern per rule.

Examples:

```text
performance-reward-dashboard-architect.mdc
evidence-and-source-standard.mdc
quality-gates.mdc
```

Do not include `rule` in the filename unless needed to distinguish the concept.

### Skills

Path:

```text
.cursor/skills/<capability-group>/<skill-name>/SKILL.md
```

The final skill frontmatter `name` must exactly match `<skill-name>`.

Skill names must:

- use lowercase letters, numbers, and hyphens;
- describe a reusable capability or workflow;
- distinguish analysis, design, review, and implementation where materially different;
- avoid vague names such as `dashboard-helper` or `expert`.

Preferred patterns:

```text
<domain>-analysis
<object>-design
<object>-review
<decision>-framing
<relationship>-visualisation
```

Examples:

```text
fixed-reward-analysis
kpi-measure-design
visual-hierarchy-design
review-dashboard
```

Only frontmatter fields verified against current official Cursor documentation may be activated. At minimum, active skills require a valid `name` and a precise `description` that explains both capability and invocation conditions.

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

Do not use personal names, model names, or seniority theatre such as `super-genius-agent`.

### Commands

If reusable Cursor commands are added later, use:

```text
.cursor/commands/<imperative-workflow>.md
```

Examples:

```text
review-dashboard.md
create-dashboard-brief.md
run-evaluations.md
```

Commands are distinct from skills. A command is an explicit reusable workflow; a skill is a reusable capability that may be selected dynamically.

## Artifact identifiers

Every substantive governed artifact must receive an immutable identifier in frontmatter.

Format:

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
| `EX` | Worked example |
| `EVAL` | Evaluation scenario or expected result |
| `SCRIPT` | Validation or generation script |

### Domain codes

Use a short uppercase code from the controlled register. Initial codes are:

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
| `QA` | Assurance and quality |
| `EXEC` | Executive benchmark or example |
| `BP` | Business Partner benchmark or example |
| `MGR` | Manager benchmark or example |

New codes require an update to this standard. Existing IDs are never renumbered after publication.

## Frontmatter keys

Use lowercase snake_case for metadata keys because keys are machine-oriented rather than path names.

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

Optional keys must use the same convention:

```yaml
owner:
reviewers:
source_as_of:
applicable_jurisdictions:
```

Dates use ISO 8601 calendar format:

```text
YYYY-MM-DD
```

Use YAML lists for multiple values. Do not encode lists as comma-separated strings.

## Status values

Use only these uppercase values:

```text
PLACEHOLDER
RESEARCH IN PROGRESS
DRAFT
IN REVIEW
APPROVED
SUPERSEDED
```

`SUPERSEDED` requires a `superseded_by` field containing an artifact ID and relative path.

## Priority values

Use only:

```text
critical
high
medium
low
```

Priority is lower-case because it is a sortable metadata value, not a lifecycle state.

## Version names

### Repository releases

Use Semantic Versioning tags:

```text
v0.1.0
v0.2.0
v1.0.0
```

### Artifact content versions

Use `content_version` without a leading `v`:

```yaml
content_version: 0.1.0
```

Increment:

- major for incompatible scope, schema, or method changes;
- minor for meaningful backward-compatible additions;
- patch for corrections that do not alter intended use.

## Branch names

Format:

```text
<type>/<scope>-<short-description>
```

Allowed types:

```text
research
docs
feat
fix
refactor
test
chore
release
```

Examples:

```text
docs/phase-0-standards
research/fixed-reward-value-drivers
feat/executive-storyline-skill
fix/dependency-validator
```

Keep branch names under 60 characters where practical.

## Commit messages

Format:

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
```

Examples:

```text
docs: define repository naming standard
research: add fixed reward source matrix
feat: implement KPI definition schema
```

A commit summary must describe the result, not the activity duration or tool used.

## Pull-request titles

Use a result-oriented title that can become useful release history:

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

## Headings and terminology

- Use sentence case for Markdown headings.
- Use `Performance & Reward` in prose.
- Define an abbreviation on first use before using it repeatedly.
- Use `Business Partner` when referring to the audience archetype; use the controlled code `BP` only in identifiers.
- Use `people manager` unless referring to a formally named product audience.
- Use `Power BI`, `Cursor`, `DAX`, `IBCS`, and `KPI` with their accepted casing.
- Use `data visualisation` in prose and `visualisation` in paths, following Australian English.
- Use `organisation`, `labour`, `colour`, and other Australian English spellings unless quoting a source or using a product-defined field.

## Public-repository restrictions

Names must not include:

- employee names or identifiers;
- confidential organisational names, codes, or internal systems unless authorised;
- unreleased program names;
- credentials, tokens, tenant identifiers, or private URLs;
- client-specific terminology presented as universal practice.

Use neutral examples and clearly marked fictional values.

## Rename and deprecation procedure

For an approved artifact:

1. Record the reason for rename.
2. Identify all inbound and outbound references.
3. Rename the path and update references in one pull request.
4. Preserve the immutable artifact ID.
5. Add a changelog entry.
6. Run internal-link and dependency validation.
7. Where external links may exist, leave a short redirect file only when useful and safe.

## Anti-patterns

- Encoding status in filenames: `draft-`, `final-`, `approved-`.
- Encoding version in filenames unless distributing a release artifact.
- Reusing one artifact ID for a different concept.
- Creating aliases without declaring an authority.
- Naming skills after broad personas rather than bounded capabilities.
- Using `PR` in paths where it can mean either Performance & Reward or pull request.
- Renaming approved files only to improve aesthetics.

## Acceptance criteria

This standard can move to `IN REVIEW` when:

- all scaffold paths have been checked for conformance;
- required exceptions and migrations are recorded;
- the artifact-ID register has been created;
- validation rules can be implemented without unresolved naming ambiguity;
- Cursor-specific conventions have been verified against current official documentation.

It can move to `APPROVED` after independent review and a successful trial against at least one skill, one knowledge pack, one schema, one evaluation, and one pull request.

## Sources and review notes

This project convention is informed by Cursor's official rule documentation, which places project rules in `.cursor/rules`, uses MDC metadata, and recommends focused, composable rules. Cursor's official 2.4 release material describes Agent Skills as `SKILL.md` packages that are dynamically discovered and can include instructions and scripts.

- [Cursor Rules](https://docs.cursor.com/context/rules), Cursor, retrieved 2026-07-17.
- [Cursor 2.4: Subagents, Skills, and Image Generation](https://cursor.com/changelog/2-4), Cursor, retrieved 2026-07-17.
- [Best practices for coding with agents](https://cursor.com/blog/agent-best-practices), Cursor, retrieved 2026-07-17.

Product-specific details must be reverified before the standard is approved because Cursor capabilities and metadata may change.
