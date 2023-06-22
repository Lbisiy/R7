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

        print(f"Получение настроек портала с кодом:", response.status_code)
        print(data)

    def email_activation(self) -> None:
        """
        Обновление настроек активации электронной почты PUT api/2.0/settings/emailactivation
        :return: None
        """
        url_email_activation = self.url_API_settings + '/emailactivation'
        response = requests.put(url_email_activation, headers=self.headers)
        data = response.json()

        print(f"Получение настроек активации электронной почты с кодом:", response.status_code)
        print(data)

    def ip_restrictions(self) -> None:
        """
        Получение ограничений IP-портала GET api/2.0/settings/iprestrictions
        :return: None
        """
        url_email_activation = self.url_API_settings + '/iprestrictions'
        response = requests.get(url_email_activation, headers=self.headers)
        data = response.json()

        print(f"Получение ограничений IP-портала с кодом:", response.status_code)
        print(data)

    def get_smtp(self) -> None:
        """
        Получение настроек SMTP GET api/2.0/settings/smtp
        :return: None
        """
        url_smtp = self.url_API_settings + '/smtp'
        response = requests.get(url_smtp, headers=self.headers)
        data = response.json()

        print(f"Получение настроек SMTP с кодом:", response.status_code)
        print(data)

    def test_smtp(self) -> None:
        """
        Тестирование настроек SMTP GET api/2.0/settings/smtp/test
        :return: None
        """
        url_test_smtp = self.url_API_settings + '/smtp/test'
        response = requests.get(url_test_smtp, headers=self.headers)
        data = response.json()

        print(f"Тестирование SMTP с кодом:", response.status_code)
        print(data)

    def get_sso(self) -> None:
        """
        Получение настроек SSO api/2.0/settings/ssov2
        :return: None
        """
        url_sso = self.url_API_settings + '/ssov2'
        response = requests.get(url_sso, headers=self.headers)
        data = response.json()

        print(f"Получение настроек SSO с кодом:", response.status_code)
        print(data)

    def get_paasword_settings(self) -> None:
        """
        Получение настроек пароля к порталу GET api/2.0/settings/security/password
        :return: None
        """
        url_get_password_settings = self.url_API_settings + '/security/password'
        response = requests.get(url_get_password_settings, headers=self.headers)
        data = response.json()

        print(f"Получение настроек пароля к порталу с кодом:", response.status_code)
        print(data)

    def get_security_settings(self) -> None:
        """
        Получение настроек безопасности продукта GET api/2.0/settings/security
        :return: None
        """
        url_get_security_settings = self.url_API_settings + '/security'
        response = requests.get(url_get_security_settings, headers=self.headers)
        data = response.json()

        print(f"Получение настроек безопасности продукта с кодом:", response.status_code)
        print(data)

    def get_size_quota(self) -> None:
        """
        Получение квоты использования пространства GET api/2.0/settings/quota
        :return: None
        """
        url_get_size_quota = self.url_API_settings + '/quota'
        response = requests.get(url_get_size_quota, headers=self.headers)
        data = response.json()

        print(f"Получение квоты использования пространства с кодом:", response.status_code)
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
    settings_.get_size_quota()
