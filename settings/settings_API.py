import requests

from authentication.auth_API import Authentication


class CommonSettings:
    def __init__(self, url_auth: str, data_auth: dict) -> None:
        token = Authentication().request_auth(url_auth, data_=data_auth)
        self.headers = {'Authorization': f'Bearer {token}'}

        self.url_API_settings = url_auth + '/api/2.0/settings'

    def get_logo(self) -> None:
        """
        Получение URL изображения лого портала GET api/2.0/settings/logo
        :return: None
        """
        url_get_logo = self.url_API_settings + '/logo'
        response = requests.get(url_get_logo, headers=self.headers)
        data = response.url

        print(f"Получение лого портала с кодом:", response.status_code)
        print(data)

    def get_socket_settings(self) -> None:
        """
        Получение настроек сокета GET api/2.0/settings/socket
        :return: None
        """
        url_socket_settings = self.url_API_settings + '/socket'
        response = requests.get(url_socket_settings, headers=self.headers)
        data = response.json()

        print(f"Получение настроек сокета с кодом:", response.status_code)
        print(data)

    def get_portal_settings(self) -> None:
        """
        Получение настроек портала GET api/2.0/settings
        :return: None
        """
        response = requests.get(self.url_API_settings, headers=self.headers)
        data = response.json()

        print(data)

    def email_activation(self) -> None:
        """
        Обновление настроек активации электронной почты PUT api/2.0/settings/emailactivation
        :return: None
        """
        url_email_activation = self.url_API_settings + '/emailactivation'
        response = requests.put(url_email_activation, headers=self.headers)
        data = response.json()

        print(data)


if __name__ == "__main__":

    """
 **************************************************************************************************
     Данные для авторизации (при запуске подставлять свои значения)
 **************************************************************************************************
     """
    url_auth = "http://192.168.25.179"
    data_auth = {
        "userName": "safin.marat@r7-office.ru",
        "password": "12345678"
    }

    """
**************************************************************************************************
    Данные для обновления настроек активации электронной почты
**************************************************************************************************
       """
    data_email_activation = {
        "show": True,
    }

    settings_ = CommonSettings(url_auth, data_auth)
    settings_.email_activation()
