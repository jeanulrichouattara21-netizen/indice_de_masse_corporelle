import streamlit as st

# Fonction de calcul de l'IMC
def calculer_IMC(poids, taille_m):
    return round(poids / (taille_m ** 2), 2)

def afficher_resultat(IMC):
    if IMC < 18.5:
        return "Insuffisance pondérale (maigreur)."
    elif 18.5 <= IMC <= 24.9:
        return "Corpulence normale"
    elif 25 <= IMC <= 29.9:
        return "Surpoids"
    elif 30 <= IMC <= 34.9:
        return "Obésité modérée (classe I)"
    elif 35 <= IMC <= 39.9:
        return "Obésité sévère (classe II)"
    else:
        return "Obésité massive (classe III)"

# Interface utilisateur Streamlit
st.set_page_config(page_title="Calculateur d'IMC", layout="centered")
st.title("Calculateur d'IMC")
st.write("Bienvenue ! Entrez vos données pour connaître votre indice de masse corporelle.")

# Entrées utilisateur
poids = st.number_input("Entrez votre poids (kg)", min_value=1.0, step=0.1)
taille = st.number_input("Entrez votre taille (m)", min_value=0.5, step=0.01)

# Calcul et affichage
if poids and taille:
    imc = calculer_IMC(poids, taille)
    st.subheader(f"Votre IMC est : {imc}")
    st.info(afficher_resultat(imc))