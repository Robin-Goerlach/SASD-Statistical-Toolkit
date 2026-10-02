# Math dependency and readiness gate

[Deutsch](../de/MATH-DEPENDENCY.md)

**Policy: Math first, statistical implementation second.** Documentation,
contracts and reference-case preparation may proceed now. Each language must
satisfy the relevant capability gate before statistical code is introduced.
Completion of every future Math feature is not required; the selected statistical
milestone requires a defined, stable and validated subset.

## Observed upstream baseline

Inspected on 2026-10-02:
[Robin-Goerlach/SASD-Math-Toolkit at e4eb8e4](https://github.com/Robin-Goerlach/SASD-Math-Toolkit/tree/e4eb8e4fb63803af060569b305daece87c9cfe7a).
Its README describes a C#/.NET 10 foundation and a 1.0.0 release baseline,
including QR, SVD, Cholesky, dense/sparse solvers and least squares.
The inspected tree contains src/dotnet, not a C++ implementation.

This is inventory evidence, **not** a local build/test, package availability
check or approval to start this project. No Math dependency is pinned here yet.
The project's readiness record remains pending for both languages.

## Capability requests

| Key | Math responsibility | Needed by | Current integration state |
| --- | --- | --- | --- |
| MATH-BASE | Versioned package/build, floating-point and error conventions | M1 descriptive pilot | Pending evidence and binding choice |
| MATH-SUM | Reusable stable summation primitives if pilot design needs them | M1 centered summaries | Request/review; do not invent upstream API names |
| MATH-SPECIAL | log-gamma, incomplete gamma/beta, erf/erfc or equivalent approved primitives | M2 distributions and tails | Capability audit required |
| MATH-ROOT | Bracketed monotone inversion with explicit stopping diagnostics | M2 selected quantiles | Match existing solvers to required contract |
| MATH-QR | Rank-aware full-rank least squares and residual diagnostics | M4 linear models | Described upstream for C#; integration pending |
| MATH-SVD | Explicit rank/conditioning and approved deficient-rank policy | M4 diagnostics; later model expansion | Described upstream for C#; integration pending |
| MATH-EIGEN | Symmetric eigensystems with accuracy diagnostics | M5 PCA/multivariate | Capability-specific validation required |
| MATH-OPT | Generic constrained/unconstrained optimization as required | M5 GLM/nonlinear/advanced models | Request only after selected-model contract |
| MATH-RNG | General PRNG if adopted as cross-toolkit numerical infrastructure | M5 simulation | Ownership/algorithm decision still open |

Not every row is required for M1. If it needs no additional reusable summation
primitive, record that justification; the statistical centered accumulator still
belongs here. Do not move estimators into Math merely to satisfy a dependency.

## Per-language gate record

Before coding a milestone, record:

1. Language, milestone and required capability keys.
2. Exact Math package version or source commit and license; never floating main.
3. Public API mapping, numeric types, matrix layout and error/status mapping.
4. Upstream validation evidence plus a reproducible local build/import/integration smoke.
5. Unresolved accuracy or capability gaps and their upstream resolution.
6. Maintainer approval date and reference; update the procedure matrix accordingly.

| Language | Milestone | Pinned dependency | Local evidence | Gate |
| --- | --- | --- | --- | --- |
| C#/.NET | M1 | Not selected | Not run | Pending |
| C++ | M1 | Not available/selected in this baseline | Not run | Pending |

A ready C# gate does not approve C++. C++ needs a suitable Math implementation
first, or an explicitly approved alternative dependency architecture documented
in a new ADR. Do not silently introduce a native bridge or copy C# numerical code
into the statistical tree.
