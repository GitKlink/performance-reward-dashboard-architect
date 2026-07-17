---
artifact_id: STD-CORE-006
status: PLACEHOLDER
phase: 1
priority: critical
depends_on:
  - artifact_id: ARCH-CORE-001
    path: ../architecture/agent-architecture.md
  - artifact_id: ARCH-CORE-003
    path: ../architecture/skill-routing-model.md
  - artifact_id: STD-CORE-005
    path: example-authoring-standard.md
blocks:
  - evaluation rubric
  - release quality gates
content_version: 0.1.0
last_reviewed: 2026-07-17
next_review: 2026-08-17
---

# Evaluation standard

## Document state

This is the first substantive draft. The lifecycle status remains `PLACEHOLDER` until the benchmark suite, expected-result files, scoring calibration, and integrated Phase 12 review process are implemented.

## Purpose

Define how architecture, knowledge, routing, skills, outputs, subagents, Power BI guidance, and release packages are tested consistently.

## Evaluation principles

1. Decision usefulness is the primary outcome.
2. Critical failures cannot be averaged away by visual quality.
3. Required behaviour is separated from acceptable alternatives.
4. Deterministic checks and judgement-based review use different methods.
5. Static, interactive, hybrid, and operational products are interpreted differently where appropriate.
6. Results are traceable to exact artifact versions and source commits.
7. Evaluations include positive, negative, ambiguous, adversarial, and regression cases.
8. Reviewers record findings before correction begins.
9. Integrated independent review is concentrated in Phase 12.
10. Passing CI does not prove P&R, analytical, audience, or design quality.

## Objects evaluated

### Repository architecture

- component boundaries;
- context strategy;
- routing model;
- source-of-truth ownership;
- information architecture;
- release architecture.

### Knowledge

- definitions;
- evidence quality;
- domain boundaries;
- KPI catalogues;
- selection rules;
- freshness and limitations.

### Skills

- metadata and discovery;
- invocation and non-invocation;
- method completeness;
- knowledge and schema dependencies;
- output quality;
- context load;
- interaction with adjacent skills.

### Subagents

- trigger appropriateness;
- task isolation;
- handoff completeness;
- evidence and finding quality;
- tool and permission boundaries;
- avoidance of authority duplication.

### Dashboard outputs

- briefs;
- KPI definitions;
- analytical plans;
- page architectures;
- static pages;
- interactive experiences;
- visual specifications;
- implementation handoffs;
- critiques.

### Release package

- dependency closure;
- current Cursor compatibility;
- package integrity;
- documentation and migration;
- privacy, security, and licensing;
- benchmark and regression results.

## Evaluation layers

### Layer 1 — Deterministic validation

Performed by scripts and CI.

Examples:

- valid metadata;
- unique IDs;
- existing paths;
- dependency closure;
- schema validation;
- source references;
- internal links;
- required sections;
- package manifest and file hashes;
- placeholder exclusion.

### Layer 2 — Routing evaluation

Tests whether the correct skills and subagents are selected, sequenced, and pruned.

### Layer 3 — Artifact-quality evaluation

Tests one output against its schema and quality criteria.

### Layer 4 — End-to-end scenario evaluation

Tests the full route from request through output and handoff.

### Layer 5 — Integrated independent review

A fresh reviewer or review team assesses the complete architecture and release candidate in Phase 12.

## Severity model

| Severity | Definition | Development response | Release effect |
|---|---|---|---|
| `critical` | Unsafe, materially misleading, circular, unusable, privacy-breaching, or fundamentally untrustworthy | stop relevant work and correct owning artifact | blocks release |
| `major` | Materially weakens correctness, decision usefulness, traceability, accessibility, security, or maintainability | correct before formal approval | blocks approval and release |
| `minor` | Localised weakness with limited decision risk | schedule correction | may release only with explicit acceptance where appropriate |
| `editorial` | Wording, formatting, or presentation issue without behavioural impact | correct when practical | does not block |

## Critical failure categories

A result fails regardless of score when it:

- supports the wrong decision or audience;
- uses a materially incorrect KPI formula, population, time basis, or aggregation;
- presents an unsupported causal conclusion as fact;
- exposes unauthorised employee-level or confidential information;
- relies on fabricated, irrelevant, or misrepresented evidence;
- makes a high-stakes policy or legal decision without appropriate authority;
- activates a placeholder as a runtime capability;
- omits a mandatory release dependency;
- creates a known security or row-level access failure;
- gives a Power BI implementation that cannot produce the claimed result and does not disclose the limitation;
- makes a static export depend on hidden interaction for its core message;
- cannot be reconstructed from repository artifacts and tested source state;
- contains unlicensed proprietary material in the public package.

