---
status: DRAFT
phase: 2
priority: critical
depends_on:
  - docs/architecture/agent-architecture.md
  - docs/standards/skill-authoring-standard.md
  - docs/standards/example-authoring-standard.md
  - docs/standards/evaluation-standard.md
blocks:
  - schema-backed templates
  - foundational skill activation
last_reviewed: 2026-07-17
---

# Output schemas

## Purpose

This directory contains the machine-readable contracts used by skills, templates, examples, evaluations, and implementation handoffs.

Schemas own field meaning and validation. Templates present those fields for human use but do not redefine them.

## Schema dialect

All active schemas use JSON Schema Draft 2020-12 expressed in YAML.

Each schema contains:

- `$schema` and stable `$id`;
- title and purpose;
- top-level object type;
- `additionalProperties: false`;
- repository metadata under `x-repository`;
- required and optional fields;
- enums, patterns, formats, and nested definitions;
- schema and content versions.

## Current schema set

| Artifact ID | File | Purpose |
|---|---|---|
| `SCHEMA-CORE-001` | `research-record.schema.yaml` | research question, sources, claims, findings, limitations, and review |
| `SCHEMA-AUD-001` | `audience-decision-profile.schema.yaml` | audience, decision, action, consumption, detail, privacy, and assumptions |
| `SCHEMA-PR-001` | `kpi-definition.schema.yaml` | complete metric definition and implementation requirements |
| `SCHEMA-CORE-002` | `dashboard-brief.schema.yaml` | agreed dashboard business, analytical, data, experience, and governance scope |
| `SCHEMA-UX-001` | `page-specification.schema.yaml` | one page's role, hierarchy, measures, layout, interactions, and feasibility |
| `SCHEMA-VIZ-001` | `visual-specification.schema.yaml` | one exhibit's analytical relationship, encoding, interaction, and implementation |
| `SCHEMA-QA-001` | `design-review.schema.yaml` | severity-ranked findings, rubric, corrections, and gate decision |
| `SCHEMA-PBI-001` | `implementation-handoff.schema.yaml` | semantic model, measures, pages, security, tests, deployment, and acceptance |

All eight are development drafts. They are validated structurally but have not yet been calibrated through complete example and skill workflows.

## Ownership rules

- A schema owns field definitions and constraints.
- A template maps one-to-one to its schema.
- A skill references the schema it produces or validates.
- An example identifies the schema version it demonstrates.
- An evaluation validates output against the applicable schema before judgement-based scoring.
- A downstream artifact must not introduce undeclared fields silently.

## Versioning

Schema version follows Semantic Versioning:

- major: incompatible field removal, rename, type change, or semantic change;
- minor: backward-compatible optional fields or allowed values;
- patch: clarification or constraint correction that preserves valid existing records.

Before `1.0.0`, breaking changes may occur in minor versions, but migration impact must still be documented.

Every record should identify the schema version used where compatibility matters.

## Validation

Run:

```bash
python3 scripts/validate-schemas.py --warnings-as-errors
```

The validator checks:

- YAML parsing;
- Draft 2020-12 schema validity;
- stable schema and artifact IDs;
- filename and `$id` agreement;
- required repository metadata;
- required fields declared in `properties`;
- duplicate schema IDs and artifact IDs;
- optional valid and invalid example fixtures.

Schema validation runs in GitHub Actions.

## Example fixtures

Fixtures may be added under:

```text
schemas/examples/
```

Naming:

```text
<schema-subject>.valid.yaml
<schema-subject>.invalid.yaml
```

A valid fixture must pass. An invalid fixture must fail for the intended reason.

One file per subject is sufficient initially. More cases may use a suffix after the subject when the validator is extended to support named cases.

## Template mapping

Expected template pairs:

```text
research-record.schema.yaml          → templates/research-record.md
audience-decision-profile.schema.yaml → templates/audience-decision-profile.md
kpi-definition.schema.yaml           → templates/kpi-definition.md
dashboard-brief.schema.yaml          → templates/dashboard-brief.md
page-specification.schema.yaml       → templates/page-specification.md
visual-specification.schema.yaml     → templates/visual-specification.md
design-review.schema.yaml            → templates/design-review.md
implementation-handoff.schema.yaml   → templates/implementation-handoff.md
```

`templates/wireframe-specification.md` is a presentation aid derived from page and visual specifications rather than a separate authoritative schema unless implementation proves that it needs a distinct contract.

## Development sequence

1. Validate schema structure.
2. Align the corresponding template.
3. Create one valid and one invalid fixture.
4. Use the schema in a synthetic end-to-end workflow.
5. Correct field gaps and version changes.
6. Add skill output-contract references.
7. Run integrated Phase 12 evaluation before approval.

## Current limitations

- No template-to-schema validator exists yet.
- No complete valid and invalid fixture set exists yet.
- Artifact-register entries for the eight schemas still need to be added.
- Cross-schema references are intentionally lightweight in `0.1.0` to reduce coupling during development.
- Organisation-specific fields and policy thresholds are not embedded in public schemas.
- Schema compatibility has not yet been tested against active skills.

## Anti-patterns

- Adding fields only to a template.
- Creating one schema per audience for the same artifact type.
- Embedding organisation policy as a universal enum.
- Using free-form text where a stable controlled value is required.
- Overconstraining early drafts before realistic examples exist.
- Allowing `additionalProperties` to hide undeclared fields.
- Changing field semantics without a version change.
- Treating structural schema validity as proof of business correctness.

## Immediate next work

Align all eight templates, add representative fixtures, register the schemas, and extend validation to check template headings against required schema fields.
