# Descriptive statistics pilot — draft v0.1

Status: draft; milestone M1; requirement scope defined in
[REQUIREMENTS.md](../docs/en/REQUIREMENTS.md).

Procedures: STAT-DESC-001 (summary), STAT-DESC-002 (sample covariance),
STAT-DESC-003 (Pearson correlation).

## Inputs and options

Univariate summary consumes a sequence x. Paired procedures consume aligned
x and y with equal length. Options: missing_policy = reject (default) or omit.
No weights, sorting, table dependency or mutation of input is permitted.
NaN/infinity rules follow [CONVENTIONS.md](CONVENTIONS.md).

## Definitions

For retained finite observations x_i, n = used_count:

- Mean: m = (sum x_i)/n, defined for n >= 1.
- Centered sum: M2 = sum (x_i-m)^2.
- Population variance: M2/n, defined for n >= 1.
- Sample variance: M2/(n-1), defined for n >= 2.
- Sample standard deviation: sqrt(sample variance), defined for n >= 2.
- Minimum/maximum: retained extrema, defined for n >= 1.
- Sample covariance: C/(n-1), where C = sum (x_i-m_x)(y_i-m_y), n >= 2.
- Pearson correlation: C/sqrt(M2_x*M2_y), n >= 2 and both centered sums positive.

These are mathematical definitions, not permission to use unstable raw sums in code.
Covariance has product units; variance has squared units; correlation is unitless.

## Result shape

Summary returns counts plus mean, minimum, maximum, population_variance,
sample_variance and sample_standard_deviation, with availability per metric.
Covariance and correlation return their respective value, counts and status.
Combined accumulator APIs are optional language design choices, not extra
statistical contracts. Streaming/merge APIs require additional order/merge cases.

| Case | Summary outcome | Paired outcome |
| --- | --- | --- |
| n=0 after omission | insufficient_data; all estimates absent; counts valid | insufficient_data; value absent |
| n=1 | partial; mean/extrema valid, population variance 0; sample measures unavailable with insufficient_data | insufficient_data; value absent |
| n>=2, constant | success; both variances/SD exactly 0 | covariance valid and 0; correlation undefined_statistic if either variable constant |
| NaN with reject | invalid_input; no estimates | invalid_input; no estimates |
| NaN with omit | Drop observation, preserve counts | Drop complete pair, preserve pair counts |
| Infinity, unequal pair lengths, unsupported option | invalid_input; no estimates | invalid_input; no estimates |
| Unrepresentable result or numerical contract failure | numerical_failure for affected result; no fabricated estimate | numerical_failure; no fabricated estimate |

## Algorithm selection

Before approval, compare a centered two-pass implementation with an online
Welford-style update and centered covariance update. Assess scaling, overflow,
accumulation error and behavior with large offsets and small spread.
The draft does not yet select an implementation algorithm.

Do not compute variance from sum(x*x) - sum(x)^2/n. Do not silently force negative
variance to zero or correlation into [-1,1]. If a rounding correction is justified,
its bound and diagnostic must be part of the approved contract.
Avoid overflow in sqrt(M2_x*M2_y) through an approved scaling approach.

## Acceptance

- Execute every case in [descriptive-cases.json](../conformance/descriptive-cases.json).
- Add independent NIST/reference cases before validation status.
- Verify translation and scaling identities within documented accuracy bounds.
- Verify covariance symmetry and correlation behavior on positive/negative linear pairs.
- Include near-constant, permuted-order and representability stress cases when the algorithm is selected.
- Inspect comments, non-mutation, allocations and actual dependency mapping.

For the small hand-derived fixtures, atol=1e-12 and rtol=1e-12 apply unless
overridden in that fixture. Counts/status and constant zeros are exact.
Stress/reference cases require their own tolerances; passing the small fixtures
does not establish general numerical accuracy.
