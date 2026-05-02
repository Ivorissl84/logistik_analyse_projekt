import pandas as pd
import numpy as np

def generate_bestaende(
    anzahl_artikel=100,
    min_bestand=0,
    max_bestand=500,
    seed=42,
    output_path="../data/bestaende.csv"
):
    """
    Generiert eine synthetische Stichtags-Bestandsdatei.
    - Artikelnummern: 100000–100000+anzahl_artikel
    - Bestände: realistische ABC-Verteilung
    """

    np.random.seed(seed)

    # Artikelnummern erzeugen
    artikel = np.arange(100000, 100000 + anzahl_artikel)

    # ABC-Verteilung simulieren
    # A: hohe Bestände, B: mittel, C: niedrig
    verteilung = np.random.choice(["A", "B", "C"], size=anzahl_artikel, p=[0.2, 0.3, 0.5])

    bestaende = []
    for art, klasse in zip(artikel, verteilung):
        if klasse == "A":
            bestand = np.random.randint(200, max_bestand)
        elif klasse == "B":
            bestand = np.random.randint(50, 200)
        else:  # C
            bestand = np.random.randint(min_bestand, 50)

        bestaende.append([art, bestand])

    df = pd.DataFrame(bestaende, columns=["artikel", "bestand"])

    df.to_csv(output_path, index=False)
    print(f"bestaende.csv erfolgreich erzeugt → {output_path}")


if __name__ == "__main__":
    generate_bestaende()
