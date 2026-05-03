import pandas as pd
import numpy as np


def generate_place():
    """
    Erzeugt einen realistischen 6-stelligen Lagerplatzcode.
    Format: A10302
        A1 = Gang
        03 = Regal
        02 = Ebene
    """

    gang_buchstabe = np.random.choice(list("ABC"))      # A, B, C
    gang_nummer = np.random.randint(1, 4)               # 1–3

    regal = np.random.randint(1, 21)                    # 01–20
    ebene = np.random.randint(1, 6)                     # 01–05

    return f"{gang_buchstabe}{gang_nummer}{regal:02d}{ebene:02d}"


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
    Lagerplätze werden jetzt realistisch als 6-stellige Codes erzeugt.
    """

    np.random.seed(seed)

    # 1) Bestände laden
    bestaende = pd.read_csv(input_bestaende)

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

    # 5) Artikel ziehen
    artikel = np.random.choice(artikel_liste, size=anzahl_bewegungen, replace=True)

    # 6) Mengen
    mengen = np.random.randint(1, 40, size=anzahl_bewegungen)

    # 7) Umlagerungsgründe
    gruende = np.random.choice(
        ["Kapazitätsausgleich", "Kommissionierung", "Qualitätsprüfung", "Fehlplatzierung"],
        size=anzahl_bewegungen,
        p=[0.45, 0.30, 0.15, 0.10]
    )

    # 8) Von- und Nach-Plätze erzeugen (6-stellig)
    von_plaetze = [generate_place() for _ in range(anzahl_bewegungen)]
    nach_plaetze = [generate_place() for _ in range(anzahl_bewegungen)]

    # Sicherstellen, dass nicht von == nach
    for i in range(anzahl_bewegungen):
        while nach_plaetze[i] == von_plaetze[i]:
            nach_plaetze[i] = generate_place()

    # 9) DataFrame bauen
    umlagerungen = pd.DataFrame({
        "datum": datum.sort_values().values,
        "artikel": artikel,
        "menge": mengen,
        "von_platz": von_plaetze,
        "nach_platz": nach_plaetze,
        "grund": gruende
    })

    # 10) Speichern
    umlagerungen.to_csv(output_path, index=False)

    print(f"umlagerungen.csv erfolgreich erzeugt → {output_path}")
    print("Anzahl Datensätze:", len(umlagerungen))


if __name__ == "__main__":
    generate_umlagerungen()
