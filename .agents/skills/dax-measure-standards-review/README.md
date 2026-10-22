# DAX Measure Standards Reviewer — project-local installed capability

This **read-only Cursor skill** reviews a DAX-measures CSV against a pinned,
copied snapshot of the canonical engineering standards. The source repository
is the [Power BI / Fabric Architect](https://github.com/GitKlink/performance-reward-dashboard-architect);
the actual standards authority is
[power-bi-fabric-standards](https://github.com/GitKlink/power-bi-fabric-standards).

## Project-local installation

Use [Architect SETUP.md](../../../SETUP.md) **from a local Architect clone**
to install into the **Power BI project currently open in Cursor**.
The installer runs a dry-run first and asks approval to create:

- `.agents/skills/dax-measure-standards-review/` (this directory).
- `docs/power-bi-architect/standards/semantic-model/` (copied standards).
- `docs/power-bi-architect/installation.json` and
  `docs/power-bi-architect/standards/source-manifest.json` (provenance).

Once installed, you do **not need** the Architect or Standards Git checkout
open alongside the Power BI project.

## Run a real CSV inventory review

In Power BI Desktop → DAX Query View:

~~~dax
EVALUATE
    INFO.VIEW.MEASURES()
~~~

Save a UTF-8 CSV **privately**, ideally including `Name`, `Table`,
`Description`, `FormatString`, `FormatStringDefinition`, `IsHidden`,
`DisplayFolder` and optionally `Expression`. The only required column is
`Name`; absent optional fields are flagged as **not evaluated**.

From the **target Power BI project root**:

~~~powershell
python .agents/skills/dax-measure-standards-review/scripts/review_measures.py --input "C:\\private\\measure-inventory.csv" --standards-root "docs/power-bi-architect/standards" --domain variable_reward --out-dir "C:\\private\\dax-measure-review"
~~~

Reports are `review.md` and `review.json` in your chosen private directory.
Return 0 is **partial review executed**, not full standards conformance.
Return 2 blocks on invalid CSV or unverifiable standards.

## Test without Power BI data

From the **target project root** (the synthetic fixture is installed with the skill):

~~~powershell
python .agents/skills/dax-measure-standards-review/scripts/review_measures.py --input ".agents/skills/dax-measure-standards-review/examples/measure-inventory.synthetic.csv" --standards-root "docs/power-bi-architect/standards" --domain variable_reward --out-dir "C:\\private\\synthetic-review"
~~~

The reviewer validates copied documents against an approved, immutable
`references/source-lock.json` containing Git blob IDs for **all 11**
standards documents, as well as the installation manifest's SHA-256 values.
The approved Standards commit is `2d6eb0c2dd627b7607c0ad28a4ea6866e5427aa9`.
This verification does not require the source Git checkout at review time.
The previous direct Git-clone verification mode remains supported.

The copied standards are a **versioned consumer snapshot**, not the canonical
editing home. Do not edit installed standards to change rules: propose changes
upstream and use a separately reviewed update.

## Limitations

- CSV metadata only; no PBIP/TMDL model ingestion, compile or numeric reconciliation.
- No automatic DAX renames, rewrites, model edits or silent updates.
- Mechanical checks are a **subset**; business semantics and glossary decisions
  still require expert/human review.
- Keep salary, employee, incentive, proprietary DAX and actual model exports private.

See [SKILL.md](SKILL.md) and [rule coverage](references/check-coverage.md).

## Output schema

`review.json` uses `power-bi-fabric-architect-dax-measure-review-v1`.
The previously experimental identifier with the planning skill's name was
corrected before the real-model pilot.
