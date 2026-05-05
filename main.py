from src.data_loading import load_data
from src.kpi_berechnung import berechne_kpis
from src.engpass_score import berechne_engpass_score, top_engpaesse
from src.umlagerungen_analyse import analyse_umlagerungen, print_umlagerungen_summary
from src.visualisierung import (
    plot_top_umschlag,
    plot_top_durchschnittsbestand,
    plot_top_lagerdauer,
    plot_top_engpass,
    plot_top_umlagerungen,
    plot_umlagerungsgruende
)


def main():
    """
    Hauptpipeline des Projekts.

    Schritte:
        1. Daten laden
        2. KPIs berechnen
        3. Engpass-Score berechnen
        4. Kritischste Artikel ausgeben
        5. Umlagerungen analysieren
        6. Visualisierungen erzeugen und speichern
    """

    # ---------------------------------------------------
    # 1. Daten laden
    # ---------------------------------------------------
    # Lädt alle Rohdaten (Bestände, WE, WA, Umlagerungen)
    bestaende, wareneingang, warenausgang, umlagerungen = load_data()

    # ---------------------------------------------------
    # 2. KPIs berechnen
    # ---------------------------------------------------
    # Rekonstruktion der Monatsbestände + Lagerkennzahlen
    kpi_df = berechne_kpis(bestaende, wareneingang, warenausgang)

    # ---------------------------------------------------
    # 3. Engpass-Score berechnen
    # ---------------------------------------------------
    # Engpass-Score ergänzt die KPI-Tabelle um Kritikalitätsbewertung
    kpi_df = berechne_engpass_score(kpi_df)

    # ---------------------------------------------------
    # 4. Top-Engpässe anzeigen
    # ---------------------------------------------------
    print("\n--- Kritischste Artikel (Top 20) ---")
    print(top_engpaesse(kpi_df, n=20).to_string())

    # ---------------------------------------------------
    # 5. Umlagerungen analysieren
    # ---------------------------------------------------
    # Liefert Statistiken zu Umlagerungsvolumen, Gründen und Top-Artikeln
    umlagerungen_stats = analyse_umlagerungen(umlagerungen)
    print_umlagerungen_summary(umlagerungen_stats)

    # ---------------------------------------------------
    # 6. Visualisierungen erzeugen
    # ---------------------------------------------------
    # KPI-basierte Diagramme
    plot_top_umschlag(kpi_df)
    plot_top_durchschnittsbestand(kpi_df)
    plot_top_lagerdauer(kpi_df)
    plot_top_engpass(kpi_df)

    # Umlagerungsdiagramme
    plot_top_umlagerungen(umlagerungen_stats)
    plot_umlagerungsgruende(umlagerungen_stats)


if __name__ == "__main__":
    main()
