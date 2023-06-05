import requests


class Authentication:
    def __init__(self):
        self.url = None
        self.data = None

    def request_auth(self, url, data_):
        """
        Аутентификация с получением токена
        :param url: url аутентификаци, например("http://192.168.25.179/api/2.0/authentication")
        :param data_: словарь {логин, пароль}
        :return: None
        """
        response = requests.post(url, json=data_)
        token = response.json()['response']['token']
        print("Аутентификация с кодом", response.status_code)
        return token


if __name__ == "__main__":
    url_api = "http://192.168.25.179/api/2.0/authentication"
    data = {
        "userName": "safin.marat@r7-office.ru",
        "password": "12345678"
    }
    req = Authentication()
    req.request_auth(url_api, data)