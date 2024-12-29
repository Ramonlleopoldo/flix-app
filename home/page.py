import streamlit as st
from movies.services import MovieServices
import plotly.express as px


def show_home():
    movie_service = MovieServices()
    movie_stats = movie_service.get_movie_stats()

    st.header('Estastisticas de filmes')

    if len(movie_stats['movies_by_genre']) > 0:
        fig = px.pie(
            movie_stats['movies_by_genre'],
            values='count',
            names='genre__name',
            title="Filmes por Gênero"
        )
        st.plotly_chart(fig)

    st.subheader('Total de filmes cadastrados')
    st.write(movie_stats['total_movies'])

    st.subheader("Quantidadede filmes por gênero")
    for genre in movie_stats['movies_by_genre']:
        st.write(f'{genre['genre__name']}: {genre['count']}')

    st.subheader("Total de avaliações:")
    st.write(movie_stats['total_reviews'])

    st.subheader('Media geral de estrelas')
    st.write(movie_stats['average_stars'])
