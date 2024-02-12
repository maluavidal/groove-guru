import streamlit as st
import calendar
import locale
from scripts.data_cleaning import clean_data

locale.setlocale(locale.LC_ALL, 'pt_BR')

df = clean_data()

st.title("Visualização de Faixas")
musica = st.selectbox(
    "Selecione uma música: ",
    df['track_name']
)
if musica:
    df.set_index('track_name', inplace=True)
    musica_info = df.loc[[musica]]

    st.header(musica_info.index[0])
    st.subheader(musica_info['artist(s)_name'].iloc[0])
    st.write(f"Lançamento: {musica_info['released_day'].iloc[0]} de {calendar.month_name[musica_info['released_month'].iloc[0]]} de {musica_info['released_year'].iloc[0]}")
    st.write(f"Streams: {musica_info['streams'].iloc[0]}")

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.subheader("Spotify")
        st.write(musica_info['in_spotify_charts'].iloc[0])
    with c2:
        st.subheader("Deezer")
        st.write(musica_info['in_deezer_charts'].iloc[0])
    with c3:
        st.subheader("Apple Music")
        st.write(musica_info['in_apple_charts'].iloc[0])
    with c4:
        st.subheader("Shazam")
        st.write(musica_info['in_shazam_charts'].iloc[0])
else:
    st.write("Por favor, selecione uma música")
