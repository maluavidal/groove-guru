import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(page_title= 'GrooveGuru')

with st.container():#Título do texto
    st.header('Análise de Dados das músicas em 2023')
    st.write('---')
    st.subheader('Classificando músicas em energéticas')
bando_dados = pd.read_csv("spotify-2023.csv", sep = ',')
mais_energetica = bando_dados[bando_dados['energy_%'] > 50]
menos_energetica = bando_dados[bando_dados['energy_%'] < 50]
print(menos_energetica)
with st.container():
    st.scatter_chart(bando_dados, x='energy_%', y='track_name',)
