# DAX Measure Standards Reviewer — first usable version

The read-only Python checker analyses a measure-metadata CSV export. A Cursor-compatible [SKILL.md](SKILL.md) explains how to combine its mechanical findings with the canonical measure standard, glossary, relevant domain representation and human interpretation. **No DAX or semantic-model changes are made.**

## Requirements

- Python 3.10+ and Git
- A locally accessible **private** clone of `GitKlink/power-bi-fabric-standards`
- Standards checkout pinned to SHA `2d6eb0c2dd627b7607c0ad28a4ea6866e5427aa9` with clean `semantic-model/` folder
- A CSV containing at least `Name`, ideally from Power BI DAX Query View:

~~~dax
EVALUATE
    INFO.VIEW.MEASURES()
~~~

Include `Table`, `Description`, `FormatString`, `FormatStringDefinition`, `IsHidden` and `DisplayFolder` when available; missing optional columns make the assessment **incomplete**, not a pass. Expressions may be suppressed by model permissions or live connectivity.

## Start here — PowerShell

**Do not overwrite or detach an existing working standards checkout.** If needed, create a separate clone using your authorised GitHub identity:

~~~powershell
git clone https://github.com/GitKlink/power-bi-fabric-standards.git C:\analytics\power-bi-fabric-standards
git -C C:\analytics\power-bi-fabric-standards switch --detach 2d6eb0c2dd627b7607c0ad28a4ea6866e5427aa9
~~~

Keep real measure inventory files in a **private, untracked folder**; do not put them or the generated report in the public Architect repository.

From the **Architect repo root**:

~~~powershell
python .agents/skills/dax-measure-standards-review/scripts/review_measures.py --input "C:\private\measure-inventory.csv" --standards-root "C:\analytics\power-bi-fabric-standards" --domain variable_reward --out-dir "C:\private\dax-measure-review"
~~~

Use another domain key from `--help` or omit `--domain` for generic review.

The reports are `review.md` and `review.json` under the output directory. Return code **0 = review ran**, not full conformance. Return code **2 = blocked** due to invalid input, permissions, checkout mismatch or filesystem problem.

In Cursor, open Architect and the standards clone (local multi-root when needed), then ask: **Use dax-measure-standards-review to assess this export and propose a DAX measure naming/metadata refactor without applying it.**

## Local tests

~~~powershell
python -m unittest discover -s tests -p "test_dax_measure_reviewer.py" -v
~~~

Tests use synthetic fixtures/mocks. Real Git repository access, Cursor skill discovery and Power BI model round-trip are **not yet integration tested**. See the exact [mechanical coverage](references/check-coverage.md).

## Boundaries

- No duplicate copy of canonical standards text is committed to Architect.
- No automatic renames, TMDL edits, DAX expression changes, dependency rewrites or numerical reconciliation.
- Naming/metadata checks are a **reviewed subset** of one pinned standards revision. A zero-finding result is **not** full standards compliance.
- Business definitions, root-first concept grouping, eligibility, population, calculation grain, and Change vs Variance require human/domain approval.
- This v0 accepts CSV inventory only; native PBIP/TMDL ingestion is the next integration step.

Official sources: [Microsoft INFO.VIEW.MEASURES](https://learn.microsoft.com/en-us/dax/info-view-measures-function-dax), [Cursor Skills](https://cursor.com/docs/skills).

## Output schema migration (terminology correction)

Before the first real-model pilot, the report's `schema_version` was corrected from the inaccurate original project-branding identifier to `power-bi-fabric-architect-dax-measure-review-v1`. Any early consumer matching the old schema identifier must update its check. Report fields and the checker rules remain otherwise unchanged. This is a **schema identifier change**, not a new validator capability.
