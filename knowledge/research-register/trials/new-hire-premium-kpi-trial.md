---
artifact_id: EX-FIXED-001
status: DRAFT
phase: 0
priority: high
depends_on:
  - STD-CORE-001: ../../../docs/standards/naming-standard.md
  - STD-CORE-002: ../../../docs/standards/research-standard.md
  - STD-CORE-003: ../../../docs/standards/citation-standard.md
  - KNOW-CORE-001: ../README.md
  - KNOW-CORE-002: ../sources.yaml
blocks:
  - Phase 0 KPI-research review
  - future fixed-reward KPI catalogue
content_version: 0.1.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Trial: New-hire premium KPI definition

## Purpose

Test the repository's naming, research, citation, KPI-definition, and evidence-versus-project-decision standards against a Performance & Reward measure.

This trial does not yet establish an approved enterprise KPI. It provides a candidate definition for later review in the fixed-reward and market-competitiveness workstreams.

## Research question

How should a dashboard measure whether external hires are entering at higher fixed pay than comparable incumbents without allowing job mix, geography, currency, or timing to distort the result?

## Decision supported

Determine whether new-hire pay positioning indicates:

- a targeted and explainable hiring premium;
- broader external-market movement;
- potential incumbent pay compression;
- inconsistent offer practice;
- a need for deeper cohort or employee-level review.

## External concept

Mercer Australia describes its new-hire pay rate as the relativity between salaries offered to new staff and salaries paid to existing employees in the same role within an organisation. A positive result indicates that new hires are attracting salaries above current employees in the role; a negative result indicates the reverse.[^mercer-au]

SHRM defines pay compression as employee pay being very close to the pay of more-experienced employees in the same job or employees in higher-level roles, and notes that market rates overtaking historical incumbent increases can contribute to the condition.[^shrm-compression]

Mercer also uses new-hire premiums relative to incumbents as an indicator that compression issues may exist.[^mercer-merit]

These sources support the concept and interpretation. They do not provide a complete universal calculation specification for this repository.

## Candidate repository definition

### Individual matched premium

For each eligible external hire \(i\):

\[
P_i =
\frac{\text{FTE fixed pay of new hire } i}
{\text{median FTE fixed pay of comparable incumbents at the hire date}}
- 1
\]

### Headline KPI

\[
\text{Median new-hire premium} = \operatorname{median}(P_i)
\]

This is a **project-defined calculation** informed by the external concept. It is not presented as Mercer's proprietary formula.

## Why the calculation is employee-first

A simple ratio of total or average new-hire pay to total or average incumbent pay can be distorted when the two populations contain different mixes of jobs, levels, locations, or salaries.

Calculating a matched premium for each hire and then taking the median:

- compares each hire with an appropriate internal reference;
- reduces the effect of extreme offers;
- supports a distribution view rather than one blended number;
- makes cohort coverage visible;
- allows the same method to operate across different salary scales.

This is a supported analytical design decision, not an externally mandated standard.

## Comparator cohort

A comparable incumbent cohort should normally match the new hire on:

1. job profile or approved equivalent role;
2. job level or grade;
3. country and relevant labour market;
4. currency;
5. employment type;
6. full-time-equivalent pay basis;
7. effective date.

Business unit may be added only where internal labour markets or pay structures materially differ.

Comparator precedence should be defined before calculation. A candidate hierarchy is:

```text
Exact job profile + level + labour market
→ approved job-family proxy + level + labour market
→ no comparable cohort
```

The measure must not silently broaden the comparator until a result appears.

## Time basis

Preferred comparison:

```text
New hire's accepted starting fixed pay
versus
comparable incumbent fixed pay effective on the hire date
```

This avoids comparing a new-hire starting offer with incumbent pay after a later salary review.

Where historical effective-dated incumbent pay is unavailable, a current-state approximation may be calculated, but it must be labelled and kept separate from the preferred measure.

## Pay basis

Preferred headline basis:

```text
annualised full-time-equivalent fixed reward
```

Exclude from the headline unless a separate measure is defined:

- variable reward;
- one-off sign-on payments;
- retention payments;
- overtime;
- temporary allowances;
- equity grants;
- employer on-costs.

A total guaranteed cash or total remuneration version may be defined separately where the business question requires it. Different pay bases must not be combined in one series.

## Eligible new-hire population

Candidate inclusion rule:

- external hires;
- commenced within the selected lookback period;
- active or valid at the relevant measurement point;
- complete starting-pay and comparator attributes;
- not part of a separately governed structured-entry program unless reported as its own cohort.

Candidate exclusions:

- internal transfers;
- promotions;
- rehires where prior service materially affects pay, unless separately classified;
- contractors and non-employees;
- graduate, trainee, or apprentice programs where starting rates follow a distinct structure;
- cases without a valid comparator cohort.

The final domain standard must decide these rules explicitly.

## Supporting KPIs

A single premium number is insufficient. The dashboard should pair it with:

| Measure | Purpose |
|---|---|
| Comparable-hire coverage | Shows whether the headline represents the eligible population |
| Percentage with positive premium | Shows prevalence, not only magnitude |
| Percentage above materiality threshold | Highlights potentially significant cases |
| Median premium by job family, level, and labour market | Locates concentration |
| Distribution of individual premiums | Reveals overlap, outliers, and asymmetry |
| Incumbent position-to-market or range position | Tests whether the internal reference is itself behind market |
| New-hire market position | Distinguishes internal premium from external-market premium |

## Materiality thresholds

No universal adverse threshold is established by the sources used in this trial.

**Project decision required:** Define materiality based on reward philosophy, data precision, normal offer flexibility, cohort size, and the decision being supported.

