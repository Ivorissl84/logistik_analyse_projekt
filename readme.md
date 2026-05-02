# Logistik Analyse Projekt  
Datenanalyse eines fiktiven Lagers mit Beständen, Wareneingängen, Warenausgängen und Umlagerungen

## 📦 Projektüberblick  
Dieses Projekt bildet ein vollständiges, realitätsnahes Lagerumfeld ab und zeigt, wie ein Data Analyst logistische Daten strukturiert analysiert, KPIs berechnet und Engpässe identifiziert.

Das Projekt umfasst:

- 100 Artikel  
- 1.000 Wareneingänge  
- 1.500 Warenausgänge  
- 200 Umlagerungen  
- vollständige KPI‑Berechnung  
- automatische Visualisierungen  
- einen Engpass‑Score zur Priorisierung kritischer Artikel  

Alle Daten sind synthetisch, aber realistisch modelliert.

---

## 📁 Projektstruktur

logistik_analyse_projekt/
│
├── main.py                     # Hauptpipeline
│
├── data/                       # CSV-Daten
│   ├── bestaende.csv
│   ├── wareneingang.csv
│   ├── warenausgang.csv
│   └── umlagerungen.csv
│
├── plots/                      # Automatisch erzeugte Diagramme
│
├── src/
│   ├── data_loading.py         # Daten laden & vorbereiten
│   ├── kpi_berechnung.py       # KPI-Berechnung
│   ├── engpass_score.py        # Engpass-Score & Top-Artikel
│   └── visualisierung.py       # Diagramme erzeugen & speichern
│
└── eda/
    ├── data_understanding.py   # Struktur- & Plausibilitätschecks
    └── explorative_analyse.py  # Explorative Analysen

---

## 🗂️ Datensätze

### bestaende.csv
- Artikelnummer  
- Bestand  

### wareneingang.csv
- Datum  
- Artikel  
- Menge  
- Lieferant  
- Lieferschein  

### warenausgang.csv
- Datum  
- Artikel  
- Menge  
- Grund  
- Belegnummer  

### umlagerungen.csv
- Datum  
- Artikel  
- Menge  
- Von‑Platz  
- Nach‑Platz  
- Grund  

---

## 🎯 Ziel des Projekts

Dieses Projekt zeigt typische Aufgaben eines Data Analysts im Logistikumfeld:

- Verständnis von Materialflüssen  
- Berechnung zentraler Lager‑KPIs  
- Identifikation kritischer Artikel  
- Engpass‑Erkennung  
- Visualisierung von Bestands‑ und Bewegungsdaten  
- Entwicklung eines eigenen Engpass‑Scores  
- Aufbau einer reproduzierbaren Analyse‑Pipeline  

---

## 📈 Berechnete KPIs

### Durchschnittsbestand
Durchschnitt der monatlichen Endbestände.

### Lagerumschlag
Jahresverbrauch geteilt durch Durchschnittsbestand.

### Lagerdauer
Durchschnittsbestand geteilt durch Tagesverbrauch.

---

## 🚨 Engpass‑Score (USP des Projekts)

Ein eigens entwickelter Score zur Priorisierung kritischer Artikel:

Engpass‑Score = Lagerumschlag / (Durchschnittsbestand + 1)

Interpretation:

- Hoher Score → kritisch  
- Niedriger Score → unkritisch  
- +1 verhindert Division durch 0  

Damit lassen sich Engpässe frühzeitig erkennen.

---

## 📉 Visualisierungen

Automatisch erzeugte Diagramme:

- Top‑Artikel nach Lagerumschlag  
- Top‑Artikel nach Durchschnittsbestand  
- Artikel mit niedrigster Lagerdauer  
- Top‑Artikel nach Engpass‑Score  

Alle Diagramme werden im Ordner `plots/` gespeichert.

---

## 🔧 Technische Umsetzung

### Hauptpipeline (main.py)
1. Daten laden  
2. KPIs berechnen  
3. Engpass‑Score berechnen  
4. Top‑Artikel ausgeben  
5. Diagramme erzeugen  

### Technologien
- Python 3  
- pandas  
- seaborn  
- matplotlib  

---

## ▶️ Ausführung

Im Projektverzeichnis:

python main.py

Die Diagramme erscheinen anschließend im Ordner `plots/`.

---

## 🧠 Was dieses Projekt zeigt

- Fähigkeit zur strukturierten Datenanalyse  
- Verständnis logistischer KPIs  
- Entwicklung eigener Metriken (Engpass‑Score)  
- saubere Code‑Struktur & Modularisierung  
- Visualisierung & Storytelling mit Daten  
- realistische End‑to‑End‑Pipeline  

---

## 👤 Autor

Jan‑Ivo  Oelfke
Logistik‑Profi auf dem Weg zum Data Analyst
