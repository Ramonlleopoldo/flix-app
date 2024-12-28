import streamlit as st
from api.service import Auth


def login(username, password):
    # instanciando a classe auth importada de API.service
    auth_service = Auth()
    # capturando a resposta de auth ao fornecer o username e password
    response = auth_service.get_token(
        username=username,
        password=password,
    )
    # caso erro vai retornar o erro na tela do usuario
    if response.get('error'):
        st.text(f'Falaha ao realizar o login, erro: {response.get('error')}')
    else:
        # caso contrario vamos armazenar na session state o token retornado no access
        st.session_state.token = response.get('access')
        st.rerun()


def logout():
    for key in st.session_state.keys():
        del st.session_state[key]
    st.rerun()
