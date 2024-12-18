import streamlit as st
import json


def calculate_yearly_costs(yacht_value, length, crew_members):
    # Coûts annuels estimés en pourcentage de la valeur du yacht
    insurance = yacht_value * 0.01  # 1% pour l'assurance
    maintenance = yacht_value * 0.03  # 3% pour la maintenance générale

    # Coûts d'amarrage basés sur la longueur (estimation : 1000€ par mètre par an)
    docking = length * 1000

    # Coûts d'équipage (estimation : 45000€ par membre d'équipage par an)
    crew_cost = crew_members * 45000

    # Carburant et autres consommables (estimation : 2% de la valeur du yacht)
    fuel_supplies = yacht_value * 0.02

    return {
        "Assurance": insurance,
        "Maintenance": maintenance,
        "Frais d'amarrage": docking,
        "Équipage": crew_cost,
        "Carburant et consommables": fuel_supplies
    }


def format_currency(amount):
    return f"{amount:,.2f} €"


def main():
    st.title("💫 Calculateur de Coûts d'Entretien de Yacht")

    st.write("""
    Cet outil vous aide à estimer les coûts annuels d'entretien de votre yacht.
    Veuillez remplir les informations ci-dessous pour obtenir une estimation.
    """)

    # Inputs
    col1, col2 = st.columns(2)

    with col1:
        yacht_value = st.number_input(
            "Valeur du yacht (€)",
            min_value=100000,
            max_value=100000000,
            value=1000000,
            step=100000,
            help="Entrez la valeur actuelle de votre yacht"
        )

        length = st.number_input(
            "Longueur du yacht (mètres)",
            min_value=5,
            max_value=100,
            value=15,
            step=1,
            help="Entrez la longueur totale du yacht"
        )

    with col2:
        crew_members = st.number_input(
            "Nombre de membres d'équipage",
            min_value=0,
            max_value=20,
            value=2,
            step=1,
            help="Entrez le nombre total de membres d'équipage nécessaires"
        )

    # Calcul des coûts
    costs = calculate_yearly_costs(yacht_value, length, crew_members)

    # Affichage des résultats
    st.header("Estimation des Coûts Annuels")

    # Création d'un tableau personnalisé
    st.write("### Détail des coûts")
    for category, cost in costs.items():
        col1, col2 = st.columns([2, 1])
        col1.write(f"**{category}**")
        col2.write(format_currency(cost))

    # Calcul et affichage du coût total
    total_cost = sum(costs.values())
    st.markdown("---")
    st.metric(
        "Coût Total Annuel",
        format_currency(total_cost),
        f"{(total_cost / yacht_value) * 100:.1f}% de la valeur du yacht"
    )

    # Graphique simple avec streamlit
    st.header("Répartition des Coûts")
    chart_data = {
        "categories": list(costs.keys()),
        "values": list(costs.values())
    }
    st.bar_chart(chart_data["values"], use_container_width=True)

    # Notes et avertissements
    st.info("""
    ℹ️ Note : Ces calculs sont des estimations basées sur des moyennes du secteur.
    Les coûts réels peuvent varier en fonction de nombreux facteurs, notamment :
    - La localisation et les tarifs d'amarrage locaux
    - L'âge et l'état du yacht
    - Le type de maintenance requis
    - Les salaires locaux de l'équipage
    - La consommation réelle de carburant
    """)


if __name__ == "__main__":
    main()