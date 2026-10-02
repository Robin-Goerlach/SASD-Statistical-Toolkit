# Shared conformance evidence

[Descriptive contract](../spec/DESCRIPTIVE-STATISTICS.md) · [Quality policy](../docs/en/QUALITY.md)

descriptive-cases.json contains original hand-derived pilot examples and boundary
cases. It is a fixture format for future C++ and C# runners, **not an executable
statistical test suite**. Current documentation CI checks its structure.

JSON cannot store IEEE NaN/infinity. The input tokens "NaN", "+Infinity" and
"-Infinity" mean those exact numeric values when decoded by a future runner.
They must not be parsed using locale-dependent numeric rules. Other strings
are invalid fixture input.

An expected null means an unavailable estimate, never zero. expected fields are
required assertions; unspecified additional diagnostics may be returned.
expected_metric_status supplies per-metric availability categories.
Numerical comparisons use each case's atol/rtol or the file default. Zero results
in constant cases are exact as required by the contract. Counts/status are exact.
If a native API throws, the runner maps the exception to the shared input error
category rather than treating the case as a computation failure.

Before validation, add independent reference cases with source, version, settings,
certified precision and redistribution evidence. Keep manual cases alongside them.
Never derive expected values from the implementation being tested.

Die JSON-Fälle sind gemeinsame Referenzdaten, keine heute laufenden Statistiktests.
Null bedeutet nicht verfügbar. NaN-/Unendlich-Tokens werden von den späteren
Sprachtests ausdrücklich dekodiert. Unabhängige Referenzen sind vor Validierung
zu ergänzen; die Handfälle ersetzen diese Nachweise nicht.
