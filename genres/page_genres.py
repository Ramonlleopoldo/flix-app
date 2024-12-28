import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from genres.services import GenresServices


def show_genres():
    genres_service = GenresServices()
    genres = genres_service.get_genres()

    if genres:
        st.header("Gêneros")
        st.write("Lista de gêneros:")
        AgGrid(data=pd.DataFrame(genres),
               key='genres_grid')
    else:
        st.warning("Nenhum gênero registrado!")
    st.header('Cadastrar novo gênero')
    name = st.text_input('Digite o nome do novo gênero:')
    if st.button('Salvar'):
        genres_service.post_genre(name)
        st.rerun()

    st.header('Atualizar gênero')
    col1, col2 = st.columns(2)
    with col1:
        st.text('Digite o ID do genero que deseja alterar')
        id = st.text_input('ID')
    with col2:
        st.text('Digite o novo gênero')
        name = st.text_input('Novo gênero')
    if st.button('Salvar novo gênero'):
        genres_service.update_genre(id, name)
        st.rerun()

    st.header("Deletar gênero")
    id = st.text_input("ID do genero")
    if st.button('Deletar'):
        genres_service.delete_genre(id)
        st.rerun()
