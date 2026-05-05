import os
import pandas as pd

# ---------------------------------------------------------
# 0. Pfade korrekt setzen
# ---------------------------------------------------------
# BASE_DIR zeigt auf das Projekt-Root, unabhängig vom Startpunkt
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

print("Working directory:", os.getcwd())
print("Data directory:", DATA_DIR)

# ---------------------------------------------------------
# 1. Daten einlesen
# ---------------------------------------------------------
# Rohdaten aus dem data/-Ordner laden
bestaende = pd.read_csv(os.path.join(DATA_DIR, "bestaende.csv"))
wareneingang = pd.read_csv(os.path.join(DATA_DIR, "wareneingang.csv"))
warenausgang = pd.read_csv(os.path.join(DATA_DIR, "warenausgang.csv"))
umlagerungen = pd.read_csv(os.path.join(DATA_DIR, "umlagerungen.csv"))

print("Daten erfolgreich geladen.")

# Alle DataFrames in einem Dictionary sammeln
datasets = {
    "bestaende": bestaende,
    "wareneingang": wareneingang,
    "warenausgang": warenausgang,
    "umlagerungen": umlagerungen,
}

# ---------------------------------------------------------
# 2. Grundchecks
# ---------------------------------------------------------
print("\n--- Grundchecks ---")

# Basisinformationen zu jeder Tabelle ausgeben
for name, df in datasets.items():
    print(f"\n### {name} ###")
    print("Form:", df.shape)
    print("Datentypen:")
    print(df.dtypes)
    print("Null-Werte:")
    print(df.isnull().sum())
    print("Erste 5 Zeilen:")
    print(df.head())

# ---------------------------------------------------------
# 3. Plausibilitätschecks
# ---------------------------------------------------------
print("\n--- Plausibilitätschecks ---")

# Datumsbereiche prüfen
for name, df in datasets.items():
    if "datum" in df.columns:
        print(f"\n{name}: Datumsbereich")
        print("Min:", df["datum"].min())
        print("Max:", df["datum"].max())

# Mengen prüfen (negative oder Null-Mengen)
for name, df in datasets.items():
    if "menge" in df.columns:
        print(f"\n{name}: Mengenprüfung")
        print("Negative Mengen:", (df["menge"] < 0).sum())
        print("Null-Mengen:", (df["menge"] == 0).sum())

# Umlagerungen prüfen (von_platz != nach_platz)
if "von_platz" in umlagerungen.columns:
    print("\nUmlagerungen: von != nach")
    print("Fehlerhafte Zeilen:", (umlagerungen["von_platz"] == umlagerungen["nach_platz"]).sum())

# ---------------------------------------------------------
# 4. Verknüpfungschecks
# ---------------------------------------------------------
print("\n--- Verknüpfungschecks ---")

# Artikelmengen pro Tabelle bestimmen
artikel_bestaende = set(bestaende["artikel"])
artikel_we = set(wareneingang["artikel"])
artikel_wa = set(warenausgang["artikel"])
artikel_um = set(umlagerungen["artikel"])

print("\nArtikel pro Tabelle:")
print("bestaende:", len(artikel_bestaende))
print("wareneingang:", len(artikel_we))
print("warenausgang:", len(artikel_wa))
print("umlagerungen:", len(artikel_um))

# Überschneidungen und Lücken analysieren
print("\nArtikel NUR im Bestand:", len(artikel_bestaende - (artikel_we | artikel_wa | artikel_um)))
print("Artikel OHNE Lagerplatz:", len((artikel_we | artikel_wa | artikel_um) - artikel_bestaende))
print("Artikel in ALLEN Tabellen:", len(artikel_bestaende & artikel_we & artikel_wa & artikel_um))

# ---------------------------------------------------------
# 5. Data Cleaning
# ---------------------------------------------------------
print("\n--- Data Cleaning ---")

# Datumsspalten konvertieren
for name, df in datasets.items():
    if "datum" in df.columns:
        df["datum"] = pd.to_datetime(df["datum"], format="%Y-%m-%d")
        print(f"{name}: Datum in datetime umgewandelt")

# Spaltennamen vereinheitlichen
for name, df in datasets.items():
    df.columns = df.columns.str.lower()
    print(f"{name}: Spaltennamen in Kleinbuchstaben umgewandelt")

# Null-Werte im Bestand behandeln
if "bestand" in bestaende.columns:
    bestaende["bestand"] = bestaende["bestand"].fillna(0)

# max_bestand nur behandeln, wenn vorhanden
if "max_bestand" in bestaende.columns:
    bestaende["max_bestand"] = bestaende["max_bestand"].fillna("nicht gepflegt")
else:
    print("Hinweis: Keine Spalte 'max_bestand' im Bestand vorhanden.")

# Warengruppe prüfen, falls vorhanden
if "warengruppe" in bestaende.columns:
    fehlende_wg = bestaende["warengruppe"].isna().sum()
    print(f"Warengruppen ohne Zuordnung (sichtbar gelassen): {fehlende_wg}")
else:
    print("Hinweis: Keine Spalte 'warengruppe' im Bestand vorhanden.")
