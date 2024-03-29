from streamlit_dashboard.info.data_preprocessing import preprocess_data, select_features, scale_features
from streamlit_dashboard.info.clustering import calculate_elbow_silhouette, optimal_number_of_clusters, train_kmeans_model, train_random_forest, evaluate_model, train_svm, train_knn, train_gradient_boosting
from recmendacao import recommend_songs, open_spotify_track
from streamlit_dashboard.info.data_analysis import show_basic_statistics, analyse_clusters
from sklearn.model_selection import train_test_split
import pandas as pd

features = [
        'danceability_%',
        'valence_%',
        'bpm',
        'energy_%',
        'acousticness_%',
        'instrumentalness_%',
        'liveness_%',
        'speechiness_%',
        'key',
        'mode'
    ]

def compare_models(X_train, X_test, y_train, y_test):
    models = {
        'Random Forest': train_random_forest(X_train, y_train),
        'SVM': train_svm(X_train, y_train),
        'k-NN': train_knn(X_train, y_train),
        'Gradient Boosting': train_gradient_boosting(X_train, y_train)
    }

    model_metrics = {}
    for name, model in models.items():
        print(f"Avaliando modelo: {name}")
        metrics = evaluate_model(model, X_test, y_test)
        model_metrics[name] = metrics

    best_model = None
    best_score = -1
    for name, metrics in model_metrics.items():
        score = (metrics['accuracy'] + metrics['recall'] + metrics['f1'] + metrics['precision']) / 4
        if score > best_score:
            best_model = name
            best_score = score

    print(f"Melhor modelo com base na pontuação geral: {best_model} (Pontuação: {best_score})")
    return models[best_model]

def get_user_preferences():
    # Solicitar ao usuário suas preferências musicais
    favorite_artists = input("Quais são seus artistas favoritos? (separados por vírgula): ").split(',')
    favorite_songs = input("Quais são suas músicas favoritas? (separadas por vírgula): ").split(',')

    return favorite_artists, favorite_songs

def search_user_preferences(dataset, favorite_artists, favorite_songs):
    # Consultar o conjunto de dados para identificar músicas e artistas correspondentes
    user_favorite_songs = dataset[dataset['track_name'].isin(favorite_songs)]
    user_favorite_artists = dataset[dataset['artist(s)_name'].isin(favorite_artists)]

    return user_favorite_songs, user_favorite_artists


def build_user_training_dataset(user_favorite_songs, user_favorite_artists):
    # Concatenar músicas e artistas preferidos pelo usuário
    user_training_data = pd.concat([user_favorite_songs, user_favorite_artists])

    # Selecionar características relevantes e atributo de cluster
    user_training_features = user_training_data[['danceability_%', 'valence_%', 'bpm', 'energy_%', 'acousticness_%',
                                                 'instrumentalness_%', 'liveness_%', 'speechiness_%', 'key', 'mode']]
    user_training_labels = user_training_data['cluster']

    return user_training_features, user_training_labels

def assign_clusters_to_user_preferences(user_favorite_songs, user_favorite_artists, kmeans_model, scaler):
    user_features = user_favorite_songs._append(user_favorite_artists)
    user_features = user_features.drop(columns=['track_name', 'artist(s)_name'])  # Remover colunas não utilizadas

    # Selecionar apenas as características relevantes
    user_features = select_features(user_features, features)

    # Escalar as características usando o scaler fornecido
    user_features_scaled = scaler.transform(user_features)

    # Atribuir clusters com base nas características escaladas
    user_clusters = kmeans_model.predict(user_features_scaled)

    # Adicionar a coluna de cluster ao conjunto de dados do usuário
    user_favorite_songs['cluster'] = user_clusters[:len(user_favorite_songs)]
    user_favorite_artists['cluster'] = user_clusters[len(user_favorite_songs):]

    return user_favorite_songs, user_favorite_artists, user_features_scaled

def main():
    file_path = 'spotify-2023.csv'

    dataset = preprocess_data(file_path)

    sample_size = 800
    dataset_sample = dataset.sample(n=sample_size, random_state=0)

    show_basic_statistics(dataset_sample)

    # Preparação e normalização das características para todo o conjunto de dados
    X = select_features(dataset, features)
    X_scaled, scaler = scale_features(X)

    # Calcular o Método Elbow e o Coeficiente de Silhueta
    k_range = range(2, 21)
    inertia_values, silhouette_scores = calculate_elbow_silhouette(X_scaled, k_range)

    # Encontrar o número ótimo de clusters
    optimal_k = optimal_number_of_clusters(inertia_values)
    print("Número ótimo de clusters:", optimal_k)

    # Treinar o modelo K-Means
    kmeans_model = train_kmeans_model(X_scaled, optimal_k)

    # Adicionando a coluna de cluster ao dataset
    dataset['cluster'] = kmeans_model.predict(X_scaled)
    analyse_clusters(kmeans_model, optimal_k, X_scaled, features, scaler)

    # Coletar preferências do usuário
    favorite_artists, favorite_songs = get_user_preferences()

    # Consultar o conjunto de dados para identificar músicas e artistas correspondentes
    user_favorite_songs, user_favorite_artists = search_user_preferences(dataset, favorite_artists, favorite_songs)

    # Atribuir clusters aos itens de preferência do usuário e ajustar um novo scaler
    user_favorite_songs, user_favorite_artists, scaler_user = assign_clusters_to_user_preferences(user_favorite_songs, user_favorite_artists, kmeans_model, scaler)

    # Construir conjunto de dados de treinamento do usuário
    X_user, y_user = build_user_training_dataset(user_favorite_songs, user_favorite_artists)

    # Dividir o conjunto de dados do usuário em treinamento e teste
    X_train, X_test, y_train, y_test = train_test_split(X_user, y_user, test_size=0.2, random_state=0)

    # Comparar modelos e selecionar o melhor
    best_model = compare_models(X_train, X_test, y_train, y_test)

    # Recomendar músicas com base nas preferências do usuário
    recommendations = recommend_songs(X_user, dataset, features, scaler, kmeans_model, best_model, num_recommendations=5)
    print("Músicas recomendadas:")
    print(recommendations[['track_name', 'artist(s)_name']])

    '''Permitir ao usuário abrir uma música recomendada no Spotify'''
    track_name_input = input("Digite o nome da música que você quer ouvir no Spotify ou 'sair' para finalizar: ")
    if track_name_input.lower() != 'sair':
        open_spotify_track(track_name_input)

if __name__ == "__main__":
    main()
