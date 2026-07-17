---
artifact_id: STD-CORE-005
status: PLACEHOLDER
phase: 1
priority: high
depends_on:
  - artifact_id: ARCH-CORE-001
    path: ../architecture/agent-architecture.md
  - artifact_id: STD-CORE-001
    path: naming-standard.md
  - artifact_id: STD-CORE-002
    path: research-standard.md
  - artifact_id: STD-CORE-003
    path: citation-standard.md
  - artifact_id: EX-CORE-001
    path: ../../knowledge/research-register/trials/cursor-rules-and-skills-trial.md
  - artifact_id: EX-CORE-002
    path: ../../knowledge/research-register/trials/internal-source-of-truth-decision-trial.md
  - artifact_id: EX-FIXED-001
    path: ../../knowledge/research-register/trials/new-hire-premium-kpi-trial.md
  - artifact_id: EX-CONSULT-001
    path: ../../knowledge/research-register/trials/consulting-attribution-trial.md
  - artifact_id: EX-VIZ-001
    path: ../../knowledge/research-register/trials/graphical-perception-trial.md
blocks:
  - worked examples
  - benchmark scenarios
content_version: 0.1.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Example-authoring standard

## Document state

This is the first substantive draft. The lifecycle status remains `PLACEHOLDER` until representative executive, Business Partner, manager, interactive, static, and failure examples are authored and validated.

## Purpose

Define how examples, benchmark inputs, expected results, failure cases, and synthetic datasets demonstrate repository behaviour without creating hidden rules, exposing sensitive information, or pretending that one worked design is universally correct.

## Principles

1. Examples demonstrate; standards and schemas govern.
2. Inputs and expected behaviour remain separate.
3. Synthetic values are visibly fictional.
4. Every example declares audience, decision, domain, consumption mode, and workflow stage.
5. Acceptable alternatives are documented where design judgement permits them.
6. Critical failures are explicit.
7. Examples are reproducible without conversation history.
8. Examples reference authoritative knowledge and schemas rather than redefining them.
9. Failure and adversarial examples are as important as successful examples.
10. Public examples never contain real employee, company, client, or licensed market data.

## Example types

### Worked example

Demonstrates a method from input through output.

Use for:

- dashboard briefs;
- KPI definitions;
- page architectures;
- visual specifications;
- implementation handoffs;
- design reviews.

### Pattern example

Shows one bounded technique rather than a complete dashboard.

Examples:

- action title transformation;
- variance-table design;
- executive KPI hierarchy;
- distribution comparison;
- filter-context treatment.

### Benchmark scenario

Provides a controlled input used to test routing or output behaviour.

It must not reveal the expected answer inside the input.

### Expected result

Defines required behaviours, acceptable alternatives, and critical failures for a benchmark scenario.

### Negative example

Shows a plausible but incorrect output and explains why it fails.

### Adversarial example

Tests ambiguity, conflicting goals, incomplete data, unsupported causality, privacy risk, misleading aggregation, or prompt wording likely to trigger an incorrect route.

### Regression fixture

Preserves an input and expected behaviour after a defect is found and corrected.

### Migration example

Shows how an artifact or package moves between versions.

## File locations

### Worked examples

```text
examples/<audience-or-mode>/<descriptive-name>.md
```

### Benchmark scenarios

```text
evaluations/scenarios/<scenario-id>.md
```

### Expected results

```text
evaluations/expected-results/<scenario-id>.md
```

### Regression fixtures

```text
evaluations/regression/<defect-or-scenario-id>/
```

A scenario and expected result share a stable `scenario_id` in metadata.

## Required example metadata

```yaml
artifact_id:
status:
content_version:
example_type:
scenario_id:
title:
primary_audience:
secondary_audiences:
decision_mode:
decision:
actions_supported:
performance_reward_domains:
consumption_mode:
workflow_stage:
requested_output:
skills_demonstrated:
knowledge_dependencies:
schema_dependencies:
synthetic_data: true
jurisdiction:
assumptions:
limitations:
acceptable_alternatives:
critical_failures:
```

Fields may be omitted only when they do not apply and the schema permits omission.

## Worked-example structure

```markdown
# Example title

## Purpose

## Scenario

## Input

## Confirmed constraints

## Assumptions

## Method demonstrated

## Output

## Why this works

## Acceptable alternatives

## Failure modes

## Knowledge and schema references

## Validation
```

The output section contains the actual worked artifact or a direct link to it.

## Benchmark-scenario structure

A benchmark input contains only information a real user or project could provide.

```markdown
# Scenario title

## User request

## Available artifacts

## Known data

## Constraints

## Hidden evaluator notes
```

