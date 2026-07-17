---
artifact_id: STD-CORE-002
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
blocks:
  - STD-CORE-003
  - PLAN-CORE-001
  - all governed knowledge artifacts
  - all research-dependent Cursor skills
content_version: 0.2.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Research standard

## Purpose

This standard defines how evidence is framed, gathered, assessed, synthesised, recorded, reviewed, and refreshed for the Performance & Reward Dashboard Architect.

The goal is decision-ready knowledge that is:

- accurate and appropriately current;
- traceable to evidence;
- explicit about uncertainty and applicability;
- safe for a public repository;
- reusable by modular Cursor skills without unnecessary context duplication.

## Scope

This standard applies to:

- Performance & Reward domain knowledge;
- consulting communication techniques;
- visual design and data visualisation;
- dashboard user experience and information architecture;
- Cursor and Power BI product behaviour;
- regulatory and governance content;
- KPI definitions, calculations, and diagnostic methods;
- examples and evaluations that make factual or methodological claims;
- research used to author rules, skills, subagents, schemas, and templates.

Administrative instructions and clearly labelled project decisions do not need artificial external evidence.

## Principles

1. Begin with a decision or capability need, not a broad topic.
2. Use the most authoritative source appropriate to the specific claim.
3. Separate evidence, synthesis, inference, and project decision.
4. Treat product, market, regulatory, and legal information as time-sensitive.
5. Do not attribute a technique to a consulting firm without direct support.
6. Prefer synthesis over copying.
7. Capture limitations, counterevidence, and applicability boundaries.
8. Research once, store once, and reference the authoritative artifact.
9. Do not publish confidential, personal, licensed, or proprietary material.
10. A plausible statement without evidence remains unverified.
11. Source authority is claim-relative: a firm is primary for its own published method, but not automatically primary for claims about effectiveness.
12. An approval review must be independent of the authoring workflow.

## Research brief

Before substantive research begins, create a research record containing:

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

Weak:

```text
Research executive dashboards.
```

Strong:

```text
Which conclusion-led communication, visual hierarchy, and comparison techniques should an executive Performance & Reward summary use when the primary decision is whether to endorse or redirect reward investment?
```

## Research classes

| Class | Examples | Primary evidence expectation |
|---|---|---|
| Stable theory | visual perception, statistics | original research, established textbooks, standards |
| Current product | Cursor, Power BI | official documentation, release notes, product guidance |
| P&R professional practice | fixed reward, performance, job architecture | professional bodies, methodology owners, academic research |
| Regulatory or legal | pay transparency, privacy, remuneration regulation | legislation, regulator, official guidance |
| Consulting technique | Pyramid Principle, issue trees, exhibits | original author, official firm publication, direct public methodology |
| Practitioner pattern | defects, limitations, workarounds | reproducible cases, issue trackers, identified practitioners |
| Project decision | audience model, quality gate, repository architecture | decision record with rationale and alternatives |

A knowledge artifact may combine classes, but each claim keeps the evidence standard appropriate to its class.

## Source hierarchy

### Primary authoritative

Use for direct factual claims where available:

- legislation and regulator guidance;
- official product documentation and release notes;
- original research and recognised standards;
- original publications defining named methods;
- official methodology pages from the method owner;
- first-party technical specifications;
- official data and statistical releases.

### Authoritative synthesis

Use to interpret or compare primary evidence:

- peer-reviewed reviews;
- recognised professional bodies;
- reputable academic or research institutions;
- established consulting, reward, and workforce-research organisations;
- high-quality vendor methodology publications with commercial interest disclosed.

### Practitioner evidence

Use for implementation experience, defects, limitations, and edge cases:

- documented technical articles;
- public case studies;
- issue trackers and release discussions;
- reproducible community reports;
- conference material from identifiable practitioners.

Practitioner evidence does not silently replace official product or regulatory sources. It may show that official guidance is incomplete, version-dependent, or inconsistent with observed behaviour.

### Discovery-only

Use only to locate stronger evidence:

- unsourced blogs;
- search-result summaries;
- aggregators and content farms;
- AI-generated text;
- anonymous posts;
- copied frameworks without provenance.

Discovery-only material cannot be the sole support for a published material claim.

## Domain-specific rules

### Cursor and Power BI

