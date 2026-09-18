---
template_id: TPL-UX-001
status: DRAFT
content_version: 0.1.0
schema: ../schemas/page-specification.schema.yaml
schema_version: 0.1.0
last_reviewed: 2026-07-17
---

# Page specification: <title>

## Page metadata

| Field | Value |
|---|---|
| Page ID | `PAGE-<PROJECT>-<NNN>` |
| Dashboard brief ID | |
| Status | `DRAFT` |
| Display order | |
| Page role | `summary` / `driver` / `diagnostic` / `detail` / `action` / `methodology` / `appendix` |
| Consumption mode | `interactive` / `static` / `hybrid` |
| Expected reading time | |

## Audience, decision, and action

| Field | Value |
|---|---|
| Audience | |
| Decision supported | |
| Actions supported | |

## Governing message or question

<Action-led conclusion or the primary page question.>

### Action title

<Use only where the evidence supports a conclusion-led title.>

### Subtitle or scope line

<Population, period, geography, currency, or other material scope.>

## Scope context

| Field | Value |
|---|---|
| Population | |
| Time period | |
| Organisational scope | |
| Currency or unit | |
| Visible filter context | `true` / `false` |
| Comparison context | |

## Content hierarchy

| Level | Purpose | Content | Dominant | Reading order |
|---:|---|---|---|---:|
| 1 | `orientation` / `conclusion` / `evidence` / `driver` / `context` / `action` / `definition` / `source` | | | |

## Measures

| KPI ID | Role | Priority | Comparator | Target or tolerance | Format | Commentary required |
|---|---|---|---|---|---|---|
| | | | | | | |

## Visuals

- `VISUAL-<PROJECT>-<NNN>`

## Commentary

| Field | Value |
|---|---|
| Required | `true` / `false` |
| Purpose | `conclusion` / `explanation` / `implication` / `recommendation` / `action` / `methodology` |
| Source | `authored` / `rules-based` / `model-assisted` / `not-applicable` |
| Maximum length | |

## Interactions

### Filters

| Filter | Scope | Persistence | Default |
|---|---|---|---|
| | `page` / `section` / `report` | | |

### Navigation

| Destination | Trigger | Context preserved |
|---|---|---|
| | | |

| Field | Value |
|---|---|
| Cross-filtering | `true` / `false` |
| Detail access | |
| Reset behaviour | |
| Scenario or input controls | |
| Static fallback | |

## Layout

### Canvas

| Width | Height | Unit | Aspect ratio |
|---:|---:|---|---|
| | | `pixels` / `points` / `inches` / `millimetres` | |

### Grid

| Columns | Rows | Outer margin | Gutter | Baseline |
|---:|---:|---:|---:|---:|
| | | | | |

### Zones

| Zone ID | Purpose | X | Y | Width | Height | Visual IDs |
|---|---|---:|---:|---:|---:|---|
| | | | | | | |

### Whitespace strategy

<Explain spacing and grouping decisions.>

### Responsive or mobile notes

<Complete only where required.>

## Accessibility

| Field | Value |
|---|---|
| Reading order | |
| Colour independence | |
| Keyboard and focus | |
| Alternative text | |
| Contrast | |
| Text size | |
| Cognitive-load notes | |

## Power BI implementation

| Field | Value |
|---|---|
| Feasibility status | `not-reviewed` / `feasible` / `feasible-with-constraints` / `not-feasible` / `requires-prototype` |
| Required features | |
| Model dependencies | |
| Measure dependencies | |
| Performance risks | |
| Security requirements | |
| Export behaviour | |
| Implementation notes | |

## Sources and definitions

| Field | Value |
|---|---|
| Visible source note | |
| Definition access | `direct-label` / `footnote` / `tooltip` / `methodology-page` / `linked-document` |
| Data-as-of label | |

## Quality checks

| Check | Status | Finding |
|---|---|---|
| Audience and decision fit | `not-run` / `pass` / `fail` / `not-applicable` | |
| Metric integrity | | |
| Story and hierarchy | | |
| Accessibility | | |
| Power BI feasibility | | |
| Static export or interaction behaviour | | |

## Assumptions

- 

## Open questions

- 

## Superseded by

<Leave blank unless superseded.>
