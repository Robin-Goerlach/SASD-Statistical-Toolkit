# SASD Statistical Toolkit

**Wiederverwendbare Statistik für C++ und C#, auf Grundlage des SASD Math Toolkit.**

[English](README.md) · [Dokumentation](docs/de/README.md) · [Roadmap](docs/de/ROADMAP.md) · [Mitwirken](CONTRIBUTING.md)

Das SASD Statistical Toolkit ist als Statistikmotor für eine umfassende Analyseumgebung geplant: Datenaufbereitung, explorative Analyse, Wahrscheinlichkeitsverteilungen, Inferenz, statistische Modelle, Simulation, Qualitätsanalyse und reproduzierbare Berichte. Anwendungen können daraus eine interaktive Statistik-Workbench aufbauen und den Rechenkern zugleich als Bibliothek, aus Skripten oder in Stapelverarbeitung verwenden.

**Aktueller Stand: Dokumentationsgrundlage. Hier existieren noch keine Statistikbibliothek, ausführbare Anwendung oder installierbaren Pakete.** Alle folgenden Fähigkeiten sind geplant. Das Repository enthält derzeit Verträge, Architektur, Abnahmekriterien, einen Verfahrenskatalog und getrennte Bereiche für spätere C++- und C#-Implementierungen.

## Zuerst die Grundlage

Das [SASD Math Toolkit](https://github.com/Robin-Goerlach/SASD-Math-Toolkit) liefert die numerische Grundlage. Vor Implementierungsbeginn in einer Sprache müssen dessen benötigte Fähigkeiten das Freigabetor in [MATH-DEPENDENCY.md](docs/de/MATH-DEPENDENCY.md) bestehen. Fehlende allgemeine numerische Funktionen entstehen zuerst dort; dieses Projekt baut keine konkurrierende lineare Algebra oder Bibliothek spezieller Funktionen auf.

Die Statistikschicht verantwortet Schätzer, Inferenz, Modelldiagnostik und statistische Bedeutung. Eine numerische Least-Squares-Lösung wird erst durch Annahmen, Freiheitsgrade, Unsicherheit und Diagnostik zu einer statistischen Regression.

## Geplante Funktionsbereiche

| Bereich | Umfang |
| --- | --- |
| Daten und Vorbereitung | Variablenmetadaten, fehlende Werte, Filter, Gruppen, Transformationen, Importadapter |
| Exploration | Beschreibende Kennzahlen, Quantile, Häufigkeitstabellen, empirische Verteilungen, Diagrammspezifikationen |
| Wahrscheinlichkeit und Inferenz | Verteilungen, Konfidenzintervalle, parametrische und Rangtests, Mehrfachtests |
| Modelle | Lineare Modelle, ANOVA/ANCOVA, verallgemeinerte lineare und nichtlineare Modelle |
| Erweiterte Analyse | Multivariate Analyse, Zeitreihen, Überlebensanalyse, Reliabilität, Versuchsplanung |
| Simulation und Qualität | Stichproben, Resampling, Monte Carlo, Regelkarten und Fähigkeitsuntersuchungen |
| Ergebnisse und Abläufe | Typisierte Ergebnisse, Analyserezepte, Herkunftsnachweise, Berichts- und Exportadapter |

Der [Funktionskatalog](docs/de/FEATURE-CATALOG.md) trennt den Einstieg vom späteren Ausbau. Er verspricht keine vollständige Umsetzung aller Bereiche im ersten Release.

## Struktur

| Ort | Verantwortung |
| --- | --- |
| [docs/en](docs/en/README.md), [docs/de](docs/de/README.md) | Englische Standarddokumentation und deutsche Planungsdokumentation |
| [spec](spec/README.md) | Gemeinsame mathematische Verträge, Verfahrenskennungen und numerische Konventionen |
| [conformance](conformance/README.md) | Sprachunabhängige Referenzfälle und Herkunftsnachweise |
| [src/cpp](src/cpp/README.md), [src/dotnet](src/dotnet/README.md) | Getrennte spätere Implementierungen |
| [tests](tests/README.md), [samples](samples/README.md) | Getrennte spätere Testausführung und ausführbare Beispiele |
| [docs/implementations](docs/implementations/README.md) | Sprachspezifische Dokumentation und Handbuchgliederungen |
| [tools](tools/README.md) | Ausschließlich Dokumentationsprüfung |

C++ und C# teilen Verhalten und Referenzfälle, ohne verpflichtende Laufzeitbrücke. Ihre APIs dürfen den jeweiligen Sprachkonventionen folgen. Oberflächen, Dateiformate und Berichtsrenderer bleiben außerhalb des Statistik-Rechenkerns.

## Einstieg

1. [Zielbild](docs/de/VISION.md) und [Architektur](docs/de/ARCHITECTURE.md) lesen.
2. [Anforderungen](docs/de/REQUIREMENTS.md) und [statistische Konventionen](spec/CONVENTIONS.md) prüfen.
3. Math-Freigabetor vor Auswahl eines Implementierungsmeilensteins erfüllen.
4. Den kleinen Pilot für beschreibende Statistik spezifizieren und prüfen, bevor der Ausbau beginnt.

Aktuelle Dokumentationsprüfung, vom Repository-Hauptverzeichnis aus:

```bash
python3 tools/check_docs.py
```

Sie prüft Struktur und Dokumentationskonsistenz, keine statistischen Algorithmen. C++/.NET-Build- und Testbefehle werden erst mit den tatsächlichen Projekten ergänzt.

## Lizenz

[MIT](LICENSE), entsprechend der bei Anlage des Repositorys gewählten Lizenz.
