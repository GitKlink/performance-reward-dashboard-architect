---
artifact_id: STD-CORE-003
status: DRAFT
phase: 0
priority: critical
depends_on:
  - STD-CORE-001: docs/standards/naming-standard.md
  - STD-CORE-002: docs/standards/research-standard.md
  - BUILD-ORDER.md
  - DEPENDENCIES.md
blocks:
  - schemas/research-record.schema.yaml
  - templates/research-record.md
  - knowledge/research-register/
  - all evidence-based knowledge artifacts
content_version: 0.1.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Citation Standard

## Purpose

This standard defines how the repository cites external evidence, internal artifacts, formulas, datasets, product documentation, standards, and project decisions.

The objective is to make every material claim:

- traceable;
- reviewable;
- durable when files move;
- explicit about source quality and freshness;
- usable by humans and Cursor agents without loading unnecessary research context.

## Scope

This standard applies to:

- knowledge packs;
- research records;
- methodology and architecture documents containing external claims;
- KPI and calculation definitions;
- examples and evaluations that depend on evidence;
- rules, skills, and subagents that cite authoritative repository content;
- public-facing documentation.

Administrative instructions and clearly labelled project decisions do not require external citations, but they must reference the relevant internal decision or standard where one exists.

## Core rules

1. Cite the claim, not merely the paragraph topic.
2. Place the citation immediately after the supported statement.
3. Prefer the original source over a source that repeats it.
4. Cite unstable facts every time they are materially used.
5. Record retrieval date, version, jurisdiction, and effective date when relevant.
6. Distinguish evidence, inference, and project decision.
7. Do not use a citation that does not actually support the wording.
8. Do not create the appearance of certainty by stacking weak sources.
9. Keep citations readable in Markdown and durable in version control.
10. Preserve copyright by paraphrasing and using brief quotations only when necessary.

## Repository citation model

The repository uses two linked layers:

### Layer 1 — Claim-level citation

Use a descriptive Markdown footnote immediately after the claim:

```markdown
Cursor project rules are stored under `.cursor/rules` and use MDC files.[^cursor-rules]
```

### Layer 2 — Source record

Define the footnote under `## Sources` in the same file:

```markdown
[^cursor-rules]: Cursor, “Rules,” updated date not stated, retrieved 2026-07-17, https://docs.cursor.com/context/rules.
```

For high-value or repeatedly used sources, also create an entry in the central research register once its schema is approved.

A local footnote remains required even when the source exists in the central register, because the file must remain intelligible when viewed independently.

## Footnote identifiers

Use stable descriptive identifiers rather than sequence-only labels.

Preferred:

```text
[^cursor-rules]
[^mckinsey-visual-performance]
[^wgea-employer-pay-gaps-2026]
[^cleveland-mcgill-1984]
```

Avoid:

```text
[^1]
[^source]
[^website]
```

Identifier rules:

- lowercase kebab-case;
- concise but unique within the file;
- include year when the source is periodic or version-sensitive;
- do not reuse one identifier for different sources.

## Source-entry formats

### Web page

```text
Organisation or author, “Page title,” publication or updated date if known, retrieved YYYY-MM-DD, URL.
```

Example:

```markdown
[^cursor-rules]: Cursor, “Rules,” updated date not stated, retrieved 2026-07-17, https://docs.cursor.com/context/rules.
```

### Product documentation or release note

Include product, version or release, feature state, and retrieval date where available:

```markdown
[^cursor-2-4-skills]: Cursor, “Subagents, Skills, and Image Generation,” release 2.4, 2026, retrieved 2026-07-17, https://cursor.com/changelog/2-4.
```

### Journal article

```text
Author(s), “Article title,” Journal, volume(issue), year, page range, DOI or stable URL.
```

### Book

```text
Author, Title, edition, publisher, year, relevant page or chapter.
```

Use a page or chapter when supporting a specific method or quotation.

### Standard

```text
Standards body, Standard identifier and title, edition or year, clause or section, stable URL where public.
```

Do not reproduce restricted standards content beyond fair, brief description.

### Legislation or regulation

```text
Jurisdiction, instrument title and identifier, current compilation or effective date, section or clause, official URL, retrieved date.
```

