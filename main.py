import streamlit as st
import pandas as pd


def get_crew_recommendation(length):
    if 12 <= length <= 15:
        return "1 membre d'équipage"
    elif 16 <= length <= 22:
        return "2 membres d'équipage"
    elif 23 <= length <= 27:
        return "3 membres d'équipage"
    elif 28 <= length <= 33:
        return "4 à 5 membres d'équipage"
    elif 34 <= length <= 40:
        return "6 à 7 membres d'équipage"
    elif 41 <= length <= 50:
        return "7 à 8 membres d'équipage"
    elif 51 <= length <= 60:
        return "9 à 12 membres d'équipage"
    return "1 membre d'équipage"


def calculate_crew_cost(length):
    if 12 <= length <= 15:
        return 45000
    elif 16 <= length <= 22:
        return 75000
    elif 23 <= length <= 27:
        return 110000
    elif 28 <= length <= 33:
        return 250000
    elif 34 <= length <= 40:
        return 325000
    elif 41 <= length <= 50:
        return 430000
    elif 51 <= length <= 60:
        return 570000
    return 45000


def calculate_yearly_costs(yacht_value, length):
    insurance = yacht_value * 0.005
    maintenance = yacht_value * 0.03
    docking = length * 1000
    crew_cost = calculate_crew_cost(length)
    consumables = yacht_value * 0.0030

    return {
        "Assurance": insurance,
        "Maintenance": maintenance,
        "Frais d'amarrage": docking,
        "Équipage": crew_cost,
        "Consommables": consumables
    }


def format_currency(amount):
    return f"{amount:,.2f} €"


def main():
    st.title("💫 Calculateur de Coûts d'Entretien de Yacht")

    st.write("""
   Cet outil vous aide à estimer les coûts annuels d'entretien de votre yacht.
   Veuillez remplir les informations ci-dessous pour obtenir une estimation.
   """)

    st.warning("""
    ⛵ Ce calculateur est destiné aux bateaux **entre 12 et 60 mètres** de longueur ou d'**une valeur comprise entre 500 000€ et 20 millions d'euros avec un equipage** 💶
    """)

    col1, col2 = st.columns(2)

    with col1:
        yacht_value = st.number_input(
            "Valeur du yacht (€)",
            min_value=500000,
            max_value=20000000,
            value=1000000,
            step=100000,
            help="Entrez la valeur actuelle de votre yacht"
        )

    with col2:
        length = st.number_input(
            "Longueur du yacht (mètres)",
            min_value=12,
            max_value=60,
            value=12,
            step=1,
            help="Entrez la longueur totale du yacht"
        )

    crew_recommendation = get_crew_recommendation(length)
    st.write("### 👥 Équipage recommandé")
    st.info(f"Pour un yacht de {length} mètres, la recommandation est de : **{crew_recommendation}**")

    costs = calculate_yearly_costs(yacht_value, length)

    st.header("Estimation des Coûts Annuels")

    st.write("### Détail des coûts")
    for category, cost in costs.items():
        col1, col2 = st.columns([2, 1])
        col1.write(f"**{category}**")
        col2.write(format_currency(cost))
        if category == "Frais d'amarrage":
            st.caption("*Les coûts mentionnés sont spécifiques au secteur de la **Côte d'Azur**.*")

    total_cost = sum(costs.values())
    st.markdown("---")
    st.metric(
        "Coût Total Annuel",
        format_currency(total_cost),
        f"{(total_cost / yacht_value) * 100:.1f}% de la valeur du yacht"
    )

    st.header("Répartition des Coûts")
    df = pd.DataFrame({
        'Catégorie': list(costs.keys()),
        'Coût': list(costs.values())
    })
    df = df.set_index('Catégorie')
    st.bar_chart(df)

    st.info("""
   ℹ️ Note : Ces calculs sont des estimations basées sur des moyennes du secteur.
   Les coûts réels peuvent varier en fonction de nombreux facteurs, notamment :
   - La localisation et les tarifs d'amarrage locaux
   - L'âge et l'état du yacht
   - Le type de maintenance requis
   - Les salaires locaux de l'équipage
   - La consommation réelle des consommables
   """)


if __name__ == "__main__":
    main()