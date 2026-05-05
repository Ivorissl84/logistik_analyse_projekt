import os
import pandas as pd

# ---------------------------------------------------------
# 0. Pfade korrekt setzen
# ---------------------------------------------------------
# BASE_DIR zeigt auf das Projekt-Root, unabhängig vom Startpunkt
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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

# ---------------------------------------------------------
# 2. Daten vorbereiten
# ---------------------------------------------------------
# Datumsspalten in datetime konvertieren
for df in [wareneingang, warenausgang, umlagerungen]:
    df["datum"] = pd.to_datetime(df["datum"], format="%Y-%m-%d")

# Spaltennamen vereinheitlichen (Kleinbuchstaben)
for df in [bestaende, wareneingang, warenausgang, umlagerungen]:
    df.columns = df.columns.str.lower()

# Umlagerungen: Platzspalten harmonisieren
umlagerungen.rename(columns={"von_platz": "platz_von", "nach_platz": "platz_nach"}, inplace=True)

# ---------------------------------------------------------
# 3. Überblick über Mengen
# ---------------------------------------------------------
print("\n--- Überblick über Mengen ---")
print("Wareneingang gesamt:", wareneingang["menge"].sum())
print("Warenausgang gesamt:", warenausgang["menge"].sum())
print("Umlagerungen gesamt:", umlagerungen["menge"].sum())

# ---------------------------------------------------------
# 4. Artikel-Toplisten
# ---------------------------------------------------------
print("\n--- Top 5 Artikel nach Eingang ---")
print(wareneingang.groupby("artikel")["menge"].sum().sort_values(ascending=False).head())

print("\n--- Top 5 Artikel nach Ausgang ---")
print(warenausgang.groupby("artikel")["menge"].sum().sort_values(ascending=False).head())

print("\n--- Top 5 Artikel nach Umlagerungen ---")
print(umlagerungen.groupby("artikel")["menge"].sum().sort_values(ascending=False).head())

# ---------------------------------------------------------
# 5. Warengruppen-Analysen
# ---------------------------------------------------------
# Warengruppen nur analysieren, wenn Spalte vorhanden ist
if "warengruppe" in wareneingang.columns:
    print("\n--- Warengruppen Eingang ---")
    print(wareneingang.groupby("warengruppe")["menge"].sum())
else:
    print("\nHinweis: Keine Warengruppe-Spalte im Wareneingang vorhanden.")

if "warengruppe" in warenausgang.columns:
    print("\n--- Warengruppen Ausgang ---")
    print(warenausgang.groupby("warengruppe")["menge"].sum())
else:
    print("\nHinweis: Keine Warengruppe-Spalte im Warenausgang vorhanden.")

if "warengruppe" in umlagerungen.columns:
    print("\n--- Warengruppen Umlagerungen ---")
    print(umlagerungen.groupby("warengruppe")["menge"].sum())
else:
    print("\nHinweis: Keine Warengruppe-Spalte in Umlagerungen vorhanden.")

# ---------------------------------------------------------
# 6. Zeitreihen (Monate)
# ---------------------------------------------------------
# Monat aus Datum extrahieren
wareneingang["monat"] = wareneingang["datum"].dt.month
warenausgang["monat"] = warenausgang["datum"].dt.month
umlagerungen["monat"] = umlagerungen["datum"].dt.month

print("\n--- Eingang pro Monat ---")
print(wareneingang.groupby("monat")["menge"].sum())

print("\n--- Ausgang pro Monat ---")
print(warenausgang.groupby("monat")["menge"].sum())

print("\n--- Umlagerungen pro Monat ---")
print(umlagerungen.groupby("monat")["menge"].sum())

# ---------------------------------------------------------
# 7. Platz-Aktivität
# ---------------------------------------------------------
print("\n--- Aktivste Plätze (Umlagerungen von) ---")
print(umlagerungen.groupby("platz_von")["menge"].sum().sort_values(ascending=False).head())

print("\n--- Aktivste Plätze (Umlagerungen nach) ---")
print(umlagerungen.groupby("platz_nach")["menge"].sum().sort_values(ascending=False).head())

# ---------------------------------------------------------
# 8. Lieferanten-Analyse
# ---------------------------------------------------------
# Lieferanten nur analysieren, wenn Spalte vorhanden ist
if "lieferant" in wareneingang.columns:
    print("\n--- Top Lieferanten nach Menge ---")
    print(wareneingang.groupby("lieferant")["menge"].sum().sort_values(ascending=False).head())
else:
    print("\nHinweis: Keine Lieferanten-Spalte im Wareneingang vorhanden.")
