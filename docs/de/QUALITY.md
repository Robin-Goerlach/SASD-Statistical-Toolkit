# Numerische Qualität und Release-Nachweise

[English](../en/QUALITY.md)

## Nachweisebenen

| Ebene | Erforderlicher Nachweis | Beispiel |
| --- | --- | --- |
| Mathematik | Definition, Domäne, Annahmen und Herleitung | Varianznenner und Mindestumfang |
| Manuell | Kleine eigene Datensätze mit exakten/rationalen Ergebnissen | [1,2,3,4,5]: Mittelwert 3, Stichprobenvarianz 5/2 |
| Unabhängig | Zertifizierte Daten oder fixierte Referenzimplementierung mit Optionen | NIST-Kennzahlen; Werkzeug/Version und Befehl festgehalten |
| Grenzen | Leer/einzeln/konstant/fehlend/ungültig/extrem | Große Grundwerte bei geringer Streuung |
| Eigenschaften | Mathematische Beziehungen mit begründeter Toleranz | Translationsinvarianz der Varianz; Symmetrie der Kovarianz |
| Integration | Echter Sprachbuild, Abhängigkeit und Paketnutzung | Saubere Installation und In-Memory-Kennzahl |
| Anwendung | Daten-, Rezept-, Ergebnis-/Exportkonsistenz | Ausgeschlossene Zeilen bleiben im Ergebnis nachvollziehbar |

Eigenschaftsprüfungen ergänzen unabhängige Fälle. C++-/C#-Übereinstimmung allein
ist kein unabhängiger Nachweis: Beide können denselben Denkfehler enthalten.

## Numerische Regeln

- Zentrierte geprüfte Momentenverfahren verwenden; keine Subtraktion großer Rohquadratsummen.
- Über-/Unterlauf und Skalierung prüfen. Endliche Eingaben können Zwischenwerte überfordern.
- Kleine obere Wahrscheinlichkeiten direkt berechnen; nicht ausschließlich 1 minus gerundete CDF.
- Allgemeine lineare Modelle mit QR/rangbewussten Methoden statt Normalgleichungen lösen.
- Schätzwerte, Standardfehler, Intervalle und numerische Diagnostik unterscheiden.
- Instabile Wahrscheinlichkeiten/Korrelationen nicht stillschweigend beschneiden; Nichtkonvergenz nicht als Erfolg ausgeben.

Verträge wählen Methode und Genauigkeitsziel vor Freigabe. Ein allgemeines
Epsilon genügt nicht. Vergleich: abs(Ergebnis-Referenz) <= atol +
rtol*abs(Referenz), mit je Ausgabe begründeten Einheiten und Skalen.
Wahrscheinlichkeiten nahe null benötigen ggf. logarithmische oder relative
Kriterien; Quantile zusätzlich Wahrscheinlichkeitsresiduen. Anzahlen/Status sind exakt.

## Referenzregister

Am 02.10.2026 als Quellen geprüfte Primärreferenzen:

- [NIST Statistical Reference Datasets](https://itl.nist.gov/div898/strd/):
  zertifizierte Referenzen für Kennzahlen, ANOVA und Regression.
- [NIST-Hintergrund zu univariaten Daten](https://www.itl.nist.gov/div898/strd/univ/backgroundinfo.html):
  beschreibt den Referenzumfang der Kennzahlen.
- [R-Stichprobenquantile](https://www.stat.ethz.ch/R-manual/R-devel/library/stats/html/quantile.html):
  alternative Quantildefinitionen.
- [R-Normalverteilung](https://www.stat.math.ethz.ch/R-manual/R-devel/library/stats/html/Normal.html):
  ausdrückliche Verteilungsseiten und logarithmische Wahrscheinlichkeiten.

Dies sind Quellenlinks, keine übernommenen Datensätze oder bereits ausgeführten
Vergleiche. Veränderliche Dokumentationsseiten fixieren keine Referenzlaufzeit.
Vor Übernahme eines Falls Quelle/Version, Abrufdatum, Lizenz/Weitergabeprüfung,
zertifizierte Genauigkeit, Transformationen und Ergebnisableitung festhalten.

## Reproduzierbarkeitsstufen

1. Semantisch: dasselbe freigegebene Verfahren, Optionen und Datenverständnis.
2. Numerisch: Übereinstimmung innerhalb begründeter Vertragstoleranzen.
3. Bitweise: identische Bits für erklärte Plattform, Toolchain und Ausführung.

Sprachübergreifend ist Stufe 2 das Standardziel. Stufe 3 benötigt ausdrückliche
Festlegung von Reduktionsreihenfolge, Mathematikbibliotheken, PRNG und parallelen
Streams. Ein Seed allein garantiert keine identischen sprachübergreifenden Zufallsfolgen.

## Release-Freigabe

Kein Verfahren wird vor Abschluss von Vertrag, Math-Freigabe, unabhängigen und
Grenzfällen, Sprachtests, Beispielen und EN/DE-Handbuch veröffentlicht.
Toolchains/Plattformen und Abhängigkeiten exakt festhalten. Prüfungslücken und
bekannte numerische Grenzen nennen. Optimierungen müssen dieselben Nachweise erhalten.

Dokumentations-CI prüft interne Links, gepaarte Planungskennungen, Kataloge und
Referenzfallstruktur. Sie führt keine Statistikverfahren aus und erteilt keine
mathematische Freigabe.
