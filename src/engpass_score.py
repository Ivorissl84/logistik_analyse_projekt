import pandas as pd


def berechne_engpass_score(kpi_df):
    """
    Berechnet den Engpass-Score für jeden Artikel.

    Formel:
        Engpass-Score = Lagerumschlag / (Durchschnittsbestand + 1)

    Interpretation:
        - Hoher Score = hoher Verbrauch bei gleichzeitig niedrigem Bestand
        - Niedriger Score = Artikel ist weniger kritisch
        - "+1" verhindert Division durch 0

    Parameter:
        kpi_df: DataFrame mit mindestens den Spalten
                'lagerumschlag' und 'durchschnittsbestand'

    Rückgabe:
        DataFrame mit zusätzlicher Spalte 'engpass_score'
    """

    # ---------------------------------------------------
    # 1. DataFrame kopieren, um Original nicht zu verändern
    # ---------------------------------------------------
    df = kpi_df.copy()

    # ---------------------------------------------------
    # 2. Fehlende Werte robust behandeln
    # ---------------------------------------------------
    df["lagerumschlag"] = df["lagerumschlag"].fillna(0)
    df["durchschnittsbestand"] = df["durchschnittsbestand"].fillna(0)

    # ---------------------------------------------------
    # 3. Engpass-Score berechnen
    # ---------------------------------------------------
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

    # ---------------------------------------------------
    # 1. Nach Engpass-Score sortieren und oberste n Zeilen zurückgeben
    # ---------------------------------------------------
    return df.sort_values("engpass_score", ascending=False).head(n)
