# Daten, Analyseabläufe und Ausgabe

[English](../en/WORKFLOWS.md)

Diese Verträge leiten M3 und spätere Arbeit. Heute sind sie keine implementierten
Schemata. Der M1-Kern verarbeitet unmittelbar numerische Beobachtungen.

## Variablen und Daten

Jede Variable erhält stabile ID, Namen, Label, physischen Typ, sinnvolles
Messniveau (nominal/ordinal/metrisch), optionale Einheit und Wertelabels.
Das Messniveau unterstützt Voraussetzungsprüfungen, erzwingt aber keine automatische
Testwahl. Kategorien, Zeichenketten und Datum/Zeit brauchen ausdrückliche Kodierung.
Numerische Kategoriecodes sind nicht automatisch Messwerte.

Fehlend ist ein eigener Zustand neben gespeicherten Zahlenwerten. Tabellenadapter
übersetzen deklarierte Fehlwertlabels/-masken in die vereinbarte Kernregel.
Unendlichkeit ist ungültig, nicht fehlend. Fehlende Beobachtungen niemals durch null
ersetzen. Ausschlüsse nennen Quellzeilen, Grund, Regel und Wirkung auf die Analyse.

Filter und abgeleitete Variablen ergeben einen neuen logischen Snapshot oder eine
Sicht und erhalten die Quelle. Gruppenreihenfolge, Faktorkontraste und Referenzstufen
sind ausdrücklich. Verbinden/Umformen erfordert Zeilen-/Schlüsselprüfung.
Importeinstellungen nennen Kodierung, Trennzeichen, Kopfzeile, Dezimalzeichen,
Anführungszeichen, Typzuordnung und Fehlwerttokens; Locale darf Werte nicht heimlich verändern.

## Analyserezept

Ein vorgeschlagenes versioniertes Rezept enthält:

- Rezept-/Schema- und Verfahrens-/Vertragsversionen.
- Unveränderliche Datenidentität oder vom Aufrufer gelieferte Inhaltsidentität mit Vertrauensstufe.
- Variablen, Zeilenauswahl, Gruppen und Transformationen in Ausführungsreihenfolge.
- Fehlwert-/Gewichtsregel, Modellformel/Kontraste und Methodenoptionen.
- Alternativhypothese, Konfidenzniveau und ggf. Familie der Mehrfachtests.
- Zufallsalgorithmus/-version, Seed/Zustand und ggf. Streameinstellungen.
- Sprach-/Paket-/Math-Versionen und relevante Ausführungskonfiguration.

Die Anwendung bestimmt Speicherung und Datenhashing. Rezepte enthalten
standardmäßig keine privaten Daten. Geänderte Daten erhalten eine neue Identität;
Cacheausgabe darf nicht als neuer Lauf erscheinen. Abbruch liefert einen eigenen
Status und veröffentlicht Teilausgabe nicht als abgeschlossene Analyse.

## Strukturierte Ergebnisse

| Bestandteil | Inhalt | Darstellungsverantwortung |
| --- | --- | --- |
| Schätzwerte | Typisierte Zahlen, Einheiten, Unsicherheit und Verfügbarkeit | Rundung und Übersetzung |
| Tabellen | Spaltenschema, stabile Zeilen-/Spalten-IDs, Zahlenzellen, Labels | Layout, Sortierung, Exportgestaltung |
| Diagnostik | Statuscodes, Annahmen, Warnungen, Konvergenz/Rang | Erklärung und Schweregrad |
| Diagrammspezifikation | Zahlenreihen, Rollen, Achsen/Einheiten, Transformationen | Grafik und Bearbeitung |
| Herkunft | Rezept-/Daten-/Verfahrens-/Abhängigkeitsidentität, Ausführungsnachweis | Historie und Berichtsmetadaten |

Inferenz nennt Effekt und Unsicherheit zusammen mit Teststatistik und p-Wert.
Ausgaben erklären, welche Annahmen geprüft, vom Aufrufer zugesichert oder ungeprüft
sind. Ein p-Wert ist nicht die Wahrscheinlichkeit einer wahren Nullhypothese.
Automatische Schlussfolgerungen dürfen Designannahmen und Mehrfachvergleiche nicht verbergen.

Adapter können später JSON/CSV/HTML exportieren. Text/HTML wird maskiert;
Tabellenexporte benötigen eine Regel für formelähnliche Zeichenketten.
Dateischreiben, Berechtigungen und Exportziele bestimmt die Anwendung.

## Erste durchgehende Abnahme

Eine eigene numerische CSV wird mit ausdrücklichen Einstellungen importiert.
Eine Variable enthält einen deklarierten Fehlwert. Ein Filter bestimmt die
Analysezeilen; Kennzahlen enthalten passende Anzahlen und Diagnostik.
Die Anwendung speichert das Rezept, exportiert Rohzahlen/Metadaten und wiederholt
den Lauf auf demselben Snapshot. Ergebnisse erfüllen die Toleranz; die Quelle bleibt unverändert.

Dies ist ein M3-Abnahmeziel, heute kein ausführbares Beispiel.
