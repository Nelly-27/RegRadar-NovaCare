"""RegRadar - prototype de veille réglementaire pour NovaCare Logistics.

Lancer avec :  streamlit run app.py
"""

import pandas as pd
import streamlit as st

# ---------------------------------------------------------------------------
# 1. Configuration de la page
# ---------------------------------------------------------------------------
st.set_page_config(page_title="RegRadar - NovaCare", page_icon="📡", layout="wide")

# ---------------------------------------------------------------------------
# 2. Les données : une alerte = un dictionnaire.
#    Pour ajouter une alerte, copiez un bloc { ... }, collez-le à la suite
#    et modifiez les valeurs (sans oublier la virgule entre les blocs).
# ---------------------------------------------------------------------------
ALERTES = [
    {
        "Zone": "UE",
        "Source officielle": "EUR-Lex",
        "Lien": "https://eur-lex.europa.eu/eli/reg/2026/1744/oj/fra",
        "Actualité": "Règlement (UE) 2026/1744 (« omnibus numérique IA ») : "
        "report des obligations « haut risque » de l'AI Act",
        "Date": "2026-07-08",
        "Thème": "IA et simplification législative",
        "Impact sur NovaCare": "L'IA qui analyse les patients dispose de plus de temps "
        "pour se mettre en conformité (décembre 2027). "
        "La qualification « haut risque » reste à établir.",
        "Niveau": "Moyen",
    },
    {
        "Zone": "États-Unis",
        "Source officielle": "Federal Register",
        "Lien": "https://www.federalregister.gov/documents/2026/06/25/2026-12909/"
        "securing-the-nation-against-advanced-cryptographic-attacks",
        "Actualité": "Publication du décret 14412 « Securing the Nation Against "
        "Advanced Cryptographic Attacks »",
        "Date": "2026-06-25",
        "Thème": "Cybersécurité et cryptographie",
        "Impact sur NovaCare": "Aucune obligation directe pour une entreprise privée. "
        "Des règles futures viseront les fournisseurs du gouvernement fédéral. "
        "À anticiper dans le choix du chiffrement et des clés.",
        "Niveau": "Faible",
    },
    {
        "Zone": "Asie-Pacifique",
        "Source officielle": "APEC",
        "Lien": "https://www.apec.org/meeting-papers/sectoral-ministerial-meetings/"
        "telecommunicationsandinformation/2026-apec-digital-and-ai-ministerial-statement",
        "Actualité": "Adoption de la déclaration ministérielle de Chengdu "
        "sur le numérique et l'IA",
        "Date": "2026-07-23",
        "Thème": "IA, confiance numérique et flux de données",
        "Impact sur NovaCare": "Texte non contraignant : il signale une orientation "
        "(flux de données, cybersécurité, IA responsable) dans la zone "
        "où NovaCare opère à Singapour.",
        "Niveau": "Faible",
    },
]

# Pastilles de couleur affichées devant le niveau d'impact
PASTILLES = {"Faible": "🟢 Faible", "Moyen": "🟡 Moyen", "Élevé": "🔴 Élevé"}

# Transformation de la liste en tableau (DataFrame) pour pouvoir filtrer
df = pd.DataFrame(ALERTES)
df["Date"] = pd.to_datetime(df["Date"])
df["Niveau d'impact"] = df["Niveau"].map(PASTILLES)

# ---------------------------------------------------------------------------
# 3. Titre
# ---------------------------------------------------------------------------
st.title("📡 RegRadar - veille réglementaire NovaCare")
st.caption(
    "Prototype pédagogique : 3 alertes issues de sources officielles (UE, États-Unis, "
    "Asie-Pacifique) et leur impact potentiel sur NovaCare Logistics."
)

# ---------------------------------------------------------------------------
# 4. Filtres dans la barre latérale
# ---------------------------------------------------------------------------
st.sidebar.header("Filtres")

zones = st.sidebar.multiselect(
    "Zone", sorted(df["Zone"].unique()), default=sorted(df["Zone"].unique())
)
themes = st.sidebar.multiselect(
    "Thème", sorted(df["Thème"].unique()), default=sorted(df["Thème"].unique())
)
niveaux = st.sidebar.multiselect(
    "Niveau d'impact",
    ["Faible", "Moyen", "Élevé"],
    default=["Faible", "Moyen", "Élevé"],
)

# On garde seulement les lignes qui respectent les trois filtres
filtre = (
    df["Zone"].isin(zones) & df["Thème"].isin(themes) & df["Niveau"].isin(niveaux)
)
resultats = df[filtre].sort_values("Date", ascending=False)

# ---------------------------------------------------------------------------
# 5. Indicateurs
# ---------------------------------------------------------------------------
col1, col2, col3 = st.columns(3)
col1.metric("Alertes affichées", len(resultats))
col2.metric("Zones couvertes", resultats["Zone"].nunique())
col3.metric("Impact moyen ou élevé", int(resultats["Niveau"].isin(["Moyen", "Élevé"]).sum()))

# ---------------------------------------------------------------------------
# 6. Tableau des alertes
# ---------------------------------------------------------------------------
st.subheader("Alertes réglementaires")

if resultats.empty:
    st.info("Aucune alerte ne correspond aux filtres choisis.")
else:
    st.dataframe(
        resultats[
            ["Zone", "Actualité", "Date", "Thème", "Niveau d'impact", "Source officielle", "Lien"]
        ],
        hide_index=True,
        column_config={
            "Date": st.column_config.DateColumn("Date", format="DD/MM/YYYY"),
            "Lien": st.column_config.LinkColumn("Lien", display_text="Ouvrir"),
        },
    )

    # -----------------------------------------------------------------------
    # 7. Détail de l'impact pour chaque alerte
    # -----------------------------------------------------------------------
    st.subheader("Impact potentiel sur NovaCare")
    for _, alerte in resultats.iterrows():
        niveau = alerte["Niveau d'impact"]
        with st.expander(f"{alerte['Zone']} - {alerte['Actualité']}"):
            st.markdown(f"**Niveau d'impact :** {niveau}")
            st.markdown(f"**Thème :** {alerte['Thème']}")
            st.markdown(f"**Impact :** {alerte['Impact sur NovaCare']}")
            st.markdown(f"**Source :** [{alerte['Source officielle']}]({alerte['Lien']})")