- Use official documentation and release notes as the default baseline.
- Record retrieval date and version or release where available.
- Use practitioner sources for reproducible limitations and workarounds.
- Label preview, beta, deprecated, legacy, and version-specific behaviour.
- Reverify implementation-sensitive claims before activation and release.

Cursor places project rules under `.cursor/rules` and documents dynamically loaded Agent Skills separately from persistent rules.[^cursor-rules][^cursor-practices]

### Performance & Reward

- Prefer recognised professional bodies, regulators, methodology owners, original research, and established market-research providers.
- Distinguish universal principles from vendor-specific models.
- Do not generalise a commercial survey without understanding sample, sector, geography, and effective period.
- Define formulas, population rules, effective-date logic, and aggregation locally even when the concept is externally sourced.
- Keep internal equity, external market position, performance differentiation, affordability, employee experience, and talent outcomes analytically distinct.
- Do not infer causation from co-movement.

### Consulting-firm techniques

Classify firm-specific statements as:

| Label | Meaning |
|---|---|
| `Published methodology` | The firm explicitly describes the method |
| `Published example` | The technique is visible in an official exhibit or case |
| `Observed convention` | Repeated official examples suggest a pattern, but no declared standard exists |
| `General consulting practice` | Broad practice with no exclusive firm attribution |
| `Project synthesis` | The repository combines multiple practices into its own recommendation |

Do not write “Firm X uses Y” unless the evidence supports that exact scope.

### Regulation and law

- Official legislation, regulators, and government guidance define obligations.
- Secondary sources may explain but not establish the obligation.
- Record jurisdiction, status, commencement date, applicability threshold, and source date.
- Add a non-legal-advice note where users could mistake the content for legal advice.
- Reverify immediately before an affected release.

### Visual design and data visualisation

- Prefer original empirical research, established textbooks, and recognised standards.
- Distinguish measured perceptual findings from design heuristics.
- Do not convert heuristics into universal laws.
- Treat accessibility requirements separately from aesthetic preferences.

## Freshness rules

| Evidence type | Default verification requirement |
|---|---|
| Cursor and Power BI behaviour | within 30 days of authoring or release review |
| Preview or beta functionality | at each material use and release |
| Law and regulation | at authoring and immediately before affected release |
| Market data and salary movement | latest appropriate effective period explicitly recorded |
| Consulting-firm methodology | page availability and publication date checked at review |
| Stable academic theory | original publication recorded; no artificial recency rule |
| Project decision | review when dependencies or architecture change |

Updating a retrieval date requires actually reopening and checking the source.

## Required process

### 1. Frame

- Define the decision or capability.
- Resolve audience, domain, jurisdiction, and consumption mode.
- State scope and exclusions.
- Identify dependencies and consumers.

### 2. Plan sources

- Identify required primary sources.
- Define acceptable synthesis and practitioner evidence.
- Set freshness requirements.
- Identify copyright, licence, and confidentiality constraints.

### 3. Search and challenge

- Use terminology variants.
- Follow citations to original sources.
- Search deliberately for contradictory evidence.
- Record material failed searches and gaps.

### 4. Capture evidence

Each reusable source record contains:

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

`relevant_artifacts` contains only registered immutable artifact IDs. Future destinations belong in `planned_consumers`.

### 5. Build a claims matrix

| Claim ID | Claim | Evidence | Confidence | Applicability | Repository treatment |
|---|---|---|---|---|---|

The claims matrix may remain in the research record, but it must be available for review.

### 6. Synthesise

Organise findings around:

- decision questions;
- causal or value-driver logic;
- selection rules;
- audience differences;
- BAU and non-BAU applications;
- interactive and static implications;
- limitations and anti-patterns.

Do not produce a source-by-source literature dump unless the artifact is explicitly a review.

### 7. Resolve conflicts

1. Confirm definition, population, period, and jurisdiction alignment.
2. Prefer direct primary evidence for factual claims.
3. Present materially different credible views.
4. Label the repository's selected position as a project decision.
5. Preserve unresolved uncertainty.

### 8. Review

A reviewer assesses:

- authority and source diversity;
- recency and version relevance;
- accurate representation;
- unsupported causal language;
- missing counterevidence;
- consulting attribution;
- P&R and audience applicability;
- duplication;
- copyright, privacy, and public-repository safety.

An approval reviewer must not be the sole author of the material changes. An internal pre-review may identify defects but cannot satisfy the independent-review gate.

