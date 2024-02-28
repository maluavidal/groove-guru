import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def plot_pca(X_scaled):
    """Visualiza a redução de dimensionalidade usando PCA."""
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)

    plt.figure(figsize=(8, 6))
    plt.scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.5)
    plt.title('PCA de Amostra de Dados')
    plt.xlabel('Componente Principal 1')
    plt.ylabel('Componente Principal 2')
    plt.grid(True)
    plt.show()

def plot_elbow_method(k_range, inertia_values):
    """Visualiza o Método Elbow para ajudar a determinar o número ótimo de clusters."""
    plt.figure(figsize=(8, 6))
    plt.plot(k_range, inertia_values, 'bo-')
    plt.title('Método Elbow para K-Means Clustering')
    plt.xlabel('Número de Clusters (k)')
    plt.ylabel('Inércia')
    plt.grid(True)
    plt.show()

def plot_silhouette_coefficient(k_range, silhouette_scores):
    """Visualiza o Coeficiente de Silhueta para cada valor de k."""
    plt.figure(figsize=(8, 6))
    plt.plot(k_range, silhouette_scores, 'ro-')
    plt.title('Coeficiente de Silhueta para K-Means Clustering')
    plt.xlabel('Número de Clusters (k)')
    plt.ylabel('Coeficiente de Silhueta')
    plt.grid(True)
    plt.show()