## Major failure categories

Examples:

- missing material comparator or target;
- incomplete audience or decision framing;
- significant domain overlap or contradiction;
- misleading visual encoding without reaching critical severity;
- inaccessible interaction or colour treatment;
- missing metric limitations or data-quality caveat;
- unnecessary context loading that causes routing failures;
- incorrect skill invocation with material output impact;
- incomplete implementation handoff;
- unreconciled static and interactive page roles;
- missing migration guidance for a breaking change;
- release compatibility not verified.

## Weighted quality rubric

Score each dimension from `0` to `4`.

| Dimension | Weight | Core question |
|---|---:|---|
| Decision usefulness | 15 | Does the output help the intended owner make or execute the required decision? |
| Audience fit | 10 | Is detail, language, navigation, and emphasis appropriate to the audience? |
| Analytical and KPI integrity | 15 | Are grain, population, formula, time logic, comparator, and interpretation sound? |
| Performance & Reward accuracy | 15 | Are domain concepts, value drivers, boundaries, and governance correct? |
| Story and communication | 10 | Is the governing message and logical sequence clear? |
| Visual hierarchy and design | 10 | Does the visual structure direct attention and encode information appropriately? |
| Experience and consumption mode | 10 | Does interaction, navigation, reading order, or export behaviour fit the product mode? |
| Power BI feasibility and performance | 5 | Can the design be implemented and maintained as claimed? |
| Accessibility | 5 | Can users perceive and operate the product without avoidable barriers? |
| Governance and maintainability | 5 | Are evidence, privacy, ownership, definitions, and future maintenance adequate? |
| **Total** | **100** | |

## Score definitions

| Score | Meaning |
|---:|---|
| `4` | Strong, complete, and decision-ready; no material correction required |
| `3` | Sound with limited non-material improvements |
| `2` | Partially sound; one or more material weaknesses require correction |
| `1` | Fundamentally weak or incomplete |
| `0` | Missing, incorrect, unsafe, or inapplicable |

A high weighted score does not override critical or major findings.

## Provisional thresholds

Thresholds are project decisions and must be calibrated against benchmark results before release.

### Development smoke pass

- no critical failure;
- required schema fields present;
- route broadly correct;
- weighted score at least `60`.

Used only to continue draft development.

### Formal review candidate

- no critical failure;
- no more than two unresolved major findings;
- weighted score at least `75`;
- decision usefulness, analytical integrity, and P&R accuracy each score at least `3`.

### Release approval candidate

- no unresolved critical or major finding;
- weighted score at least `85`;
- no dimension below `3`;
- decision usefulness, analytical integrity, P&R accuracy, and audience fit each score at least `3.5` on the agreed scoring scale;
- all deterministic release checks pass;
- required independent review completed.

Phase 12 must calibrate whether these thresholds distinguish acceptable and unacceptable outputs reliably. Changes require a documented evaluation-standard update.

## Product-mode interpretation

### Static

The experience dimension evaluates:

- fixed reading order;
- visible filter and scope context;
- direct labels;
- self-contained message;
- print and export behaviour;
- page sequence;
- no dependence on hover or drill-through.

### Interactive

The experience dimension evaluates:

- navigation;
- filter persistence;
- drill-down and drill-through;
- tooltips and detail on demand;
- reset and recovery;
- performance;
- security;
- interaction discoverability.

### Hybrid

Evaluate summary, diagnostic, and action pages according to their declared role. Penalise pages that attempt to be simultaneously presentation-led and unrestrictedly exploratory without a coherent hierarchy.

### Operational or manager action

Emphasise:

- accountable population;
- exception prioritisation;
- deadlines and completion state;
- employee-level security;
- clarity of next action;
- audit and handoff.

## Audience-specific interpretation

### Executive

Critical questions:

- Is the decision explicit?
- Are material variances, drivers, risks, and implications visible?
- Is the summary defensible without hidden detail?
- Can it be understood within the expected reading time?

### Business Partner

Critical questions:

- Can the user move from overview to diagnosis?
- Are distributions, segments, peers, and context available?
- Can findings support stakeholder discussion without overclaiming?

### People manager

Critical questions:

