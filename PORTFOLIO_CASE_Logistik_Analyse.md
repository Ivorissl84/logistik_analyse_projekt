# Logistik Analyse – Portfolio Case  
Optimierung eines Produktionslagers durch datengetriebene Bestands‑ und Prozessanalyse

## 🎯 Projektziel

Dieses Projekt zeigt, wie ich als angehender Data Analyst ein reales logistisches Problem strukturiert analysiere und daraus konkrete Handlungsempfehlungen ableite.  
Im Fokus steht ein Produktionslager, das regelmäßig mit Materialengpässen, unklaren Bestandsbewegungen und ineffizienten Umlagerungen zu kämpfen hat.

Mein Ziel war es, durch Datenanalyse:

- Transparenz über Bestände und Materialflüsse zu schaffen  
- Engpassrisiken frühzeitig sichtbar zu machen  
- KPIs zu entwickeln, die Disposition & Planung unterstützen  
- organisatorische Schwachstellen im Lagerprozess aufzudecken  
- datenbasierte Entscheidungen zu ermöglichen  

---

## 🏭 Ausgangssituation

Das Lager eines Maschinenbauunternehmens meldet:

- wiederkehrende Fehlteile  
- verspätete Produktionsaufträge  
- unklare Bestandsabweichungen  
- häufige Umlagerungen ohne klare Ursache  

Die Herausforderung:  
**Viele Daten existieren – aber niemand nutzt sie.**

Genau hier setzt meine Analyse an.

---

## 🔍 Vorgehensweise & Methodik

Ich habe das Projekt wie ein echter Analyst aufgebaut:

### 1. **Daten verstehen & bereinigen**
- Prüfung der Datenqualität  
- Erkennen von Ausreißern, Dubletten und fehlenden Werten  
- Harmonisierung von Artikelnummern und Lagerplatzcodes  
- Strukturierung der Bewegungsdaten (Ein‑, Ausgänge, Umlagerungen)

### 2. **KPI‑Modell entwickeln**
Ich habe drei zentrale Lager‑KPIs berechnet:

- **Durchschnittsbestand**  
- **Lagerumschlag**  
- **Lagerdauer**

Diese KPIs bilden die Grundlage für jede Bestandsoptimierung.

### 3. **Engpass‑Score entwickeln (USP des Projekts)**
Um kritische Artikel schnell zu erkennen, habe ich einen eigenen Score entwickelt:

**Engpass‑Score = Lagerumschlag / (Durchschnittsbestand + 1)**

Damit lassen sich Artikel priorisieren, die:
- viel verbraucht werden  
- wenig Bestand haben  
- schnell ausgehen  

### 4. **Umlagerungsanalyse**
Besonders spannend:  
Viele Umlagerungen betrafen Artikel, die ohnehin kritisch waren.

Ich habe analysiert:

- welche Artikel am häufigsten umgelagert werden  
- welche Gründe angegeben wurden  
- welche Lagerplätze besonders „auffällig“ sind  
- ob Umlagerungen Engpässe verstärken  

### 5. **Visualisierung & Storytelling**
Alle Ergebnisse wurden visualisiert, u. a.:

- Top‑Artikel nach Lagerumschlag  
- Artikel mit niedrigster Lagerdauer  
- Engpass‑Score Ranking  
- Umlagerungs‑Heatmap  
- häufigste Umlagerungsgründe  

---

## 📈 Zentrale Erkenntnisse

### 🔥 1. Kritische Artikel sind klar identifizierbar
Mehrere Artikel laufen regelmäßig an die Verfügbarkeitsgrenze.  
Der Engpass‑Score zeigt diese Artikel sofort.

### 🔥 2. Bestände sind ungleich verteilt
Einige Artikel liegen monatelang ungenutzt, während andere permanent fehlen.

### 🔥 3. Umlagerungen sind ein Frühwarnsignal
Artikel mit vielen Umlagerungen sind oft dieselben, die Engpässe verursachen.

### 🔥 4. Lagerplatzstrategie ist ineffizient
Das 6‑stellige Lagerplatzsystem (Gang–Regal–Ebene) zeigt:
- bestimmte Bereiche sind überlastet  
- andere werden kaum genutzt  

### 🔥 5. Disposition arbeitet ohne datenbasierte Priorisierung
Mit KPIs und Score wäre eine klare Priorisierung möglich.

---

## 💡 Business Impact

Durch die Analyse können folgende Verbesserungen erzielt werden:

- **Reduzierung von Fehlteilen**  
- **Stabilere Produktionsplanung**  
- **Weniger Notfall‑Umlagerungen**  
- **Bessere Bestandsverteilung**  
- **Höhere Transparenz für Disposition & Einkauf**  
- **Schnellere Reaktion auf kritische Artikel**  

Dieses Projekt zeigt, wie Datenanalyse direkt zu operativen Verbesserungen führt.

---

## 🛠️ Eingesetzte Technologien

- Python (pandas, seaborn, matplotlib)  
- Jupyter / PyCharm  
- CSV‑Datenverarbeitung  
- KPI‑Modellierung  
- Explorative Datenanalyse (EDA)  
- Visual Analytics  

---

## 👤 Über mich

Ich bin Jan‑Ivo Oelfke – Fachkraft für Lagerlogistik mit über 10 Jahren Erfahrung und auf dem Weg zum Data Analyst.  
Ich verbinde tiefes Prozesswissen aus der Logistik mit datengetriebenem Denken und moderner Analysekompetenz.

Dieses Projekt zeigt meine Fähigkeit:

- komplexe Daten zu strukturieren  
- KPIs sinnvoll zu modellieren  
- Muster & Risiken zu erkennen  
- datenbasierte Entscheidungen vorzubereiten  
- technische und fachliche Perspektiven zu verbinden
---