A dashboard may show configurable bands, but it must not imply that a value such as 5% or 10% is universally acceptable or unacceptable.

## Interpretation rules

### Positive premium may indicate

- external market movement;
- scarce-skill hiring pressure;
- outdated salary ranges;
- incumbent pay compression;
- deliberate payment for additional capability or experience;
- inconsistent offer discretion;
- a weak comparator match.

### Negative premium may indicate

- incumbents are ahead of current hiring rates;
- new hires enter lower in the range as intended;
- changes in candidate experience or job scope;
- a declining external market;
- comparator or timing problems.

### The measure does not prove

- unlawful pay inequity;
- that incumbent pay should automatically be increased;
- that a premium caused attrition;
- that the salary structure is incorrect;
- that every positive premium is undesirable.

It is a diagnostic signal requiring segmentation and context.

## Minimum sample and confidentiality

The final KPI standard must define:

- minimum comparator cohort size;
- minimum number of hires for published aggregation;
- suppression and rounding rules;
- treatment of unique roles;
- access controls for employee-level cases.

The public repository will not prescribe organisation-specific thresholds before the privacy and governance framework is completed.

## Candidate KPI specification

| Field | Candidate definition |
|---|---|
| Name | Median new-hire premium |
| Business question | Are external hires entering above comparable incumbents, and where is that concentrated? |
| Unit | Percentage |
| Grain | Individual eligible external hire |
| Numerator | New-hire annualised FTE fixed pay |
| Denominator | Median annualised FTE fixed pay of comparable incumbents at hire date |
| Aggregation | Median of individual premiums |
| Comparator | Prior period, internal materiality band, market position |
| Direction | Context-dependent; increasing positive premium is generally a watch signal |
| Frequency | Monthly or quarterly diagnostic; cycle summary where relevant |
| Main segments | Job profile, level, labour market, business unit, critical skill |
| Coverage measure | Comparable eligible hires divided by all eligible external hires |
| Key limitation | Results depend on comparator quality and effective-dated pay availability |

## Alternative calculations considered

### Ratio of medians

\[
\frac{\operatorname{median}(\text{new-hire pay})}
{\operatorname{median}(\text{incumbent pay})} - 1
\]

Use only within a tightly controlled homogeneous cohort. It is simpler but less suitable as an enterprise headline because mix changes can distort the result.

### Difference in median compa-ratio

```text
Median new-hire compa-ratio minus median incumbent compa-ratio
```

Useful across currencies and pay scales when salary-range midpoints are reliable and consistently governed. It measures relative range position rather than direct internal pay premium.

### New-hire versus market premium

```text
New-hire pay divided by market reference minus one
```

This answers a different question. It must not be labelled as the internal new-hire premium.

## Claims matrix

| Claim ID | Claim | Source IDs | Confidence | Repository treatment |
|---|---|---|---|---|
| NHP-001 | New-hire pay rate compares new-hire salary with existing employees in the same role | `mercer-au-remuneration-trends-2026` | Established for Mercer's public concept | Publish with attribution |
| NHP-002 | Positive new-hire relativity means new hires are above current employees in the role | `mercer-au-remuneration-trends-2026` | Established for Mercer's public concept | Publish with attribution |
| NHP-003 | New-hire premiums can indicate compression | `mercer-transforming-merit-new-hire-premium`, `shrm-pay-compression-glossary` | Supported synthesis | Publish as diagnostic, not proof |
| NHP-004 | Employee-first matched calculation is the preferred enterprise method | Project analytical design | Project decision | Label clearly |
| NHP-005 | A specific 5% or 10% threshold is universally material | No sufficient source | Unresolved/rejected | Do not publish as universal standard |
| NHP-006 | Positive premium causes attrition | Sources in this trial are insufficient for causal claim | Unresolved | Do not claim |

## What the trial revealed about the standards

### Research standard

- A professional source may define a concept without providing enough detail for implementation.
- The repository must separate external concept, local formula, and organisation-specific policy.
- KPI research must capture cohort, timing, pay basis, aggregation, coverage, and interpretation limits.
- A useful diagnostic should not be promoted to a causal measure.

### Citation standard

- The external concept can be cited directly while the project formula is labelled separately.
- Source records need usage restrictions because public pages may sit beside licensed market data.
- A claim matrix makes rejected universal thresholds visible.

### Naming standard

- `new-hire-premium` is appropriate for the internal comparison measure.
- `new-hire-market-premium` must be a separate name.
- `new-hire-pay-rate` may be retained only when specifically referring to Mercer's named public concept.

## Acceptance result

**Trial result: PASS WITH DOMAIN DECISIONS REQUIRED**

The standards supported a clear separation between external concept, project formula, and future organisation-specific implementation. The candidate KPI is suitable for Phase 5 research but is not yet approved for agent use.

## Sources

[^mercer-au]: Mercer Australia, “Remuneration Trends & Insights,” March-quarter 2026 content as retrieved 2026-07-17, https://www.mercer.com/en-au/insights/total-rewards/compensation/remuneration-and-salary-trends/. Central source ID: `mercer-au-remuneration-trends-2026`.

[^shrm-compression]: SHRM, “HR Glossary — Pay Compression,” updated date not stated, retrieved 2026-07-17, https://www.shrm.org/mena/topics-tools/tools/hr-glossary. Central source ID: `shrm-pay-compression-glossary`.

[^mercer-merit]: Mercer, “Transforming merit — From flawed to fair,” updated date not stated, retrieved 2026-07-17, https://www.mercer.com/en-us/insights/total-rewards/transforming-merit-from-flawed-to-fair/. Central source ID: `mercer-transforming-merit-new-hire-premium`.
