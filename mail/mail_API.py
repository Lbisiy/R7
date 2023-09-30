import requests

from authentication.auth_API import Authentication


class Mail:

    def __init__(self, url_auth: str, data_auth: dict) -> None:
        token = Authentication().request_auth(url_auth, data_=data_auth)
        self.headers = {'Authorization': f'Bearer {token}'}

        self.url_API_mail = url_auth + '/api/2.0/mail'
        print("Инициализация Модуля Почта")
        print("***************************************************")

    def create_account_by_email_password(self, data_create_account: dict) -> None:
        """
        Создание аккаунта с помощью email и пароля POST api/2.0/mail/accounts/simple
        :param data_create_account: данные создаваемого аккаунта
        :return: None
        """
        url_create_account = self.url_API_mail + '/accounts/simple'
        response = requests.post(url_create_account, json=data_create_account, headers=self.headers)
        print("Подключение учетной записи почты с помощью логина и пароля с кодом:", response.status_code)

    def delete_account(self, data_delete_account: dict) -> None:
        """
        Удаление аккаунта DELETE api/2.0/mail/accounts
        :param data_delete_account: даннеы удаляемого аккаунта
        :return: None
        """
        url_delete_account = self.url_API_mail + '/accounts'
        response = requests.delete(url_delete_account, json=data_delete_account, headers=self.headers)
        print(f"Удаление учетной записи почты <<{data_delete_account['email']}>> с кодом:", response.status_code)

    def send_email(self, data_send_email: dict) -> None:
        """
        Отправление эл.письма PUT api/2.0/mail/messages/simpleSend
        :param data_send_email: данные отправляемого письма
        :return: None
        """
        url_send_email = self.url_API_mail + '/messages/simpleSend'
        response = requests.put(url_send_email, json=data_send_email, headers=self.headers)
        print(f"Отправка письма с кодом:", response.status_code)

    def get_mail_operation(self) -> None:
        """
        Получения списка всех почтовых операций GET api/2.0/mail/operations
        :return: None
        """
        url_mail_operation = self.url_API_mail + '/operations'
        response = requests.get(url_mail_operation, headers=self.headers)
        data = response.json()
        print(data)
        print(f"Список почтовых операций с кодом:", response.status_code)

    def create_filter(self, data_create_filter: dict) -> None:
        """
        Создание фильтра POST api/2.0/mail/filters
        :param data_create_filter: данные создаваемого фильтра
        :return: None
        """
        url_create_filter = self.url_API_mail + '/filters'
        response = requests.post(url_create_filter, json=data_create_filter, headers=self.headers)
        print(f"Создание фильтра с кодом:", response.status_code)

    def get_filters(self) -> None:
        """
        Получения списка всех фильтров во всех mails GET api/2.0/mail/filters
        :return: None
        """
        url_get_filters = self.url_API_mail + '/filters'
        response = requests.get(url_get_filters, headers=self.headers)
        data = response.json()
        print(data)
        print(f"Получение фильтров с кодом:", response.status_code)

    def check_filter(self, data_check_filter: dict) -> None:
        """
        Проверка результатов работы фильтра, заданного в запросе POST api/2.0/mail/filters/check
        :param data_check_filter: данные фильтра
        :return: None
        """
        url_check_filters = self.url_API_mail + '/filters/check'
        response = requests.post(url_check_filters, json=data_check_filter, headers=self.headers)
        data = response.json()
        print(data)
        print(f"Проверка результатов работы фильтра с кодом:", response.status_code)


if __name__ == "__main__":
    """
**************************************************************************************************
    Данные для авторизации (при запуске подставлять свои значения)
**************************************************************************************************
    """
    url_auth = "http://192.168.26.130/"
    data_auth = {
        "userName": "safin.marat@r7-office.ru",
        "password": "Hsuhsh35dr"
    }

    """
**************************************************************************************************
    Данные для создания фильтра
**************************************************************************************************
    """
    data_create_filter = {
        "filter": {
        "id": 0,
        "name": "Support2",
        "position": 2,
        "enabled": True,
        "filterData": '',
        "conditions": [{'key': 0, 'operation': 0, 'value': 'maratsafin_let@mail.ru'}],
        "actions": [{'action': 3, 'data': ''}],
        "options": {'matchMultiConditions': 0,
                    'applyTo': {
                        'folders': [1], 'mailboxes': [], 'withAttachments': 0
                                },
                    'ignoreOther': False
                    }
        }
    }
