# Architecture decision register

[Deutsch](../de/DECISIONS.md)

Baseline: 2026-10-02. Established decisions reflect the repository request.
Proposals require review before implementation; they are not hidden approvals.

| ID | Status | Decision and reason | Consequence |
| --- | --- | --- | --- |
| ADR-001 | Established | Independent statistics repository on SASD Math Toolkit | Separate lifecycle; Math readiness gates precede code |
| ADR-002 | Established | Separate C++ and C# implementations and language documentation | Shared behavior/reference cases; no mandatory runtime bridge |
| ADR-003 | Established | Documentation-first initialization | No dummy algorithms or build projects; current CI checks docs only |
| ADR-004 | Established | Preserve existing MIT license | No license migration implied by another toolkit's choices |
| ADR-005 | Proposed | Keep UI in consuming workbench applications | Reusable engine; GUI framework and existing-workbench relationship remain open |
| ADR-006 | Proposed | English canonical, German paired documentation | Stable IDs/options shared; simultaneous semantic updates |
| ADR-007 | Proposed | Explicit options, typed results and provenance | No silent missingness/weight policy; versioned procedure semantics |
| ADR-008 | Proposed | Binary64 pilot, native APIs per language | Numeric agreement within tolerances; no universal bitwise guarantee |
| ADR-009 | Proposed | C++20 and .NET 10 as candidate targets | Freeze actual toolchains only with each first implementation and Math pin |
| ADR-010 | Proposed | Small unweighted descriptive pilot before broad expansion | Refine numerical/result conventions with independent evidence |

## Questions to resolve at their gates

- Which Math capability/version/package is suitable for the first language?
- Which common numerical primitives still need upstream work?
- Which full-rank regression API and rank tolerance fit the statistical contract?
- Which PRNG algorithm and ownership support simulation and cross-language streams?
- Which data-provider interface allows adapters without a compulsory data framework?
- Which quantile/weight/contrast definitions are included in initial public APIs?
- Which UI host and report renderer consume the eventual workflow services?

Open questions do not block unrelated documentation work. Resolve only those
that affect the chosen milestone before its implementation.

## Updating decisions

Keep IDs stable. Record status, date, context, alternatives, final decision and
consequences in an expanded ADR when a proposal is adopted or superseded.
Do not rewrite history to imply earlier implementation approval.
