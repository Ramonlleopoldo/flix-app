import streamlit as st
from login.page_login import show_login
from genres.page_genres import show_genres
from actors.page_actors import show_actors
from movies.page_movies import show_movies
from reviews.page_reviews import show_reviews


def main():
    if 'token' not in st.session_state:
        show_login()
    else:
        # menu de navegaçãos
        add_selectbox = st.sidebar.selectbox(
            "Selecione uma açãa",
            ("Inicio", "Generos", "Atores/Atrizes", "Lista de Filmes", "Avaliações")
        )
        if add_selectbox == "Inicio":
            st.title("Bem vindo ao flix API")
        if add_selectbox == "Generos":
            show_genres()
        if add_selectbox == "Atores/Atrizes":
            show_actors()
        if add_selectbox == "Lista de Filmes":
            show_movies()
        if add_selectbox == "Avaliações":
            show_reviews()


if __name__ == '__main__':
    main()
