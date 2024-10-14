import requests
from app.config.config import Config

class HTTPController:
    _instance = None
    _deployment_id = Config.DEPLOYMENT_ID
    BASE_URL = Config.BASE_URL

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(HTTPController, cls).__new__(cls)
            cls._instance.session = requests.Session()
            cls._instance.token = None 
        return cls._instance

    def _get_token(self):
        user = Config.USER
        password = Config.PASSWORD
        payload = f'{{"userid":"{user}","password":"{password}"}}'
        headers = {
            'content-type': "application/json",
            'x-deployment-id': self._deployment_id
        }
        response = self.session.post(f'{self.BASE_URL}/dbapi/v4/auth/tokens', data=payload, headers=headers)
        token = response.json().get('token')
        self.token = token
        return token

    def _get_headers(self, additional_headers=None):
        headers = {
            'Authorization': f'Bearer {self.token}',
            'content-type': "application/json",
            'x-deployment-id': self._deployment_id
        }
        if additional_headers:
            headers.update(additional_headers)
        return headers

    def _handle_response(self, response, path, method, **kwargs):
        if response.status_code == 401:
            print('401::::')
            error_response = response.json()
            if any(error['code'] == 'authentication_failure' for error in error_response.get('errors', [])):
                self._get_token()
                headers = self._get_headers(kwargs.get('headers'))
                if method == 'get':
                    return self.session.get(f'{self.BASE_URL}/{path}', headers=headers, **kwargs)
                elif method == 'post':
                    return self.session.post(f'{self.BASE_URL}/{path}', headers=headers, **kwargs)
        print('NOT 401::::')
        return response

    def get(self, path, headers=None, **kwargs):
        if self.token is None:
            self._get_token()
        headers = self._get_headers(headers)
        response = self.session.get(f'{self.BASE_URL}/{path}', headers=headers, **kwargs)
        response = self._handle_response(response, path, 'get', **kwargs)
        response.raise_for_status()
        return response.json()

    def post(self, path, data=None, json=None, headers=None, **kwargs):
        if self.token is None:
            self._get_token()
        headers = self._get_headers(headers)
        response = self.session.post(f'{self.BASE_URL}/{path}', data=data, json=json, headers=headers, **kwargs)
        response = self._handle_response(response, path, 'post', **kwargs)
        response.raise_for_status()
        return response.json()
