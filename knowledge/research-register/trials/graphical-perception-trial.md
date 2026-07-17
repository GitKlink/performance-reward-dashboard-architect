---
artifact_id: EX-VIZ-001
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
  - Phase 0 stable-research review
  - future visual-perception knowledge pack
  - future chart-selection skill
content_version: 0.1.0
last_reviewed: 2026-07-17
next_review: 2027-07-17
---

# Trial: Stable graphical-perception research

## Purpose

Test the repository's handling of an established research paper whose findings are influential but frequently simplified into rigid chart-selection folklore.

## Research question

What can the repository safely derive from Cleveland and McGill's 1984 graphical-perception research, and how should the future chart-selection capability avoid overstating it?

## Decision supported

Determine how perceptual accuracy should influence visual selection for Performance & Reward dashboards without turning one experimental ranking into an absolute hierarchy for every task, audience, or user.

## Primary research

Cleveland and McGill define graphical perception as the visual decoding of quantitative and qualitative information encoded in graphs. Their paper aims to provide a scientific foundation for graphical methods by identifying elementary perceptual tasks and testing how accurately people perform them.[^cleveland-mcgill]

The research supports the broad principle that different graphical encodings are not equally accurate for quantitative comparison.[^cleveland-mcgill]

The paper's contribution is not simply a list of approved and prohibited chart types. It provides a theory-and-experiment approach for evaluating how viewers decode graphical marks.

## Bounded repository interpretation

### Supported principles

1. **Chart choice must follow the comparison task.** A visual is not effective merely because it is familiar or attractive.
2. **Quantitative comparisons should favour encodings that support accurate judgement.** Position and length are generally stronger starting points than area, volume, or angle for precise comparison.
3. **A chart-selection recommendation should state the perceptual task.** Examples include common-position comparison, non-aligned position, length, direction, angle, area, or colour intensity.
4. **Precision requirements matter.** A rough composition question may tolerate an encoding that would be weak for precise ranking.
5. **The entire design still matters.** Scale, labelling, sorting, density, accessibility, and context can improve or undermine the chosen encoding.

### Unsupported simplifications

Do not state:

- that bar charts are always better than every alternative;
- that pie charts are universally invalid;
- that a population-average ranking predicts every individual's performance;
- that perceptual accuracy is the only chart-selection criterion;
- that the 1984 experiments directly establish Power BI usability or executive reading behaviour;
- that a chart with a high-ranked encoding automatically communicates the right business message.

## Performance & Reward applications

### Precise category comparison

Use a sorted bar or dot plot when comparing:

- fixed-reward increase by rating;
- pay position across job families;
- budget variance by division;
- attrition rates across critical populations.

The primary task is position or length comparison.

### Distribution comparison

A histogram, strip plot, box plot, or small multiple may be more appropriate than a ranked bar when the question concerns overlap, spread, skew, or outliers.

The visual should be selected for the distribution question rather than forced into a simple category-ranking pattern.

### Part-to-whole communication

A composition visual may support a broad share question, but precise comparison across many components should use aligned bars or a table. The repository must distinguish approximate orientation from exact comparison.

### Executive emphasis

A highly accurate encoding can still fail if the executive cannot identify the decision, comparator, material exception, or action. Perceptual accuracy is one input to the design system, not a substitute for decision framing and visual hierarchy.

## Claims matrix

| Claim ID | Claim | Source IDs | Confidence | Repository treatment |
|---|---|---|---|---|
| VIZ-001 | Graphical perception concerns visual decoding of information encoded in graphs | `cleveland-mcgill-graphical-perception-1984` | Established | Publish |
| VIZ-002 | The paper identifies elementary perceptual tasks and evaluates their accuracy | `cleveland-mcgill-graphical-perception-1984` | Established | Publish |
| VIZ-003 | Different encodings can support different levels of quantitative accuracy | `cleveland-mcgill-graphical-perception-1984` | Established | Publish |
| VIZ-004 | Position and length should be preferred starting points for precise dashboard comparison | Research-informed repository synthesis | Supported synthesis | Publish with scope |
| VIZ-005 | The experimental ordering is a universal law applying to every person and task | None sufficient | Unsupported | Reject |
| VIZ-006 | Perceptual rank alone determines the correct chart | None | Unsupported | Reject |

## Selection-rule prototype

The future chart-selection skill should ask in this order:

1. What business question and decision does the visual support?
2. What relationship must be perceived: comparison, trend, distribution, composition, correlation, flow, or variance?
3. How precise must the judgement be?
4. Which perceptual task does each candidate visual require?
5. What audience, accessibility, density, and interaction constraints apply?
6. Can the visual be implemented and exported reliably in Power BI?

This sequence prevents perceptual research from being isolated from business and implementation context.

## What the trial revealed about the standards

### Research standard

- Stable theory does not need artificial recency, but later evidence may qualify how broadly it should be applied.
- Original research should be used rather than relying on secondary chart-ranking summaries.
- The repository needs a clear boundary between research finding and design heuristic.

### Citation standard

- One primary paper can support narrow claims about its own method and findings.
- Broader design recommendations must be labelled as synthesis.
- The DOI is preferable to copied or unauthorised PDF links.

### Naming standard

- Use `graphical-perception` for the research concept.
- Use `chart-selection` for the applied skill.
- Do not name a skill after the researchers because the skill will combine multiple evidence bases and implementation constraints.

## Acceptance result

**Trial result: PASS**

The standards preserve the value of the research while preventing a simplistic universal chart ranking. The result can inform Phase 7 and Phase 8 research after independent review.

## Source

[^cleveland-mcgill]: William S. Cleveland and Robert McGill, “Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods,” *Journal of the American Statistical Association* 79, no. 387 (1984): 531–554, https://doi.org/10.1080/01621459.1984.10478080. Central source ID: `cleveland-mcgill-graphical-perception-1984`.
