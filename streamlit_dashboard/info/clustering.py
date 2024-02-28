from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import silhouette_score, accuracy_score
from math import sqrt
import numpy as np

# Seção de Classificação
def train_random_forest(X_train, y_train):
    """Treina o modelo de Random Forest."""
    rf_model = RandomForestClassifier(random_state=0)
    rf_model.fit(X_train, y_train)
    return rf_model

def evaluate_model(model, X_test, y_test):
    """Avalia o modelo de Random Forest."""
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print("Acurácia do modelo:", accuracy)


# Seção de Clusterização
def calculate_elbow_silhouette(X, k_range, n_samples=1000, max_iter=300, tol=1e-4):
    inertia_values = []
    silhouette_scores = []

    if X.shape[0] > n_samples:
        indices = np.random.choice(X.shape[0], n_samples, replace=False)
        X_sample = X[indices]
    else:
        X_sample = X

    for k in k_range:
        kmeans = KMeans(n_clusters=k, init='k-means++', max_iter=max_iter, tol=tol, random_state=0)
        cluster_labels = kmeans.fit_predict(X_sample)
        inertia_values.append(kmeans.inertia_)
        if k > 1:
            silhouette_avg = silhouette_score(X_sample, cluster_labels)
            silhouette_scores.append(silhouette_avg)

    return inertia_values, silhouette_scores

def optimal_number_of_clusters(wcss):
    """
    Esta função determina o número ótimo de clusters para K-Means usando o Método do Cotovelo.
    O método calcula a distância de cada ponto (valor de WCSS) até uma linha que conecta o primeiro
    e o último ponto da curva WCSS. O wcss é um lista de valores de WCSS (Within-Cluster Sum of Square).

    Ele retorna o número ótimo de clusters baseado na maior distância de um ponto até a linha.
    Esse é o ponto de equilibrio entre a quantidade de clusters e a variação explicada.
    """
    x1, y1 = 2, wcss[0]
    x2, y2 = 20, wcss[len(wcss)-1]

    distances = []
    for i in range(len(wcss)):
        x0 = i + 2
        y0 = wcss[i]
        numerator = abs((y2-y1) * x0 - (x2-x1) * y0 + x2 * y1 - y2 * x1)
        denominator = sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
        distances.append(numerator / denominator)

    return distances.index(max(distances)) + 2

def train_kmeans_model(X, n_clusters):
    """Treina o modelo K-Means com o número especificado de clusters."""
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    kmeans.fit(X)
    return kmeans