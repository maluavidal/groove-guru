import streamlit as st
import pandas as pd

def adicionandoColunaCores(arquivo, parametro_1, parametro_2):
    linhas_arquivo = len(arquivo)
    cores_correspondentes = []
    for linhas in range(linhas_arquivo):
        if arquivo.loc[linhas, parametro_1] > 70 and arquivo.loc[linhas, parametro_2] > 150:
            cores_correspondentes.append('#FF0000') #VERMELHO
        elif 70 > arquivo.loc[linhas, parametro_1] and arquivo.loc[linhas, parametro_1] > 30 and 150 > arquivo.loc[linhas, parametro_2] and arquivo.loc[linhas, parametro_2] > 60:
            cores_correspondentes.append('#FFFF00') #AMARELO
        else:
            cores_correspondentes.append('#0000FF') #AZUL
    arquivo['cores'] = cores_correspondentes
    return arquivo

st.set_page_config(page_title= 'GrooveGuru')
with st.container():
    st.header('Análise de Dados das músicas em 2023')
    st.write('---')
    st.subheader('Classificando músicas em energéticas')
banco_dados = pd.read_csv("spotify-2023.csv", sep = ',')
banco_dados = adicionandoColunaCores(banco_dados, 'energy_%', 'bpm')
with st.container():
    linha = 'energy_%'
    coluna = 'bpm'
    st.scatter_chart(
    banco_dados,
    x = linha,
    y = coluna,
    color = 'cores'
)