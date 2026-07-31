---
artifact_id: STD-CORE-003
status: DRAFT
phase: 0
priority: critical
depends_on:
  - artifact_id: CTRL-CORE-001
    path: ../../BUILD-ORDER.md
  - artifact_id: CTRL-CORE-002
    path: ../../DEPENDENCIES.md
  - artifact_id: STD-CORE-001
    path: naming-standard.md
  - artifact_id: STD-CORE-002
    path: research-standard.md
blocks:
  - schemas/research-record.schema.yaml
  - templates/research-record.md
  - knowledge/research-register/
  - all evidence-based knowledge artifacts
content_version: 0.2.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Citation standard

## Purpose

This standard defines how the repository cites external evidence, internal artifacts, formulas, datasets, product documentation, standards, and project decisions.

Every material claim should be:

- traceable;
- reviewable;
- durable when files move;
- explicit about source quality and freshness;
- usable without loading the full research trail.

## Scope

This standard applies to:

- knowledge packs and research records;
- methodology and architecture documents containing external claims;
- KPI and calculation definitions;
- evidence-based examples and evaluations;
- rules, skills, and subagents that reference governed knowledge;
- public-facing documentation.

Administrative instructions and clearly labelled project decisions do not require external citations, but they should reference the relevant internal authority where one exists.

## Core rules

1. Cite the claim, not merely the paragraph topic.
2. Place the citation immediately after the supported statement.
3. Prefer the original source over a source that repeats it.
4. Cite unstable facts whenever materially used.
5. Record retrieval date, version, jurisdiction, and effective date where relevant.
6. Distinguish evidence, synthesis, inference, and project decision.
7. Use only citations that support the exact wording.
8. Do not create false certainty by stacking weak sources.
9. Use readable Markdown and stable source IDs.
10. Paraphrase by default and quote only when exact wording matters.
11. Apply this standard to the standards themselves before approval.
12. An approval reviewer must be independent of the authoring workflow.

## Repository citation model

The repository uses two linked layers.

### Claim-level citation

Use a descriptive Markdown footnote directly after the claim:

```markdown
Cursor project rules are stored under `.cursor/rules`.[^cursor-rules]
```

### Local source entry

Define the footnote under `## Sources` in the same file:

```markdown
[^cursor-rules]: Cursor, “Rules,” updated date not stated, retrieved 2026-07-17, https://docs.cursor.com/context/rules. Central source ID: `cursor-rules`.
```

A local source entry remains required even when the source exists in the central register. The central register supports reuse and freshness review; the local citation keeps the artifact independently readable.

## Footnote identifiers

Use stable descriptive lowercase kebab-case identifiers.

Preferred:

```text
[^cursor-rules]
[^mckinsey-visual-performance-2022]
[^wgea-employer-pay-gaps-2026]
[^cleveland-mcgill-1984]
```

Avoid:

```text
[^1]
[^source]
[^website]
```

Include the year when a source is periodic or version-sensitive.

## Source-entry formats

### Web page

```text
Organisation or author, “Page title,” publication or updated date if known, retrieved YYYY-MM-DD, canonical URL.
```

### Product documentation or release note

Include product, version or release, feature state, and retrieval date:

```markdown
[^cursor-skills]: Cursor, “Subagents, Skills, and Image Generation,” release 2.4, 2026, retrieved 2026-07-17, https://cursor.com/changelog/2-4. Central source ID: `cursor-2-4-subagents-skills`.
```

### Journal article

```text
Author(s), “Article title,” Journal, volume(issue), year, pages, DOI or stable URL.
```

### Book

```text
Author, Title, edition, publisher, year, relevant page or chapter.
```

### Standard

```text
Standards body, identifier and title, edition or year, clause or section, stable URL where public.
```

Do not reproduce restricted standards content beyond a brief lawful description.

### Legislation or regulation

```text
Jurisdiction, instrument title and identifier, current compilation or effective date, section or clause, official URL, retrieved date.
```

### Official dataset

```text
Publisher, dataset or release title, reference period, table or series identifier, release date, URL, retrieved date.
```

### Commercial survey or market publication

Include geography, effective period, sample or coverage where available, and access limitations. Do not commit licensed tables or proprietary pay data.

