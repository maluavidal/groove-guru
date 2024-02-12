from sklearn.metrics.pairwise import euclidean_distances
import webbrowser

def search_songs(song_name, dataset):
    """Busca músicas que contenham o nome fornecido."""
    return dataset[dataset['track_name'].str.contains(song_name, case=False, na=False)]

def user_song_selection(songs_found):
    print("Músicas encontradas:")
    for index, row in songs_found.iterrows():
        print(f"{index}: {row['track_name']} by {row['artist(s)_name']}")

    selected_song_index = input("Insira o número da música que você está buscando: ")

    try:
        selected_song_index = int(selected_song_index)
        if selected_song_index < 0 or selected_song_index >= len(songs_found):
            print("Índice inválido. Tente novamente.")
            return None
    except ValueError:
        print("Entrada inválida. Insira um número válido.")
        return None

    return selected_song_index


def recommend_songs(user_features, dataset, features, scaler, kmeans_model, rf_model_user, num_recommendations=5):
    # Escalar as características do usuário usando o scaler
    user_features_scaled = scaler.transform(user_features)

    # Prever o cluster do usuário usando o modelo K-Means
    user_cluster = kmeans_model.predict(user_features_scaled)[0]

    # Filtrar o conjunto de dados com base no cluster do usuário
    user_recommendations = dataset[dataset['cluster'] == user_cluster]

    # Selecionar as características relevantes das recomendações do usuário
    user_recommendation_features = user_recommendations[features]

    # Escalar as características das recomendações do usuário usando o scaler
    user_recommendation_features_scaled = scaler.transform(user_recommendation_features)

    # Prever as probabilidades de classificação das recomendações do usuário usando o modelo Random Forest do usuário
    user_recommendation_probs = rf_model_user.predict_proba(user_recommendation_features_scaled)

    # Selecionar as top n recomendações com base nas probabilidades de classificação
    top_recommendations_indices = user_recommendation_probs[:, 1].argsort()[-num_recommendations:][::-1]
    top_recommendations = user_recommendations.iloc[top_recommendations_indices]

    return top_recommendations



def open_spotify_track(track_name):
    """Faz procura da faixa via nome no Spotify."""
    base_url = "https://open.spotify.com/search/"
    url = base_url + track_name
    webbrowser.open(url)