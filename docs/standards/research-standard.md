---
artifact_id: STD-CORE-002
status: DRAFT
phase: 0
priority: critical
depends_on:
  - STD-CORE-001: docs/standards/naming-standard.md
  - BUILD-ORDER.md
  - DEPENDENCIES.md
blocks:
  - docs/standards/citation-standard.md
  - docs/plans/research-program.md
  - all governed knowledge artifacts
  - all research-dependent Cursor skills
content_version: 0.1.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Research Standard

## Purpose

This standard defines how evidence is gathered, assessed, synthesised, recorded, reviewed, and refreshed for the Performance & Reward Dashboard Architect.

The objective is not to collect the largest number of sources. It is to produce decision-ready knowledge that is:

- accurate;
- appropriately current;
- traceable to authoritative evidence;
- explicit about uncertainty;
- suitable for the intended audience and jurisdiction;
- reusable by modular Cursor skills without unnecessary context duplication.

## Scope

This standard applies to:

- Performance & Reward domain knowledge;
- consulting communication techniques;
- visual-design and data-visualisation research;
- dashboard UX and information architecture;
- Power BI and Cursor product behaviour;
- regulatory and governance content;
- KPI definitions, calculations, and diagnostic methods;
- examples that make factual or methodological claims;
- research used to author rules, skills, subagents, schemas, and evaluation cases.

It does not require citations for purely administrative repository instructions or clearly labelled project decisions that do not claim external authority.

## Research principles

1. **Begin with a decision or capability need, not a broad topic.**
2. **Use the most authoritative source appropriate to the claim.**
3. **Separate evidence from interpretation and project design decisions.**
4. **Treat current product, market, and regulatory information as time-sensitive.**
5. **Do not attribute a technique to a consulting firm without direct support.**
6. **Prefer synthesis over copying.** Preserve copyright and avoid long quotations.
7. **Capture limitations, conflicting evidence, and applicability boundaries.**
8. **Research once, store once, and reference the authoritative knowledge artifact.**
9. **Do not publish confidential, personal, licensed, or proprietary source material.**
10. **A plausible statement without evidence remains unverified.**

## Required research brief

Before substantive research begins, create or complete a research record containing:

```yaml
artifact_id:
research_question:
decisions_supported:
intended_consumers:
audiences:
domain:
consumption_modes:
jurisdictions:
as_of_date:
scope:
exclusions:
required_source_types:
freshness_requirement:
known_assumptions:
open_questions:
```

The research question must be narrow enough to determine what evidence would answer it.

Weak:

```text
Research executive dashboards.
```

Strong:

```text
Which conclusion-led communication, visual hierarchy, and comparison techniques should an executive Performance & Reward summary use when the primary decision is whether to endorse or redirect reward investment?
```

## Research classes

Every research task must be assigned at least one class because source quality and freshness differ by class.

| Class | Examples | Primary evidence expectation |
|---|---|---|
| Stable theory | visual perception, Gestalt, statistical principles | original research, established textbooks, standards |
| Current product | Cursor, Power BI, Power BI Service | official documentation, release notes, product blogs |
| P&R professional practice | fixed reward, performance, job architecture | professional bodies, established methodology providers, original research |
| Regulatory or legal | pay transparency, prudential remuneration, privacy | legislation, regulator, official guidance |
| Consulting technique | Pyramid Principle, issue trees, exhibit conventions | original author, firm publication, direct public methodology |
| Observed practitioner pattern | implementation limitations, community workarounds | reproducible case evidence, issue trackers, practitioner sources |
| Organisation-specific decision | audience model, quality gate, naming convention | project decision record with rationale |

A knowledge artifact may combine classes, but claims must retain the correct evidence standard.

## Source hierarchy

### Level 1 — Primary authoritative sources

Preferred source of truth:

- legislation and official regulatory guidance;
- official product documentation and release notes;
- original research papers and standards;
- original books or publications defining a named method;
- official methodology pages from the organisation that owns the method;
- first-party technical specifications;
- official public data and statistical releases.

### Level 2 — Authoritative synthesis

Use to interpret or compare primary evidence:

- peer-reviewed review papers;
- recognised professional bodies;
- reputable academic or research institutions;
- established consulting, reward, and workforce-research organisations;
- high-quality vendor methodology publications where the commercial interest is clear.

### Level 3 — Practitioner evidence

Use for implementation experience, edge cases, and observed limitations:

- well-documented engineering or analytics articles;
- public case studies;
- issue trackers and release discussions;
- community forum posts with reproducible detail;
- conference presentations from identifiable practitioners.

Practitioner evidence must not override official product or regulatory sources. It may demonstrate that official behaviour is incomplete, version-dependent, or unreliable in practice.

### Level 4 — Discovery-only sources

May help locate better evidence but must not be the final authority:

