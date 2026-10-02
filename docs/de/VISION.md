# Zielbild und Umfang

[English](../en/VISION.md)

## Zweck

Ein offener, wiederverwendbarer Statistikmotor soll eine umfassende interaktive
Analyseumgebung ermöglichen, ohne Berechnungen an eine einzelne Anwendung zu binden.
Forscher, Ingenieure, Analysten, Lehrende und Anwendungsentwickler sollen eine
Fragestellung formulieren, Daten vorbereiten, ein eindeutig bestimmtes Verfahren
ausführen, Annahmen und Diagnostik prüfen und das Ergebnis reproduzieren können.

Das Ziel umfasst allgemeine Statistik und Ingenieurstatistik. Numerische
Korrektheit und Erklärbarkeit haben Vorrang vor der Anzahl der Menüeinträge.
Bibliotheksfunktionen und interaktive Analysen verwenden denselben statistischen Vertrag.

## Produktverantwortung

Dieses Repository verantwortet Statistikbibliotheken, gemeinsame Analyseverträge,
Referenzfälle und wiederverwendbare Dienste für Verfahren, Abläufe und Ergebnisse.
Eine nutzende Workbench verantwortet Fenster, Dateneditor, Menüs, Projektübersicht
und Berichtsanzeige. Diese Grundlage wählt noch keine GUI-Implementierung.

Eine spätere Workbench kann anbieten:

- Daten- und Variablenansicht mit Typen, Einheiten, Wertelabels und fehlenden Werten.
- Geführte Verfahrensauswahl mit ausdrücklicher Variablen-, Gruppen- und Optionswahl.
- Ergebnisbaum mit Tabellen, Diagnostik und Diagrammen sowie erneut ausführbaren Analyserezepten.
- Stapelverarbeitung und reproduzierbaren Berichtsexport über dieselben Dienste.

Desktop-Pakete, Kollaborationsserver, Cloudspeicher und Benutzerkonten bleiben
Aufgaben der Anwendungen und werden keine Abhängigkeiten des Rechenkerns.

## Typische Abläufe

| Fragestellung | Benötigter Ablauf | Nachweis im Ergebnis |
| --- | --- | --- |
| Wie sieht diese Messreihe aus? | Import/Prüfung, Variablenauswahl, Zusammenfassung, Histogramm/ECDF | Einheiten, Anzahlen, Ausschlüsse, Quantilkonvention, Diagrammdaten |
| Unterscheiden sich zwei Gruppen? | Unabhängiges/gepaartes Design bestimmen, Daten prüfen, freigegebenen Test wählen | Effekt, Intervall, Statistik, ggf. Freiheitsgrade, p-Wert, Annahmen |
| Welche Variablen erklären ein Ergebnis? | Designmatrix bilden, Modell anpassen, Residuen und Rang prüfen | Formel/Kodierung, Koeffizienten, Unsicherheit, Anpassungs- und Einflussdiagnostik |
| Ist ein Prozess stabil und fähig? | Beobachtungen ordnen, Untergruppen/Grenzwerte bestimmen, Stabilität prüfen | Regeln, Verletzungen, Fähigkeitsannahmen und Unsicherheit |
| Kann jemand die Analyse wiederholen? | Unveränderliche Datenidentität und vollständiges Rezept speichern; erneut ausführen | Verfahren/Version, Abhängigkeiten, Optionen, Seed, Transformationen und Status |

Dies sind Zielabläufe, heute keine ausführbaren Beispiele. Der erste Pilot
liefert einen kleinen Kennzahlendienst und sichert zunächst die Korrektheit.

## Erfolgskriterien

- Jedes ausgelieferte Verfahren besitzt eindeutige Semantik und unabhängige Abnahmenachweise.
- Ergebnisse nennen ausgeschlossene Beobachtungen und unerfüllte Voraussetzungen.
- Anwendungen nutzen typisierte Ergebnisse, ohne formatierte Texte auszuwerten.
- Beide Sprachimplementierungen erfüllen dieselben freigegebenen Verträge.
- Datenaufbereitung und Analyse werden aufgezeichnet und bleiben nicht in verstecktem UI-Zustand.
- Das breite Ziel umgeht weder das Math-Freigabetor noch überlädt es das erste Release.

## Anfängliche Abgrenzung

Das erste Release umfasst nicht sämtliche anspruchsvollen Verfahren, automatische
Methodenauswahl, einen vollständigen Dateneditor, fremde Kommandosprachen oder
Kompatibilität zu binären Projektformaten. Diese benötigen eigene Entwürfe und
Freigaben. Keine Oberfläche darf ihre heutige Verfügbarkeit suggerieren.
