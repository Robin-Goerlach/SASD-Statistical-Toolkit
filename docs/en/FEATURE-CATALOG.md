# Capability catalog

[Deutsch](../de/FEATURE-CATALOG.md)

All entries are planned. Priority A is the initial sequence; B extends the usable
analysis platform; C needs separate research and approval. A priority does not
indicate implementation status. Exact procedure status is in [procedures.json](../../spec/procedures.json).

| Family | A — foundation/first releases | B — subsequent expansion | C — separately designed |
| --- | --- | --- | --- |
| Data preparation | Numeric vectors, metadata contracts, missing masks; later CSV, filters/groups | Recode, derive variables, joins/reshape, spreadsheet adapters | Large/out-of-core data, external binary formats |
| Descriptive statistics | Counts, extrema, mean, sample/population variance, SD, covariance, Pearson correlation | Quantiles, frequency tables, histogram, ECDF, robust summaries | Weighted quantiles, streaming approximations |
| Probability | Normal, Student t, chi-square, F, binomial, Poisson in dependency order | Beta, gamma, exponential, lognormal and other approved families | Mixtures and specialized distributions |
| Inference | Mean intervals, one-sample/Welch/paired t tests, explicit alternatives | Rank tests, proportion tests, contingency tests, multiplicity corrections | Exact/conditional designs and complex surveys |
| Regression | Simple/full-rank multiple linear models, residuals and inference | Factor contrasts, model comparison, prediction intervals, GLM | Penalized/mixed models and advanced nonlinear fitting |
| Group comparisons | One-way ANOVA after distribution/model gates | ANCOVA, factorial ANOVA, post-hoc comparisons | Repeated measures and hierarchical designs |
| Multivariate | — | PCA, clustering, discriminant/factor analysis after specifications | Multivariate inference and structural equation modelling |
| Time series | — | ACF/PACF, decomposition, forecasting baselines | ARIMA/state-space and irregular-series models |
| Survival/reliability | — | Kaplan–Meier, life tables, log-rank, reliability summaries | Cox/parametric survival and reliability models |
| Simulation | — | Explicit PRNG, sampling, bootstrap and permutation methods | Parallel stream reproducibility and advanced Monte Carlo |
| Engineering quality | — | Control charts, process capability with stability checks | Measurement systems, acceptance sampling, reliability plans |
| Experimental design | — | Basic factorial designs and design-analysis links | Response surfaces, optimal and sequential designs |
| Output | Typed results and diagnostics; later table/plot specifications | Reusable HTML/CSV/JSON report adapters | Rich document exporters and application layout systems |
| Workflow | Explicit options/provenance; later versioned recipes | Procedure registry, batch runner, rerunnable analysis history | Foreign syntax compatibility and plugin execution |

## Release boundary

The first pilot is **only** unweighted descriptive summaries plus covariance and
Pearson correlation for numeric observations. Exact quantiles, distributions,
inference, model fitting, table import and GUI flows are later milestones.

The first useful library release can combine the validated pilot, selected
distributions, basic inference and full-rank linear models. Its exact advertised
scope is decided at the release gate, using delivered capabilities per language.
It must not be described as a complete analysis suite.

## Procedure lifecycle

catalogued → draft → approved → implemented → validated → released.

Approval is a recorded maintainer decision after mathematical/numerical review.
Implementation alone does not establish validation. A feature is advertised only
for the languages that reached the corresponding gate; language parity is a
long-term requirement, not an excuse to falsely claim two working packages.

## GUI integration horizon

A future workbench can combine a data editor, variable editor, procedure dialogs,
output tree, plot editing and report export. This repository first supplies the
services and contracts needed by those screens. UI framework selection and the
relationship to any existing SASD workbench are still open (ADR-005).
