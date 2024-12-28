import requests
import streamlit as st
from login.service import logout


class GenresRepository:
    def __init__(self):
        self.__base_url = 'https://ramonlleopoldo.pythonanywhere.com/api/v1/'
        self.__genres_url = f'{self.__base_url}genres/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_genres(self):
        response = requests.get(self.__genres_url, headers=self.__headers)
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API: {response.status_code}')

    def post_genre(self, genre):
        response = requests.post(url=self.__genres_url,
                                 data=genre,
                                 headers=self.__headers)
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API: {response.status_code}')

    def update_genre(self, id, name, method='PATCH'):
        if method not in ['PATCH', 'PUT']:
            raise Exception('Metodo permitido apenas "PATCH" ou "PUT"')
        update_url = f'{self.__genres_url}{id}/'
        if method == 'PATCH':
            response = requests.patch(url=update_url, data=name, headers=self.__headers)
        elif method == 'PUT':
            response = requests.put(url=update_url, data=name, headers=self.__headers)
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API: {response.status_code}')

    def delete_genre(self, id):
        delete_url = f'{self.__genres_url}{id}/'
        response = requests.delete(url=delete_url,
                                   headers=self.__headers)
        if response.status_code == 204:
            return {'mensagem': 'Gênero deletado com sucesso'}
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API: {response.status_code}')
