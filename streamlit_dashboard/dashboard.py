import streamlit as st

st.title("Dashboard GrooveGuru")
st.write("Esta ferramenta tem por finalidade oferecer uma visualização simples e eficaz das funcionalidades do GrooveGuru.")
st.markdown(
    """
    **👈 Selecione uma aba** para visualizar detalhadamente.
    #### Sitemap:
    - Home: Esta página, clicando nela você retornará para cá.
    - Visualização das faixas: Filtre uma faixa específica e receba suas informações.
    - Visão Global: Informações gerais sobre o dataset e insights dele extraídos.
    - Recomendação personalizada de músicas: Receba recomedações musicais com base nas suas preferências pessoais!

    #### Para mais informações:

    - Visite nosso [Github](https://github.com/maluavidal/groove-guru)
    - Visualize o [Dataset](https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023)

    """
)
st.sidebar.success("Selecione uma página acima.")

