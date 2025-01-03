from genres.repository import GenresRepository
import streamlit as st


class GenresServices:
    def __init__(self):
        self.genre_repository = GenresRepository()

    def get_genres(self):
        if 'genres' in st.session_state:
            return st.session_state.genres
        genres = self.genre_repository.get_genres()
        st.session_state.genres = genres
        return genres

    def post_genre(self, name):
        name = name.strip().title()
        genres_list = self.genre_repository.get_genres()
        for genre in genres_list:
            if genre['name'] == name:
                return st.error('Esse genero já existe')
        genre_data = dict(name=name)
        st.success("Gênero cadastrado com sucesso")
        new_genres = self.genre_repository.post_genre(genre_data)
        st.session_state.genres.append(new_genres)
        return new_genres

    def update_genre(self, id, name):
        name = name.strip().title()
        genres_list = self.genre_repository.get_genres()
        for genre in genres_list:
            if genre['name'] == name:
                return st.error('Esse gênero já existe')
        genre_data = dict(name=name)
        print(self.genre_repository.update_genre(id, genre_data))
        st.success("Gênero atualizado com sucesso.")
        return self.genre_repository.update_genre(id, genre_data)

    def delete_genre(self, id):
        st.success('Gênero deletado com sucesso.')
        return self.genre_repository.delete_genre(id)