### Conference presentation or webinar

Include presenter, title, event, organiser, date, slide or timestamp where relevant, and stable URL.

### GitHub repository, issue, pull request, or commit

Use the canonical URL and pin implementation-sensitive claims to a release, commit, issue, or pull request where practical.

### Internal repository artifact

Use a relative link plus immutable artifact ID:

```markdown
The research process follows [STD-CORE-002](research-standard.md).
```

When referring to an approved version-sensitive decision, include the content version.

## Claim placement

### Single claim

```markdown
Project rules are stored under `.cursor/rules`.[^cursor-rules]
```

### Multiple claims

Cite each independently:

```markdown
Project rules are stored under `.cursor/rules`.[^cursor-rules] Agent Skills are loaded dynamically when relevant.[^cursor-practices]
```

Do not use one citation at the end of a paragraph containing several unrelated claims.

### Tables

- If one source supports the whole table, cite the title or introductory sentence and add a source note.
- If rows use different sources, add row-level footnotes or a `Source` column.
- Numbers, thresholds, and benchmark values require direct support.

### Diagrams and frameworks

Use one of:

```text
Source:
Adapted from:
Project synthesis informed by:
```

`Adapted from` means the source structure remains recognisable. `Project synthesis informed by` means multiple ideas were combined into a new repository structure.

## Evidence, synthesis, inference, and decision

### Evidence

```markdown
**Evidence:** Official Cursor documentation places project rules in `.cursor/rules`.[^cursor-rules]
```

### Supported synthesis

```markdown
**Supported synthesis:** Focused persistent rules and dynamically loaded skills should reduce unnecessary context compared with one monolithic rule.[^cursor-rules][^cursor-practices]
```

### Inference

```markdown
**Inference:** The same context separation may improve reliability for this repository's long-running dashboard workflows.[^cursor-practices]
```

The source supports the premise; the conclusion remains labelled as inference.

### Project decision

```markdown
**Project decision:** This repository uses one persistent rule per bounded concern.
```

A project decision does not need an external citation unless it claims external authority. It should link to the internal decision or architecture artifact.

## Source quality

Research records classify sources as:

```text
primary-authoritative
authoritative-synthesis
practitioner-evidence
discovery-only
```

Authority is claim-relative. An official consulting article is primary for what the firm says its method is, but not automatically primary evidence that the method improves performance.

## Current and unstable information

For current products, law, regulation, market data, schedules, or other unstable information, include:

- retrieval date;
- publication or update date where available;
- version, release, or effective period;
- jurisdiction where relevant;
- review trigger.

Do not convert a version-specific feature into a permanent capability without qualification.

## Consulting-firm attribution

Firm-specific claims require a direct official source.

Acceptable:

```markdown
McKinsey's public article describes a `1-3-10` principle for visual performance management.[^mckinsey-vpm]
```

Not acceptable:

```markdown
McKinsey always uses this dashboard layout.
```

Observed conventions must be labelled and supported by representative official examples. General consulting practices should not be attributed to one firm without evidence.

## Formula and KPI citations

A KPI definition separates:

1. externally sourced concept;
2. repository-specific formula;
3. organisation-specific implementation.

Example:

```markdown
The external concept compares new-hire pay with comparable incumbent pay.[^mercer-new-hire]

**Repository definition:**

\[
\text{New-hire premium} =
\frac{\text{new-hire FTE fixed pay}}
{\text{median comparable incumbent FTE fixed pay}}
- 1
\]
```

A project-designed formula does not require false external attribution. It must be labelled as a repository definition and justified in the KPI artifact.

Every published KPI links to its approved KPI-definition artifact.

## Quotations

- Use quotation marks or a block quote for verbatim text.
- Cite page, section, paragraph, or timestamp where available.
- Keep quotations brief.
- Never reconstruct a quotation from memory.
- Do not splice fragments in a misleading way.
- Prefer paraphrase.
- Do not reproduce lyrics, proprietary standards, licensed market data, or substantial copyrighted passages.

## Citation laundering

When a source repeats another source:

1. follow the citation to the original where accessible;
2. cite the original for the underlying claim;
3. cite the secondary source only for its independent interpretation;
4. record when the original is inaccessible.

