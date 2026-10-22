---
name: dax-measure-standards-review
description: Review exported Power BI DAX measures against the private canonical Semantic Measure Standard, producing a read-only findings report and human-approved refactor proposal. Use for measure naming, folders, descriptions, formatting, hidden/technical measures, and DAX measure inventory audits.
---

# DAX Measure Standards Review — v0

**Purpose:** review a Power BI semantic-model measure inventory and propose changes **without editing DAX, TMDL, model files or standards**. This is the first vertical slice of the Wayfinder architect, not a full validator.

## Required sources and order

1. Identify the **actual PBIP/product repository** (write owner for a future authorised change) and the user's requested domain.
2. Locate the local clone of the **private** Git repository `GitKlink/power-bi-fabric-standards`; do not substitute web search, an HTML explorer or a copied prompt.
3. Verify its `HEAD` equals the reviewed baseline SHA `2d6eb0c2dd627b7607c0ad28a4ea6866e5427aa9`. The checker blocks any different revision. Do not switch an existing checkout without user approval; use a separate pinned clone if necessary.
4. Read, in order, directly from that private clone:
   - `semantic-model/README.md`
   - `semantic-model/semantic_measure_standard.md`
   - `semantic-model/business_glossary.md`
   - `semantic-model/domains/semantic_measure_standard_<selected-domain>.md` if relevant.
5. Do **not** turn `semantic_measure_standard_improvement_backlog.md` into a rule source; it is proposal material.
6. Separately seek an **approved domain business contract** for eligibility, calculations, grain, time basis and metric meaning. A semantic-model domain file alone does not authorise changes to business semantics; Wayfinder [Issue #6](https://github.com/GitKlink/performance-reward-dashboard-architect/issues/6) is still relevant.

If the source is unavailable or mismatched, **stop and report the precise missing source/revision** rather than claiming compliance.

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

From the **Wayfinder repository root**, with Python 3.10+ and Git available:

~~~powershell
python .agents/skills/dax-measure-standards-review/scripts/review_measures.py --input "C:\private\measure-inventory.csv" --standards-root "C:\analytics\power-bi-fabric-standards" --domain variable_reward --out-dir "C:\private\dax-measure-review"
~~~

Use a different domain from `--help` when appropriate, or omit `--domain` for generic measures. The checker **reads** the input CSV and Git-pinned standards metadata, then writes only `review.json` and `review.md` in the explicitly selected local output directory. It does not connect to Power BI or write model files.

A return code of **0** means the partial review ran, **not** that the model is conformant. Return code **2** blocks review on invalid CSV, missing/mismatched private standards or filesystem errors.

## Review and propose

1. Open `review.md`. Explain each mechanical finding with its exact rule ID and canonical source section. Treat the output as **partial coverage**, never full standards compliance.
2. Look at measures with no mechanical findings too. Check root-first family grouping, terminology, approved abbreviations, Change vs Variance semantics, context compression, visibility intent, description quality, true business grain, lifecycle status and the selected domain's exceptions.
3. Compare each business concept with domain authority and the existing model. **Do not infer that `Avg Fixed Salary` means `Fixed Reward Average` without confirming its denominator and definition.**
4. Produce an approval table: **table, old name, proposed name, proposed folder, description/format suggestion, rule/source reference, confidence, dependencies/impact, requires approval**.
5. For any ambiguous business meaning or missing expression, write **Needs domain owner confirmation**, not a speculative rename.
6. Explicitly record what could not be checked: DAX parser/engine validity, numerical equivalence, dependencies, QA rowcount coverage, synonyms, model compile and hidden-context rules.
7. **Stop after the proposal.** Do not run a rename, dependency rewrite, TMDL patch, TMSL/XMLA script or DAX update without a distinct approved apply-and-validate phase.

## Safety and privacy

- Do not write in the private standards clone, DAX/M library or unrelated workspace roots.
- Do not store the export or resulting report in the public Wayfinder repository. Keep them in a private workspace and review permissions.
- Do not report employee, pay, rating or incentive data. This skill reviews model metadata, not underlying workforce rows.
- If local standards diverge from the pinned baseline, do not bypass the checker by editing the SHA. Propose a reviewed profile update with tests.
- Do not claim a blank expression means the measure is blank: `INFO.VIEW.MEASURES()` may suppress expressions depending on permissions.

## Reference

See [check coverage and limitations](references/check-coverage.md). The skill's standard-selection workflow and report are reviewable, but **Cursor auto-discovery and real PBIP integration remain to be tested**.
