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

Das Lager verwendet ein strukturiertes 6‑stelliges Lagerplatzsystem (Gang–Regal–Ebene), z. B. A10302.

Alle Daten sind synthetisch, aber realistisch modelliert.

## 📁 Projektstruktur

logistik_analyse_projekt/  
│  
├── main.py                     – Hauptpipeline  
│  
├── data/                       – CSV‑Daten  
│   ├── bestaende.csv  
│   ├── wareneingang.csv  
│   ├── warenausgang.csv  
│   └── umlagerungen.csv  
│  
├── plots/                      – Automatisch erzeugte Diagramme  
│  
├── src/  
│   ├── data_loading.py         – Daten laden & vorbereiten  
│   ├── kpi_berechnung.py       – KPI‑Berechnung  
│   ├── engpass_score.py        – Engpass‑Score & Top‑Artikel  
│   ├── umlagerungen_analyse.py – Analyse der Umlagerungen  
│   └── visualisierung.py       – Diagramme erzeugen & speichern  
│  
└── eda/  
    ├── data_understanding.py   – Struktur‑ & Plausibilitätschecks  
    └── explorative_analyse.py  – Explorative Analysen  

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
- Von‑Platz (6‑stelliger Lagerplatzcode: Gang–Regal–Ebene, z. B. A10302)  
- Nach‑Platz (6‑stelliger Lagerplatzcode: Gang–Regal–Ebene, z. B. B21504)  
- Grund  

## 📊 Analyse & Erkenntnisse

Bei der Analyse der Bestands‑ und Bewegungsdaten habe ich zuerst geprüft, wie sich die Artikel über das Jahr hinweg verhalten. Dabei ist mir aufgefallen, dass es deutliche Unterschiede zwischen den Artikeln gibt: Einige haben einen sehr hohen Verbrauch und gleichzeitig relativ niedrige Bestände, während andere kaum bewegt werden.

Über die KPI‑Berechnung konnte ich das genauer einordnen:

- Lagerumschlag zeigt, welche Artikel regelmäßig verbraucht werden.  
- Durchschnittsbestand zeigt, wie viel Material im Schnitt vorgehalten wird.  
- Lagerdauer zeigt, wie lange ein Artikel im Lager liegt, bevor er verbraucht wird.

Durch die Kombination dieser KPIs konnte ich Artikel identifizieren, die ein erhöhtes Engpassrisiko haben – vor allem Artikel mit:

- hohem Verbrauch  
- niedrigen Beständen  
- kurzer Lagerdauer  

Der entwickelte Engpass‑Score hilft, kritische Artikel schnell zu erkennen.

Insgesamt zeigt die Analyse:

- Mehrere Artikel kommen regelmäßig an die Grenze der Verfügbarkeit.  
- Einige Warengruppen haben deutlich höhere Bewegungsraten als andere.  
- Die Bestandsverteilung ist nicht optimal.  

## 🔄 Analyse der Umlagerungen

Die Umlagerungsdaten zeigen, wie häufig Artikel innerhalb des Lagers den Platz wechseln und welche Gründe dafür angegeben wurden.

Das Lager verwendet ein strukturiertes 6‑stelliges Lagerplatzsystem (Gang–Regal–Ebene), z. B.:

- A10302  
- B21504  
- C11201  

Auffällig war:

- Umlagerungen konzentrieren sich auf wenige Artikel  
- Viele Umlagerungen betreffen ohnehin kritische Artikel  
- Häufige Gründe:
  - Kapazitätsausgleich  
  - Kommissionierunterstützung  
  - Qualitätsprüfung  
  - Fehlplatzierungen  

Daraus folgt:

- Artikel mit vielen Umlagerungen sollten hinsichtlich Lagerplatz & Disposition überprüft werden  
- Häufige Umlagerungen erhöhen das Risiko operativer Verzögerungen  
- Eine bessere Platzstrategie könnte Umlagerungen reduzieren  

## 📈 Berechnete KPIs

### Durchschnittsbestand  
Durchschnitt der monatlichen Endbestände.

### Lagerumschlag  
Jahresverbrauch geteilt durch Durchschnittsbestand.

### Lagerdauer  
Durchschnittsbestand geteilt durch Tagesverbrauch.

## 🚨 Engpass‑Score (USP des Projekts)

Engpass‑Score = Lagerumschlag / (Durchschnittsbestand + 1)

Interpretation:

- hoher Score → kritisch  
- niedriger Score → unkritisch  
- +1 verhindert Division durch 0  

## 📉 Visualisierungen

Automatisch erzeugte Diagramme:

- Top‑Artikel nach Lagerumschlag  
- Top‑Artikel nach Durchschnittsbestand  
- Artikel mit niedrigster Lagerdauer  
- Top‑Artikel nach Engpass‑Score  
- Top‑Artikel nach Anzahl Umlagerungen  
- Häufigste Umlagerungsgründe  

Alle Diagramme werden im Ordner plots/ gespeichert.

## 🔧 Technische Umsetzung

### Hauptpipeline (main.py)
1. Daten laden  
2. KPIs berechnen  
3. Engpass‑Score berechnen  
4. Top‑Artikel ausgeben  
5. Umlagerungen analysieren  
6. Diagramme erzeugen  

### Technologien
- Python 3  
- pandas  
- seaborn  
- matplotlib  

## ▶️ Ausführung

Im Projektverzeichnis:

python main.py

## 🧠 Was dieses Projekt zeigt

- strukturierte Datenanalyse  
- Verständnis logistischer KPIs  
- Entwicklung eigener Metriken  
- Analyse organisatorischer Engpässe  
- saubere Code‑Struktur  
- Visualisierung & Storytelling  

## 👤 Autor

Jan‑Ivo Oelfke  
Fachkraft für Lagerlogistik auf dem Weg zum Data/Prozess Analyst