### 9. Publish and refresh

- Move approved knowledge into its authoritative artifact.
- Apply `STD-CORE-003` citations.
- Update status, content version, source-as-of date, and next review.
- Record downstream artifacts needing refresh.

## Triangulation

One source may be sufficient when it directly defines:

- current official product behaviour;
- a legal or regulatory obligation;
- the source owner's named method;
- a narrow and accurately scoped fact.

Two or more independent sources are normally required when:

- making causal workforce claims;
- recommending a cross-industry design practice;
- comparing consulting approaches;
- claiming predictive value for attraction, retention, performance, fairness, or productivity;
- generalising from a survey or case;
- official documentation conflicts with observed behaviour.

Multiple sources repeating one unsupported origin do not constitute triangulation.

## Evidence labels

| Label | Meaning |
|---|---|
| `Established` | Strong direct or convergent evidence |
| `Supported synthesis` | Reasonable conclusion combining evidence |
| `Preliminary` | Limited or emerging evidence |
| `Inference` | Logical conclusion not directly stated |
| `Project decision` | Deliberate repository choice |
| `Unresolved` | Evidence insufficient or conflicting |
| `Rejected` | Considered and not accepted |

Never present inference or project decision as externally established fact.

## KPI and quantitative research

Every KPI must establish or explicitly decide:

- business question;
- conceptual definition;
- formula, numerator, denominator, and unit;
- grain, population, and exclusions;
- effective date and time logic;
- aggregation and weighting;
- comparator and benchmark;
- direction and materiality;
- segmentation;
- coverage and data quality;
- minimum sample and confidentiality;
- interpretation risks and misuse conditions.

A familiar metric name does not guarantee a standard formula. Historical cohort definitions must avoid survivorship and selection bias.

## Causal language

Use language proportionate to evidence:

- `is associated with` for observational relationships;
- `may indicate` for diagnostic signals;
- `contributes to` where multiple drivers exist;
- `causes` only with adequate causal evidence.

## Copyright, privacy, and public safety

- Paraphrase in original repository language.
- Quote only when exact wording is necessary and keep quotations brief.
- Do not reproduce proprietary frameworks, licensed pay data, research tables, or graphics without permission.
- Do not commit personal information, real employee examples, private URLs, credentials, tenant identifiers, confidential policies, or unapproved organisation names.
- Use synthetic examples.

## Research handoff

A research contributor or subagent returns:

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

The handoff must be concise enough to use without importing the entire research trail into the main context.

## Failure conditions

Research fails review if it:

- relies on AI output as evidence;
- uses only discovery-level sources for a material claim;
- makes unsupported firm attribution;
- omits jurisdiction or effective date for unstable content;
- hides conflicting evidence;
- defines a KPI without population and aggregation rules;
- introduces survivorship or selection bias without disclosure;
- copies protected or proprietary material excessively;
- exposes confidential or personal information;
- duplicates an existing authority;
- lacks a clear decision or capability use.

## Acceptance criteria

This standard can move to `IN REVIEW` when:

- the research-record **field contract** covers the required brief, source, claim, uncertainty, and handoff fields;
- the central source-register format validates;
- stable-theory, current-product, P&R KPI, consulting-attribution, and project-decision trials are complete;
- freshness and uncertainty rules are enforced or tested;
- the internal pre-review's critical and major findings are resolved.

A formal Phase 2 schema is not required for the Phase 0 status transition; it must implement this approved field contract later.

This standard can move to `APPROVED` after independent review and correction of all critical and major findings. It must receive a mandatory post-implementation review after the first Phase 3 audience pack and first Phase 4 holistic P&R pack; that review may revise the approved standard but does not block initial Phase 0 approval.

## Sources

[^cursor-rules]: Cursor, “Rules,” updated date not stated, retrieved 2026-07-17, https://docs.cursor.com/context/rules. Central source ID: `cursor-rules`.

[^cursor-practices]: Cursor, “Best practices for coding with agents,” 2026, retrieved 2026-07-17, https://cursor.com/blog/agent-best-practices. Central source ID: `cursor-agent-best-practices`.

## Review notes

The internal Phase 0 pre-review removed the approval deadlock, replaced the formal-schema prerequisite with a field contract, formalised reviewer independence, separated registered artifacts from planned consumers, and added survivorship-bias controls for KPI research.
