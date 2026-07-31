---
status: DRAFT
phase: 2
priority: CRITICAL
depends_on:
  - knowledge/performance-reward/holistic-value-driver-tree.md
  - knowledge/performance-reward/fixed-reward.md
  - docs/standards/skill-authoring-standard.md
blocks:
  - fixed reward workflow evaluations
last_reviewed: 2026-07-31
activation: DISABLED
---

# Fixed Reward Analysis Skill — Implementation Draft

> This skill remains intentionally non-invokable. Do not add active Cursor `name` and `description` frontmatter until the knowledge dependencies, output contracts, and benchmark tests have passed review.

## Purpose

Provide a repeatable method for analysing fixed-reward questions and translating them into a decision-ready diagnostic, dashboard brief, KPI specification, semantic-model requirement, or implementation handoff.

The skill must load the fixed-reward knowledge pack rather than reproducing its definitions.

## Invoke when

The request concerns one or more of the following:

- salary or fixed-pay positioning;
- salary-review planning or outcomes;
- salary budgets, allocation, redistribution, or utilisation;
- compa-ratio, range penetration, range compliance, compression, or inversion;
- hiring, promotion, retention, market, or equity adjustments that change recurring pay;
- fixed-reward recommendations, approvals, processing, or payment reconciliation;
- executive, HRBP, Reward Partner, manager, payroll, finance, or governance reporting for fixed reward.

## Do not invoke when

- the request is solely about variable incentive design or outcomes;
- the request is solely about performance ratings without a fixed-pay decision;
- the user only needs generic Power BI implementation help with no fixed-reward logic;
- the required population, date, pay definition, or decision state cannot be determined and proceeding would materially misstate the result;
- the request would expose unauthorised identifiable remuneration data.

## Required inputs

At minimum, resolve or explicitly record:

- audience and decision owner;
- decision or question to be supported;
- population and exclusions;
- effective or observation date;
- fixed-pay definition;
- local and reporting currency requirements;
- lifecycle state: opening, recommendation, approved, processed, or paid;
- relevant job, range, organisation, location, and eligibility dimensions;
- output mode: diagnostic, dashboard brief, KPI definition, model design, review, or implementation handoff.

For budget or cycle work also resolve:

- cycle and version;
- opening budget and later adjustments;
- mandatory, discretionary, promotional, market, retention, reserve, and exception components where applicable;
- allocation hierarchy and decision authority;
- effective-date and in-year cost rules.

## Knowledge to load

Always load:

1. `knowledge/performance-reward/holistic-value-driver-tree.md`
2. `knowledge/performance-reward/fixed-reward.md`

Load only when relevant:

- `knowledge/performance-reward/job-architecture.md`
- `knowledge/performance-reward/market-competitiveness.md`
- `knowledge/performance-reward/performance-management.md`
- `knowledge/performance-reward/pay-equity.md`
- `knowledge/performance-reward/governance-and-controls.md`
- audience profiles;
- Power BI implementation packs;
- KPI, dashboard, page, visual, and implementation schemas.

## Method

### Step 1 — Frame the decision

State:

- who must decide or act;
- what decision is required;
- by when;
- at what organisational and employee grain;
- whether the product supports planning, recommendation, approval, processing, payment, or retrospective review.

Reject vague framing such as “show salary data” or “build a compensation dashboard.” Convert it into a decision statement.

### Step 2 — Establish the authoritative population and time basis

Define:

- eligible population;
- excluded and special populations;
- point-in-time date or analysis period;
- treatment of hires, exits, transfers, promotions, leave, and part-time changes;
- which date determines organisation, manager, job, level, range, and currency attributes.

Flag any temporal mismatch before calculating or designing visuals.

### Step 3 — Separate lifecycle states

Identify which records represent:

- opening position;
- system guidance;
- manager recommendation;
- calibrated recommendation;
- approval;
- payroll-ready outcome;
- processed result;
- paid result.

Do not merge these states for convenience.

### Step 4 — Select the analytical branches

Choose only the branches required by the decision:

- positioning and range compliance;
- salary movement and differentiation;
- budget and affordability;
- market and hiring pressure;
- compression and inversion;
- equity and internal consistency;
- governance, exceptions, and reconciliation;
- employee and manager experience.

