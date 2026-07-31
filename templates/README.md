---
status: DRAFT
phase: 2
priority: critical
depends_on:
  - ../schemas/README.md
  - ../docs/standards/example-authoring-standard.md
blocks:
  - schema-backed skill outputs
  - worked examples
last_reviewed: 2026-07-17
---

# Output templates

## Purpose

Templates provide human-usable Markdown structures for the repository's schema-backed outputs.

A template:

- mirrors one schema;
- explains how to complete the fields;
- supports both Cursor generation and human review;
- does not redefine schema semantics;
- keeps unknown, unresolved, and not-applicable information visible;
- remains usable without conversation history.

## Current template set

| Template ID | File | Schema | Status |
|---|---|---|---|
| `TPL-CORE-001` | `research-record.md` | `research-record.schema.yaml` | Draft aligned |
| `TPL-AUD-001` | `audience-decision-profile.md` | `audience-decision-profile.schema.yaml` | Draft aligned |
| `TPL-PR-001` | `kpi-definition.md` | `kpi-definition.schema.yaml` | Draft aligned |
| `TPL-CORE-002` | `dashboard-brief.md` | `dashboard-brief.schema.yaml` | Draft aligned |
| `TPL-UX-001` | `page-specification.md` | `page-specification.schema.yaml` | Draft aligned |
| `TPL-VIZ-001` | `visual-specification.md` | `visual-specification.schema.yaml` | Draft aligned |
| `TPL-QA-001` | `design-review.md` | `design-review.schema.yaml` | Draft aligned |
| `TPL-PBI-001` | `implementation-handoff.md` | `implementation-handoff.schema.yaml` | Draft aligned |
| Pending | `wireframe-specification.md` | Derived from page and visual specifications | Placeholder |

## Template rules

1. The schema owns field names, allowed values, required status, and meaning.
2. The template may group fields into readable sections.
3. Completion guidance is concise and does not embed full domain knowledge.
4. Tables are used where structured comparison improves completion and review.
5. Empty required fields are not silently omitted.
6. `Unknown`, `not applicable`, and `unresolved` are distinguished.
7. A template must not include real employee or confidential example data.
8. A template version changes when its schema mapping or instructions change materially.
9. Skills reference the template and schema they produce.
10. Examples use copied instances, not modified competing versions of templates.

## Unknown and unresolved values

Use:

```text
UNKNOWN — fact should be available but has not been obtained
UNRESOLVED — a decision or ambiguity remains open
NOT APPLICABLE — the field does not apply to the scenario
NOT YET REVIEWED — a required check has not been performed
```

Do not leave a material field blank when its state matters to downstream work.

## Mapping requirements

Every required schema field must appear in the corresponding template either:

- as a labelled field;
- as a table column;
- as a clearly named section;
- or through a documented repeated structure.

Optional fields may be omitted from the visible template only when the template explains how to add them and omission does not create ambiguity.

## Derived wireframe template

`wireframe-specification.md` is initially a derived presentation aid.

It should combine:

- page metadata and role;
- canvas and grid;
- layout zones;
- visual IDs and titles;
- interaction markers;
- reading order;
- annotations and implementation notes.

It does not need a separate schema unless practical use reveals fields that cannot be represented cleanly through page and visual specifications.

## Validation roadmap

Current validation confirms the eight schemas are structurally valid.

Next validation should check:

- every template declares an existing schema;
- template schema version matches;
- required schema fields have a template mapping;
- duplicate template IDs do not exist;
- template links resolve;
- placeholders cannot be selected as completed outputs.

Judgement-based review remains necessary for usability and ambiguity.

## Development testing

For each template:

1. create a minimal valid fixture;
2. create a realistic completed synthetic example;
3. use it through the intended skill workflow;
4. validate the resulting structured record against the schema;
5. identify fields that are redundant, missing, or difficult to interpret;
6. version schema and template changes together.

## Anti-patterns

- Adding a field only to a Markdown template.
- Copying domain definitions into every template.
- Treating optional as permission to hide material uncertainty.
- Creating audience-specific copies of the same output contract.
- Using one long free-form section instead of structured fields.
- Changing a template without checking schema compatibility.
- Requiring pixel-identical or prose-identical output.
- Embedding organisation-specific policy in the public template.

## Immediate next work

Complete the wireframe aid, add template validation, create valid fixtures, and use the audience, KPI, dashboard brief, page, and visual templates in the first synthetic vertical-slice example.
