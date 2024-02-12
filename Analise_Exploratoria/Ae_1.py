import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

bando_dados = pd.read_csv("spotify-2023.csv", sep = ',', encoding='latin1')

# Criação do gráfico de dispersão
plt.figure(figsize=(15, 10))

#Aplicação do K-Means para agrupar os dados
kmeans = KMeans(n_clusters=5)  # Número de clusters desejado
clusters = kmeans.fit_predict(bando_dados[['parametro_1', 'parametro_2']])

# Mapeamento das cores para os clusters
colors = ['blue', 'green', 'yellow','red', 'purple','#B4E33D','black']  # Defina as cores dos clusters aqui

for cluster in range(7):
    plt.scatter(bando_dados[clusters == cluster]['parametro_1'], bando_dados[clusters == cluster]['parametro_2'], c=colors[cluster], alpha=0.5)

plt.xlabel('Parâmetro')
plt.ylabel('Parâmetro 2')
plt.title('Título da Análise')

# Exibição do gráfico no Streamlit
st.pyplot(plt)