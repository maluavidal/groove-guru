import streamlit as st
from  plotagem import plot_pca, plot_elbow_method, plot_silhouette_coefficient
from scripts.data_cleaning import clean_data
from data_preprocessing import scale_features, select_features,preprocess_data
from data_analysis import plot_correlation_matrix,plot_feature_distribution
from clustering import calculate_elbow_silhouette



st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Análise de Dados com Streamlit")

# Carregar e limpar os dados
df = clean_data()
file_path = 'archive/all/spotify-2023.csv'
df = preprocess_data(file_path)

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
# Visualização dos dados
st.header("Visualização dos Dados")


X = select_features(df, features)
X_scaled, scaler = scale_features(X)

# Calcular o Método Elbow e o Coeficiente de Silhueta
k_range = range(2, 21)
inertia_values, silhouette_scores = calculate_elbow_silhouette(X_scaled, k_range)

# Visualizações
st.subheader("Visualizão do método elbow para Encontrar o Número de Clusters")
st.write("O gráfico representa o método usado para determinar o número ideal de clusters em agrupamentos K-Means.O gráfico em questão mostra uma queda acentuada na inércia até cerca de 5 a 7 clusters, após o qual ela começa a nivelar, indicando um ponto de “cotovelo” em que indica o número ideal de clusters.")
st.pyplot(plot_elbow_method(k_range,inertia_values))
st.subheader("Visualizão da Matriz de Correlação entre os Atributos")
st.write("A matriz a seguir ajuda a entender como os atributos musicais se relacionam entre si. ")

st.pyplot(plot_correlation_matrix(df,features))

st.subheader("Visualizão do Gráfico do Coeficiente de Silhueta")
st.write("O gráfico a seguir nos permite indentificar através do coeficiente de silhueta a qualidade da separação dos clusters do algoritmo.")

st.pyplot(plot_silhouette_coefficient(k_range,silhouette_scores))

st.subheader("Visualizão do PCA")

st.pyplot(plot_pca(X_scaled))
st.subheader("Distribuição de cada Característica em Grupos de Subplots")
st.write("Gráfico ilustra a frequencia com que as medidas das caracteristicas aparecem.")
st.pyplot(plot_feature_distribution(df,features))
#plot_silhouette_coefficient(k_range, silhouette_scores)  # Visualização do Coeficiente de Silhueta


# Visualização da Redução de Dimensionalidade usando PCA
# plot_pca(X_scaled)
# plot_elbow_method(k_range,inertia_values)
# plot_correlation_matrix(df,features)
# plot_pairwise_relationships(df,features)
