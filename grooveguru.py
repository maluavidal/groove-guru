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

# Criação do gráfico de dispersão
plt.figure(figsize=(10, 6))

#Aplicação do K-Means para agrupar os dados
kmeans = KMeans(n_clusters=3)  # Número de clusters desejado
clusters = kmeans.fit_predict(banco_dados[['liveness_%', 'acousticness_%']])



# Cluster Novo Criação do gráfico de dispersão Performace Ao Vivo
plt.figure(figsize=(10, 6))

#Aplicação do K-Means para agrupar os dados
kmeans = KMeans(n_clusters=5)  # Número de clusters desejado
clusters = kmeans.fit_predict(banco_dados[['bpm', 'liveness_%']])

#Mapeamento das cores para os clusters
colors = ['blue', 'green', 'yellow', 'purple','#19FFA7']  # Defina as cores dos clusters aqui

for cluster in range(5):
    plt.scatter(banco_dados[clusters == cluster]['bpm'], banco_dados[clusters == cluster]['liveness_%'], c=colors[cluster], alpha=0.5)

plt.xlabel('BPM')
plt.ylabel('Perfomaces ao Vivo (%)')
plt.title('Relação entre BPM e Performaces ao Vivo')

#Exibição do gráfico no Streamlit   
st.pyplot(plt)


# Cluster Novo Criação do gráfico de dispersão Acústico
plt.figure(figsize=(10, 6))

#Aplicação do K-Means para agrupar os dados
kmeans = KMeans(n_clusters=5)  # Número de clusters desejado
clusters = kmeans.fit_predict(banco_dados[['bpm', 'acousticness_%']])

#Mapeamento das cores para os clusters
colors = ['red', 'green', 'blue', 'purple','#19FFA7']  # Defina as cores dos clusters aqui

for cluster in range(5):
    plt.scatter(banco_dados[clusters == cluster]['bpm'], banco_dados[clusters == cluster]['acousticness_%'], c=colors[cluster], alpha=0.5)

plt.xlabel('BPM')
plt.ylabel('Musicas Acústicas (%)')
plt.title('Relação entre BPM e Músicas Acústicas')

#Exibição do gráfico no Streamlit   
st.pyplot(plt)


# Cluster Novo Criação do gráfico de dispersão Instrumental
plt.figure(figsize=(10, 6))

#Aplicação do K-Means para agrupar os dados
kmeans = KMeans(n_clusters=5)  # Número de clusters desejado
clusters = kmeans.fit_predict(banco_dados[['bpm', 'instrumentalness_%']])

#Mapeamento das cores para os clusters
colors = ['red', 'green', 'blue', 'purple','#19FFA7']  # Defina as cores dos clusters aqui

for cluster in range(5):
    plt.scatter(banco_dados[clusters == cluster]['bpm'], banco_dados[clusters == cluster]['instrumentalness_%'], c=colors[cluster], alpha=0.5)

plt.xlabel('BPM')
plt.ylabel('Elementos Instrumentais (%)')
plt.title('Relação entre BPM e Tipos de Elementos Instrumentais')

#Exibição do gráfico no Streamlit   
st.pyplot(plt)
