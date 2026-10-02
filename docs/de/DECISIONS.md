# Architekturentscheidungen

[English](../en/DECISIONS.md)

Grundlage: 02.10.2026. Feststehende Entscheidungen entsprechen dem Repositoryauftrag.
Vorschläge brauchen vor Implementierung Prüfung und sind keine verdeckte Freigabe.

| Kennung | Status | Entscheidung und Grund | Folge |
| --- | --- | --- | --- |
| ADR-001 | Feststehend | Eigenes Statistikrepository auf SASD Math Toolkit | Eigener Lebenszyklus; Math-Freigaben vor Code |
| ADR-002 | Feststehend | C++-/C#-Implementierungen und Sprachdokumentation getrennt | Gemeinsames Verhalten/Referenzen; keine Pflichtbrücke |
| ADR-003 | Feststehend | Initialisierung mit Dokumentation | Keine Scheinverfahren/-Builds; aktuelle CI prüft nur Dokumentation |
| ADR-004 | Feststehend | Vorhandene MIT-Lizenz erhalten | Keine implizite Lizenzübernahme aus anderen Toolkits |
| ADR-005 | Vorschlag | UI in nutzenden Workbench-Anwendungen belassen | Wiederverwendbarer Kern; GUI und Beziehung zu bestehenden Workbenches offen |
| ADR-006 | Vorschlag | Englisch maßgeblich, Deutsch gepaart | Gemeinsame IDs/Optionen; gleichzeitige inhaltliche Pflege |
| ADR-007 | Vorschlag | Ausdrückliche Optionen, typisierte Ergebnisse und Herkunft | Keine stillen Fehlwert-/Gewichtsregeln; versionierte Verfahren |
| ADR-008 | Vorschlag | Binary64-Pilot, sprachübliche APIs | Numerische Toleranzübereinstimmung; keine allgemeine Bitgarantie |
| ADR-009 | Vorschlag | C++20 und .NET 10 als mögliche Ziele | Toolchains erst mit erster Implementierung und Math-Fixierung verbindlich |
| ADR-010 | Vorschlag | Kleiner ungewichteter Kennzahlenpilot vor breitem Ausbau | Numerik-/Ergebnisregeln mit unabhängigen Nachweisen erproben |

## Fragen an den jeweiligen Freigabetoren

- Welche Math-Fähigkeiten/-Version/-Pakete passen zur ersten Sprache?
- Welche allgemeinen numerischen Bausteine müssen vorher in Math entstehen?
- Welche Regressions-API und Rangtoleranz passen zum statistischen Vertrag?
- Welcher PRNG und welche Zuständigkeit ermöglichen Simulation/sprachübergreifende Streams?
- Welche Datenanbieter-Schnittstelle ermöglicht Adapter ohne Pflichtframework?
- Welche Quantil-/Gewichts-/Kontrastdefinitionen gehören zur ersten öffentlichen API?
- Welche UI-Anwendung und Berichtsrenderer verwenden später die Ablaufdienste?

Offene Fragen blockieren keine unabhängige Dokumentationsarbeit. Vor Umsetzung
nur die Fragen verbindlich lösen, die den gewählten Meilenstein betreffen.

## Pflege

Kennungen erhalten. Bei Annahme/Ablösung eines Vorschlags Status, Datum, Kontext,
Alternativen, Entscheidung und Folgen in einer ausführlichen ADR festhalten.
Historie nicht so umschreiben, dass frühere Implementierungsfreigabe suggeriert wird.