### Official dataset or statistical release

```text
Publisher, dataset or release title, reference period, table or series identifier, release date, URL, retrieved date.
```

### Commercial survey or market publication

Include geography, sample or coverage description where available, effective period, and access limitations.

Do not commit licensed tables or proprietary pay data.

### Conference presentation or webinar

Include presenter, title, event, organiser, date, slide or timestamp where relevant, and stable URL.

### GitHub repository, issue, pull request, or commit

Use the canonical URL and pin implementation-sensitive evidence to a commit, release, issue, or pull request where possible:

```text
Owner/repository, path or issue title, commit SHA or issue number, date, URL.
```

### Internal repository artifact

Use a relative link plus immutable artifact ID:

```markdown
The research process must follow [STD-CORE-002](../../docs/standards/research-standard.md).
```

When referring to an approved decision that may change materially, include the content version:

```text
STD-CORE-002 v0.1.0
```

## Claim placement

### Single claim

```markdown
Project rules are persistent, reusable context supplied to Cursor Agent.[^cursor-rules]
```

### Multiple claims from different sources

Cite each claim independently:

```markdown
Project rules are stored under `.cursor/rules`.[^cursor-rules] Agent Skills are loaded dynamically when relevant.[^cursor-agent-best-practices]
```

Do not place one citation at the end of a paragraph containing several unsupported factual claims.

### Entire table

If all values come from one source, cite the table title or introductory sentence and include source details directly below the table.

If rows or columns come from different sources, add a `Source` column or row-level footnotes.

### Diagrams and adapted frameworks

Use one of:

```text
Source:
Adapted from:
Project synthesis informed by:
```

`Adapted from` means the source structure remains recognisable. `Project synthesis informed by` means the repository combined multiple ideas into a new structure.

## Evidence, inference, and decision notation

Where a reader could confuse interpretation with evidence, use explicit labels.

### Evidence

```markdown
**Evidence:** Official Cursor documentation places project rules in `.cursor/rules`.[^cursor-rules]
```

### Inference

```markdown
**Inference:** A small number of focused rules should reduce persistent context load compared with one large rule.[^cursor-rules]
```

The source supports the premise; the file must clearly identify that the conclusion is inferred.

### Project decision

```markdown
**Project decision:** This repository uses one rule per bounded concern and keeps each rule under 500 lines.
```

A project decision does not require an external citation unless it claims external authority. It should reference the relevant architecture or standard artifact.

## Source-quality labels

Research records must classify sources as:

```text
primary-authoritative
authoritative-synthesis
practitioner-evidence
discovery-only
```

These labels normally remain in the research record rather than cluttering the final knowledge file. Include them in the published file when source quality is central to interpretation.

## Current and unstable information

For product behaviour, law, regulation, market data, schedules, or other unstable information, include:

- `retrieved_date`;
- publication or updated date when available;
- version, release, or effective period;
- jurisdiction where relevant;
- a review trigger.

Example:

```markdown
Cursor 2.4 introduced Agent Skills in the editor and CLI.[^cursor-2-4-skills]
```

Do not silently generalise a version-specific feature into a permanent capability.

## Consulting-firm attribution

Firm-specific claims require a direct official source.

Acceptable:

```markdown
McKinsey's public article describes a 1–3–10 approach to visual performance management.[^mckinsey-1-3-10]
```

Not acceptable:

```markdown
McKinsey always uses this dashboard layout.
```

If the evidence is based on recurring public exhibits rather than a declared method, label it `Observed convention` and cite representative official examples.

General consulting practices should not be attributed to one firm without evidence.

## Formula and KPI citations

A KPI definition must distinguish:

1. externally sourced concept;
2. repository-specific formula;
3. organisation-specific implementation.

Example:

```markdown
The external concept is new-hire pay relative to comparable incumbent pay.[^source]

**Repository definition:**

\[
\text{New-hire premium} = \frac{\text{new-hire FTE fixed pay}}{\text{median comparable incumbent FTE fixed pay}} - 1
\]
```

The formula requires a citation only when adopted from an external standard. A project-designed formula must be labelled as a repository definition and justified through the KPI-definition artifact.

