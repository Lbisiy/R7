import requests

from authentication.auth_API import Authentication


class Mail:

    def __init__(self, url_auth: str, data_auth: dict) -> None:
        token = Authentication().request_auth(url_auth, data_=data_auth)
        self.headers = {'Authorization': f'Bearer {token}'}

        self.url_API_mail = url_auth + '/api/2.0/mail'

    def create_filter(self, data_create_filter: dict):
        """

        :return:
        """
        url_create_filter = self.url_API_mail + '/filters'
        response = requests.post(url_create_filter, json=data_create_filter, headers=self.headers)
        data = response.json()

        print(data)

    def get_filters(self):
        url_get_filters = self.url_API_mail + '/filters'
        response = requests.get(url_get_filters, headers=self.headers)
        data = response.json()

        print(data)

    def check_filter(self, data):
        url_check_filters = self.url_API_mail + '/filters/check'

        response = requests.post(url_check_filters, json=data, headers=self.headers)
        data = response.json()

        print(data)


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
    Данные для авторизации (при запуске подставлять свои значения)
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
   # data = {'id': 6, 'name': '1'}

    mail = Mail(url_auth, data_auth)
    mail.get_filters()
   # mail.create_filter(data_create_filter)
    mail.check_filter(data_create_filter)
