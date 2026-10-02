# Math-Abhängigkeit und Freigabetor

[English](../en/MATH-DEPENDENCY.md)

**Grundsatz: zuerst Math, danach Statistikimplementierung.** Dokumentation,
Verträge und Referenzfälle dürfen jetzt entstehen. Jede Sprache muss vor
Statistikcode die benötigten Fähigkeiten freigegeben haben. Nicht sämtliche
zukünftigen Math-Funktionen müssen fertig sein; der gewählte Statistikmeilenstein
benötigt eine definierte, stabile und validierte Teilmenge.

## Beobachteter Ausgangsstand

Geprüft am 02.10.2026:
[Robin-Goerlach/SASD-Math-Toolkit bei e4eb8e4](https://github.com/Robin-Goerlach/SASD-Math-Toolkit/tree/e4eb8e4fb63803af060569b305daece87c9cfe7a).
Die README beschreibt C#/.NET 10 und eine 1.0.0-Release-Grundlage mit QR, SVD,
Cholesky, dichten/dünnbesetzten Lösern und Least Squares. Der geprüfte Baum
enthält src/dotnet, keine C++-Implementierung.

Das ist eine Bestandsaufnahme, **kein** lokaler Build/Test, keine Paketprüfung
und keine Startfreigabe für dieses Projekt. Hier ist noch keine Math-Abhängigkeit
fixiert. Beide Sprachfreigaben bleiben offen.

## Benötigte Fähigkeiten

| Schlüssel | Math-Verantwortung | Benötigt für | Integrationsstand |
| --- | --- | --- | --- |
| MATH-BASE | Versioniertes Paket/Build, Gleitkomma- und Fehlerkonventionen | M1 Kennzahlenpilot | Nachweise und Anbindung offen |
| MATH-SUM | Wiederverwendbare stabile Summation, falls Pilotentwurf sie benötigt | M1 zentrierte Kennzahlen | Anfrage/Prüfung; keine erfundenen upstream APIs |
| MATH-SPECIAL | log-Gamma, unvollständige Gamma/Beta, erf/erfc oder freigegebene Alternative | M2 Verteilungen/Randwahrscheinlichkeiten | Fähigkeitsprüfung erforderlich |
| MATH-ROOT | Geklammerte monotone Inversion mit Abbruchdiagnostik | M2 ausgewählte Quantile | Vorhandene Löser mit Vertrag abgleichen |
| MATH-QR | Rangbewusste Least Squares bei vollem Rang, Residuendiagnostik | M4 lineare Modelle | Für C# upstream beschrieben; Integration offen |
| MATH-SVD | Rang/Kondition und freigegebene Regel bei Rangdefizit | M4 Diagnostik; später Modellausbau | Für C# upstream beschrieben; Integration offen |
| MATH-EIGEN | Symmetrische Eigenwertprobleme mit Genauigkeitsdiagnostik | M5 PCA/multivariat | Fähigkeitsbezogene Validierung erforderlich |
| MATH-OPT | Benötigte allgemeine beschränkte/unbeschränkte Optimierung | M5 GLM/nichtlineare/erweiterte Modelle | Erst nach Modellvertrag anfordern |
| MATH-RNG | Allgemeiner PRNG bei toolkitübergreifender Zuordnung | M5 Simulation | Zuständigkeit/Algorithmus offen |

Nicht jede Zeile ist für M1 erforderlich. Falls kein zusätzlicher allgemeiner
Summationsbaustein gebraucht wird, ist das zu begründen. Der zentrierte Statistik-
Akkumulator gehört trotzdem hierher. Schätzer werden nicht allein wegen der
Abhängigkeit nach Math verschoben.

## Freigabenachweis je Sprache

Vor Implementierung eines Meilensteins festhalten:

1. Sprache, Meilenstein und erforderliche Fähigkeitsschlüssel.
2. Exakte Math-Paketversion oder Quellcommit und Lizenz; kein veränderliches main.
3. API-Zuordnung, Zahlentypen, Matrixanordnung und Fehler-/Statuszuordnung.
4. Upstream-Nachweise und reproduzierbarer lokaler Build-/Import-/Integrations-Smoke.
5. Offene Genauigkeits-/Funktionslücken und ihre Behebung in Math.
6. Maintainerfreigabe mit Datum/Referenz und angepasste Verfahrensmatrix.

| Sprache | Meilenstein | Fixierte Abhängigkeit | Lokaler Nachweis | Freigabe |
| --- | --- | --- | --- | --- |
| C#/.NET | M1 | Nicht gewählt | Nicht ausgeführt | Offen |
| C++ | M1 | In dieser Grundlage nicht verfügbar/gewählt | Nicht ausgeführt | Offen |

C#-Freigabe erteilt keine C++-Freigabe. C++ benötigt zuerst eine passende
Math-Implementierung oder eine ausdrücklich freigegebene alternative Architektur
mit neuer ADR. Keine stillschweigende native Brücke und keine kopierten
C#-Numerikkerne im Statistikbereich.
