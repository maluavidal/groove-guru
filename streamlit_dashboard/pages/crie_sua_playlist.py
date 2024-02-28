import pandas as pd
import streamlit as st
from scripts.data_cleaning import clean_data

df = clean_data()

def create_playlist():
    st.title("Criar Playlist")
    new_playlist_name = st.text_input("Digite o nome da nova playlist:")

    if st.button("Criar Playlist") and new_playlist_name:
        st.session_state[new_playlist_name] = []
        st.success(f"Playlist '{new_playlist_name}' criada com sucesso!")

    existing_playlists = list(st.session_state.keys())

    if existing_playlists:
        st.write("Playlists existentes:")
        for playlist_name in existing_playlists:
            st.write(f"- {playlist_name}")

def add_songs():
    st.title("Adicionar Músicas à Playlist")
    selected_playlist = st.selectbox("Selecione a playlist:", [""] + list(st.session_state.keys()))

    if selected_playlist:
        playlist = st.session_state.get(selected_playlist, [])
        selected_songs = st.multiselect("Selecione as músicas:", df['track_name'])
        if st.button("Adicionar à Playlist") and selected_songs:
            playlist.extend([song for song in selected_songs if song not in playlist])
            st.session_state[selected_playlist] = playlist
            st.success("Músicas adicionadas à playlist com sucesso!")

    if selected_playlist:
        st.write("Músicas na Playlist:")
        for i, song in enumerate(playlist, start=1):
            st.write(f"{i}. {song}")

        if not playlist:
            st.write("Nenhuma música na Playlist.")

def remove_songs():
    st.title("Remover Músicas da Playlist")
    selected_playlist = st.selectbox("Selecione a playlist:", [""] + list(st.session_state.keys()))

    if selected_playlist:
        playlist = st.session_state.get(selected_playlist, [])
        if playlist:
            songs_to_remove = st.multiselect("Selecione as músicas a serem removidas:", playlist)
            if st.button("Remover Músicas") and songs_to_remove:
                st.session_state[selected_playlist] = [song for song in playlist if song not in songs_to_remove]
                st.success("Músicas removidas da playlist com sucesso!")

    if selected_playlist:
        display_playlist(selected_playlist)


def display_playlist(playlist_name):
    playlist = st.session_state.get(playlist_name, [])
    if playlist:
        st.write("Músicas na Playlist:")
        for i, song in enumerate(playlist, start=1):
            st.write(f"{i}. {song}")
    else:
        st.write("Nenhuma música na Playlist.")

def main():
    st.sidebar.title("Menu")
    pages = {
        "Criar Playlist": create_playlist,
        "Adicionar Músicas": add_songs,
        "Remover Músicas": remove_songs,
    }
    page = st.sidebar.radio("Selecione a ação:", tuple(pages.keys()))
    pages[page]()

if __name__ == "__main__":
    main()
