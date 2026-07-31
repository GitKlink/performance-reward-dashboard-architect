---
template_id: TPL-PR-001
status: DRAFT
content_version: 0.1.0
schema: ../schemas/kpi-definition.schema.yaml
schema_version: 0.1.0
last_reviewed: 2026-07-17
---

# KPI definition: <name>

## Identity and decision use

| Field | Value |
|---|---|
| KPI ID | `KPI-<DOMAIN>-<NNN>` |
| Status | `DRAFT` |
| Short name | |
| Performance & Reward domain | |
| Measure role | `outcome` / `driver` / `leading-signal` / `activity` / `control` / `context` / `diagnostic` |
| Time orientation | |
| Business question | |
| Decisions supported | |
| Audiences | |

## Definition

<Define exactly what the measure represents.>

### Conceptual source

| Field | Value |
|---|---|
| Source IDs | |
| Repository-defined | `true` / `false` |
| Organisation policy required | `true` / `false` |

## Formula

```text
<Expression>
```

| Component | Definition | Unit |
|---|---|---|
| Numerator | | |
| Denominator | | |
| | | |

### Calculation treatment

| Field | Value |
|---|---|
| Null and zero treatment | |
| Sign convention | |
| Rounding | |
| Example calculation | |

## Grain and population

| Field | Value |
|---|---|
| Calculation grain | |
| Reporting grain | |
| Entity key | |
| Duplicate treatment | |
| Eligibility date | |
| Cohort logic | |
| Survivorship-bias control | |
| Coverage denominator | |

### Included population

- 

### Excluded population

- 

## Time logic

| Field | Value |
|---|---|
| Effective date | |
| Reporting period | |
| Lookback or window | |
| Snapshot or event rule | |
| Comparison alignment | |
| Late-arriving data | |

## Aggregation

| Field | Value |
|---|---|
| Method | |
| Roll-up rule | |
| Weighting | |
| Non-additive dimensions | |
| Small-group treatment | |
| Custom method | |

## Unit, currency, and FTE basis

| Field | Value |
|---|---|
| Unit | |
| Currency | |
| FX date or method | |
| Annualised | `true` / `false` |
| FTE adjusted | `true` / `false` |
| Pay basis | |

## Direction and materiality

| Field | Value |
|---|---|
| Direction | `higher-is-better` / `lower-is-better` / `target-range` / `context-dependent` / `neutral` |
| Rationale | |
| Materiality rule | |

## Comparators

| Comparator type | Definition | Source | Tolerance | Priority |
|---|---|---|---|---|
| | | | | `primary` / `secondary` / `diagnostic` |

## Segmentation

| Dimension | Purpose | Privacy risk |
|---|---|---|
| | | |

## Interpretation

### What it may indicate

- 

### What it does not prove

- 

### Diagnostic follow-ups

- 

| Field | Value |
|---|---|
| Causal-language status | `descriptive` / `association-only` / `diagnostic-signal` / `causal-supported` / `not-applicable` |

## Data requirements

### Required fields

- 

### Source systems

- 

| Field | Value |
|---|---|
| Historical depth | |
| Effective dating required | `true` / `false` |
| Joins and keys | |

## Data quality

| Field | Value |
|---|---|
| Coverage measure | |
| Minimum coverage | |
| Reconciliation | |

### Known risks

- 

### Validation rules

- 

## Privacy

| Field | Value |
|---|---|
| Sensitivity | |
| Minimum-group rule | |
| Employee-level access | |
| Suppression or rounding | |
| Export restrictions | |

## Display guidance

| Field | Value |
|---|---|
| Default format | |
| Preferred comparison | |
| Recommended visual relationship | |
| Suitable as headline KPI | `true` / `false` |
| Tooltip or definition text | |

## Power BI implementation notes

| Field | Value |
|---|---|
| Semantic-model requirements | |
| DAX or calculation notes | |
| Performance risks | |

### Test cases

| Case | Expected result | Tolerance |
|---|---|---|
| | | |

## Limitations

- 

## Ownership and review

| Field | Value |
|---|---|
| Business owner | |
| Definition owner | |
| Data owner | |
| Review cadence | |
| Last reviewed | |
| Next review trigger | |
| Superseded by | |
