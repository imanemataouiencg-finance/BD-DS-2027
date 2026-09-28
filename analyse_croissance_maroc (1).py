"""
Analyse des freins à la croissance économique du Maroc (2015-2026)
====================================================================

Ce script :
  1. importe le dataset d'indicateurs macroéconomiques marocains ;
  2. calcule quelques statistiques descriptives et corrélations ;
  3. génère un graphique de synthèse (4 panneaux) sauvegardé en PNG.

Sources des données (voir aussi le rapport) :
  - Haut-Commissariat au Plan (HCP), Comptes nationaux
    https://www.hcp.ma/
  - Bank Al-Maghrib (BAM), Rapports annuels & Statistiques monétaires
    https://www.bkam.ma/
  - Banque mondiale, World Development Indicators (WDI)
    https://databank.worldbank.org/source/world-development-indicators
  - FMI, World Economic Outlook Database
    https://www.imf.org/en/Publications/WEO

Le fichier `maroc_indicateurs.csv` compile ces séries (croissance du PIB réel,
croissance du PIB agricole, taux de chômage, taux d'inflation, part de
l'agriculture dans le PIB) pour la période 2015-2026.

Dépendances : pandas, matplotlib  (pip install pandas matplotlib)
"""

import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# 1. Import des données
# ---------------------------------------------------------------------------
CSV_PATH = "maroc_indicateurs.csv"
df = pd.read_csv(CSV_PATH)
df = df.sort_values("annee").reset_index(drop=True)

print("Aperçu du dataset :")
print(df.to_string(index=False))

# ---------------------------------------------------------------------------
# 2. Statistiques descriptives et corrélations
# ---------------------------------------------------------------------------
stats = {
    "Croissance PIB moyenne (2015-2026)": df["croissance_pib_reel_pct"].mean(),
    "Chômage moyen": df["taux_chomage_pct"].mean(),
    "Chômage 2015": df["taux_chomage_pct"].iloc[0],
    "Chômage 2026": df["taux_chomage_pct"].iloc[-1],
    "Corrélation PIB réel / PIB agricole": df["croissance_pib_reel_pct"].corr(
        df["croissance_pib_agricole_pct"]
    ),
    "Corrélation PIB réel / Chômage": df["croissance_pib_reel_pct"].corr(
        df["taux_chomage_pct"]
    ),
    "Corrélation PIB réel / Inflation": df["croissance_pib_reel_pct"].corr(
        df["taux_inflation_pct"]
    ),
}

print("\nIndicateurs clés :")
for k, v in stats.items():
    print(f"  - {k} : {v:.2f}")

# ---------------------------------------------------------------------------
# 3. Graphique de synthèse (4 panneaux)
# ---------------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(13, 9))
fig.suptitle(
    "Qu'est-ce qui freine la croissance au Maroc ? (2015-2026)",
    fontsize=15,
    fontweight="bold",
)

# Panneau 1 : PIB réel vs PIB agricole -> dépendance climatique
ax = axes[0, 0]
ax.plot(df["annee"], df["croissance_pib_reel_pct"], marker="o", color="#1f4e79",
        linewidth=2, label="Croissance du PIB réel (%)")
ax.plot(df["annee"], df["croissance_pib_agricole_pct"], marker="s", color="#70ad47",
        linewidth=2, linestyle="--", label="Croissance du PIB agricole (%)")
ax.axhline(0, color="grey", linewidth=0.8)
ax.set_title("1. Croissance globale vs croissance agricole")
ax.set_ylabel("%")
ax.legend(fontsize=8)
ax.grid(alpha=0.3)

# Panneau 2 : Taux de chômage
ax = axes[0, 1]
ax.bar(df["annee"], df["taux_chomage_pct"], color="#c00000")
ax.set_title("2. Taux de chômage")
ax.set_ylabel("%")
ax.set_ylim(0, 15)
ax.grid(alpha=0.3, axis="y")

# Panneau 3 : Inflation
ax = axes[1, 0]
ax.bar(df["annee"], df["taux_inflation_pct"], color="#ed7d31")
ax.set_title("3. Taux d'inflation")
ax.set_ylabel("%")
ax.grid(alpha=0.3, axis="y")

# Panneau 4 : Part de l'agriculture dans le PIB (déclin structurel)
ax = axes[1, 1]
ax.plot(df["annee"], df["part_agriculture_pib_pct"], marker="D", color="#7030a0",
        linewidth=2)
ax.set_title("4. Part de l'agriculture dans le PIB")
ax.set_ylabel("%")
ax.grid(alpha=0.3)

for a in axes.flat:
    a.set_xlabel("Année")
    a.set_xticks(df["annee"])
    a.tick_params(axis="x", rotation=45)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("croissance_maroc_freins.png", dpi=150)
print("\nGraphique sauvegardé : croissance_maroc_freins.png")
