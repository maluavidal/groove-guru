from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
from math import sqrt
import numpy as np
import pandas as pd

# Importe a função clean_data do arquivo data_cleaning.py
from limpeza_dados import clean_data

def calculate_elbow_silhouette(X, k_range, n_samples=1000, max_iter=300, tol=1e-4):
    inertia_values = []
    silhouette_scores = []

    if X.shape[0] > n_samples:
        indices = np.random.choice(X.shape[0], n_samples, replace=False)
        sample_X = X[indices]
    else:
        sample_X = X

    for k in k_range:
        kmeans = KMeans(n_clusters=k, init='k-means++', max_iter=max_iter, tol=tol, random_state=0)
        cluster_labels = kmeans.fit_predict(sample_X)
        inertia_values.append(kmeans.inertia_)

        if k > 1:
            silhouette_avg = silhouette_score(sample_X, cluster_labels)
            silhouette_scores.append(silhouette_avg)

    return inertia_values, silhouette_scores

def optimal_number_of_clusters(wcss):
    distances = []
    for i in range(len(wcss)):
        x0 = i + 2
        y0 = wcss[i]
        x1, y1 = 2, wcss[0]
        x2, y2 = len(wcss) + 1, wcss[-1]
        numerator = abs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1)
        denominator = sqrt((y2 - y1)**2 + (x2 - x1)**2)
        distances.append(numerator / denominator)
    
    return distances.index(max(distances)) + 2

def clustering_methods(df):
    df_numeric = df.select_dtypes(include='number')  # seleciona apenas colunas numéricas
    X = df_numeric.values
    k_range = range(1, 10)
    
    # Modelo do cotovelo
    inertia_values, silhouette_scores = calculate_elbow_silhouette(X, k_range)
    
    plt.figure(figsize=(16, 8))
    plt.plot(k_range, inertia_values, 'bx-')
    plt.xlabel('k')
    plt.ylabel('Distortion')
    plt.title('The Elbow Method showing the optimal k')
    plt.show()
    
    # Método da silhueta 
    plt.figure(figsize=(16, 8))
    plt.plot(k_range[1:], silhouette_scores, 'bx-')
    plt.xlabel('k')
    plt.ylabel('Silhouette Score')
    plt.title('The Silhouette Method showing the optimal k') 
    plt.show()

    # Número ótimo de clusters usando o Método do Cotovelo
    optimal_k_elbow = optimal_number_of_clusters(inertia_values)
    print(f"Número ótimo de clusters (Elbow Method): {optimal_k_elbow}")

    # Número ótimo de clusters usando o Método da Silhueta
    optimal_k_silhouette = silhouette_scores.index(max(silhouette_scores)) + 2
    print(f"Número ótimo de clusters (Silhouette Method): {optimal_k_silhouette}")

    # Treinamento do modelo K-Means com o número ótimo de clusters (escolha o método que preferir)
    optimal_k = optimal_k_elbow  # Pode escolher o resultado do Método do Cotovelo ou da Silhueta
    kmeans_model = train_kmeans_model(X, optimal_k)
    
    return kmeans_model

def train_kmeans_model(X, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    kmeans.fit(X)
    return kmeans

df = clean_data('spotify-2023.csv')
kmeans_model = clustering_methods(df)