# SASD Statistical Toolkit

**Reusable statistics for C++ and C#, built on SASD Math Toolkit.**

[Deutsch](README.de.md) · [Documentation](docs/en/README.md) · [Roadmap](docs/en/ROADMAP.md) · [Contributing](CONTRIBUTING.md)

SASD Statistical Toolkit is planned as the statistical engine for a broad analysis environment: data preparation, exploratory analysis, probability distributions, inference, statistical modelling, simulation, quality analysis and reproducible reporting. Applications can combine these capabilities into an interactive statistical workbench while also using the engine from libraries, scripts and batch jobs.

**Current state: documentation foundation. No statistical library, executable application or installable package exists here yet.** All capabilities below are planned. The repository currently provides contracts, architecture, acceptance criteria, a procedure catalog and separate homes for future C++ and C# implementations.

## Foundation first

[SASD Math Toolkit](https://github.com/Robin-Goerlach/SASD-Math-Toolkit) supplies the numerical foundation. Before implementation starts in either language, its required Math capabilities must pass the readiness gate in [MATH-DEPENDENCY.md](docs/en/MATH-DEPENDENCY.md). Missing generic numerical functions are developed there first; this project does not grow a competing linear algebra or special functions library.

The statistical layer owns estimators, inference, model diagnostics and statistical meaning. A numerical least-squares solution becomes a statistical regression only when the statistical layer adds assumptions, degrees of freedom, uncertainty and diagnostics.

## Planned capability families

| Family | Scope |
| --- | --- |
| Data and preparation | Variable metadata, missing values, filters, groups, transformations, import adapters |
| Exploration | Descriptive summaries, quantiles, frequency tables, empirical distributions, plot specifications |
| Probability and inference | Distributions, confidence intervals, parametric and rank tests, multiplicity |
| Models | Linear models, ANOVA/ANCOVA, generalized linear and nonlinear models |
| Extended analysis | Multivariate analysis, time series, survival, reliability, experimental design |
| Simulation and quality | Sampling, resampling, Monte Carlo, control charts and capability studies |
| Results and workflows | Typed results, analysis recipes, provenance, report/export adapters |

The [feature catalog](docs/en/FEATURE-CATALOG.md) separates initial scope from later expansion. It does not promise that every family will be delivered in the first release.

## Repository map

| Location | Responsibility |
| --- | --- |
| [docs/en](docs/en/README.md), [docs/de](docs/de/README.md) | English default and German planning documentation |
| [spec](spec/README.md) | Shared mathematical contracts, procedure IDs and numerical conventions |
| [conformance](conformance/README.md) | Language-independent reference cases and provenance |
| [src/cpp](src/cpp/README.md), [src/dotnet](src/dotnet/README.md) | Separate future implementations |
| [tests](tests/README.md), [samples](samples/README.md) | Separate future test runners and runnable examples |
| [docs/implementations](docs/implementations/README.md) | Language-specific documentation and handbook outlines |
| [tools](tools/README.md) | Documentation validation only |

C++ and C# share behavior and reference cases, not a mandatory runtime bridge. Their APIs can follow their language conventions. UI frameworks, file formats and report renderers remain outside the statistical computation core.

## Start here

1. Read the [vision](docs/en/VISION.md) and [architecture](docs/en/ARCHITECTURE.md).
2. Review the [requirements](docs/en/REQUIREMENTS.md) and [statistical conventions](spec/CONVENTIONS.md).
3. Complete the Math dependency gate before selecting an implementation milestone.
4. Specify and validate the small descriptive-statistics pilot before expanding.

For the current documentation check, run from the repository root:

```bash
python3 tools/check_docs.py
```

This validates repository structure and documentation consistency; it does not validate statistical algorithms. Build and test commands for C++/.NET will be added with their actual projects.

## License

[MIT](LICENSE), as established when this repository was created.
