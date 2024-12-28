import streamlit as st
from movies.repository import MovieDirectory


class MovieServices:
    def __init__(self):
        self.movie_service = MovieDirectory()

    def get_movies(self):
        return self.movie_service.get_movies()

    def post_actors(self, title, genre, actors, release_data, resume):
        title = title.strip().title()
        movie = dict(
            title=title,
            genre=genre,
            actors=actors,
            release_data=release_data,
            resume=resume,
        )
        st.success(f'Filme "{title}" Salvo com sucesso')
        return self.movie_service.post_movies(movie)

    def delete_movies(self, id):
        st.success("Filme deletado com sucesso!")
        return self.movie_service.delete_movies(id)
