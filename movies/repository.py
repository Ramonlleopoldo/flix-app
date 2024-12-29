import requests
from login.service import logout
import streamlit as st


class Movierepository:
    def __init__(self):
        self.__base_url = 'https://ramonlleopoldo.pythonanywhere.com/api/v1/'
        self.__movies_url = f'{self.__base_url}movies/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_movies(self):
        response = requests.get(url=self.__movies_url,
                                headers=self.__headers)
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API: {response.status_code}')

    def post_movies(self, movie):

        response = requests.post(url=self.__movies_url,
                                 data=movie,
                                 headers=self.__headers
                                 )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API: {response.status_code} {movie}')

    def delete_movies(self, id):
        movies_delete_url = f'{self.__movies_url}{id}/'
        response = requests.delete(url=movies_delete_url,
                                   headers=self.__headers)
        if response.status_code == 204:
            return {'mensagem': 'Gênero deletado com sucesso'}
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API: {response.status_code}')

    def get_movie_stats(self):
        movie_stats_url = f'{self.__movies_url}stats/'
        response = requests.get(url=movie_stats_url,
                                headers=self.__headers)
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API: {response.status_code}')
