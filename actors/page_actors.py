import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from actors.service import ActorsService


def show_actors():
    # Opções disponivel para input de nacionalidade
    nationality_options = ['USA', 'Brazil']

    actors_service = ActorsService()
    actors = actors_service.get_actors()

    # Lista de atores/atrizes
    if actors:
        st.header("Atores e Atrizes")
        AgGrid(data=pd.DataFrame(actors),
               key='actors_grid')
    else:
        st.warning("Nenhum Ator ou atriz cadastrado!")

    # Cadastrar ator/atriz
    st.header("Cadastrar novo ator ou atriz")
    name = st.text_input("Nome ator/atriz")
    nationality = st.selectbox('Nacionalidade', nationality_options)

    if st.button('Salvar'):
        actors_service.post_actors(name, nationality)
        st.rerun()

    # Atualizar ator/atriz
    st.header("Atualizar Ator/Atriz")
    col1, col2, col3 = st.columns(3)
    with col1:
        id = st.text_input('id')
    with col2:
        name = st.text_input("Novo ator")
    with col3:
        for i in range(1):
            att_nationality = st.selectbox('Escolha a nacionalidade', ['USA', 'Brazil'], key=f'selectbox{i}')

    if st.button('salvar', key='button_update'):
        actors_service.update_actors(id, name, att_nationality)
        st.rerun()

    # Deletar ator/atriz
    st.header('Deletar ator/atriz')
    id_delete = st.text_input("Digite o ID do ator que deseja excluir")

    if st.button('Salvar', key='button_delete'):
        actors_service.delete_actor(id_delete)
        st.rerun()
