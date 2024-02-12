import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler




with st.container():#Título do texto
    st.header('Análise de Dados das músicas em 2023')
    st.write('---')
    st.subheader('Classificando músicas em energéticas')
bando_dados = pd.read_csv("spotify-2023.csv", sep = ',', encoding='latin1')



# bando_dados.info() # informa descrições a base de dados como quantidade de linha, colunas, tamanho etc

#descricao = bando_dados.describe() #informações que fornecem uma descrição rápida e simples dos dados. Podendo incluir média, mediana, moda, valor mínimo, valor máximo
#print(descricao)

#desvio_padrao_bpm = bando_dados['bpm'].std()#calcular o desvio padrao de bpm
#print(desvio_padrao_bpm)

#plt.figure(figsize=(30,10)) # boxplot para relacionar musicas populares com as dancantes
#sns.boxplot(x='in_spotify_charts', y ='danceability_%', data=bando_dados)
#plt.xlabel('Popularidade no Spotify')
#plt.ylabel('Dancabilidade (%)')
#plt.title('Relacao entre Popularidade e Dançabilidade de Músicas')
#st.pyplot(plt.gcf())

# Criação do gráfico de dispersão
plt.figure(figsize=(10, 6))

#Aplicação do K-Means para agrupar os dados
kmeans = KMeans(n_clusters=4)  # Número de clusters desejado
clusters = kmeans.fit_predict(bando_dados[['liveness_%', 'in_spotify_charts']])

# Mapeamento das cores para os clusters
colors = ['green', 'purple', 'orange','pink']  # Defina as cores dos clusters aqui

for cluster in range(4):
    plt.scatter(bando_dados[clusters == cluster]['liveness_%'], bando_dados[clusters == cluster]['in_spotify_charts'], c=colors[cluster], alpha=0.5)

plt.xlabel('liveness(%)')
plt.ylabel('Pos.Charts')
plt.title('Relação entre Musicas Ao Vivo e Pos. Charts de Musicas com Clusters')

# Exibição do gráfico no Streamlit
st.pyplot(plt) 

#selected_columns = ['danceability_%', 'valence_%']

# Padronize os dados
#scaler = StandardScaler()
#scaled_data = scaler.fit_transform(bando_dados[selected_columns])

# Aplique o algoritmo K-means para a clusterização
#kmeans = KMeans(n_clusters=3)  # Escolha o número de clusters desejado
#bando_dados['cluster'] = kmeans.fit_predict(scaled_data)

#colors = ['lightblue', 'green', 'darkblue']

# Crie um gráfico de dispersão
#sns.set(style='whitegrid')
#plt.figure(figsize=(10, 6))

# Use cores diferentes para cada cluster
#sns.scatterplot(x='danceability_%', y='valence_%', hue='cluster', data=bando_dados, palette='Set1')

# Adicione rótulos aos eixos e um título
#plt.xlabel('Danceability %')
#plt.ylabel('Valence %')
#plt.title('Clusterização de Músicas')

# Mostre o gráfico
#st.pyplot(plt) 

