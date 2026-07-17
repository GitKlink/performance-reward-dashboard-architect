---
artifact_id: EX-CONSULT-001
status: DRAFT
phase: 0
priority: high
depends_on:
  - artifact_id: STD-CORE-001
    path: ../../../docs/standards/naming-standard.md
  - artifact_id: STD-CORE-002
    path: ../../../docs/standards/research-standard.md
  - artifact_id: STD-CORE-003
    path: ../../../docs/standards/citation-standard.md
  - artifact_id: KNOW-CORE-001
    path: ../README.md
  - artifact_id: KNOW-CORE-002
    path: ../sources.yaml
blocks:
  - Phase 0 consulting-attribution review
  - future consulting-technique catalogue
content_version: 0.2.0
last_reviewed: 2026-07-17
next_review: 2026-10-17
---

# Trial: Consulting-firm technique attribution

## Purpose

Test whether the repository can describe a technique published by a major consulting firm without overstating the firm's internal standards or converting a context-specific method into a universal dashboard rule.

## Research question

What can be attributed directly to McKinsey's public visual performance management publications, and how should the repository translate that material into a bounded dashboard-design recommendation?

## Decision supported

Determine whether the agent may recommend the `1-3-10` principle for executive or operational performance pages and what caveats must accompany it.

## Published methodology

McKinsey's April 2022 article presents three principles for visual performance management: define a KPI cascade linked across organisational layers, use simple visualisation following a `1-3-10` principle, and conduct action-oriented performance meetings based on misses against target.[^mckinsey-vpm]

The article defines `1-3-10` as:

- one second to know whether performance is winning or losing;
- three seconds to identify what it is winning or losing at;
- ten seconds to determine the course of action.[^mckinsey-vpm]

A June 2022 follow-up frames visual performance management as storytelling that helps people take action, says the performance story should be understandable at a glance, and describes the visual as a one-sentence pitch rather than a full script.[^mckinsey-pitch]

These claims may be attributed to the cited publications. They do not establish a universal McKinsey presentation standard.

## Attribution classification

| Statement | Classification | Treatment |
|---|---|---|
| McKinsey's public article presents the `1-3-10` principle | Published methodology | Attribute directly |
| The cited articles emphasise action and an at-a-glance performance story | Published methodology | Attribute directly |
| Every McKinsey executive dashboard follows `1-3-10` | Unsupported generalisation | Reject |
| `1-3-10` is a universal law of perception | Unsupported claim | Reject |
| It can be used as a rapid-orientation test for suitable pages | Project synthesis | Publish as selection guidance |
| Every diagnostic page must reveal every answer in ten seconds | Misapplication | Reject |

## Repository interpretation

### Appropriate use

Use `1-3-10` as a rapid-orientation test when the page is intended to:

- communicate whether performance or risk is on track;
- surface the material driver;
- direct the user toward an immediate action, escalation, or deeper page;
- support a recurring management cadence;
- serve an audience with limited reading time.

### Inappropriate use

Do not use it as a rigid completion-time requirement when the page is intended to:

- support exploratory diagnosis;
- compare complex distributions or cohorts;
- enable employee-level planning or calibration;
- document governance evidence;
- explain a multi-stage analytical argument;
- operate as a static appendix.

### Design test

For a suitable page, ask:

1. Can the intended audience identify the current state without reading every object?
2. Can they identify the material driver or exception without relying on hover?
3. Can they identify the next action or navigation path?

This test is adapted to audience, complexity, accessibility, and consumption mode. It is not a literal stopwatch guarantee.

## Performance & Reward applications

### Executive fixed-reward page

- Orientation: forecast investment is within or outside approved tolerance.
- Driver: market remediation, mandatory increases, or discretionary allocation explains the variance.
- Action: endorse, redirect, request a scenario, or escalate a control issue.

### Manager action page

- Orientation: how many cases require attention.
- Driver: which exception or deadline dominates.
- Action: open the prioritised case list or complete the required decision.

### Business Partner diagnostic page

Apply the principle to the summary and navigation layer. Deeper diagnostic pages may require deliberate comparison and exploration.

## Claims matrix

| Claim ID | Claim | Source IDs | Confidence | Treatment |
|---|---|---|---|---|
| CAT-001 | McKinsey's article publishes the `1-3-10` principle | `mckinsey-visual-performance-management-2022` | Established | Publish with attribution |
| CAT-002 | The follow-up frames visual performance management as storytelling that supports action | `mckinsey-visual-performance-pitch-2022` | Established | Publish with attribution |
| CAT-003 | McKinsey universally applies `1-3-10` to every executive deck | None | Unsupported | Reject |
| CAT-004 | `1-3-10` is useful as a rapid-orientation test for suitable dashboard pages | Project synthesis informed by both sources | Supported synthesis | Publish with scope |
| CAT-005 | Missing the exact seconds proves poor design | None | Unsupported | Reject |

## Acceptance result

**Trial result: PASS**

The standards distinguish direct firm attribution, unsupported generalisation, and project synthesis. The method is suitable for the future technique catalogue with bounded invocation rules.

## Sources

[^mckinsey-vpm]: McKinsey & Company, “Getting visual performance management right,” 2022-04-01, retrieved 2026-07-17, https://www.mckinsey.com/capabilities/operations/our-insights/operations-blog/getting-visual-performance-management-right. Central source ID: `mckinsey-visual-performance-management-2022`.

[^mckinsey-pitch]: McKinsey & Company, “Getting visual performance management right — So, what's the pitch?,” 2022-06-06, retrieved 2026-07-17, https://www.mckinsey.com/capabilities/operations/our-insights/operations-blog/getting-visual-performance-management-right-so-whats-the-pitch. Central source ID: `mckinsey-visual-performance-pitch-2022`.
