import pandas as pd
import numpy as np


def generate_umlagerungen(
    input_bestaende="../data/bestaende.csv",
    output_path="../data/umlagerungen.csv",
    seed=42,
    anzahl_bewegungen=200,
    start="2024-01-01",
    end="2024-12-31"
):
    """
    Generiert synthetische Umlagerungen basierend auf der neuen Bestandsdatei.
    Erwartet nur:
    - artikel
    - bestand

    Da keine Plätze mehr existieren, werden realistische Lagerplätze synthetisch erzeugt.
    """

    np.random.seed(seed)

    # 1) Bestände laden
    bestaende = pd.read_csv(input_bestaende)

    if not {"artikel", "bestand"}.issubset(bestaende.columns):
        raise ValueError("bestaende.csv muss die Spalten 'artikel' und 'bestand' enthalten!")

    # 2) Artikelbasis
    artikel_liste = bestaende["artikel"].unique()

    # 3) Synthetische Lagerplätze erzeugen
    # Beispiel: A01–A50, B01–B50, C01–C50 → insgesamt 150 Plätze
    plaetze = [f"A{str(i).zfill(2)}" for i in range(1, 51)] + \
              [f"B{str(i).zfill(2)}" for i in range(1, 51)] + \
              [f"C{str(i).zfill(2)}" for i in range(1, 51)]

    # 4) Zeitraum berechnen
    start_date = pd.to_datetime(start)
    end_date = pd.to_datetime(end)
    tage = (end_date - start_date).days

    # 5) Datum erzeugen
    datum = start_date + pd.to_timedelta(
        np.random.randint(0, tage, size=anzahl_bewegungen),
        unit="D"
    )

    # 6) Artikel ziehen
    artikel = np.random.choice(artikel_liste, size=anzahl_bewegungen, replace=True)

    # 7) Mengen
    mengen = np.random.randint(1, 40, size=anzahl_bewegungen)

    # 8) Umlagerungsgründe
    gruende = np.random.choice(
        ["Kapazitätsausgleich", "Kommissionierung", "Qualitätsprüfung", "Fehlplatzierung"],
        size=anzahl_bewegungen,
        p=[0.45, 0.30, 0.15, 0.10]
    )

    # 9) Von- und Nach-Plätze erzeugen
    von_plaetze = np.random.choice(plaetze, size=anzahl_bewegungen)
    nach_plaetze = np.random.choice(plaetze, size=anzahl_bewegungen)

    # Sicherstellen, dass nicht von == nach
    mask = von_plaetze == nach_plaetze
    while mask.any():
        nach_plaetze[mask] = np.random.choice(plaetze, size=mask.sum())
        mask = von_plaetze == nach_plaetze

    # 10) DataFrame bauen
    umlagerungen = pd.DataFrame({
        "datum": datum.sort_values().values,
        "artikel": artikel,
        "menge": mengen,
        "von_platz": von_plaetze,
        "nach_platz": nach_plaetze,
        "grund": gruende
    })

    # 11) Speichern
    umlagerungen.to_csv(output_path, index=False)

    print(f"umlagerungen.csv erfolgreich erzeugt → {output_path}")
    print("Anzahl Datensätze:", len(umlagerungen))


if __name__ == "__main__":
    generate_umlagerungen()