- unsourced blogs;
- search-result summaries;
- content farms and aggregators;
- AI-generated text;
- anonymous social posts;
- copied frameworks without provenance.

Level 4 material must not appear as the sole support for a published claim.

## Domain-specific source rules

### Cursor and Power BI

- Use official documentation and release notes as the default source of truth.
- Record retrieval date and relevant version or release where available.
- Use community reports only for observed defects, limitations, or workarounds.
- Clearly label preview, beta, deprecated, legacy, or version-specific behaviour.
- Reverify implementation-sensitive claims before release.

### Performance & Reward

- Prefer original methodology owners, recognised reward and HR professional bodies, regulators, academic research, and established market-research providers.
- Distinguish universal principles from vendor-specific models.
- Do not treat a commercial survey as representative without understanding its sample, geography, sector, and effective date.
- Define formulas and population rules locally even when the conceptual metric is externally sourced.
- Separate internal equity, external market position, performance differentiation, affordability, employee experience, and talent outcomes rather than implying one proves another.

### Consulting-firm techniques

Every firm-specific statement must be labelled as one of:

| Label | Meaning |
|---|---|
| `Published methodology` | The firm explicitly describes the method or principle |
| `Published example` | The technique is visible in an official public exhibit or case |
| `Observed convention` | Repeated public examples suggest a pattern, but the firm has not declared it a standard |
| `General consulting practice` | Broadly used across firms; no exclusive attribution |
| `Project synthesis` | This repository combines multiple practices into its own recommendation |

Do not write “McKinsey uses X” or equivalent unless the source directly supports that attribution.

### Regulation and law

- Official legislation, regulator publications, and official government guidance are authoritative.
- Secondary sources may explain but must not define the obligation.
- Record jurisdiction, commencement date, applicability threshold, and status.
- Include a non-legal-advice note where content could be mistaken for legal advice.
- Reverify before a release that depends on the requirement.

### Visual design and data visualisation

- Prefer original empirical studies, established textbooks, and recognised standards.
- Distinguish experimentally supported perceptual findings from design heuristics.
- Do not convert a useful heuristic into an absolute rule without evidence.
- Record accessibility standards separately from aesthetic preferences.

## Freshness and review rules

| Evidence type | Default verification requirement |
|---|---|
| Cursor and Power BI behaviour | verified within 30 days of authoring or release review |
| Preview or beta functionality | verified at each material use and release |
| Law and regulation | verified at authoring and immediately before affected release |
| Market data and salary movement | latest appropriate effective period explicitly recorded |
| Consulting-firm public methodology | verify page remains available at review; method date recorded where known |
| Stable academic theory | original publication date recorded; no artificial recency requirement |
| Internal project decision | review when dependencies or product architecture change |

A source's webpage update date is useful but not sufficient. Assess whether the actual content is current.

## Required research process

### 1. Frame

- Define the decision or capability supported.
- Resolve audience, domain, jurisdiction, and consumption mode.
- State the boundaries and exclusions.
- Identify likely dependencies and downstream consumers.

### 2. Plan sources

- Identify required primary sources.
- Define acceptable secondary and practitioner sources.
- Set freshness requirements.
- Identify proprietary or copyright constraints.

### 3. Search broadly, then narrow

- Use multiple queries and terminology variants.
- Follow citations back to original sources.
- Search for evidence that contradicts the emerging answer.
- Record failed or insufficient searches where they affect confidence.

### 4. Capture evidence

