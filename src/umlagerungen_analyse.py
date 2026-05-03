import pandas as pd


def _normalize_umlagerungen_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalisiert typische Spaltennamen aus umlagerungen.csv,
    damit die Analyse robust funktioniert.
    """

    rename_map = {
        # Artikel
        "artikel": "artikel",
        "artikelnummer": "artikel",
        "artnr": "artikel",

        # Menge
        "menge": "menge",
        "umlagerungsmenge": "menge",
        "menge_umlagerung": "menge",

        # Grund
        "grund": "grund",
        "reason": "grund",

        # Datum
        "datum": "datum",
        "date": "datum",

        # Plätze
        "von_platz": "platz_von",
        "von": "platz_von",
        "source": "platz_von",

        "nach_platz": "platz_nach",
        "nach": "platz_nach",
        "ziel": "platz_nach",
        "target": "platz_nach",
    }

    df = df.rename(columns={col: rename_map.get(col.lower(), col.lower()) for col in df.columns})

    return df


def analyse_umlagerungen(umlagerungen_df: pd.DataFrame) -> dict:
    """
    Führt eine robuste Analyse der Umlagerungen durch.
    """

    if umlagerungen_df is None or umlagerungen_df.empty:
        return {
            "gesamt_anzahl_umlagerungen": 0,
            "umlagerungen_pro_artikel": pd.DataFrame(),
            "gruende_umlagerungen": pd.DataFrame(),
            "top_artikel_umlagerungen": pd.DataFrame(),
        }

    # Spalten normalisieren
    df = _normalize_umlagerungen_columns(umlagerungen_df)

    # Prüfen, ob die wichtigsten Spalten existieren
    required = {"artikel", "menge", "grund"}
    missing = required - set(df.columns)

    if missing:
        print(f"Warnung: Einige erwartete Spalten fehlen: {missing}")
        # fehlende Spalten mit Default-Werten auffüllen
        for col in missing:
            df[col] = "unbekannt" if col == "grund" else 0

    # Gesamtanzahl Umlagerungen
    gesamt_anzahl_umlagerungen = len(df)

    # Umlagerungen pro Artikel
    umlagerungen_pro_artikel = (
        df.groupby("artikel")
        .size()
        .reset_index(name="anzahl_umlagerungen")
        .sort_values("anzahl_umlagerungen", ascending=False)
    )

    # Gründe
    gruende_umlagerungen = (
        df.groupby("grund")
        .size()
        .reset_index(name="anzahl")
        .sort_values("anzahl", ascending=False)
    )

    # Top 10
    top_artikel_umlagerungen = umlagerungen_pro_artikel.head(10)

    return {
        "gesamt_anzahl_umlagerungen": gesamt_anzahl_umlagerungen,
        "umlagerungen_pro_artikel": umlagerungen_pro_artikel,
        "gruende_umlagerungen": gruende_umlagerungen,
        "top_artikel_umlagerungen": top_artikel_umlagerungen,
    }


def print_umlagerungen_summary(stats: dict) -> None:
    """
    Konsolenausgabe der wichtigsten Ergebnisse.
    """

    print("\n--- Analyse der Umlagerungen ---")
    print(f"Gesamtanzahl Umlagerungen: {stats['gesamt_anzahl_umlagerungen']}")

    if not stats["umlagerungen_pro_artikel"].empty:
        print("\nArtikel mit den meisten Umlagerungen:")
        for _, row in stats["umlagerungen_pro_artikel"].head(5).iterrows():
            print(f"- Artikel {row['artikel']}: {row['anzahl_umlagerungen']} Umlagerungen")

    if not stats["gruende_umlagerungen"].empty:
        print("\nHäufigste Umlagerungsgründe:")
        for _, row in stats["gruende_umlagerungen"].iterrows():
            print(f"- {row['grund']}: {row['anzahl']}")
