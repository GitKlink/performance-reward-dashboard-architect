---
name: dax-measure-standards-review
description: Review exported Power BI DAX measures against the canonical Semantic Measure Standard, producing a read-only findings report and human-approved refactor proposal. Use for measure naming, folders, descriptions, formatting, hidden/technical measures, and DAX measure inventory audits.
---

# DAX Measure Standards Review — v0

**Purpose:** review a Power BI semantic-model measure inventory and propose changes **without editing DAX, TMDL, model files or standards**. This is the first vertical slice of the Power BI / Fabric Architect, not a full validator.

## Required sources and read order

1. Identify the **current Power BI/PBIP project** and the domain under review.
2. **Prefer the installed project-local standards snapshot**:
   `docs/power-bi-architect/standards/`, recorded in
   `docs/power-bi-architect/installation.json`.
   The snapshot and this skill are copied from approved Git repositories and
   pinned to Standards SHA `2d6eb0c2dd627b7607c0ad28a4ea6866e5427aa9`.
   The checker validates **all 11 source Git blobs** against the immutable source
   lock shipped with this installed skill. Do not silently read a different
   checkout or accept edited standards.
3. Read, in order, under `docs/power-bi-architect/standards/semantic-model/`:
   - `README.md`
   - `semantic_measure_standard.md`
   - `business_glossary.md`
   - selected `domains/semantic_measure_standard_<domain>.md` if applicable.
   - `semantic_measure_standard_improvement_backlog.md` **last** and
     **as proposals only**, never approved requirements.
4. **Backward-compatible fallback:** When working directly in the Architect
   source repository rather than an installed project, the checker can also
   accept a separate clean Git clone of `GitKlink/power-bi-fabric-standards`
   at the same pinned revision. That source mode is **not required** in an
   installed Power BI project.
5. Separately seek approved Performance & Reward business contracts for
   calculation, population, time basis and grain. Naming standards do not
   authorise a semantic change. See Architect
   [Issue #6](https://github.com/GitKlink/performance-reward-dashboard-architect/issues/6).

If the snapshot or its source lock fails integrity checking, **stop**.
Do not claim standards conformance or remove source verification.

## Prepare a real inventory (read-only)

Recommended source in **Power BI Desktop DAX Query View**:

~~~dax
EVALUATE
    INFO.VIEW.MEASURES()
~~~

Export the result to a **UTF-8 CSV** kept outside public Git repositories. Keep `Name`, `Table`, `Description`, `FormatString`, `FormatStringDefinition`, `DisplayFolder`, `IsHidden` and `Expression` when available. The checker requires `Name` only; other missing headers are explicitly reported as **not assessed**.

Metadata/expressions can be unavailable depending on permissions and connection mode. A CSV may contain confidential model definitions. Never paste it into a public PR, synthetic fixture, public issue or logging service.

An existing export with equivalent columns is acceptable; inspect its header and rows before using it. **Do not invent fields or fill missing description/format values with guesses.**

## Run the deterministic checker

From the **target Power BI project root**, with Python 3.10+ (and
`docs/power-bi-architect/standards/` installed), run:

~~~powershell
python .agents/skills/dax-measure-standards-review/scripts/review_measures.py --input "C:\\private\\measure-inventory.csv" --standards-root "docs/power-bi-architect/standards" --domain variable_reward --out-dir "C:\\private\\dax-measure-review"
~~~

The checker **reads** the CSV and immutable copied standards, and writes only
`review.json` and `review.md` to the explicit output directory. It does not
require an open Architect/Standards clone after installation, connect to
Power BI or modify DAX/model files.

Choose another domain from `--help` or omit it for generic measures.
Exit **0** means only a partial review ran; **2** blocks on invalid input,
missing/tampered source, wrong revision or filesystem errors.

## Review and propose

1. Open `review.md`. Explain each mechanical finding with its exact rule ID and canonical source section. Treat the output as **partial coverage**, never full standards compliance.
2. Look at measures with no mechanical findings too. Check root-first family grouping, terminology, approved abbreviations, Change vs Variance semantics, context compression, visibility intent, description quality, true business grain, lifecycle status and the selected domain's exceptions.
3. Compare each business concept with domain authority and the existing model. **Do not infer that `Avg Fixed Salary` means `Fixed Reward Average` without confirming its denominator and definition.**
4. Produce an approval table: **table, old name, proposed name, proposed folder, description/format suggestion, rule/source reference, confidence, dependencies/impact, requires approval**.
5. For any ambiguous business meaning or missing expression, write **Needs domain owner confirmation**, not a speculative rename.
6. Explicitly record what could not be checked: DAX parser/engine validity, numerical equivalence, dependencies, QA rowcount coverage, synonyms, model compile and hidden-context rules.
7. **Stop after the proposal.** Do not run a rename, dependency rewrite, TMDL patch, TMSL/XMLA script or DAX update without a distinct approved apply-and-validate phase.

## Safety and privacy

- Do not write in the copied canonical standards, source repositories or unrelated workspace roots.
- Do not store real CSV exports or generated reports in public repositories. Use private local folders.
- Do not report employee, pay, rating or incentive data. This skill reviews model metadata, not underlying workforce rows.
- If copied standards differ from the pinned approved source, do not bypass the Git blob lock. Propose a reviewed snapshot update with tests.
- Do not claim a blank expression means the measure is blank: `INFO.VIEW.MEASURES()` may suppress expressions depending on permissions.

## Reference

See [check coverage and limitations](references/check-coverage.md). The skill's standard-selection workflow and report are reviewable, but **Cursor auto-discovery and real PBIP integration remain to be tested**.
