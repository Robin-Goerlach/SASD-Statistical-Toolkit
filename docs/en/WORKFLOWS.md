# Data, analysis workflows and outputs

[Deutsch](../de/WORKFLOWS.md)

The contracts below guide M3 and later. They are not implemented schemas today.
The M1 core consumes numeric observations directly.

## Variable and dataset semantics

Each variable has a stable ID, name, label, physical type, measurement level
(nominal/ordinal/scale where meaningful), optional unit and value labels.
Measurement level informs procedure prerequisites; it must not force automatic
test selection. Strings/categories and date/time values need explicit encodings
before numerical analysis. Do not infer that numeric category codes are measurements.

Missingness is distinct from a stored numeric value. A table adapter translates
declared missing-value labels/masks into the agreed core policy. Infinity is invalid,
not missing. Never replace missing observations with zero. An omission must identify
the source rows, reason, rule and effect on each analysis.

Filters and derived variables produce a new logical snapshot or view, preserving
the original. Group order and factor contrast/reference levels must be explicit.
Joins and reshape operations require row/key validation before analysis.
Import settings include encoding, delimiter, header, decimal separator, quoting,
type mapping and missing-value tokens; locale must not silently change values.

## Analysis recipe

A proposed versioned recipe records:

- Recipe/schema and procedure/contract versions.
- Immutable dataset identity or caller-supplied content identity with its trust level.
- Selected variables, row selection, grouping and transformations in execution order.
- Missingness/weight policy, model formula/contrast coding and method options.
- Alternative hypothesis, confidence level and multiplicity family when applicable.
- Randomness algorithm/version, seed or state and stream settings where applicable.
- Language/package/Math versions and relevant execution configuration.

The application chooses storage and dataset hashing. Recipes do not embed
private data by default. A changed dataset produces a new identity; cached output
cannot be presented as a fresh rerun. Cancellation returns a distinct status and
must not publish partial output as a completed analysis.

## Structured outputs

| Result component | Content | Presentation responsibility |
| --- | --- | --- |
| Estimates | Typed numeric values, units, uncertainty and availability | Rounding and localization |
| Tables | Column schema, stable row/column IDs, numeric cells, labels | Layout, sorting and export style |
| Diagnostics | Status codes, assumptions, warnings, convergence/rank information | Explanation and severity display |
| Plot specification | Numeric series, semantic roles, axes/units and transformations | Graphics rendering and editing |
| Provenance | Recipe/data/procedure/dependency identity and execution record | History and report metadata |

For inference, report effect and uncertainty along with the test statistic and
p-value. Explain what assumptions were checked, supplied by the caller or left
unverified. A p-value is not the probability that the null hypothesis is true.
No automatic conclusion should conceal design assumptions or multiple comparisons.

Adapters can later export JSON/CSV/HTML. Text/HTML output must be escaped;
spreadsheet exports need an explicit policy for formula-like strings.
Applications own filesystem writes, permissions and selection of export destinations.

## Initial end-to-end acceptance scenario

An original numeric CSV is imported using explicit settings. One variable has a
declared missing entry. A filter defines the analysis rows; the engine produces
summaries with reconciled counts and diagnostics. The application saves the recipe,
exports raw numeric results plus metadata, then reruns against the same snapshot.
Results match the contract tolerance and the source file remains unchanged.

This scenario is an M3 acceptance target. It is not currently an executable sample.
