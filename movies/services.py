import streamlit as st
from movies.repository import Movierepository


class MovieServices:
    def __init__(self):
        self.movie_service = Movierepository()

    def get_movies(self):
        if 'movie' in st.session_state:
            return st.session_state.movie
        movie = self.movie_service.get_movies()
        st.session_state.movie = movie
        return movie

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
        new_movie = self.movie_service.post_movies(movie)
        st.session_state.movie.append(new_movie)
        return new_movie

    def delete_movies(self, id):
        st.success("Filme deletado com sucesso!")
        return self.movie_service.delete_movies(id)

    def get_movie_stats(self):
        return self.movie_service.get_movie_stats()
