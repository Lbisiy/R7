import requests


class Authentication:
    def __init__(self):
        self.url = None
        self.data_ = None

    def request_auth(self, url: str, data_: dict) -> str:
        """
        Аутентификация с получением токена POST api/2.0/authentication
        :param url: url аутентификации, например ("http://192.168.25.179/api/2.0/authentication")
        :param data_: словарь {логин, пароль}
        :return: token
        """
        self.url = url
        self.data_ = data_
        url_request = self.url + '/api/2.0/authentication'
        response = requests.post(url_request, json=self.data_)
        token = response.json()['response']['token']
        print()
        print("***************************************************")
        print("Аутентификация с кодом", response.status_code)
        print("***************************************************")
        return token

    def twofactor_request_auth(self, url: str, data_: dict, auth_code: int) -> str:
        """
        Двух-факторная аутентификация с получением токена POST api/2.0/authentication/{code}
        :param url: url аутентификаци, например("http://192.168.25.179/api/2.0/authentication/{code}")
        :param data_: словарь {логин, пароль}
        :param auth_code: код двух-факторной аутентификации
        :return: token
        """
        self.url = url
        self.data_ = data_
        url_request = self.url + '/api/2.0/authentication/' + str(auth_code)
        response = requests.post(url_request, json=self.data_)
        token = response.json()['response']['token']
        print("***************************************************")
        print("Двух-факторная аутентификация с кодом", response.status_code)
        print("***************************************************")
        print()
        return token

    @staticmethod
    def set_phone(url_: str, data_phone: dict) -> None:
        """
        Установка телефона пользователя POST api/2.0/authentication/setphone
        :param url: url аутентификаци, например("http://192.168.25.179/api/2.0/authentication/{code}")
        :param data_phone: словарь с данными для установки телефона
        :return: None
        """
        url_set_phone = url_ + '/api/2.0/authentication/setphone'
        response = requests.post(url_set_phone, json=data_phone)
        print("Установка телефона пользователя с кодом", response.status_code)

    @staticmethod
    def send_sms(url_: str, data_: dict) -> None:
        # не проверен
        """
        Отправление СМС с кодом аутентификации на телефон POST api/2.0/authentication/sendsms
        :param url: url аутентификаци, например("http://192.168.25.179/api/2.0/authentication/{code}")
        :param data_: словарь с данными для отправления СМС
        :return: None
        """
        url_send_sms = url_ + '/api/2.0/authentication/sendsms'
        response = requests.post(url_send_sms, json=data_)
        print("Отправление смс аутентификации с кодом", response.status_code)
        print("***************************************************")


# if __name__ == "__main__":
#     """
# **************************************************************************************************
#     Данные для авторизации (при запуске подставлять свои значения)
# **************************************************************************************************
#     """
#     url = "http://192.168.26.130"
#     data = {
#         "userName": "safin.marat@r7-office.ru",
#         "password": "Hsuhsh35dr"
#     }
#     """
# **************************************************************************************************
#     Данные для установки телефона
# **************************************************************************************************
#     """
#     data_phone = {
#         "userName": "safin.marat@r7-office.ru",
#         "password": "Hsuhsh35dr",
#         "mobilePhone": "8(921)9516961"
#     }
