# Logistik Analyse Projekt  
Datenanalyse eines Produktionslagers mit Beständen, Wareneingängen, Warenausgängen und Umlagerungen

## 🧩 Problemstellung

Das Produktionslager eines mittelständischen Maschinenbauunternehmens hat wiederholt Schwierigkeiten mit Materialverfügbarkeit und unklaren Bestandsbewegungen. Einzelne Artikel laufen unerwartet knapp, während andere über Monate ungenutzt liegen. Die Produktionsplanung meldet regelmäßig Verzögerungen, weil kritische Teile nicht rechtzeitig verfügbar sind.

Ziel der Analyse ist es:

- Transparenz über Bestände, Ein‑ und Ausgänge sowie Umlagerungen zu schaffen  
- zentrale Lager‑KPIs zu berechnen (Durchschnittsbestand, Lagerumschlag, Lagerdauer)  
- Artikel zu identifizieren, die ein erhöhtes Engpassrisiko haben  
- Muster und Auffälligkeiten im Materialfluss sichtbar zu machen  
- eine Grundlage für bessere Dispositions‑ und Produktionsentscheidungen zu schaffen  

---

## 📦 Projektüberblick  
Dieses Projekt bildet ein vollständiges, realitätsnahes Produktionslager ab und zeigt, wie ein Data Analyst logistische Daten strukturiert analysiert, KPIs berechnet und Engpässe identifiziert.

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

## 📊 Analyse & Erkenntnisse

Bei der Analyse der Bestands‑ und Bewegungsdaten habe ich zuerst geprüft, wie sich die Artikel über das Jahr hinweg verhalten. Dabei ist mir aufgefallen, dass es deutliche Unterschiede zwischen den Artikeln gibt: Einige haben einen sehr hohen Verbrauch und gleichzeitig relativ niedrige Bestände, während andere kaum bewegt werden.

Über die KPI‑Berechnung konnte ich das genauer einordnen:

- **Der Lagerumschlag** zeigt, welche Artikel regelmäßig verbraucht werden.  
- **Der Durchschnittsbestand** zeigt, wie viel Material im Schnitt vorgehalten wird.  
- **Die Lagerdauer** macht sichtbar, wie lange ein Artikel im Lager liegt, bevor er verbraucht wird.

Durch die Kombination dieser KPIs konnte ich Artikel identifizieren, die ein erhöhtes Engpassrisiko haben. Das sind vor allem Artikel mit:

- hohem Verbrauch  
- gleichzeitig niedrigen Beständen  
- und kurzer Lagerdauer  

Um diese Artikel besser priorisieren zu können, habe ich einen **Engpass‑Score** entwickelt. Der Score hilft dabei, kritische Artikel schnell zu erkennen, ohne jede KPI einzeln betrachten zu müssen.

Insgesamt zeigt die Analyse:

- Es gibt mehrere Artikel, die regelmäßig an die Grenze der Verfügbarkeit kommen.  
- Einige Warengruppen haben deutlich höhere Bewegungsraten als andere.  
- Umlagerungen finden überwiegend bei Artikeln statt, die ohnehin kritisch sind — was auf organisatorische Engpässe hindeutet.  
- Die Bestandsverteilung ist nicht optimal: Manche Artikel liegen lange, andere sind zu knapp disponiert.

Daraus lassen sich konkrete Maßnahmen ableiten:

- Sicherheitsbestände für kritische Artikel anpassen  
- Dispositionsparameter überprüfen  
- Umlagerungsprozesse standardisieren  
- Artikel mit sehr langer Lagerdauer gezielt abbauen  

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

Jan‑Ivo Oelfke
Logistik‑Profi auf dem Weg zum Data Analyst
