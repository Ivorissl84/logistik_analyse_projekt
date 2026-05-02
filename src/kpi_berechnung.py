import pandas as pd


def berechne_kpis(bestaende, wareneingang, warenausgang, jahr=2023):
    """
    Berechnet zentrale Lager-KPIs für alle Artikel.

    Berechnet werden:
        - Rekonstruierte Monatsendbestände (rückwärts aus Dezember)
        - Durchschnittsbestand (arithmetisch über 12 Monate)
        - Jahresverbrauch
        - Lagerumschlag (Jahresverbrauch / Durchschnittsbestand)
        - Lagerdauer (Durchschnittsbestand / Tagesverbrauch)

    Parameter:
        bestaende: DataFrame mit Endbestand Dezember
        wareneingang: DataFrame mit Zugängen (mit Datum)
        warenausgang: DataFrame mit Abgängen (mit Datum)
        jahr: Jahr der Rekonstruktion (Standard: 2023)

    Rückgabe:
        kpi_df: DataFrame mit allen KPIs pro Artikel
    """

    # ---------------------------------------------------------
    # 1. Monate vorbereiten
    # ---------------------------------------------------------
    wareneingang["monat"] = wareneingang["datum"].dt.to_period("M")
    warenausgang["monat"] = warenausgang["datum"].dt.to_period("M")

    eingang_monat = wareneingang.groupby(["artikel", "monat"])["menge"].sum()
    verbrauch_monat = warenausgang.groupby(["artikel", "monat"])["menge"].sum()

    alle_artikel = (
        set(bestaende["artikel"])
        | set(warenausgang["artikel"])
        | set(wareneingang["artikel"])
    )

    # ---------------------------------------------------------
    # 2. Endbestand Dezember
    # ---------------------------------------------------------
    endbestand_dez = bestaende.groupby("artikel")["bestand"].sum()

    monate = pd.period_range(f"{jahr}-01", f"{jahr}-12", freq="M")

    monatsbestaende = {artikel: {} for artikel in alle_artikel}

    # ---------------------------------------------------------
    # 3. Monatsrekonstruktion (rückwärts)
    # ---------------------------------------------------------
    for artikel in alle_artikel:
        endbestand = endbestand_dez.get(artikel, 0)

        for monat in reversed(monate):
            zugang = eingang_monat.get((artikel, monat), 0)
            abgang = verbrauch_monat.get((artikel, monat), 0)

            anfang = endbestand - zugang + abgang
            if anfang < 0:
                anfang = 0  # Datenfehler abfangen

            monatsbestaende[artikel][monat] = endbestand
            endbestand = anfang

    # ---------------------------------------------------------
    # 4. Durchschnittsbestand
    # ---------------------------------------------------------
    durchschnittsbestand = {
        artikel: sum(monatsbestaende[artikel].values()) / len(monate)
        for artikel in alle_artikel
    }

    # ---------------------------------------------------------
    # 5. Jahresverbrauch
    # ---------------------------------------------------------
    jahresverbrauch = warenausgang.groupby("artikel")["menge"].sum()

    # ---------------------------------------------------------
    # 6. Lagerumschlag
    # ---------------------------------------------------------
    lagerumschlag = {
        artikel: (
            jahresverbrauch.get(artikel, 0) / durchschnittsbestand[artikel]
            if durchschnittsbestand[artikel] > 0 else 0
        )
        for artikel in alle_artikel
    }

    # ---------------------------------------------------------
    # 7. Tagesverbrauch
    # ---------------------------------------------------------
    tagesverbrauch = {
        artikel: jahresverbrauch.get(artikel, 0) / 365
        for artikel in alle_artikel
    }

    # ---------------------------------------------------------
    # 8. Lagerdauer
    # ---------------------------------------------------------
    lagerdauer = {
        artikel: (
            durchschnittsbestand[artikel] / tagesverbrauch[artikel]
            if tagesverbrauch[artikel] > 0 else None
        )
        for artikel in alle_artikel
    }

    # ---------------------------------------------------------
    # 9. DataFrame bauen
    # ---------------------------------------------------------
    kpi_df = pd.DataFrame({
        "durchschnittsbestand": pd.Series(durchschnittsbestand),
        "lagerumschlag": pd.Series(lagerumschlag),
        "lagerdauer": pd.Series(lagerdauer),
    })

    # Sortierung für bessere Lesbarkeit
    kpi_df = kpi_df.sort_values("lagerumschlag", ascending=False)

    return kpi_df
