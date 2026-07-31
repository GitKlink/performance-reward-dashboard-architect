---
status: DRAFT
phase: 2
priority: CRITICAL
depends_on:
  - knowledge/performance-reward/holistic-value-driver-tree.md
  - STD-CORE-001
  - STD-CORE-002
  - STD-CORE-003
blocks:
  - .cursor/skills/performance-reward/fixed-reward-analysis/SKILL.md
  - evaluations/benchmark-scenarios/executive-fixed-reward-summary.md
  - pre-EOY salary planning workflow
last_reviewed: 2026-07-31
---

# Fixed Reward Knowledge Pack

## Purpose

This pack defines the fixed-reward concepts, analytical questions, modelling distinctions, and governance requirements needed to design Performance & Reward dashboards and decision-support products.

It covers recurring cash remuneration such as base salary or fixed pay and, where the organisation defines it that way, fixed-remuneration components such as employer retirement or superannuation contributions. Exact inclusions must be declared for each jurisdiction and report.

This draft separates general domain concepts from organisation-specific policy rules. It does not treat any example budget rule, range tolerance, or eligibility rule as universally applicable.

## Domain boundaries

Fixed reward includes:

- base salary or fixed pay;
- fixed-remuneration package components where included by policy;
- salary ranges and reference points;
- individual position within range;
- salary review recommendations, approvals, processing, and paid outcomes;
- promotions and fixed-pay adjustments;
- hiring salaries and premiums;
- retention and market adjustments where they alter recurring pay;
- mandatory, discretionary, structural, and exceptional increases;
- compression, inversion, minimum-pay, and range-compliance analysis;
- fixed-reward budget allocation and reconciliation.

Fixed reward does not include variable incentive outcomes, benefits, recognition awards, or performance ratings, although all may interact with fixed-pay decisions.

## Core decision model

Fixed-reward decisions should be assessed across six linked questions:

1. **Eligibility** — who is in scope and under which policy, jurisdiction, pay group, and cycle?
2. **Position** — what is the employee's current fixed pay relative to the applicable range, peers, market, and internal structure?
3. **Rationale** — what legitimate factors support a change or no change?
4. **Affordability** — what recurring and current-cycle cost does the decision create?
5. **Fairness and risk** — does the decision create or reduce unexplained disparity, compression, inversion, policy breach, or control risk?
6. **Execution** — has the recommendation been approved, processed, reconciled, and paid correctly?

## Fixed-reward value drivers

### External competitiveness

- salary-range position relative to relevant labour markets;
- hiring outcomes and offer acceptance;
- scarcity and criticality;
- prevalence and size of market adjustments;
- range currency and benchmark quality.

### Internal consistency

- pay relationship across comparable jobs and levels;
- consistency within job, level, location, and workforce segment;
- progression through ranges;
- compression between levels or manager and subordinate populations;
- inversion where lower-level or less-accountable work is paid above higher-level work without an explainable reason.

### Performance and contribution recognition

- use of performance as one input to salary movement;
- differentiation while respecting policy, budget, and range constraints;
- distinction between sustained contribution, promotion, market correction, retention, and other reasons;
- prevention of performance ratings becoming the sole determinant of fixed pay.

### Equity and employee trust

- unexplained pay differences;
- hiring versus incumbent positioning;
- demographic and cohort outcomes;
- transparency of policy and decision rationale;
- consistency of manager discretion.

### Affordability

- recurring annualised cost;
- in-year cost based on effective date;
- approved budget, allocation, forecast, and actual;
- mandatory and discretionary expenditure;
- retained, redistributed, reserve, and exception funding;
- currency and payroll impacts.

### Governance and execution

- eligibility and population control;
- delegated authority and approval;
- conduct or policy restrictions;
- exception classification;
- effective-date accuracy;
- payroll reconciliation;
- traceability from input through payment.

## Canonical business questions

### Enterprise and executive

- What is the total proposed, approved, processed, and paid recurring cost?
- How much of the budget is mandatory, discretionary, promotional, market-related, retention-related, or exceptional?
- Where are material affordability, fairness, market, or control risks concentrated?
- Does investment align with strategic workforce priorities?
- Which decisions require executive intervention or acceptance of risk?

### HR Business Partner and Reward Partner