- Is the accountable population correct?
- Are actions and exceptions prioritised?
- Is employee detail authorised and understandable?
- Can the manager complete the workflow safely?

### Reward Partner or specialist

Critical questions:

- Are definitions, calculations, controls, and reconciliation visible?
- Can the user inspect edge cases and export required detail?
- Does the product preserve methodological precision?

## Routing evaluation

For each scenario record:

```yaml
scenario_id:
resolved_dimensions:
required_skills:
optional_skills:
excluded_skills:
expected_subagents:
expected_sequence:
actual_route:
false_positives:
false_negatives:
sequence_violations:
context_load_notes:
critical_routing_failures:
```

### Routing critical failures

- omission of security for unauthorised employee detail;
- omission of metric design where the formula is ambiguous;
- omission of current research for unstable high-stakes facts;
- wrong primary P&R domain leading to materially incorrect guidance;
- static output routed without export-safe treatment;
- release workflow routed without comprehensive assurance.

### Routing quality measures

- required-skill recall;
- unnecessary-skill rate;
- primary-domain accuracy;
- audience and decision accuracy;
- consumption-mode accuracy;
- subagent overuse and underuse;
- route-order compliance;
- context loaded per route;
- output quality after routing.

## Skill evaluation

Each active skill is tested for:

- metadata and discovery;
- explicit invocation;
- automatic invocation where enabled;
- positive trigger cases;
- non-trigger cases;
- ambiguous cases;
- missing-information behaviour;
- output schema compliance;
- interaction with adjacent skills;
- context load;
- privacy and evidence boundaries;
- downstream handoff.

A skill cannot be approved because its `SKILL.md` reads well. It must perform correctly in scenarios.

## Subagent evaluation

Test:

- whether delegation was warranted;
- whether the brief was bounded;
- whether relevant context was provided without full transcript dumping;
- whether the return followed its contract;
- whether evidence and uncertainty were visible;
- whether the parent integrated findings correctly;
- whether the subagent duplicated or overrode authority;
- whether permissions and tool access were appropriate;
- whether parallel work caused conflicting edits.

## Knowledge evaluation

Review:

- source authority and diversity;
- freshness;
- claim-to-source traceability;
- domain definitions and boundaries;
- separation of external evidence and project synthesis;
- KPI population, grain, and aggregation;
- causal language;
- audience applicability;
- duplication;
- update triggers.

## KPI evaluation checklist

- [ ] business question and decision stated;
- [ ] conceptual definition clear;
- [ ] numerator and denominator defined;
- [ ] unit and grain defined;
- [ ] population and exclusions defined;
- [ ] effective-date and time logic defined;
- [ ] aggregation and weighting defined;
- [ ] comparator, target, or tolerance defined where needed;
- [ ] direction and materiality explained;
- [ ] segmentation and coverage defined;
- [ ] sample-size and confidentiality rules identified;
- [ ] limitations and misuse conditions stated;
- [ ] no survivorship or selection bias introduced silently;
- [ ] formula is implementable from available data or the gap is explicit.

## Visual and page evaluation

Review:

- analytical relationship;
- encoding and comparison precision;
- visual hierarchy;
- action title or page question;
- data density and data-ink balance;
- direct labelling;
- consistency of scales and notation;
- colour semantics;
- typography and layout;
- accessibility;
- Power BI feasibility;
- export and mobile behaviour where required.

Do not score visual polish highly when the underlying question or metric is wrong.

## Evidence evaluation

A factual claim passes when:

- the source supports the wording;
- authority is appropriate to the claim;
- current facts are fresh enough;
- firm attribution is bounded;
- inference and project decisions are labelled;
- contradictory evidence is represented where material;
- copyright and licence limits are respected.

## Deterministic versus judgement review

### Deterministic

Use scripts for:

- syntax and schema;
- IDs, paths, and dependencies;
- required fields and sections;
- source references;
- duplicate names;
- package contents and hashes;
- status restrictions;
- deterministic calculations with known fixtures.

### Judgement-based

Use benchmark and human review for:

- decision usefulness;
- audience fit;
- domain reasoning;
- story quality;
- visual selection;
- acceptable alternatives;
- context sufficiency;
- severity and risk.

Do not encode a subjective design preference as a deterministic failure without an approved rule.

## Reviewer requirements

### Development reviewer

May be the author or collaborating agent. Used for rapid local checks.

### Independent reviewer

Required for Phase 12 integrated review and final critical or major finding closure.

Must:

