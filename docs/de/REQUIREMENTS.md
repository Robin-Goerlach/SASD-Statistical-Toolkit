# Anforderungen und Abnahme

[English](../en/REQUIREMENTS.md)

MUSS gilt bei Auslieferung der betreffenden Fähigkeit. SOLL verlangt bei
Zurückstellung eine dokumentierte Begründung. Alle folgenden Implementierungsabnahmen
sind **offen**. M0-Dokumentationsprüfungen ersetzen keine numerische Abnahme.

| Kennung | Stufe | Anforderung | Abnahme |
| --- | --- | --- | --- |
| ST-001 | MUSS | Freigegebene Math-Abhängigkeiten nutzen; allgemeine Numerik nicht doppeln | AC-001: fixierte Abhängigkeit, Fähigkeitsnachweise und Integrations-Smoke je Sprache bestanden |
| ST-002 | MUSS | Statistik unabhängig von UI, Dateien und Netzwerk halten | AC-002: Abhängigkeitsprüfung und In-Memory-Aufruf ohne Anwendungsinfrastruktur |
| ST-003 | MUSS | Für jedes öffentliche Verfahren einen versionierten mathematischen Vertrag erstellen | AC-003: Eingaben, Domäne, Formeln, Annahmen, Fehler, Methode und Toleranzen geprüft |
| ST-004 | MUSS | Fehlwertregeln und Beobachtungsanzahlen offenlegen | AC-004: Ablehnungs-/Ausschlussfälle prüfen Eingabe-, verwendete und ausgeschlossene Anzahl |
| ST-005 | MUSS | Ungültige Eingabe, undefinierte Statistik und numerischen Fehler unterscheiden | AC-005: Grenzfälle prüfen maschinenlesbaren Status und fehlende Schätzwerte |
| ST-006 | MUSS | Typisierte, strukturierte Ergebnisse liefern | AC-006: Tabellen/Diagnostik verwenden Rohwerte; Rundung verändert keine Berechnung |
| ST-007 | MUSS | Analyseoptionen und Herkunft vollständig erhalten | AC-007: Wiederholung eines gespeicherten Rezepts erfüllt seine Reproduzierbarkeitsstufe |
| ST-008 | MUSS | Jedes Verfahren unabhängig validieren | AC-008: manuelle, Grenz- und unabhängige Referenzfälle bestehen dokumentierte Toleranzen |
| ST-009 | MUSS | C++ und C# getrennt und fachlich konform halten | AC-009: jede ausgelieferte Sprache führt gemeinsame Fälle aus; Matrix nennt Unterschiede |
| ST-010 | MUSS | Inferenzannahmen und diagnostische Grenzen nennen | AC-010: freigegebene Test-/Modellfälle enthalten Annahmen, ggf. Freiheitsgrade und Warnungen |
| ST-011 | MUSS | Verteilungsseiten, Konfidenzniveau, Alternativen und Mehrfachtests bestimmen | AC-011: extreme Randwahrscheinlichkeiten, Alternativen sowie korrigierte/unkorrigierte Kennzeichnung geprüft |
| ST-012 | MUSS | Gewichte, Faktorkodierung und Gruppierung vor Unterstützung festlegen | AC-012: nicht unterstützte Gewichte abgelehnt; unterstützte Semantik mit Referenzfällen geprüft |
| ST-013 | SOLL | Wiederholbare Simulation und Resampling ermöglichen | AC-013: Generator-ID, Seed/Zustand, Streamregel und Methodenversion reproduzieren Fälle |
| ST-014 | SOLL | Wiederverwendbare Tabellen-/Diagramm-/Berichtsadapter bereitstellen | AC-014: Export enthält Metadaten/Diagnostik; Rechenkern ohne Rendererabhängigkeit |
| ST-015 | MUSS | Jedes ausgelieferte Verfahren zweisprachig dokumentieren | AC-015: C++-/C#-Beispiele, Grenzen und EN/DE-Handbücher entsprechen ausgeliefertem Verhalten |
| ST-016 | SOLL | Zeit/Speicher vor Optimierungen messen | AC-016: Arbeitslast, Plattform, Ausgangswerte und Genauigkeitseinfluss dokumentiert |
| ST-017 | MUSS | Datenintegrität durch ausdrückliche Vorbereitungsschritte sichern | AC-017: Quellsnapshot unverändert, Rezept deterministisch, Ausschlüsse nachvollziehbar |
| ST-018 | MUSS | Verträge kompatibel und Paketabhängigkeiten ausdrücklich halten | AC-018: Release-Matrix verbindet Vertrag, Paket, Math-Version und Kompatibilitätsänderungen |

## Abnahmeumfang des ersten Piloten

M1 umfasst ST-001 bis ST-009, ST-015 und ST-018 für eine In-Memory-Kennzahlen-API.
ST-007 hält bei direkten Aufrufen Verfahren, Optionen und Abhängigkeiten fest;
die vollständige Rezeptausführung folgt in M3. ST-010/ST-011 beginnen mit Inferenz.
ST-012 wird zunächst durch ausdrückliche Ablehnung nicht unterstützter Gewichte
erfüllt. ST-017 beginnt mit Daten-/Ablaufadaptern.

Für Anzahl, Mittelwert, Varianz, Standardabweichung, Kovarianz und Korrelation
bestimmen [Pilotvertrag](../../spec/DESCRIPTIVE-STATISTICS.md) und
[Referenzfälle](../../conformance/descriptive-cases.json) die Prüfungen.
Weitere Verfahren bleiben Katalogeinträge bis zur Vertragsfreigabe.

## Nachverfolgbarkeit

Jeder Implementierungs-PR nennt Anforderungs- und Verfahrenskennungen,
Vertragsversion, Math-Nachweise, Testfälle und Handbuchanpassungen. Die Abnahme
erfolgt je Verfahren und Sprache. Ein Einzelbeispiel oder eine erfolgreiche
Dokumentationsprüfung genügt nicht.
