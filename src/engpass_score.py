import pandas as pd


def berechne_engpass_score(kpi_df):
    """
    Berechnet den Engpass-Score für jeden Artikel.

    Formel:
        Engpass-Score = Lagerumschlag / (Durchschnittsbestand + 1)

    Interpretation:
        - Hoher Score = Artikel hat hohen Verbrauch bei gleichzeitig niedrigem Bestand
        - Niedriger Score = Artikel ist weniger kritisch
        - "+1" verhindert Division durch 0 bei Artikeln ohne Bestand

    Parameter:
        kpi_df: DataFrame mit mindestens den Spalten
                - 'lagerumschlag'
                - 'durchschnittsbestand'

    Rückgabe:
        DataFrame mit zusätzlicher Spalte:
            - 'engpass_score'
    """

    df = kpi_df.copy()

    # Robust gegen fehlende Werte
    df["lagerumschlag"] = df["lagerumschlag"].fillna(0)
    df["durchschnittsbestand"] = df["durchschnittsbestand"].fillna(0)

    # Engpass-Score berechnen
    df["engpass_score"] = df["lagerumschlag"] / (df["durchschnittsbestand"] + 1)

    return df


def top_engpaesse(df, n=20):
    """
    Gibt die Top-n Artikel mit dem höchsten Engpass-Score zurück.

    Parameter:
        df: DataFrame mit Spalte 'engpass_score'
        n: Anzahl der zurückzugebenden Artikel

    Rückgabe:
        DataFrame der Top-n Artikel
    """
    return df.sort_values("engpass_score", ascending=False).head(n)
