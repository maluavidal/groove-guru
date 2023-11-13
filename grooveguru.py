import streamlit as st
import pandas as pd
import numpy as np
#import seaborn as sns
#import matplotlib.pyplot as plt
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

bando_dados.info() # informa descrições a base de dados como quantidade de linha, colunas, tamanho etc

descricao = banco_dados.describe() #informações que fornecem uma descrição rápida e simples dos dados. Podendo incluir média, mediana, moda, valor mínimo, valor máximo
print(descricao)

desvio_padrao_bpm = bando_dados['bpm'].std()#calcular o desvio padrao de bpm
print(desvio_padrao_bpm)

plt.figure(figsize=(10,6)) # boxplot para relacionar musicas populares com as dancantes
sns.boxplot(x='in_spotify_charts', y ='danceability_%')
plt.xlabel('Popularidade no Spotify')
plt.ylabel('Dancabilidade (%)')
plt.title('Relacao entre Popularidade e Dançabilidade de Músicas')
plt.show()