- Which organisations, jobs, managers, or cohorts have unusual positioning or movement patterns?
- Where do proposed outcomes create compression, inversion, range breaches, or unexplained disparities?
- Are hiring and promotion practices creating structural pay issues?
- Which employees or groups require investigation rather than automatic adjustment?
- How will redistribution or retained budget affect intended outcomes?

### Manager

- Who is eligible and what decision is required?
- What is the available budget and policy boundary?
- What relevant employee context may be considered?
- Which recommendations require explanation or approval?
- What impact will the recommendation have on range position and team consistency?

### Governance, payroll, and finance

- Do control totals reconcile across source, recommendation, approval, processing, and payment states?
- Are effective dates, currencies, pay frequencies, and annualisation rules correct?
- Are exceptions approved by the correct authority?
- Can each material outcome be traced to its source rule and decision?

## Canonical measures and definitions

Every measure must declare population, date, currency, fixed-pay definition, and status.

### Fixed pay

The recurring pay amount at the declared effective date. The report must specify whether the value is:

- base salary only;
- total fixed remuneration;
- annualised or actual-period pay;
- full-time equivalent or actual part-time amount;
- local currency or reporting currency.

### Range minimum, midpoint, and maximum

The applicable salary-range reference points for the employee's job, level, location, pay group, or other approved range key at the relevant date.

### Compa-ratio

`Fixed pay / Range midpoint`

Compa-ratio is a positioning indicator, not a complete measure of market competitiveness, performance, fairness, or required salary action.

### Range penetration

`(Fixed pay - Range minimum) / (Range maximum - Range minimum)`

The result should normally be presented with explicit treatment for missing, zero-width, or invalid ranges and for values below minimum or above maximum.

### Salary movement amount

`New fixed pay - Current fixed pay`

### Salary movement percentage

`Salary movement amount / Current fixed pay`

A defined treatment is required where current fixed pay is zero, missing, or not comparable.

### Annualised recurring cost

The full-year recurring increase created by the decision, using the declared fixed-pay definition.

### In-year cost

The cost falling within the relevant financial or reward period after considering effective date, pay frequency, and eligible service.

### Budget utilisation

`Allocated or approved spend / Available budget`

The numerator and denominator must use the same state and scope. Proposed spend should not be compared to paid budget without a clear label.

### Below-minimum and above-maximum population

Count and proportion of eligible employees whose fixed pay is outside the applicable range at the declared point in time.

### New-hire premium

A governed comparison between recently hired employees and a defined incumbent comparator population. It must declare hire window, job and location matching, experience treatment, population exclusions, and whether the comparison uses median, mean, or another statistic.

It must not be interpreted automatically as evidence that new hires are overpaid or incumbents are underpaid.

### Compression indicator

A defined shortfall in expected pay separation between adjacent levels, manager and subordinate populations, or materially different job sizes.

There is no universal compression threshold. The expected separation rule must be an explicit organisation-specific parameter.

## Required status distinctions

Fixed-reward products must not collapse these states:

- current or opening position;
- system-calculated guidance;
- manager recommendation;
- calibrated recommendation;
- approved outcome;
- payroll-ready outcome;
- processed outcome;
- paid outcome;
- cancelled or superseded outcome.

A single field labelled "salary outcome" is insufficient where multiple lifecycle stages exist.

## Canonical analytical grain

A robust model will usually distinguish:

- **point-in-time fixed-pay snapshot** — one row per worker or employment at an effective date;
- **salary recommendation** — one row per worker, cycle, recommendation version, and decision state;
- **pay-change event** — one row per effective-dated pay change;
- **budget allocation** — one row per cycle, organisation or allocation owner, budget component, and version;
- **range snapshot** — one row per range key and effective date;
- **exception** — one row per employee or allocation exception and resolution state;
- **approval event** — one row per decision, authority, and timestamp;
- **payroll result** — one row per processed pay element or reconciled outcome where required.

These grains should not be forced into a single wide table when doing so loses version, status, effective-date, or lineage information.

## Time rules

Every fixed-reward analysis must specify:

- opening, recommendation, approval, effective, processing, and payment dates;
- whether employee, job, organisation, and manager attributes are evaluated at opening date, decision date, effective date, or another date;
- how transfers, promotions, hires, exits, leave, and part-time changes are handled;
- whether movement is annualised;
- treatment of retroactive or future-dated changes;
- the financial period used for in-year cost;
- exchange-rate source and date where reporting currency is used.