Repeated secondary sources do not count as independent triangulation.

## Links and durability

- Prefer canonical HTTPS URLs and DOI links.
- Remove tracking parameters and avoid temporary signed URLs.
- Pin implementation-sensitive evidence to versions or commits where practical.
- Use relative links for repository files.
- Run internal-link validation before approval.
- Do not use private or raw local file-system paths in public citations.

## Central source register

The central register lives at:

```text
knowledge/research-register/sources.yaml
```

Each source record contains:

```yaml
source_id:
title:
author_or_organisation:
source_type:
evidence_level:
url_or_doi:
publication_date:
updated_date:
retrieved_date:
version:
jurisdiction:
lifecycle_state:
licence_or_usage_notes:
relevant_artifacts:
planned_consumers:
relevant_claims:
review_notes:
```

Rules:

- `source_id` is stable lowercase kebab-case.
- `relevant_artifacts` contains only registered immutable artifact IDs.
- Future destinations belong in `planned_consumers`.
- A new materially distinct edition or release receives a separate record where needed.
- Restricted or rejected sources remain recorded when required to explain decisions.

## Citation density

Citations are required for:

- non-common factual claims;
- numbers, dates, thresholds, and benchmark values;
- current product capabilities;
- legal and regulatory requirements;
- firm-specific methods or conventions;
- named theories and research findings;
- causal or predictive claims;
- external definitions and formulas;
- source-attributed limitations.

Citations are not normally required for:

- repository navigation;
- clearly labelled project decisions;
- explicitly fictional examples;
- transparent arithmetic;
- labelled logical deductions whose premises are cited.

## Prohibited practices

- Citing a search-result snippet instead of the source.
- Citing AI output as evidence.
- Listing sources that are never connected to claims.
- Using a prestigious but irrelevant source.
- Citing outdated product documentation without qualification.
- Hiding uncertainty behind a large bibliography.
- Linking to pirated, unauthorised, confidential, or private material.
- Citing internal documents in public artifacts without approval.
- Using a citation to disguise a repository decision as an external requirement.

## Review checklist

A reviewer confirms:

- each material claim has support;
- the source supports the exact wording;
- primary sources were used where appropriate;
- firm attribution is bounded correctly;
- date, version, jurisdiction, population, and effective period are present where relevant;
- evidence, synthesis, inference, and decision are separated;
- quotations are exact, brief, and lawful;
- links resolve and source records are sufficient to relocate the evidence;
- public-repository restrictions are satisfied;
- the artifact itself follows this citation standard.

An internal pre-review can identify defects but cannot provide independent approval.

## Acceptance criteria

This standard can move to `IN REVIEW` when:

- the research-record **field contract** includes all required source and claim fields;
- the central source register validates with warnings treated as errors;
- one product claim, P&R KPI, academic claim, consulting attribution, and internal decision have been cited successfully;
- internal-link and source-reference validators operate in CI;
- the internal pre-review's critical and major findings are resolved;
- the naming and research standards use the citation model for material external claims.

A formal Phase 2 schema is not required for the Phase 0 status transition; it must later implement this approved field contract.

This standard can move to `APPROVED` after independent review and correction of all critical and major findings. It must be reviewed after its first use in an audience knowledge pack and holistic P&R pack, but that post-implementation review does not block initial approval.

## Sources

[^cursor-rules]: Cursor, “Rules,” updated date not stated, retrieved 2026-07-17, https://docs.cursor.com/context/rules. Central source ID: `cursor-rules`.

[^cursor-practices]: Cursor, “Best practices for coding with agents,” 2026, retrieved 2026-07-17, https://cursor.com/blog/agent-best-practices. Central source ID: `cursor-agent-best-practices`.

[^cursor-skills]: Cursor, “Subagents, Skills, and Image Generation,” release 2.4, 2026, retrieved 2026-07-17, https://cursor.com/changelog/2-4. Central source ID: `cursor-2-4-subagents-skills`.

## Review notes

The internal Phase 0 pre-review removed the formal-schema dependency from the status transition, resolved the later-phase approval deadlock, required reviewer independence, aligned the standard with the updated source register, and made self-application a condition of approval.
