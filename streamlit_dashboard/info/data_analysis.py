import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show_basic_statistics(dataset):
    """Exibe estatísticas básicas do dataset."""
    print("Estatísticas Básicas:")
    print(dataset.describe())

def plot_feature_distribution(dataset, features, rows_per_group=4):
    """Plota a distribuição de cada característica em grupos de subplots."""
    num_features = len(features)
    num_groups = (num_features + rows_per_group - 1) // rows_per_group

    for group in range(num_groups):
        start_idx = group * rows_per_group
        end_idx = min(start_idx + rows_per_group, num_features)
        group_features = features[start_idx:end_idx]

        fig, axes = plt.subplots(len(group_features), 1, figsize=(10, 4 * len(group_features)))
        if len(group_features) == 1:  # Ajuste para o caso de um único gráfico
            axes = [axes]

        for i, feature in enumerate(group_features):
            sns.histplot(dataset[feature], kde=True, ax=axes[i])
            axes[i].set_title(f'Distribuição de {feature}')
            axes[i].set_xlabel(feature)
            axes[i].set_ylabel('Frequência')

        plt.tight_layout()
        plt.show()

def plot_correlation_matrix(dataset, features):
    """Plota a matriz de correlação entre as características."""
    corr_matrix = dataset[features].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    plt.title('Matriz de Correlação')
    plt.show()

def plot_pairwise_relationships(dataset, features, features_per_plot=4):
    """Plota as relações par-a-par entre subconjuntos das características."""
    num_features = len(features)
    num_plots = (num_features + features_per_plot - 1) // features_per_plot

    for i in range(num_plots):
        start_idx = i * features_per_plot
        end_idx = min(start_idx + features_per_plot, num_features)
        subset_features = features[start_idx:end_idx]

        sns.pairplot(dataset[subset_features])
        plt.show()

def analyse_clusters(kmeans_model, k, X_scaled, features, scaler):
    # Calcular médias das características para cada cluster
    cluster_centers = kmeans_model.cluster_centers_
    cluster_feature_means = scaler.inverse_transform(cluster_centers)
    features_mean_df = pd.DataFrame(cluster_feature_means, columns=features)

    # Exibir o perfil de cada cluster
    for i in range(k):
        print(f"Cluster {i} profile:")
        print(features_mean_df.iloc[i])
        print("\n")