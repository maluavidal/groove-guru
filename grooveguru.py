import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


with st.container():#Título do texto
    st.header('Análise de Dados das músicas em 2023')
    st.write('Análise de Estilos e Visualizações')
    st.subheader('Comparando Popularidade com Dançabilidade')

banco_dados = pd.read_csv("spotify-2023.csv", sep = ',', encoding='latin1')

banco_dados.info() # informa descrições a base de dados como quantidade de linha, colunas, tamanho etc
st.write(banco_dados.head(1000))

banco_dados.info() # informa descrições a base de dados como quantidade de linha, colunas, tamanho etc
descricao = banco_dados.describe() #informações que fornecem uma descrição rápida e simples dos dados. Podendo incluir média, mediana, moda, valor mínimo, valor máximo
st.write(descricao)

desvio_padrao_bpm = banco_dados['bpm'].std() #calcular o desvio padrao de bpm
st.write(desvio_padrao_bpm)

plt.figure(figsize=(30,10)) # boxplot para relacionar musicas populares com as dancantes
sns.boxplot(x='in_spotify_charts', y ='danceability_%', data=banco_dados)  # Adicione 'data=banco_dados' aqui
plt.xlabel('Popularidade no Spotify')
plt.ylabel('Dancabilidade (%)')
plt.title('Relacao entre Popularidade e Dançabilidade de Músicas')
st.pyplot(plt.gcf())  # Adicione esta linha para exibir o gráfico no Streamlit

#plt.figure(figsize=(10,6))
#plt.scatterplot(data=banco_dados, x='acousticness_%', y='liveness_%', size='streams', sizes=(1, 100), alpha=0.5)
#plt.xlabel('Acústica (%)')
#plt.ylabel('Ao Vivo (%)')
#plt.title('Relação entre Músicas Acústicas e Ao Vivo com Popularidade')
#st.pyplot(plt.gcf())  # Adicione esta linha para exibir o gráfico no Streamlit

# Criação do gráfico de dispersão
plt.figure(figsize=(10, 6))

#Aplicação do K-Means para agrupar os dados
kmeans = KMeans(n_clusters=3)  # Número de clusters desejado
clusters = kmeans.fit_predict(banco_dados[['liveness_%', 'acousticness_%']])

# Mapeamento das cores para os clusters
colors = ['red', 'blue', 'green']  # Defina as cores dos clusters aqui

for cluster in range(3):
    plt.scatter(banco_dados[clusters == cluster]['liveness_%'], banco_dados[clusters == cluster]['acousticness_%'], c=colors[cluster], alpha=0.5)

plt.xlabel('Liveness (%)')
plt.ylabel('Acousticness (%)')
plt.title('Relação entre Acüstica nas Músicas e Músicas Ao Vivo')

# Exibição do gráfico no Streamlit
st.pyplot(plt) 