For each source, record:

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
relevant_claims:
limitations:
licence_or_usage_notes:
```

### 5. Build a claims matrix

Each material claim must be traceable to evidence:

| Claim ID | Claim | Evidence | Confidence | Applicability | Notes |
|---|---|---|---|---|---|

The matrix may remain in a research record rather than the final knowledge file, but it must be available for review.

### 6. Synthesise

Organise findings around:

- decision questions;
- causal or value-driver logic;
- selection rules;
- audience differences;
- BAU and non-BAU applications;
- interactive and static reporting implications;
- limitations and anti-patterns.

Do not write a source-by-source literature dump unless the artifact is explicitly a review.

### 7. Resolve conflicts

When credible sources disagree:

1. confirm they address the same definition, population, period, and jurisdiction;
2. prefer direct and primary evidence for factual claims;
3. present materially different viewpoints fairly;
4. identify the repository's chosen position as a project decision;
5. preserve unresolved uncertainty rather than manufacturing consensus.

### 8. Review

A reviewer must assess:

- source authority and diversity;
- recency and version relevance;
- accurate representation of sources;
- unsupported causal language;
- missing counterevidence;
- firm-attribution accuracy;
- applicability to P&R and the intended audience;
- duplication with existing knowledge files;
- copyright, privacy, and public-repository safety.

### 9. Publish and schedule refresh

- Move approved knowledge into its authoritative file.
- Add citations according to `STD-CORE-003`.
- Update status, content version, source-as-of date, and next review.
- Record downstream artifacts requiring refresh.

## Triangulation requirements

### One source may be sufficient when

- an official product document directly defines current supported behaviour;
- legislation or a regulator directly states an obligation;
- an original source defines its own named method;
- the claim is narrow, uncontroversial, and accurately scoped.

### Two or more independent sources are normally required when

- making causal claims about workforce or organisational outcomes;
- recommending a cross-industry design practice;
- comparing consulting approaches;
- asserting that a metric predicts attraction, retention, performance, fairness, or productivity;
- generalising from a commercial survey or case study;
- official product documentation conflicts with observed behaviour.

Triangulation does not mean citing multiple sources that repeat the same unsupported origin.

## Evidence and uncertainty labels

Use these labels in research records and, where material, in knowledge artifacts:

| Label | Meaning |
|---|---|
| `Established` | Strong direct or convergent authoritative evidence |
| `Supported synthesis` | Reasonable conclusion combining multiple sources |
| `Preliminary` | Limited evidence or emerging practice |
| `Inference` | Logical conclusion not directly stated by the evidence |
| `Project decision` | Deliberate repository design choice |
| `Unresolved` | Evidence is insufficient or conflicting |

Never present `Inference` or `Project decision` as externally established fact.

## Quantitative and KPI research

For every KPI or calculation, research must establish or explicitly decide:

- business question;
- conceptual definition;
- formula;
- numerator and denominator;
- unit;
- population and exclusions;
- effective date and time logic;
- aggregation method;
- comparison and benchmark;
- direction of improvement;
- materiality threshold;
- segmentation;
- sample-size or confidentiality constraints;
- known interpretation risks.

A widely used metric name does not guarantee a standard formula. The repository definition remains mandatory.

## Causal language

Use language proportionate to the evidence:

- `is associated with` for observational relationships;
- `may indicate` for diagnostic signals;
- `contributes to` where multiple drivers exist;
- `causes` only with adequate causal evidence.

A dashboard pattern must not imply that a P&R intervention caused a workforce outcome merely because the measures moved together.

## Copyright and quotation

- Paraphrase source ideas in original language.
- Quote only when exact wording is necessary.
- Keep quotations brief and cite immediately.
- Do not reproduce proprietary frameworks, pay data, research tables, or copyrighted graphics without permission.
- Describe inaccessible proprietary material as unavailable rather than inventing its contents.

## Privacy, confidentiality, and public-repository safety

Do not commit:

- personal information;
- employee-level examples derived from real people;
- confidential market data;
- licensed salary-survey tables;
- internal policies, business rules, or organisation names not approved for public release;
- private URLs, credentials, tenant identifiers, or screenshots containing sensitive information.

Use synthetic or clearly fictional examples.

## Research handoff requirements

A research subagent or contributor must return:

```yaml
research_question:
executive_summary:
findings:
selection_rules:
techniques_considered:
techniques_rejected:
claims_requiring_caution:
conflicts_and_gaps:
recommended_repository_changes:
sources:
next_review_trigger:
```

The return must be concise enough for the parent agent to use without importing the entire research trail into its context.

## Failure conditions

Research fails review if it:

- relies on AI output as evidence;
- uses only discovery-level sources for a material claim;
- attributes a method to a firm without direct support;
- omits jurisdiction or effective date for unstable content;
- hides conflicting evidence;
- defines a KPI without population and aggregation rules;
- copies source language or proprietary material excessively;
- introduces confidential or personal information;
- duplicates an existing authoritative knowledge artifact;
- lacks a clear decision or capability use.

## Acceptance criteria

This standard can move to `IN REVIEW` when:

- the research-record schema maps to all required fields;
- one stable-theory topic and one current-product topic have been trialled;
- one P&R KPI definition has been traced from evidence to repository decision;
- a firm-attribution example has been classified correctly;
- source freshness and uncertainty can be validated consistently.

It can move to `APPROVED` after independent evidence review and successful use in the first Phase 3 and Phase 4 research workstreams.

## Sources and review notes

The current-product provisions are informed by Cursor's official documentation that project rules are version-controlled files under `.cursor/rules`, by Cursor's 2.4 release description of dynamically discovered `SKILL.md` skills, and by its guidance that skills keep context focused by loading specialised capabilities when relevant.

- [Cursor Rules](https://docs.cursor.com/context/rules), Cursor, retrieved 2026-07-17.
- [Cursor 2.4: Subagents, Skills, and Image Generation](https://cursor.com/changelog/2-4), Cursor, retrieved 2026-07-17.
- [Best practices for coding with agents](https://cursor.com/blog/agent-best-practices), Cursor, retrieved 2026-07-17.

This standard is principally a repository governance decision. Its effectiveness must be validated through actual research artifacts rather than assumed from documentation alone.
