import os
import pandas as pd

# ---------------------------------------------------------
# Globale Pfade
# ---------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")


def load_data():
    """
    Lädt alle Rohdaten aus dem data/-Ordner und bereitet sie einheitlich auf.

    Rückgabe:
        bestaende (DataFrame)
        wareneingang (DataFrame)
        warenausgang (DataFrame)
        umlagerungen (DataFrame)
    """

    # --- 1. CSVs laden ---
    bestaende = pd.read_csv(os.path.join(DATA_DIR, "bestaende.csv"))
    wareneingang = pd.read_csv(os.path.join(DATA_DIR, "wareneingang.csv"))
    warenausgang = pd.read_csv(os.path.join(DATA_DIR, "warenausgang.csv"))
    umlagerungen = pd.read_csv(os.path.join(DATA_DIR, "umlagerungen.csv"))

    # --- 2. Datumsfelder konvertieren ---
    for df in [wareneingang, warenausgang, umlagerungen]:
        df["datum"] = pd.to_datetime(df["datum"], format="%Y-%m-%d")

    # --- 3. Spaltennamen vereinheitlichen ---
    for df in [bestaende, wareneingang, warenausgang, umlagerungen]:
        df.columns = df.columns.str.lower()

    # --- 4. Umlagerungen-Spalten anpassen ---
    umlagerungen.rename(
        columns={
            "von_platz": "platz_von",
            "nach_platz": "platz_nach",
        },
        inplace=True,
    )

    return bestaende, wareneingang, warenausgang, umlagerungen
