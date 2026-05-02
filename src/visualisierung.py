import os
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------------------
# Globale Pfade
# ---------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PLOTS_DIR = os.path.join(BASE_DIR, "plots")
os.makedirs(PLOTS_DIR, exist_ok=True)

# ---------------------------------------------------------
# Einheitlicher Stil für alle Diagramme
# ---------------------------------------------------------
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)
plt.rcParams["axes.titlesize"] = 16
plt.rcParams["axes.labelsize"] = 13
plt.rcParams["xtick.labelsize"] = 11
plt.rcParams["ytick.labelsize"] = 11
plt.rcParams["axes.edgecolor"] = "#333333"
plt.rcParams["axes.linewidth"] = 0.8


# ---------------------------------------------------------
# 1. Top-n Lagerumschlag
# ---------------------------------------------------------
def plot_top_umschlag(kpi_df, n=10):
    """
    Visualisiert die Top-n Artikel nach Lagerumschlag als Balkendiagramm.

    Parameter:
        kpi_df: DataFrame mit KPI-Spalten
        n: Anzahl der anzuzeigenden Artikel

    Speichert:
        plots/top_{n}_lagerumschlag.png
    """
    df = kpi_df.sort_values("lagerumschlag", ascending=False).head(n)

    plt.figure()
    ax = sns.barplot(
        data=df,
        x=df.index.astype(str),
        y="lagerumschlag",
        color="steelblue"
    )

    ax.set_title(f"Top {n} Artikel – Lagerumschlag")
    ax.set_xlabel("Artikel")
    ax.set_ylabel("Lagerumschlag")

    for p in ax.patches:
        ax.annotate(
            f"{p.get_height():.1f}",
            (p.get_x() + p.get_width() / 2, p.get_height()),
            ha="center",
            va="bottom",
            fontsize=10
        )

    plt.tight_layout()

    plot_path = os.path.join(PLOTS_DIR, f"top_{n}_lagerumschlag.png")
    plt.savefig(plot_path, dpi=150, bbox_inches="tight")
    plt.show()
    plt.close()


# ---------------------------------------------------------
# 2. Top-n Durchschnittsbestand
# ---------------------------------------------------------
def plot_top_durchschnittsbestand(kpi_df, n=10):
    """
    Visualisiert die Top-n Artikel nach Durchschnittsbestand.

    Parameter:
        kpi_df: DataFrame mit KPI-Spalten
        n: Anzahl der anzuzeigenden Artikel

    Speichert:
        plots/top_{n}_durchschnittsbestand.png
    """
    df = kpi_df.sort_values("durchschnittsbestand", ascending=False).head(n)

    plt.figure()
    ax = sns.barplot(
        data=df,
        x=df.index.astype(str),
        y="durchschnittsbestand",
        color="darkorange"
    )

    ax.set_title(f"Top {n} Artikel – Durchschnittsbestand")
    ax.set_xlabel("Artikel")
    ax.set_ylabel("Durchschnittsbestand")

    for p in ax.patches:
        ax.annotate(
            f"{p.get_height():.1f}",
            (p.get_x() + p.get_width() / 2, p.get_height()),
            ha="center",
            va="bottom",
            fontsize=10
        )

    plt.tight_layout()

    plot_path = os.path.join(PLOTS_DIR, f"top_{n}_durchschnittsbestand.png")
    plt.savefig(plot_path, dpi=150, bbox_inches="tight")
    plt.show()
    plt.close()


# ---------------------------------------------------------
# 3. Top-n Lagerdauer
# ---------------------------------------------------------
def plot_top_lagerdauer(kpi_df, n=10):
    """
    Visualisiert die Top-n Artikel mit der niedrigsten Lagerdauer.

    Parameter:
        kpi_df: DataFrame mit KPI-Spalten
        n: Anzahl der anzuzeigenden Artikel

    Speichert:
        plots/top_{n}_lagerdauer.png
    """
    df = kpi_df.sort_values("lagerdauer", ascending=True).head(n)

    plt.figure()
    ax = sns.barplot(
        data=df,
        x=df.index.astype(str),
        y="lagerdauer",
        color="seagreen"
    )

    ax.set_title(f"Top {n} Artikel – Niedrigste Lagerdauer")
    ax.set_xlabel("Artikel")
    ax.set_ylabel("Lagerdauer")

    for p in ax.patches:
        ax.annotate(
            f"{p.get_height():.1f}",
            (p.get_x() + p.get_width() / 2, p.get_height()),
            ha="center",
            va="bottom",
            fontsize=10
        )

    plt.tight_layout()

    plot_path = os.path.join(PLOTS_DIR, f"top_{n}_lagerdauer.png")
    plt.savefig(plot_path, dpi=150, bbox_inches="tight")
    plt.show()
    plt.close()


# ---------------------------------------------------------
# 4. Top-n Engpass-Score
# ---------------------------------------------------------
def plot_top_engpass(kpi_df, n=10):
    """
    Visualisiert die Top-n Artikel nach Engpass-Score.

    Parameter:
        kpi_df: DataFrame mit KPI-Spalten (inkl. 'engpass_score')
        n: Anzahl der anzuzeigenden Artikel

    Speichert:
        plots/top_{n}_engpass_score.png
    """
    df = kpi_df.sort_values("engpass_score", ascending=False).head(n)

    plt.figure()
    ax = sns.barplot(
        data=df,
        x=df.index.astype(str),
        y="engpass_score",
        color="crimson"
    )

    ax.set_title(f"Top {n} Artikel – Engpass-Score")
    ax.set_xlabel("Artikel")
    ax.set_ylabel("Engpass-Score")

    for p in ax.patches:
        ax.annotate(
            f"{p.get_height():.1f}",
            (p.get_x() + p.get_width() / 2, p.get_height()),
            ha="center",
            va="bottom",
            fontsize=10
        )

    plt.tight_layout()

    plot_path = os.path.join(PLOTS_DIR, f"top_{n}_engpass_score.png")
    plt.savefig(plot_path, dpi=150, bbox_inches="tight")
    plt.show()
    plt.close()
