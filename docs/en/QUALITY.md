# Numerical quality and release evidence

[Deutsch](../de/QUALITY.md)

## Evidence layers

| Layer | Required evidence | Example |
| --- | --- | --- |
| Mathematical | Definition, domain, assumptions and derivation | Variance denominator and minimum sample size |
| Manual | Small original datasets with exact/rational results | [1,2,3,4,5] has mean 3 and sample variance 5/2 |
| Independent | Certified data or pinned external implementation, explicit options | NIST summaries; reference tool/version and command recorded |
| Boundary | Empty/singleton/constant/missing/invalid/extreme inputs | Large offsets with small spread |
| Property | Mathematical relationships within justified tolerance | Translation invariance of variance; covariance symmetry |
| Integration | Actual language build, dependency and package usage | Clean install followed by an in-memory summary |
| Application | Data, recipe, result/export consistency | Excluded-row counts remain consistent in output |

Property checks supplement independent cases. C++ versus C# agreement alone is
not independent evidence: both may contain the same conceptual error.

## Numerical design rules

- Use centered, reviewed algorithms for moments; avoid raw sum-of-squares subtraction.
- Review overflow/underflow and scaling. Finite inputs can still exceed representable intermediates.
- Compute small upper probabilities directly where needed; do not rely on 1 minus a rounded CDF.
- Use QR/rank-aware methods for general linear models rather than normal equations.
- Keep estimates, standard errors, confidence intervals and numerical diagnostics distinct.
- Do not silently clip unstable probabilities/correlations or treat non-convergence as success.

Contracts choose a method and accuracy target before approval. A universal
epsilon is insufficient. Compare using abs(actual-reference) <= atol +
rtol*abs(reference), with units and scale justified per output. Probabilities
near zero may require log-domain or relative criteria; quantiles may require
probability residuals as well as x-error. Counts/statuses are exact.

## Reference register

Primary sources to consult, checked as sources on 2026-10-02:

- [NIST Statistical Reference Datasets](https://itl.nist.gov/div898/strd/):
  certified summary, ANOVA and regression reference data.
- [NIST univariate background](https://www.itl.nist.gov/div898/strd/univ/backgroundinfo.html):
  explains its summary-statistic reference scope.
- [R sample quantiles](https://www.stat.ethz.ch/R-manual/R-devel/library/stats/html/quantile.html):
  reference for alternative quantile definitions.
- [R normal distribution](https://www.stat.math.ethz.ch/R-manual/R-devel/library/stats/html/Normal.html):
  reference for explicit tail and logarithmic probability interfaces.

These are reference links, not vendored data or already executed comparisons.
Mutable documentation pages do not pin a reference runtime. Before importing a
case, retain source/version, retrieval date, license/redistribution assessment,
original certified precision, transformations and expected-value derivation.

## Reproducibility tiers

1. Semantic: same approved procedure, options and data interpretation.
2. Numerical: outputs agree within justified contract tolerances.
3. Bitwise: identical bits on a declared platform/toolchain/execution configuration.

Tier 2 is the default target across languages. Tier 3 requires an explicit
contract, including reduction order, math libraries, PRNG and parallel streams.
A seed alone does not guarantee cross-language random sequence identity.

## Release gate

No procedure is released until its contract, Math capability gate, independent
cases, boundary cases, language runner, examples and EN/DE handbook are complete.
Record the accepted toolchains/platforms and exact dependency versions. Report
coverage gaps and known numerical limitations. Performance tuning must preserve
the same numerical acceptance evidence.

Documentation CI checks internal links, paired planning IDs, catalogs and
reference-case structure. It neither runs statistical algorithms nor approves
mathematics.
