import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from reviews.service import ReviewsService
from movies.services import MovieServices


def show_reviews():
    options = [0, 1, 2, 3, 4, 5]
    reviews_service = ReviewsService()
    list_reviews = reviews_service.get_reviews()

    # Lista de avaliações
    if list_reviews:
        st.header("Avaliações")
        st.write("Avaliações registradas:")
        AgGrid(data=pd.DataFrame(list_reviews),
               reload_data=True,
               key='genres_grid')
    else:
        st.warning("Nenhuma avalição registrada!")

    # Cadastro de nova avaliação
    st.title('Cadastrar nova avaliação')
    user_name = st.text_input("Digite seu nome")

    # Capturando lista de filmes para usuario escolher no input
    movie_service = MovieServices()
    list_movies = movie_service.get_movies()
    movie_name_id = {movie["title"]: movie["id"] for movie in list_movies}
    selected_movie_name = st.selectbox("Filme que deseja avaliar:", list(movie_name_id.keys()))
    selected_movie_id = movie_name_id[selected_movie_name]

    # Capturando nota
    stars = st.selectbox('Nota:', options)

    # Capturando comentario
    coments = st.text_area("Comentario:")

    if st.button('Salvar'):
        reviews_service.post_reviews(user_name=user_name, movie=selected_movie_id, stars=stars, coments=coments)
        st.rerun()
