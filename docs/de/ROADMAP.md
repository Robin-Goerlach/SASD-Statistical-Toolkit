# Roadmap und Abschlussbedingungen

[English](../en/ROADMAP.md)

Zukünftige Meilensteine erhalten keine Termine oder Fertigstellungsbehauptungen.
Die Umsetzung erfolgt je Sprache; gemeinsame Spezifikationsprüfung darf vorher stattfinden.

| Meilenstein | Eintritt | Ergebnis | Abschlussprüfung |
| --- | --- | --- | --- |
| M0 — Dokumentationsgrundlage | Repository vorhanden | Zielbild, Anforderungen, Konventionen, Katalog, Abhängigkeitstore, zweisprachige Struktur | Dokumentationsprüfung bestanden; Maintainer prüft Umfang und Konventionsentwürfe |
| M1 — Kennzahlenpilot | M0 geprüft; MATH-BASE und benötigte Pilotfähigkeiten für Sprache freigegeben | Ungewichtete Kennzahlen, Kovarianz/Pearson; echte Build-/Test-CI und Sprachhandbuch | Freigegebene Verträge; manuelle/unabhängige Fälle bestanden; keine instabile Rohsummenvarianz; Paket-Smoke |
| M2 — Wahrscheinlichkeit/Inferenz | M1 validiert; benötigte Spezialfunktions-/Inversionstore bestanden | Ausgewählte Verteilungen und einfache Mittelwertintervalle/-tests | Direkte obere/logarithmische Wahrscheinlichkeiten, Alternativen/Freiheitsgrade, extreme/Grenzfälle geprüft |
| M3 — Analyseabläufe | M1 validiert; Daten-/Rezeptschema freigegeben | Metadaten, Masken, Filter/Gruppen, CSV-Adapter, Verfahrensregister, strukturierte Ausgabe, Stapelrezepte | Quelle unverändert; Ausschlüsse stimmen; Rezept wiederholbar; Tabellen-/Diagrammdaten ohne Renderer |
| M4 — Statistische Modelle | M2 und QR-/Rang-/Konditionsanbindung freigegeben | Einfache/mehrfache Regression mit vollem Rang, einfaktorielle ANOVA, Residuen/Inferenz | Unabhängige Modellfälle; Rangdefizit ausdrücklich behandelt; Koeffizienten/Freiheitsgrade/Residuen geprüft |
| M5 — gezielter Ausbau | Benötigte frühere Freigaben und neue Verträge | Gewählte B-/C-Familien aus dem Katalog | Jede Familie bekommt eigene Forschungs-, Abhängigkeits- und numerische Abnahme |
| R1 — erstes nutzbares Bibliotheksrelease | Gewählte M1–M4-Fähigkeiten für beworbene Sprachen validiert | Versionierte Bibliotheken, Beispiele, EN/DE-Handbücher, Abhängigkeits-/Funktionsmatrix | Build/Installation/Ausführung auf sauberem System; Numerik-, Vertrags- und Dokumentationsaudit |

M2 und M3 müssen nicht nacheinander erfolgen. M4 braucht keine GUI und kein
fertiges Datenframework, sobald Numerik und Verträge bereit sind. R1 verlangt
nicht sämtliche M5-Familien, beide Sprachen gleichzeitig oder eine Desktopanwendung.

## M0-Stand bei Anlage

Dokumente und Verzeichnisse sind in dieser Grundlage vorhanden. Mathematische
Freigabe, Math-Integration und Implementierungsabnahmen bleiben offen.
Erfolgreiche Dokumentations-CI bestätigt Struktur, keine Produktreife.

## Nächster konkreter Schritt

spec/CONVENTIONS.md und spec/DESCRIPTIVE-STATISTICS.md prüfen, anschließend den
M1-Abhängigkeitsnachweis für die gewählte Sprache in MATH-DEPENDENCY.md ausfüllen.
Benötigte Math-Lücken vor Statistikcode im Grundlagenprojekt beheben.

## Arbeitspaket je Verfahren

Frage/Annahmen → Vertrag → Math-Bereitschaft → unabhängige Fälle → Implementierung
→ numerische Prüfung → Handbuch/Beispiele → Validierungsstatus.

Nicht den gesamten Katalog gleichzeitig beginnen. Eine kleine nachweisbar korrekte
Familie voranbringen und damit die gemeinsamen Konventionen verbessern.