## Diagnostic patterns

### Positioning diagnostic

Start with range validity and population eligibility, then examine distribution of compa-ratio or penetration by job, level, location, organisation, tenure, performance, and relevant cohort.

Do not use an enterprise average alone. Distribution, tails, and structurally different populations matter.

### Movement diagnostic

Separate zero and non-zero outcomes, then compare movement amount and percentage by reason, performance, range position, job level, organisation, manager, and cohort.

Test whether an apparent difference is driven by workforce mix, eligibility, promotion, market action, or manager discretion.

### Budget diagnostic

Reconcile opening budget, adjustments, allocations, recommendations, approvals, retained amounts, redistribution, reserves, and final actuals.

Show both absolute cost and utilisation. Highlight which components are recurring.

### Compression and inversion diagnostic

Define the expected relationship first. Identify affected pairs or groups, quantify the shortfall, and distinguish structural issues from temporary or explainable cases.

### Hiring-versus-incumbent diagnostic

Match on defensible job, level, location, and time factors. Compare distributions and control for composition before drawing conclusions.

### Equity diagnostic

Use aggregate descriptive analysis to locate differences, then apply an approved analytical method where causal or adjusted conclusions are required. Protect small populations and sensitive data.

## Power BI implementation implications

Generic Power BI skills may assist with model implementation, DAX, security, performance, and interaction design. They must preserve these domain requirements:

- effective-dated employee, job, range, and organisation attributes;
- separate recommendation, approval, processing, and payment states;
- explicit local and reporting currency measures;
- point-in-time and period measures that cannot be mixed accidentally;
- versioned budgets and recommendations;
- row-level security based on authorised workforce relationships;
- suppression or restricted access for sensitive small populations;
- reconciliation measures and visible data-quality exceptions;
- measure descriptions suitable for non-Power-BI consumers.

## Audience-specific product patterns

### Pre-EOY planning product

Focus on opening position, eligibility, budget guidance, scenario ranges, structural hotspots, and decision preparation. Do not present recommendations as final outcomes.

### Manager salary-review product

Focus on authorised employees, decision guidance, budget, rationale, policy boundaries, team consistency, and submission status.

### Executive outcome product

Focus on enterprise spend, differentiation, equity, market and structural risk, strategic investment, material exceptions, and decisions required.

### Reward operations and controls product

Focus on eligibility, workflow status, exceptions, approvals, reconciliation, effective dates, and payroll readiness.

## Governance and anti-patterns

Avoid:

- treating range midpoint as the required salary for every employee;
- automatically increasing every employee below midpoint;
- comparing part-time actual pay with full-time salary ranges;
- mixing base salary with total fixed remuneration without a declared definition;
- comparing local-currency amounts across countries without an explicit conversion method;
- calculating movement from incompatible opening and outcome snapshots;
- hiding above-range or below-range employees by clipping visual scales;
- treating promotion, market, retention, and merit increases as interchangeable;
- using manager recommendations as approved or paid outcomes;
- publishing identifiable salary data beyond authorised users;
- assuming a pay difference is inequitable or justified without further analysis;
- using generic DAX patterns that ignore effective dating or status.

## Organisation-specific rules to keep separate

The following belong in governed configuration or policy packs rather than this universal domain definition:

- salary bands and reference points;
- tolerance around midpoint or range limits;
- mandatory and discretionary percentages;
- roll-down and redistribution logic;
- eligibility rules;
- conduct restrictions;
- promotion treatment;
- minimum separation rules;
- reserve and strategic-fund rules;
- delegated approval limits;
- suppression thresholds;
- exchange-rate and annualisation conventions.

## Research and completion backlog

Before approval, this pack requires:

- current primary-source evidence for applicable remuneration, pay-equity, privacy, and governance obligations by jurisdiction;
- alignment with market competitiveness, job architecture, performance management, pay equity, and governance packs;
- approved KPI records for the canonical measures;
- worked examples using synthetic data;
- validation through pre-EOY planning, manager salary review, fixed-budget allocation, and executive outcome scenarios;
- explicit mapping to Microsoft Power BI skills and documented gap handling.
