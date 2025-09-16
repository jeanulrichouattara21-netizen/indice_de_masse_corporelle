import streamlit as st
import matplotlib.pyplot as plt

# Initialisation des variables de session
if "page" not in st.session_state:
    st.session_state.page = "accueil"
if "historique" not in st.session_state:
    st.session_state.historique = []

# 🎯 Page d'accueil
if st.session_state.page == "accueil":
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>👋 Bienvenue sur le Calculateur d'IMC</h1>", unsafe_allow_html=True)
    st.markdown("""
    Cette application vous permet de calculer votre Indice de Masse Corporelle (IMC)  
    et de suivre vos résultats tout au long de votre session.
    """)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/BMI_chart.svg/600px-BMI_chart.svg.png", caption="Tableau IMC", use_column_width=True)
    if st.button("Commencer le calcul 🧮"):
        st.session_state.page = "calcul"

# 🧮 Page de calcul
elif st.session_state.page == "calcul":
    st.markdown("<h2 style='color: #4CAF50;'>🧮 Calcul de l'IMC</h2>", unsafe_allow_html=True)

    poids = st.number_input("📦 Poids (kg)", min_value=1.0, step=0.5)
    taille = st.number_input("📏 Taille (m)", min_value=0.5, step=0.01)

    if poids and taille:
        imc = round(poids / (taille ** 2), 2)
        st.markdown(f"## 🧮 Votre IMC est : **{imc}**")

        # Interprétation visuelle
        if imc < 18.5:
            st.warning("⚠️ Maigreur")
        elif imc < 25:
            st.success("✅ Poids normal")
        elif imc < 30:
            st.info("ℹ️ Surpoids")
        else:
            st.error("❌ Obésité")

        # Graphique
        fig, ax = plt.subplots()
        ax.bar(["IMC"], [imc], color="#4CAF50")
        ax.set_ylim(0, 40)
        ax.set_ylabel("Indice")
        st.pyplot(fig)

        # Ajout à l'historique
        st.session_state.historique.append(imc)

    # 📜 Historique des IMC
    if st.session_state.historique:
        st.markdown("### 📜 Historique de vos calculs")
        for i, val in enumerate(st.session_state.historique, 1):
            st.write(f"{i}. IMC : {val}")

    # 🔄 Bouton pour revenir à l'accueil
    if st.button("↩️ Retour à l'accueil"):
        st.session_state.page = "accueil"