`Hidden evaluator notes` must live in the expected-result file, not the prompt supplied to the agent.

### Scenario metadata

```yaml
scenario_id:
benchmark_group:
primary_audience:
decision_mode:
performance_reward_domains:
consumption_mode:
workflow_stage:
difficulty:
risk_level:
expected_route_classes:
```

## Expected-result structure

```markdown
# Expected result

## Scenario reference

## Required routing

## Required discoveries or questions

## Required output behaviours

## Acceptable alternatives

## Prohibited behaviours

## Critical failures

## Scoring guidance

## Evidence and schema references
```

### Required versus preferred behaviour

Separate:

- **required** — omission makes the result materially untrustworthy;
- **preferred** — improves quality but is not mandatory;
- **acceptable alternative** — different approach that still supports the decision;
- **prohibited** — misleading, unsafe, or outside scope.

## Synthetic-data standard

### Required properties

Synthetic data must be:

- clearly labelled fictional;
- internally coherent enough to test the method;
- free of real employee names, identifiers, exact salaries, or organisational structures;
- free of copied licensed market values;
- intentionally varied enough to expose relevant edge cases;
- reproducible from a documented generation rule or static fixture.

### Naming

Use neutral fictional organisations and people only when names are necessary.

Preferred:

```text
Example Group
North Division
Employee A001
Role Family Alpha
```

Avoid realistic combinations that could be mistaken for actual employees or confidential business units.

### Numerical values

- State that values are illustrative.
- Avoid copying values from screenshots, internal dashboards, or licensed surveys.
- Use ranges and distributions that demonstrate the method without implying a market benchmark.
- Preserve mathematical consistency.
- Include edge cases deliberately where the example tests them.

### Dates

Use dates that are clearly part of the fictional scenario. Avoid accidentally presenting stale dates as current facts.

### Geography and jurisdiction

Use a fictional or declared general jurisdiction unless a real jurisdiction is essential to the scenario. Real legal or regulatory content requires current authoritative evidence.

## Privacy and redaction checklist

Before committing an example:

- [ ] all employee names and identifiers are synthetic;
- [ ] organisational names and codes are public or fictional;
- [ ] private URLs and tenant identifiers are removed;
- [ ] screenshots contain no confidential fields or metadata;
- [ ] salary and market values are synthetic;
- [ ] policy text is not copied from a confidential document;
- [ ] file properties and comments do not expose personal information;
- [ ] hidden rows, notes, or attachments have been reviewed;
- [ ] output is marked illustrative where needed;
- [ ] licences permit included assets and excerpts.

## Input and output separation

A benchmark input must not include:

- the expected route;
- the desired chart type unless explicitly requested by the user scenario;
- the hidden defect being tested;
- the evaluator's scoring language;
- the expected conclusion;
- the repository skill names unless the test concerns explicit invocation.

The expected result must not alter the input after the run merely to make the output appear correct.

## Assumptions

Every example distinguishes:

- user-supplied facts;
- repository-defined methods;
- fictional scenario facts;
- project assumptions;
- unresolved questions;
- evaluator-only expectations.

Do not conceal a necessary assumption inside the worked output.

## Acceptable alternatives

Dashboard and communication design often permit multiple valid solutions.

An expected result should describe the decision logic that must be preserved rather than requiring pixel-identical output.

Example:

```text
Required: show actual versus approved budget and the driver of variance.
Acceptable: bullet chart plus driver table, or variance KPI plus waterfall.
Not acceptable: a standalone spend total with no comparator.
```

Use exact output matching only for deterministic schemas, formulas, IDs, paths, or validation messages.

## Failure examples

A useful failure example contains:

- the incorrect output;
- why it appears plausible;
- the violated standard or knowledge authority;
- the decision risk created;
- the corrected treatment.

Failure categories include:

- wrong audience emphasis;
- no decision or action;
- misleading aggregation;
- unsupported causal claim;
- missing comparator;
- privacy or security exposure;
- inaccessible colour dependence;
- infeasible Power BI interaction;
- firm attribution without evidence;
- hidden policy assumption;
- routing to irrelevant skills;
- overloading the page with detail.

## Adversarial scenarios

Include scenarios where:

- the user requests a chart before defining the question;
- executive and specialist audiences conflict;
- a metric name hides an ambiguous formula;
- a small population creates privacy risk;
- a desired conclusion is not supported by the data;
- the requested visual is poorly suited to the analytical relationship;
- current product behaviour must be verified;
- organisation policy conflicts with general external guidance;
- the user asks for causal interpretation from observational data;
- a static export depends on hover or drill-through;
- the request includes employee detail outside the audience's authority.

