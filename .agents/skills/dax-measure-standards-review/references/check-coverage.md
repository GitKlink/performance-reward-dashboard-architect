# DAX measure reviewer — mechanical rule coverage (v0)

**Canonical authority:** PRIVATE `GitKlink/power-bi-fabric-standards`, revision `2d6eb0c2dd627b7607c0ad28a4ea6866e5427aa9`. Core file `semantic-model/semantic_measure_standard.md`; its README, business glossary, and optional domain extension are reference inputs. The script verifies their committed bytes in a clean, pinned local Git clone. **No private source text is distributed with Wayfinder.**

The validator implements a **fixed reviewed subset** of the pinned standard. A newer standard requires a separate review/profile update; merely changing the SHA constant is not an acceptable governance process.

| ID | Mechanical condition | Classification | Core standard reference | Caveat |
|---|---|---|---|---|
| `SM-NAME-050` | Measure name longer than 50 characters | Error | §6.9 | 50 hard maximum unless approved exception |
| `SM-NAME-040` | Name 41–50 chars | Warning | §6.9 | A reason may justify the soft exceedance |
| `SM-NAME-030` | Name 31–40 chars | Information | §6.9 | 30 is a preferred target, not an absolute limit |
| `SM-NAME-SPACE` | Leading/trailing whitespace | Warning | §6.8 | Conservatively advisory |
| `SM-NAME-PREFIX` | Visible name starts M_, Calc_, KPI_, Helper_ | Warning | §6.3 | Requires valid IsHidden field |
| `SM-NAME-UNDERSCORE` | Visible name has an underscore | Warning | §6.8 | Requires valid IsHidden field |
| `SM-NAME-PERCENT` | Percent sign not terminal ' %' | Warning | §6.5 | Must confirm name is a percentage, not a text token |
| `SM-DESC-MISSING` | Visible measure has empty description | Error | §8 | Missing Description header means NOT EVALUATED |
| `SM-FORMAT-MISSING` | Visible measure has neither static nor dynamic format metadata | Error | §11 | Both headers missing means NOT EVALUATED |
| `SM-FOLDER-DEPTH` | Non-technical folder path deeper than 2 levels | Warning | §7.3 | Folder may contain multiple paths separated by semicolons |
| `SM-DEPRECATED-VISIBLE` | Deprecated marker/name remains visible | Warning | §19 | Heuristic marker, not deprecation classification |
| `SM-DUPLICATE-NAME` | Same name ignoring case/edge spaces occurs more than once | Error | Model integrity / §20 search-first | Investigate source inventory duplicates too |
| `EXP-HIDDEN-UNKNOWN` | IsHidden is neither True/False nor yes/no nor 1/0 | Information | Export integrity | Other visible-only checks skipped for the row |

**Deliberately NOT claimed:** approved business concept, root-first family matching, permitted contextual compression, glossary synonyms, Change vs Variance business meaning, currency/time/eligibility semantics, correct owner table, synonyms, blank-versus-zero behavior, QA fact-table row counts, DAX validity/performance, dependencies, visual query effects, numerical reconciliation, model compilation, field parameter behavior, calculation groups, all AI semantic governance.

**Severity meanings:** Error = clear metadata gap against the currently implemented subset (not a compile failure); Warning = likely governance gap requiring confirmation; Information = optimisation or export completeness. A return code 0 means the checker completed, **not** zero findings or full conformance.

**Output:** `review.json` and `review.md`, always with `status=partial_review_only`, canonical Git SHA, source file SHA-256 digests, input SHA-256, unsupported/skipped checks. The input CSV is never rewritten.

**Export:** Microsoft documents `EVALUATE INFO.VIEW.MEASURES()` and the `Name`, `Table`, `Expression`, `Description`, `FormatString`, `FormatStringDefinition`, `IsHidden`, `DisplayFolder` fields. Expression visibility may depend on write permissions and non-live connection. Source: https://learn.microsoft.com/en-us/dax/info-view-measures-function-dax

**Gates before an apply script:** domain owner confirmation, no name collisions, dependency-aware rename plan, approved diff, actual PBIP/TMDL validation, numerical/regression checks where relevant. No apply facility is included in v0.
