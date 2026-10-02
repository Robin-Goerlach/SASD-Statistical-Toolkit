# Roadmap and completion gates

[Deutsch](../de/ROADMAP.md)

No dates or implementation-completion claims are attached to future milestones.
Execution is per language; shared specification review can precede code.

| Milestone | Entry | Deliverable | Completion check |
| --- | --- | --- | --- |
| M0 — documentation foundation | Repository exists | Vision, requirements, conventions, catalog, dependency gates, bilingual structure | Documentation checker passes; maintainer reviews scope and draft conventions |
| M1 — descriptive pilot | M0 reviewed; MATH-BASE and needed pilot capabilities approved for selected language | Unweighted summary, covariance/Pearson; real build/test CI and language handbook | Approved contracts; manual and independent cases pass; no raw-sum variance shortcut; package smoke |
| M2 — probability/inference | M1 validated; selected special-function/inversion gates pass | Selected distributions and basic mean intervals/tests | Direct tails/log probabilities tested; explicit alternatives/df; independent extreme/boundary cases |
| M3 — analysis workflows | M1 validated; data/recipe schema approved | Metadata, masks, filters/groups, CSV adapter, procedure registry, structured output, batch recipe | Source preserved; exclusions reconciled; a saved recipe reruns; renderer-independent table/plot data |
| M4 — statistical modelling | M2 plus approved QR/rank/conditioning integration | Simple/full-rank multiple regression, one-way ANOVA, residual and inferential diagnostics | Independent model cases; rank-deficient input handled explicitly; coefficient/df/residual checks |
| M5 — targeted expansion | Specific prior gates and new procedure contracts | Selected B/C families from the catalog | Each family receives its own research, dependency and numerical acceptance record |
| R1 — first useful library release | Selected M1–M4 capabilities validated for advertised languages | Versioned libraries, examples, EN/DE handbooks, dependency/feature matrix | Clean-machine build/install/run; audit of numerical evidence, contract compatibility and documentation |

M2 and M3 need not be serial. M4 can start without a GUI or a completed data
framework once its numerical dependencies and contracts are ready. R1 does not
require every M5 family, both languages at once, or a desktop application.

## M0 status at initialization

Documents and directories are provided in this baseline. Mathematical approval,
Math integration and implementation acceptance remain pending. A successful
documentation CI run means documentation structure passed, not product readiness.

## First next step

Review spec/CONVENTIONS.md and spec/DESCRIPTIVE-STATISTICS.md, then complete the
M1 dependency record for the chosen language in MATH-DEPENDENCY.md. Resolve any
required Math gap upstream before starting statistical code.

## Work package for each procedure

Question and assumptions → contract → Math readiness → independent cases →
implementation → numerical review → handbook/examples → validation status.

Do not start the entire catalog in parallel. Advance one small, demonstrably
correct family and use it to refine the shared conventions.