### Step 5 — Specify measures and comparisons

For every measure declare:

- business definition;
- numerator and denominator where relevant;
- grain;
- population;
- date basis;
- currency basis;
- status basis;
- comparator;
- blank, missing, invalid, and zero treatment;
- privacy or suppression rule;
- interpretation limitation.

Use the KPI-definition schema for any measure intended for reuse.

### Step 6 — Diagnose before prescribing

Progress through:

1. describe;
2. compare;
3. diagnose;
4. act.

Distinguish observed evidence from interpretation and hypothesis. Do not prescribe an individual salary action from compa-ratio or market position alone.

### Step 7 — Design for the audience

#### Executive

Prioritise enterprise cost, strategic allocation, material risk, equity, market pressure, control exceptions, and decisions required.

#### HR Business Partner or Reward Partner

Prioritise organisational patterns, employee and manager hotspots, structural causes, scenario analysis, and interventions.

#### Manager

Prioritise authorised employee context, budget, policy guidance, team consistency, rationale, and submission actions.

#### Governance, payroll, or finance

Prioritise eligibility, status, control totals, approvals, reconciliation, effective dates, and unresolved exceptions.

### Step 8 — Route implementation work

After domain logic is stable:

- route generic semantic-model, DAX, security, accessibility, performance, and interaction work to the relevant Microsoft or repository Power BI capability;
- retain fixed-reward grain, effective dating, statuses, definitions, calculations, and governance as binding constraints;
- require implementation verification where generic advice could collapse business distinctions.

### Step 9 — Produce the requested artifact

Use the relevant governed output structure:

- discovery or decision brief;
- KPI definition;
- dashboard brief;
- page and visual specification;
- semantic-model requirements;
- design review;
- implementation handoff;
- executive diagnostic summary.

### Step 10 — Run quality checks

Confirm that:

- population and dates are explicit;
- fixed pay is defined;
- states are not mixed;
- local and reporting currency are distinguished;
- recurring and in-year cost are distinguished;
- range metrics use the correct range and date;
- part-time and full-time values are comparable;
- privacy and access are appropriate;
- recommendations are not labelled as outcomes;
- causal claims are qualified;
- every proposed action has an owner or decision point;
- calculations can reconcile to source systems.

## Structured output contract

A completed analysis should contain:

1. **Decision statement**
2. **Audience and authorised scope**
3. **Population and time basis**
4. **Fixed-pay and currency definitions**
5. **Lifecycle state**
6. **Key questions**
7. **Measures and comparators**
8. **Findings or intended diagnostics**
9. **Interpretations and limitations**
10. **Risks, exceptions, and controls**
11. **Actions or decisions required**
12. **Power BI or artifact implementation requirements**
13. **Open questions and evidence gaps**

## Failure modes

Stop or qualify the output when:

- the range cannot be matched reliably;
- the selected employee snapshot does not align with the salary state;
- recommendation and paid outcomes cannot be distinguished;
- currency conversion is missing or inconsistent;
- the comparison population is structurally different;
- small-group analysis would create privacy risk;
- the proposed metric has no stable business definition;
- an organisation-specific policy rule is being inferred rather than supplied;
- a generic Power BI pattern would create an incorrect fixed-reward result.

## Benchmark requirements before activation

The skill must pass at least these scenarios:

1. pre-EOY salary and bonus planning, with fixed reward treated as pre-decision guidance;
2. manager salary review with authorised employee context and budget controls;
3. executive fixed-reward outcome summary;
4. budget allocation and redistribution reconciliation;
5. compression or hiring-premium diagnostic with limitations;
6. a negative test where recommendation and paid outcomes are mixed;
7. a negative test involving part-time pay or incompatible currencies.

## Activation gate

Do not activate until:

- the skill-authoring standard is approved for controlled use;
- the holistic and fixed-reward knowledge packs pass contradiction review;
- output schemas support the contract above;
- benchmark expected results exist and pass;
- Microsoft Power BI skill delegation and verification rules are documented;
- privacy and security behaviour has been reviewed.
