# Working in this repository

## Current phase

Documentation foundation only. No statistical implementation, CMake project,
.NET solution, package or desktop application exists yet. Do not invent build
commands or report planned features as implemented.

## Read before changing

- README.md and docs/en/README.md
- docs/en/ARCHITECTURE.md and docs/en/DECISIONS.md
- docs/en/MATH-DEPENDENCY.md and docs/en/ROADMAP.md
- spec/CONVENTIONS.md and the affected procedure contract

## Boundaries

- SASD Math Toolkit is a prerequisite. Implement generic numerical foundations
  there first. The readiness gate is per capability and per language.
- Keep C++ and C# source, tests, examples and handbooks separate.
- Share mathematical specifications and independently sourced reference cases.
- No UI, import, storage, network, console output or report rendering in the
  statistical computation core.
- No compulsory dependency on a future Data Toolkit or GUI toolkit.
- Use independently written code, documentation and examples. Record source
  provenance and license requirements for every external asset or dependency.

## Editing

- English is the canonical documentation language. Update paired German pages
  with the same IDs, status, decisions and acceptance criteria in the same change.
- Preserve LICENSE unless the owner explicitly requests a license change.
- Stable ST-*, AC-*, STAT-* and ADR-* identifiers must not be renumbered.
- Distinguish planned, specified, implemented and validated capabilities.
- For future code, explain assumptions and numerical choices with /// XML
  documentation in C# and /** */ Doxygen comments in C++; use // for local intent.
- Avoid placeholder APIs or fake projects merely to fill reserved directories.

## Verification now

From the repository root:

    python3 tools/check_docs.py

Review mathematical definitions and translations manually. This checker does not
prove numerical correctness or semantic translation equivalence.

## Verification when code is introduced

The first implementation change must add real language-specific build/test
commands, CI and dependency pins. Every procedure needs an approved contract,
hand-computable cases, independent references, boundary tests and tolerances.
Never regenerate expected results using the implementation under test.

## Completion report

Report changed behavior/documents, checks actually run, dependency readiness and
remaining gaps. Do not claim statistical tests passed during this documentation
phase.