Every published KPI must cite or link to its approved KPI-definition artifact.

## Quotations

- Use quotation marks or a block quote for verbatim text.
- Cite immediately with page, section, paragraph, or timestamp where available.
- Keep quotations short.
- Never reconstruct a quotation from memory.
- Do not combine fragments in a way that changes meaning.
- Prefer paraphrase for most knowledge artifacts.
- Do not reproduce song lyrics, proprietary standards, licensed market data, or substantial copyrighted passages.

## Citation laundering and provenance

Citation laundering occurs when a source is cited for a claim it copied from another source without checking the origin.

Required response:

1. follow the citation to the original source where accessible;
2. cite the original for the claim;
3. cite the secondary source only for its independent interpretation;
4. record when the original is inaccessible.

Multiple secondary sources repeating the same origin do not count as independent triangulation.

## Links and durability

- Prefer canonical HTTPS URLs.
- Prefer DOI, regulator, official documentation, or permanent publication links.
- Avoid tracking parameters and temporary signed URLs.
- Pin technical implementation claims to versions, releases, or commits where practical.
- Record an archived URL only when permitted and useful.
- Use relative links for repository files.
- Run the internal-link checker before approval.

## Source register

The central source register will live under:

```text
knowledge/research-register/
```

The approved schema must support:

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
licence_or_usage_notes:
relevant_artifacts:
review_notes:
```

Source IDs use lowercase kebab-case and must remain stable after publication.

## Citation density rules

A citation is required for:

- non-common factual claims;
- numbers, dates, thresholds, and benchmark values;
- current product capabilities;
- legal and regulatory requirements;
- firm-specific methods or conventions;
- named theories and research findings;
- causal or predictive claims;
- external definitions and formulas;
- material limitations attributed to a source.

A citation is not normally required for:

- navigation instructions within the repository;
- clearly labelled project decisions;
- examples that are explicitly fictional;
- pure logical deductions whose premises are already cited and whose inference is labelled;
- common arithmetic shown transparently.

## Prohibited citation practices

- Citing a search-result snippet instead of the underlying page.
- Citing an AI assistant response as evidence.
- Including a source in the list that is never connected to a claim.
- Using a prestigious source that does not support the statement.
- Citing an outdated product page without version qualification.
- Hiding uncertainty behind a long bibliography.
- Linking to pirated, unauthorised, or confidential material.
- Citing internal or private documents in a public artifact without approval.
- Using raw internal file-system paths as public citations.

## Review checklist

A reviewer must confirm:

- each material claim has appropriate support;
- the citation directly supports the wording;
- primary sources were used where available;
- firm attribution is accurate;
- version, date, jurisdiction, and population are included where relevant;
- evidence and inference are clearly separated;
- quotations are exact, brief, and lawful;
- URLs are canonical and accessible;
- internal links resolve;
- source entries contain enough information to relocate the evidence;
- public-repository restrictions are satisfied.

## Acceptance criteria

This standard can move to `IN REVIEW` when:

- the research-record schema implements the required source fields;
- the central research-register format is defined;
- one product claim, one P&R KPI, one academic claim, one consulting attribution, and one internal decision have been cited successfully;
- internal-link and citation validation requirements are implementable;
- a reviewer can distinguish evidence, inference, and project decision consistently.

It can move to `APPROVED` after successful use in the first audience, holistic P&R, and current-product knowledge packs.

## Sources

[^cursor-rules]: Cursor, “Rules,” updated date not stated, retrieved 2026-07-17, https://docs.cursor.com/context/rules.

[^cursor-2-4-skills]: Cursor, “Subagents, Skills, and Image Generation,” release 2.4, 2026, retrieved 2026-07-17, https://cursor.com/changelog/2-4.

[^cursor-agent-best-practices]: Cursor, “Best practices for coding with agents,” 2026, retrieved 2026-07-17, https://cursor.com/blog/agent-best-practices.

## Review notes

This citation model is a project governance decision. It uses GitHub-compatible Markdown footnotes and a planned central source register to balance local readability with reusable provenance. The model must be tested against actual knowledge artifacts before approval.
