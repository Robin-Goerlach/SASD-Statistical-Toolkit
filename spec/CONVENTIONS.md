# Statistical conventions — draft v0.1

Status: draft. Scope: default rules for future procedure contracts.
See [German explanation](../docs/de/REQUIREMENTS.md) and
[pilot details](DESCRIPTIVE-STATISTICS.md).

## Numeric inputs and missingness

- Initial numeric type: IEEE 754 binary64, subject to approval with the language binding.
- Default missing policy: reject. NaN in numeric observations denotes missing,
  not a valid real number. Explicit omit removes NaN observations and records counts.
- Infinity is invalid under both policies. Finite inputs do not guarantee finite intermediate results.
- Paired procedures use aligned observations and complete-pair omission;
  never omit independently from x and y. Unequal lengths are invalid input.
- Missing table labels/masks are converted by adapters; numeric kernels do not
  guess sentinels such as -999.
- No implicit imputation, coercion, weighting or unit conversion.

## Definitions that must be explicit

Sample variance/covariance divides by n-1; population variance/covariance by n.
APIs must identify which result is returned. The pilot summary exposes both
variances, with sample standard deviation separately named.

Future quantile default proposal: Hyndman–Fan type 7, h = 1 + (n-1)p,
linear interpolation between adjacent order statistics, p in [0,1].
This is not implemented or included in M1. Every quantile API names its method.
Weighted quantiles require a distinct approved specification.

Weights are unsupported in the pilot. Frequency, analytic/reliability,
probability/survey and importance weights are distinct concepts; adding a generic
weight vector does not establish their statistical semantics.

## Inference and distributions

Future distribution contracts state support, parameterization, PDF/PMF, CDF,
survival function, quantile, logarithmic probabilities and endpoint behavior.
For discrete distributions, define quantile as the smallest supported x with
F(x) >= p for 0 < p < 1; specify p=0/1 separately per distribution.
Survival probability is P(X>x); a test needing P(X>=x) must account for discreteness.

Every test specifies null/alternative, one-/two-sided meaning, test statistic,
degrees of freedom, p-value algorithm, exact/asymptotic choice, tie corrections
and assumptions. Two-sided discrete p-values require a procedure-specific rule.
Confidence level is explicit, with 0 < level < 1; a proposed default is 0.95.
Multiplicity corrections name the method and hypothesis family. Unadjusted
results are labelled unadjusted, not presented as a corrected family.

Model contracts specify intercept, factor encoding/contrasts, response
transformation, rank policy, objective, standard-error estimator and prediction
versus mean-response intervals. Repeated/clustered observations are not silently
treated as independent.

## Shared result vocabulary

| Code | Meaning |
| --- | --- |
| success | All requested quantities are defined and computation succeeded |
| partial | Some requested quantities are unavailable; other estimates are valid |
| insufficient_data | No requested estimate can be supplied due to observation count |
| invalid_input | Malformed/unsupported call or invalid values/options |
| undefined_statistic | A particular statistic has no definition for these data |
| numerical_failure | A defined computation could not meet its numerical contract |
| non_converged | An iterative method exhausted its approved convergence budget |
| cancelled | Caller cancellation; not a completed analysis |

Availability is per metric; an undefined statistic is never represented as numeric
zero. Storage may use optional values/null plus stable availability codes.
Language bindings may throw for malformed input, but adapters must preserve the
shared error category for the conformance runner and application.

Count accounting for accepted data: input_count = used_count + excluded_count.
For paired procedures these counts are numbers of rows/pairs, not scalars.
Invalid calls need not supply usable counts, but cannot publish valid estimates.
Warnings carry stable codes and optional localized explanations.

## Accuracy and determinism

Each procedure chooses justified absolute/relative tolerances per metric.
Exact counts and statuses are compared exactly. No global mutable epsilon or
missingness option exists. Ordering and any parallel reductions are documented.
Tier-2 numerical reproducibility is the cross-language default; bitwise behavior
and random stream identity require separate, explicit contracts.

The approved procedure specification takes precedence over these defaults.
Any override must be written and versioned, not inferred from an implementation.
