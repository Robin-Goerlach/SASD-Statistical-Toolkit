# Funktionskatalog

[English](../en/FEATURE-CATALOG.md)

Alle Einträge sind geplant. Priorität A beschreibt den Einstieg; B erweitert die
nutzbare Analyseplattform; C benötigt gesonderte Forschung und Freigabe. Priorität
ist kein Implementierungsstatus. Der genaue Verfahrensstand liegt in
[procedures.json](../../spec/procedures.json).

| Bereich | A — Grundlage/erste Releases | B — späterer Ausbau | C — gesonderter Entwurf |
| --- | --- | --- | --- |
| Datenaufbereitung | Zahlenvektoren, Metadatenverträge, Fehlwertmasken; später CSV, Filter/Gruppen | Rekodierung, abgeleitete Variablen, Verbinden/Umformen, Tabellenadapter | Große/nicht vollständig im Speicher gehaltene Daten, fremde Binärformate |
| Beschreibende Statistik | Anzahlen, Extrema, Mittelwert, Stichproben-/Populationsvarianz, SD, Kovarianz, Pearson-Korrelation | Quantile, Häufigkeiten, Histogramm, ECDF, robuste Kennzahlen | Gewichtete Quantile, Streaming-Näherungen |
| Wahrscheinlichkeit | Normal-, t-, Chi-Quadrat-, F-, Binomial-, Poissonverteilung nach Abhängigkeiten | Beta, Gamma, Exponential, Lognormal und weitere freigegebene Familien | Mischungen und besondere Verteilungen |
| Inferenz | Mittelwertintervalle, Ein-Stichproben-/Welch-/gepaarte t-Tests, ausdrückliche Alternativen | Rangtests, Anteiltests, Kontingenztests, Mehrfachtestkorrekturen | Exakte/bedingte Designs und komplexe Stichproben |
| Regression | Einfache/mehrfache lineare Modelle mit vollem Rang, Residuen und Inferenz | Faktorkontraste, Modellvergleich, Vorhersageintervalle, GLM | Regularisierte/gemischte Modelle, anspruchsvolle nichtlineare Anpassung |
| Gruppenvergleich | Einfaktorielle ANOVA nach Verteilungs-/Modellfreigabe | ANCOVA, faktorielle ANOVA, Post-hoc-Vergleiche | Wiederholte Messungen und hierarchische Designs |
| Multivariate Verfahren | — | PCA, Cluster-, Diskriminanz-/Faktorenanalyse nach Spezifikation | Multivariate Inferenz und Strukturgleichungsmodelle |
| Zeitreihen | — | ACF/PACF, Zerlegung, einfache Prognosen | ARIMA/Zustandsraum und unregelmäßige Reihen |
| Überlebensanalyse/Reliabilität | — | Kaplan–Meier, Sterbetafeln, Log-Rank, Reliabilitätskennzahlen | Cox-/parametrische Überlebens- und Reliabilitätsmodelle |
| Simulation | — | Ausdrücklicher PRNG, Stichproben, Bootstrap und Permutation | Reproduzierbare parallele Streams, anspruchsvolles Monte Carlo |
| Ingenieurqualität | — | Regelkarten, Prozessfähigkeit mit Stabilitätsprüfung | Messsystemanalyse, Annahmestichproben, Zuverlässigkeitspläne |
| Versuchsplanung | — | Einfache faktorielle Pläne mit Analysebezug | Wirkungsflächen, optimale und sequenzielle Pläne |
| Ausgabe | Typisierte Ergebnisse/Diagnostik; später Tabellen-/Diagrammspezifikation | HTML-/CSV-/JSON-Berichtsadapter | Dokumentexport und Anwendungslayout |
| Abläufe | Optionen/Herkunft; später versionierte Rezepte | Verfahrensregister, Stapelausführung, wiederholbare Historie | Fremde Syntax und Plugin-Ausführung |

## Release-Grenze

Der erste Pilot umfasst **ausschließlich** ungewichtete Kennzahlen, Kovarianz und
Pearson-Korrelation für Zahlendaten. Exakte Quantile, Verteilungen, Inferenz,
Modelle, Tabellenimport und GUI-Abläufe folgen später.

Ein erstes praktisch nutzbares Bibliotheksrelease kann den validierten Pilot,
ausgewählte Verteilungen, einfache Inferenz und lineare Modelle mit vollem Rang
kombinieren. Sein veröffentlichter Umfang wird anhand tatsächlich ausgelieferter
Fähigkeiten je Sprache am Freigabetor bestimmt. Es wird nicht als vollständige
Analyseumgebung bezeichnet.

## Verfahrenslebenszyklus

Erfasst → Entwurf → freigegeben → implementiert → validiert → veröffentlicht.

Freigabe ist eine dokumentierte Maintainerentscheidung nach mathematischer und
numerischer Prüfung. Implementierung ist keine Validierung. Fähigkeiten werden
nur für Sprachen beworben, die das entsprechende Freigabetor bestanden haben.
Langfristige Sprachparität rechtfertigt keine Behauptung zweier fertiger Pakete.

## GUI-Horizont

Eine spätere Workbench kann Daten-/Variableneditor, Verfahrensdialoge,
Ergebnisbaum, Diagrammbearbeitung und Berichtsexport verbinden. Dieses Repository
liefert zuerst dafür benötigte Dienste und Verträge. GUI-Framework und Beziehung
zu vorhandenen SASD-Workbench-Projekten sind offen (ADR-005).
