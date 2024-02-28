import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(file_name):
    # Carregar o conjunto de dados
    try:
        df = pd.read_csv(file_name, encoding='utf-8')
    except UnicodeDecodeError:
        try:
            df = pd.read_csv(file_name, encoding='latin1')
        except UnicodeDecodeError:
            df = pd.read_csv(file_name, encoding='iso-8859-1')


    # Removendo linhas com qualquer valor vazio
    df = df.dropna()

    # Substituir vírgulas por pontos na coluna 'in_shazam_charts'
    df['in_shazam_charts'] = df['in_shazam_charts'].str.replace(',', '.')

    # Converter a coluna 'in_shazam_charts' para float
    df['in_shazam_charts'] = df['in_shazam_charts'].astype(float)

    # Transformar coluna 'key' em valores numéricos
    key_encoder = LabelEncoder()
    df['key'] = key_encoder.fit_transform(df['key'])

    # Transformar coluna 'mode' em valores numéricos
    mode_encoder = LabelEncoder()
    df['mode'] = mode_encoder.fit_transform(df['mode'])

    label_encoder = LabelEncoder()
    for col in df.columns:
        if df[col].dtype == 'object' and col not in ['track_name', 'artist(s)_name']:
            df[col] = label_encoder.fit_transform(df[col])

    return df

def select_features(dataset, features):
    """Seleciona apenas as características relevantes do dataset."""
    return dataset[features]

def scale_features(X):
    """Escala as características usando StandardScaler."""
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, scaler


# Exemplo de uso
file_path = 'spotify-2023.csv'
spotify_data = preprocess_data(file_path)

# Visualizar as primeiras linhas do conjunto de dados pré-processado
print(spotify_data.head())