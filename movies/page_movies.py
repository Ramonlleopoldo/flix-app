import streamlit as st
from movies.services import MovieServices
from genres.services import GenresServices
from actors.service import ActorsService
import pandas as pd
from st_aggrid import AgGrid, ExcelExportMode
from datetime import datetime


def show_movies():
    movies_service = MovieServices()
    list_movies = movies_service.get_movies()

    # Lista de filmes
    if list_movies:
        st.header('Lista de Filmes:')
        movies_df = pd.json_normalize(list_movies)
        movies_df = movies_df.drop(columns=['actors', 'genre.id'])
        AgGrid(
            data=movies_df,
            reload_data=True,
            columns_auto_size_mode=True,
            enableSorting=True,
            enableFilter=True,
            enableColResize=True,
            excel_export_mode=ExcelExportMode.MANUAL,
            key='movies_grid',
        )
    else:
        st.warning('Nenhum filme cadastrado')

    # Cadastrar novo filme
    st.header('Cadastrar novo filme.')
    title = st.text_input("Digite o titulo do novo filme")

    # Capturando generos já registrados para seleção no input
    genre_service = GenresServices()
    list_genre = genre_service.get_genres()
    genre_name_id = {genre['name']: genre['id'] for genre in list_genre}
    selected_genre_name = st.selectbox('Seleciona o gênero', list(genre_name_id.keys()))
    genre_select_user = genre_name_id[selected_genre_name]

    # capturando atores já registrados para seleção no input
    actors_service = ActorsService()
    list_actors = actors_service.get_actors()
    actor_name_id = {actor['name']: actor['id'] for actor in list_actors}
    actor_selected = st.multiselect('Selecione ator', list(actor_name_id.keys()))
    actor_selected_id = [actor_name_id[name] for name in actor_selected]

    # Capturando release_data
    release_data = st.date_input(
        label='Data de lançamento',
        value=datetime.today(),
        min_value=datetime(1800, 1, 1).date(),
        max_value=datetime.today(),
    )
    data_formatada = release_data.strftime("%Y-%m-%d")

    # Resumo
    resume = st.text_area('Resumo:')

    if st.button('salvar'):
        movies_service.post_actors(title=title,
                                   genre=genre_select_user,
                                   actors=actor_selected_id,
                                   release_data=data_formatada,
                                   resume=resume,)
        st.rerun()

    st.header("Deletar filme")
    id_movie = st.text_input('Digite o ID do filme que deseja deletar')
    if st.button('Deletar filme'):
        movies_service.delete_movies(id_movie)
        st.rerun()
