import streamlit as st
from scripts.data_cleaning import clean_data

df = clean_data()

individual_artist_names = df['artist(s)_name'].str.split(', ').explode().unique()

st.title("Busque as músicas de seus artistas favoritos!")

artist_names = st.multiselect("Selecione o(s) artista(s):", individual_artist_names)

if st.button("Buscar"):
    if artist_names:
        filtered_df = df[df['artist(s)_name'].str.contains('|'.join(artist_names), case=False)]

        if not filtered_df.empty:
            st.write(f"Foram encontradas {len(filtered_df)} músicas para o(s) artista(s) selecionado(s).")
            st.write("Músicas:")
            st.dataframe(filtered_df[['artist(s)_name', 'track_name', 'released_year']].rename(columns={'artist(s)_name': 'Artista', 'track_name': 'Música', 'released_year': 'Ano de Lançamento'}).drop_duplicates().reset_index(drop=True))
        else:
            st.write("Nenhuma música encontrada para o(s) artista(s) selecionado(s).")
    else:
        st.write("Por favor, selecione pelo menos 1 artista.")