- begin from repository artifacts rather than the authoring conversation;
- record findings before correction;
- identify reviewed commit and versions;
- declare material sources independently rechecked;
- avoid approving corrections not revalidated;
- distinguish preference from standard violation.

### Subject-matter reviewer

Required where specialised P&R, legal, regulatory, accessibility, security, or Power BI expertise is needed.

One person or agent may fulfil several roles only when independence and competence remain credible.

## Review disagreement

When reviewers disagree:

1. confirm they are applying the same audience, decision, definitions, and scenario;
2. identify whether disagreement concerns fact, interpretation, risk tolerance, or preference;
3. consult the owning standard or knowledge artifact;
4. collect additional evidence where needed;
5. document accepted alternatives where both are valid;
6. escalate unresolved material risk to the accountable release authority;
7. record the final decision and rationale.

Do not average incompatible judgements into an artificial consensus.

## Benchmark groups

The initial suite includes:

- executive fixed-reward summary;
- executive performance summary;
- Business Partner diagnostic dashboard;
- manager action dashboard;
- static executive Power BI export;
- KPI-definition review;
- dashboard critique;
- Power BI implementation handoff;
- ambiguous discovery request;
- privacy and security adversarial case;
- unsupported-causality case;
- routing false-positive and false-negative cases.

## Regression process

When a defect is found:

1. assign a finding or defect ID;
2. save the smallest representative input;
3. record the incorrect behaviour;
4. define corrected expected behaviour;
5. correct the owning artifact or implementation;
6. add a regression fixture;
7. run the relevant local and integrated suites;
8. record the first fixed version;
9. retain the fixture unless it becomes invalid through a documented architecture change.

A correction without a regression case is incomplete when the defect is reproducible.

## Evaluation result record

```yaml
evaluation_id:
evaluation_type:
scenario_id:
tested_repository_commit:
tested_release_version:
tested_artifacts:
tested_cursor_version:
reviewers:
run_date:
deterministic_results:
routing_results:
weighted_scores:
findings:
critical_failures:
major_failures:
accepted_alternatives:
residual_risks:
gate_decision:
```

## Gate decisions

Allowed decisions:

```text
FAIL — CRITICAL
FAIL — MAJOR
DEVELOPMENT PASS
READY FOR FORMAL REVIEW
READY FOR APPROVAL
APPROVED FOR RELEASE
```

Only the release authority may record `APPROVED FOR RELEASE`, based on complete Phase 12 evidence and Phase 13 checks.

## Phase 12 integrated process

1. Freeze a release-candidate source commit.
2. Build package profiles.
3. Run all deterministic validators.
4. Run routing and skill benchmarks.
5. Run end-to-end audience scenarios.
6. Run Power BI, accessibility, privacy, security, evidence, and licensing reviews.
7. Conduct independent architecture and product review.
8. Record findings and weighted results.
9. Correct critical and major findings.
10. Add regressions.
11. Rerun the complete affected suite.
12. Produce approval recommendation for Phase 13.

## Phase 13 release decision

Release requires:

- no unresolved critical or major finding;
- release threshold met;
- runtime components and mandatory dependencies approved;
- package manifest valid;
- current product compatibility verified;
- privacy, security, and licence checks passed;
- rollback and migration instructions complete;
- final accountable approval recorded.

## Anti-patterns

- Using one weighted score as the only release criterion.
- Averaging away a critical metric or privacy failure.
- Requiring pixel-identical designs.
- Evaluating only successful prompts.
- Testing skill invocation without testing output quality.
- Testing outputs without the actual packaged agent.
- Letting the author silently approve their own major corrections.
- Treating subjective preference as deterministic policy.
- Changing a benchmark after seeing the output without versioning it.
- Running comprehensive assurance during every early draft.
- Waiting until release to add any automated validation.
- Measuring only visual quality.

## Draft acceptance assessment

This draft defines:

- evaluation objects and layers;
- severity and critical failure categories;
- weighted rubric and provisional thresholds;
- product and audience interpretation;
- routing, skill, subagent, knowledge, KPI, visual, and evidence evaluation;
- deterministic and judgement boundaries;
- reviewer requirements and disagreement handling;
- benchmark groups and regression process;
- result records and gate decisions;
- Phase 12 and Phase 13 procedures.

Before the artifact leaves `PLACEHOLDER`, it must be calibrated against the initial benchmark suite, reviewed for scoring consistency, and implemented in evaluation schemas and templates.
