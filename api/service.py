import requests


class Auth:
    def __init__(self):
        self.__base_url = 'https://ramonlleopoldo.pythonanywhere.com/api/v1/'
        self.__auth_url = f'{self.__base_url}authetication/token/'

    def get_token(self, username, password):
        # capturando o username e password de acesso
        auth_payload = {
            "username": username,
            "password": password,
        }
        # capturando a resposta obtida ao realizar o post com as informações de username e password
        auth_response = requests.post(
            self.__auth_url,
            data=auth_payload
        )
        # verificando se o status do codigo é 200 (signfica ok) caso contrario devolve um dicionario informando o erro
        if auth_response.status_code == 200:
            return auth_response.json()
        return {'error': f' Erro ao autentificar. Status code {auth_response.status_code}'}