The expected result should reward safe clarification or rejection where appropriate.

## Skill examples

A skill-local example may be compact and method-specific.

Use a repository-level example when:

- multiple skills are demonstrated;
- the example represents an end-to-end workflow;
- it is used in benchmark evaluation;
- it needs an immutable artifact ID;
- several audiences or contributors will use it.

Do not copy the same example into several skill folders.

## Example references

An example links to:

- the skill or skills demonstrated;
- authoritative knowledge;
- schemas and templates;
- source citations for external claims;
- scenario and expected result where applicable.

An example does not become a formal dependency of an upstream standard merely because it demonstrates that standard.

## Versioning

Increment `content_version` when:

- input facts change materially;
- expected behaviour changes;
- skill or schema versions require migration;
- critical failures or acceptable alternatives change;
- a regression fixture is corrected.

Changes that make a benchmark easier or harder must be recorded because they affect trend interpretation.

## Status lifecycle

### Placeholder

Location and scope exist; no usable example is present.

### Draft

Example is usable for controlled development but may depend on draft skills or schemas.

### In review

Input, expected result, synthetic-data safety, and dependencies have been checked.

### Approved

Example is suitable for release, documentation, or formal benchmark use.

### Superseded

Replacement is identified and historical benchmark results retain the version used.

## Example quality checks

Before review:

- audience and decision are explicit;
- scenario data is synthetic and coherent;
- requested output is clear;
- assumptions and limitations are visible;
- relevant skills and schemas are linked;
- expected results separate required and optional behaviour;
- critical failures are meaningful;
- acceptable alternatives prevent overfitting;
- no hidden answer leaks into the input;
- privacy and licence checks pass;
- the example can be reproduced in a fresh session.

## Canonical worked-example template

```markdown
---
artifact_id:
status: DRAFT
content_version: 0.1.0
example_type: worked-example
scenario_id:
primary_audience:
decision_mode:
performance_reward_domains: []
consumption_mode:
workflow_stage:
requested_output:
skills_demonstrated: []
knowledge_dependencies: []
schema_dependencies: []
synthetic_data: true
assumptions: []
limitations: []
---

# Title

## Purpose

## Scenario

## Input

## Confirmed constraints

## Assumptions

## Method demonstrated

## Output

## Why this works

## Acceptable alternatives

## Failure modes

## References

## Validation
```

## Canonical benchmark template

```markdown
---
artifact_id:
status: DRAFT
content_version: 0.1.0
example_type: benchmark-scenario
scenario_id:
benchmark_group:
primary_audience:
decision_mode:
performance_reward_domains: []
consumption_mode:
workflow_stage:
difficulty:
risk_level:
synthetic_data: true
---

# Scenario title

## User request

## Available artifacts

## Known data

## Constraints
```

The expected-result file contains the evaluation details.

## Required initial example set

Before this standard leaves `PLACEHOLDER`, create:

1. Executive fixed-reward static summary
2. Executive performance summary
3. Business Partner diagnostic dashboard
4. Manager action dashboard
5. Static executive Power BI export
6. KPI-definition example
7. Existing-dashboard critique
8. At least two adversarial scenarios
9. At least one privacy or security failure example
10. At least one routing false-positive regression

## Anti-patterns

- Using a real internal dashboard as a public example without full redaction and permission.
- Presenting illustrative values as facts.
- Encoding the expected answer in the user prompt.
- Requiring one exact design when alternatives are valid.
- Allowing examples to define new KPI formulas.
- Keeping only successful examples.
- Creating examples too perfect to reveal missing-information behaviour.
- Copying one example into several folders.
- Using an executive example as the default for every audience.
- Changing benchmark inputs without versioning the expected result.
- Scoring visual polish while ignoring decision usefulness or metric integrity.

## Validation requirements

Future example and evaluation validators should check:

- required metadata;
- scenario and expected-result pairing;
- synthetic-data declaration;
- artifact and skill references;
- schema references;
- duplicate scenario IDs;
- unsupported status values;
- hidden-answer leakage markers where detectable;
- missing critical-failure sections;
- invalid links;
- release-profile eligibility.

Human review remains required for realism, privacy, design alternatives, and scoring quality.

## Draft acceptance assessment

This draft defines:

- example types and locations;
- metadata and structures;
- synthetic-data and redaction rules;
- input/output separation;
- acceptable alternatives;
- negative and adversarial examples;
- version and status treatment;
- canonical templates;
- initial example set;
- validation requirements.

It must be reconciled with Phase 2 schemas, the evaluation standard, the final skill inventory, and the initial benchmark suite before status changes.
