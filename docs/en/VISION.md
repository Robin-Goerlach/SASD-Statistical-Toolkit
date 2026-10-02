# Vision and scope

[Deutsch](../de/VISION.md)

## Purpose

Provide an open, reusable statistical engine that can support a comprehensive
interactive analysis environment without tying calculations to one application.
Researchers, engineers, analysts, educators and application developers should be
able to ask an analytical question, prepare the relevant data, run an explicit
procedure, inspect assumptions and diagnostics, and reproduce the result.

The intended breadth includes both general statistical analysis and engineering
statistics. Numerical correctness and explainability take precedence over the
number of menu items. A library function and an interactive analysis should use
the same statistical contract.

## Product responsibilities

This repository owns the statistical libraries, shared analysis contracts,
reference cases, and reusable procedure/workflow/result services. A consuming
workbench owns its windows, data editor, menus, project browser and report viewer.
An initial GUI implementation is not selected by this baseline.

A future workbench can expose:

- A data view plus a variable view for types, units, value labels and missingness.
- Guided procedure selection with explicit variables, groups and options.
- An output tree of tables, diagnostics and plots, with rerunnable analysis recipes.
- Batch execution and reproducible report export using the same services.

Desktop packaging, collaboration servers, cloud storage and user accounts are
separate application concerns. They do not become dependencies of the engine.

## Representative workflows

| User question | Required workflow | Evidence in the output |
| --- | --- | --- |
| What does this measurement series look like? | Import/validate, select variable, summarize, inspect histogram/ECDF | Units, counts, exclusions, quantile convention, plot data |
| Do two groups differ? | Define independent/paired design, inspect data, choose approved test | Effect estimate, interval, statistic, df where applicable, p-value, assumptions |
| Which variables explain an outcome? | Build design matrix, fit model, inspect residuals and rank | Formula/encoding, coefficients, uncertainty, fit and influence diagnostics |
| Is a process stable and capable? | Order observations, define subgroups/specification limits, assess stability | Chart rules, violations, capability assumptions and uncertainty |
| Can another person reproduce this? | Save immutable data identity and complete analysis recipe; rerun | Procedure/version, dependencies, options, seed, transformations and status |

These are target workflows, not runnable examples today. The first pilot is a
small numerical summary service that establishes correctness before these flows.

## Success criteria

- Every delivered procedure has defined semantics and independent acceptance evidence.
- Results identify excluded observations and unmet prerequisites.
- Applications can consume typed results without parsing formatted text.
- Both language implementations conform to the same approved contracts.
- Data preparation and analysis are recorded rather than hidden in UI state.
- Broad future scope does not bypass the Math dependency gate or overload release 1.

## Initial exclusions

The first release does not attempt all advanced procedure families, automatic
method selection, a full data editor, foreign command-language compatibility or
binary project-format compatibility. These require independent designs and gates.
No interface should imply those features are already available.
