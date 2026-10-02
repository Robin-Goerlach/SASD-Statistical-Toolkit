# Documentation tools

Run from the repository root with Python 3.10 or newer:

    python3 tools/check_docs.py

Uses only the Python standard library. Checks local Markdown link targets,
paired planning document names and stable IDs, language scaffold presence,
procedure catalog shape/status and descriptive fixture structure.

It does not check external link availability, semantic translation equivalence,
Markdown rendering, statistical mathematics or numerical implementations.
The same check runs in the documentation workflow.
