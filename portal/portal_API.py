import requests

from authentication.auth_API import Authentication


class Portal:

    def __init__(self, url_auth: str, data_auth: dict) -> None:

        token = Authentication().request_auth(url_auth, data_=data_auth)
        self.headers = {'Authorization': f'Bearer {token}'}

        self.url_API_portal = url_auth + '/api/2.0/portal'

    def get_invitation_link(self, params: str) -> None:
        """
        Получение ссылки-приглашения для присоединения к порталу GET api/2.0/portal/users/invite/
        :param params: Тип сотрудника. Возможные варианты All, User, Visitor
        :return: None
        """
        data_params = ['All', 'User', 'Visitor']
        if params in data_params:
            url_get_link = self.url_API_portal + f'/users/invite/{params}'
            response = requests.get(url_get_link, headers=self.headers)
            data = response.json()

            print(data)
            print(f"Получение ссылки-приглашения к порталу с кодом:", response.status_code)

        else:
            raise ValueError("Неверный формат params")

    def get_user_count(self) -> None:
        """
        Получение кол-ва пользователей портала GET api/2.0/portal/userscount
        :return: None
        """
        url_get_count = self.url_API_portal + '/userscount'
        response = requests.get(url_get_count, headers=self.headers)
        data = response.json()

        print(data)
        print(f"Получение кол-ва пользователей портала с кодом:", response.status_code)

    def get_tariff(self) -> None:
        """
        Получение тарифа портала GET api/2.0/portal/tariff
        :return: None
        """
        url_get_tariff = self.url_API_portal + '/tariff'
        response = requests.get(url_get_tariff, headers=self.headers)
        data = response.json()

        print(data)
        print(f"Получение тарифа портала с кодом:", response.status_code)

    def get_backup_schedule(self) -> None:
        """
        Получение расписания резервного копирования GET api/2.0/portal/getbackupschedule
        :return: None
        """
        url_get_backup_schedule = self.url_API_portal + '/getbackupschedule'
        response = requests.get(url_get_backup_schedule, headers=self.headers)
        data = response.json()

        print(data)
        print(f"Получение расписания резервного копирования портала с кодом:", response.status_code)

    def get(self) -> None:
        """
        Получение текущего портала GET api/2.0/portal
        :return: None
        """
        response = requests.get(self.url_API_portal, headers=self.headers)
        data = response.json()

        print(data)
        print(f"Получение текущего портала с кодом:", response.status_code)



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
