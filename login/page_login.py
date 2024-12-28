import streamlit as st
from login.service import login


def show_login():
    st.header("Bem vindo(a) ao Flix API")
    st.text("Realize seu login para usar.")
    username = st.text_input("Nome de usuário")
    password = st.text_input(label='Senha', type='password')
    if st.button('Entrar'):
        login(username=username,
              password=password)
