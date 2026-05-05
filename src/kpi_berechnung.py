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
    # Sicherstellen, dass Bewegungsdaten ein Datumsfeld besitzen
    if "datum" not in wareneingang.columns or "datum" not in warenausgang.columns:
        raise ValueError("wareneingang/warenausgang benötigen eine 'datum'-Spalte.")

    # Monat extrahieren (Periodenformat für Gruppierung)
    wareneingang["monat"] = wareneingang["datum"].dt.to_period("M")
    warenausgang["monat"] = warenausgang["datum"].dt.to_period("M")

    # Monatliche Summen pro Artikel
    eingang_monat = wareneingang.groupby(["artikel", "monat"])["menge"].sum()
    verbrauch_monat = warenausgang.groupby(["artikel", "monat"])["menge"].sum()

    # Alle Artikel, die irgendwo vorkommen
    alle_artikel = (
        set(bestaende["artikel"])
        | set(warenausgang["artikel"])
        | set(wareneingang["artikel"])
    )

    # ---------------------------------------------------------
    # 2. Endbestand Dezember
    # ---------------------------------------------------------
    endbestand_dez = bestaende.groupby("artikel")["bestand"].sum()

    # Alle Monate des Jahres
    monate = pd.period_range(f"{jahr}-01", f"{jahr}-12", freq="M")

    # Struktur für rekonstruierte Monatsbestände
    monatsbestaende = {artikel: {} for artikel in alle_artikel}

    # ---------------------------------------------------------
    # 3. Monatsrekonstruktion (rückwärts)
    # ---------------------------------------------------------
    # Startpunkt: Dezember-Endbestand → rückwärts bis Januar
    for artikel in alle_artikel:
        endbestand = endbestand_dez.get(artikel, 0)

        for monat in reversed(monate):
            zugang = eingang_monat.get((artikel, monat), 0)
            abgang = verbrauch_monat.get((artikel, monat), 0)

            # Anfangsbestand = Endbestand - Zugang + Abgang
            anfang = endbestand - zugang + abgang

            # Negative Bestände abfangen (Datenfehler)
            if anfang < 0:
                anfang = 0

            # Endbestand des Monats speichern
            monatsbestaende[artikel][monat] = endbestand

            # Für nächsten Monat rückwärts
            endbestand = anfang

    # ---------------------------------------------------------
    # 4. Durchschnittsbestand berechnen
    # ---------------------------------------------------------
    durchschnittsbestand = {
        artikel: sum(monatsbestaende[artikel].values()) / len(monate)
        for artikel in alle_artikel
    }

    # ---------------------------------------------------------
    # 5. Jahresverbrauch berechnen
    # ---------------------------------------------------------
    jahresverbrauch = warenausgang.groupby("artikel")["menge"].sum()

    # ---------------------------------------------------------
    # 6. Lagerumschlag berechnen
    # ---------------------------------------------------------
    lagerumschlag = {
        artikel: (
            jahresverbrauch.get(artikel, 0) / durchschnittsbestand[artikel]
            if durchschnittsbestand[artikel] > 0 else 0
        )
        for artikel in alle_artikel
    }

    # ---------------------------------------------------------
    # 7. Tagesverbrauch berechnen
    # ---------------------------------------------------------
    tagesverbrauch = {
        artikel: jahresverbrauch.get(artikel, 0) / 365
        for artikel in alle_artikel
    }

    # ---------------------------------------------------------
    # 8. Lagerdauer berechnen
    # ---------------------------------------------------------
    lagerdauer = {
        artikel: (
            durchschnittsbestand[artikel] / tagesverbrauch[artikel]
            if tagesverbrauch[artikel] > 0 else None
        )
        for artikel in alle_artikel
    }

    # ---------------------------------------------------------
    # 9. KPI-DataFrame bauen
    # ---------------------------------------------------------
    kpi_df = pd.DataFrame({
        "durchschnittsbestand": pd.Series(durchschnittsbestand),
        "lagerumschlag": pd.Series(lagerumschlag),
        "lagerdauer": pd.Series(lagerdauer),
    })

    # Für bessere Lesbarkeit nach Lagerumschlag sortieren
    kpi_df = kpi_df.sort_values("lagerumschlag", ascending=False)

    return kpi_df
