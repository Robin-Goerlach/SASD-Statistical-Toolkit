# Contributing

[English documentation](docs/en/README.md) · [Deutsche Dokumentation](docs/de/README.md)

The project currently accepts specification and documentation work. Statistical
implementation starts only after the relevant Math dependency gate is satisfied.

1. Choose a requirement or procedure ID. Describe the intended outcome.
2. Check architecture decisions and required Math capabilities.
3. Specify inputs, formulas, assumptions, errors, numerical method and tolerances.
4. Add independently derived reference cases with provenance.
5. Implement within one language tree once its gate is approved.
6. Update tests, examples, procedure status and the matching handbook.

Use feature/*, fix/* or docs/* branches for normal changes and open a pull request
with the relevant IDs, actual verification and known gaps. Keep changes small
enough for mathematical and code review. The initial repository setup is a
documentation baseline, not a released statistical product.

English is the default. Paired German planning documents must carry the same
meaning, IDs and scope. Shared machine-readable contracts use stable English
keys. Language-specific examples and handbooks are maintained separately.

Use original implementations and examples. Record references and license terms;
do not add copied manuals, source listings, proprietary assets or private data.
Contributions use the existing MIT license.

Aktuell stehen Spezifikation und Dokumentation im Vordergrund. Statistikcode
beginnt erst nach Freigabe der benötigten Math-Funktionen für die jeweilige
Sprache. Änderungen sollen Kennungen, überprüfbare Ergebnisse und offene Punkte
angeben. Englische und deutsche Planungsdokumente werden gemeinsam gepflegt;
sprachspezifische Implementierungen und Handbücher bleiben getrennt.
