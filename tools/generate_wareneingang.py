import pandas as pd
import numpy as np


def generate_wareneingang(
    input_bestaende="../data/bestaende.csv",
    output_path="../data/wareneingang.csv",
    seed=42,
    anzahl_bewegungen=1000,
    start="2024-01-01",
    end="2024-12-31"
):
    """
    Generiert synthetische Wareneingänge basierend auf der neuen Bestandsdatei.
    Erwartet nur:
    - artikel
    - bestand
    """

    np.random.seed(seed)

    # 1) Bestände laden
    bestaende = pd.read_csv(input_bestaende)

    # Sicherstellen, dass die Datei die erwarteten Spalten hat
    if not {"artikel", "bestand"}.issubset(bestaende.columns):
        raise ValueError("bestaende.csv muss die Spalten 'artikel' und 'bestand' enthalten!")

    # 2) Artikelbasis
    artikel_liste = bestaende["artikel"].unique()

    # 3) Zeitraum berechnen
    start_date = pd.to_datetime(start)
    end_date = pd.to_datetime(end)
    tage = (end_date - start_date).days

    # 4) Zufällige Daten erzeugen
    datum = start_date + pd.to_timedelta(
        np.random.randint(0, tage, size=anzahl_bewegungen),
        unit="D"
    )

    artikel = np.random.choice(artikel_liste, size=anzahl_bewegungen, replace=True)
    mengen = np.random.randint(5, 60, size=anzahl_bewegungen)

    lieferanten = np.random.choice(
        ["LiefTec", "MechaPro", "InduParts", "ElektroPlus"],
        size=anzahl_bewegungen,
        p=[0.3, 0.3, 0.25, 0.15]
    )

    lieferscheine = [f"LS-{10000 + i}" for i in range(1, anzahl_bewegungen + 1)]

    # 5) DataFrame bauen
    wareneingang = pd.DataFrame({
        "datum": datum.sort_values().values,
        "artikel": artikel,
        "menge": mengen,
        "lieferant": lieferanten,
        "lieferschein": lieferscheine
    })

    # 6) Speichern
    wareneingang.to_csv(output_path, index=False)
    print(f"wareneingang.csv erfolgreich erzeugt → {output_path}")


if __name__ == "__main__":
    generate_wareneingang()
