import streamlit as st

st.title("🤖 Générateur de Texte IA 2026")
st.write("اكتب أي موضوع والـ AI يكتب ليك فقرة")

sujet = st.text_input("Votre sujet:")

if st.button("Générer"):
    if sujet:
        texte = f"Le {sujet} est un sujet très important. Il influence notre vie et notre futur."
        st.success("Voici votre texte:")
        st.write(texte)
    else:
        st.error("Écrivez un sujet svp")
