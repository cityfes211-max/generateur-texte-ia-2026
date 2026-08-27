import streamlit as st
import random

st.set_page_config(page_title="Générateur de Texte IA", page_icon="🤖", layout="centered")

# التصميم احترافي
st.markdown("""
    <style>
    .stApp {background-color: #0E1117;}
    h1 {color: #FFFFFF; text-align: center;}
    p {color: #AAAAAA; text-align: center;}
    </style>
""", unsafe_allow_html=True)

st.title("🤖 Générateur de Texte par IA 2026")
st.markdown("### *L'IA rédige un paragraphe complet sur n'importe quel sujet pour vous*")

sujet = st.text_input("**Votre sujet:**", placeholder="Ex: L'intelligence Artificielle, Le changement climatique...")

if st.button("✨ Générer le texte", use_container_width=True, type="primary"):
    if sujet:
        reponses = [
            f"Le sujet de **{sujet}** est extrêmement important dans notre société actuelle. En effet, **{sujet}** joue un rôle majeur dans notre quotidien et influence notre façon de penser et de travailler. De nombreux experts considèrent que comprendre **{sujet}** est essentiel pour innover et progresser. À l'avenir, **{sujet}** aura un impact encore plus grand dans tous les domaines.",
            
            f"Lorsque nous parlons de **{sujet}**, nous abordons un concept très vaste. **{sujet}** nécessite une recherche et un apprentissage continu. Beaucoup de personnes s'intéressent à **{sujet}** car cela leur permet de résoudre des problèmes et de développer de nouvelles compétences. Il est donc crucial d'accorder à **{sujet}** l'importance qu'il mérite."
        ]
        
        texte_genere = random.choice(reponses)
        st.success("✅ Votre texte est prêt:")
        st.write(texte_genere)
        
        st.download_button(
            label="📄 Télécharger en .txt",
            data=texte_genere,
            file_name=f"Texte_{sujet}.txt",
            mime="text/plain"
        )
    else:
        st.error("⚠️ Veuillez entrer un sujet avant de générer")
