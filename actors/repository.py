import requests
import streamlit as st
from login.service import logout


class ActorsRespository:
    def __init__(self):
        self.__base_url = 'https://ramonlleopoldo.pythonanywhere.com/api/v1/'
        self.__actors_url = f'{self.__base_url}actors/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_actors(self):
        response = requests.get(url=self.__actors_url,
                                headers=self.__headers)
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API: {response.status_code}')

    def post_actors(self, name, nationality):
        data = {
            'name': name,
            'nationality': nationality
        }
        response = requests.post(url=self.__actors_url,
                                 json=data,
                                 headers=self.__headers)
        if response.status_code == 201:
            print(name, nationality)
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API: {response.status_code}')

    def update_actor(self, id, name, nationality, method='PATCH'):
        update_actor_url = f'{self.__actors_url}{id}/'
        data = {
            'id': id,
            'name': name,
            'nationality': nationality
        }
        if method not in ['PATCH', 'PUT']:
            raise Exception('Metodo permitido apenas "PATCH" ou "PUT"')

        if method == 'PATCH':
            response = requests.patch(url=update_actor_url,
                                      json=data,
                                      headers=self.__headers)
        if method == 'PUT':
            response = requests.put(url=update_actor_url,
                                    json=data,
                                    headers=self.__headers)
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API: {response.status_code}')

    def delete_actor(self, id):
        delete_url = f'{self.__actors_url}{id}/'
        response = requests.delete(url=delete_url,
                                   headers=self.__headers)
        if response.status_code == 204:
            return {'mensagem': 'Ator deletado com sucesso'}
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API: {response.status_code}')
