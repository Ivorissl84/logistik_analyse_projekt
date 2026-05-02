import pandas as pd
import numpy as np


def generate_warenausgang(
    input_bestaende="../data/bestaende.csv",
    output_path="../data/warenausgang.csv",
    seed=42,
    anzahl_bewegungen=1500,
    start="2024-01-01",
    end="2024-12-31"
):
    """
    Generiert synthetische Warenausgänge basierend auf der neuen Bestandsdatei.
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

    # 4) Datum erzeugen
    datum = start_date + pd.to_timedelta(
        np.random.randint(0, tage, size=anzahl_bewegungen),
        unit="D"
    )

    # 5) Artikel zufällig ziehen
    artikel = np.random.choice(artikel_liste, size=anzahl_bewegungen, replace=True)

    # 6) Mengen & Gründe
    mengen = np.random.randint(3, 70, size=anzahl_bewegungen)

    gruende = np.random.choice(
        ["Versand", "Produktion", "Reparatur", "Retourenaufbereitung"],
        size=anzahl_bewegungen,
        p=[0.55, 0.25, 0.10, 0.10]
    )

    belegnummern = [f"WA-{20000 + i}" for i in range(1, anzahl_bewegungen + 1)]

    # 7) DataFrame bauen
    warenausgang = pd.DataFrame({
        "datum": datum.sort_values().values,
        "artikel": artikel,
        "menge": mengen,
        "grund": gruende,
        "belegnummer": belegnummern
    })

    # 8) Speichern
    warenausgang.to_csv(output_path, index=False)

    print(f"warenausgang.csv erfolgreich erzeugt → {output_path}")
    print("Anzahl Datensätze:", len(warenausgang))


if __name__ == "__main__":
    generate_warenausgang()
