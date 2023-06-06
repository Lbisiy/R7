import datetime

import requests

from authentication.auth_API import Authentication


class Project:

    def __init__(self, url_auth, data_auth, url_API_project) -> None:
        token = Authentication().request_auth(url_auth, data_=data_auth)
        self.headers = {'Authorization': f'Bearer {token}'}

        self.url_API_project = url_API_project

    def create_project(self, data_create_project) -> None:
        """
        Создание проекта POST api/2.0/project
        :param data_create_project: данные создаваемого проекта
        :return: None
        """
        response = requests.post(self.url_API_project, data_create_project, headers=self.headers)
        data = response.json()

        with open(f"projects/projects_{datetime.date.today()}.txt", "a") as f:
            f.writelines(str(data) + '\n')

        print(f"Создание проекта с кодом:", response.status_code)
        print(data)

    def get(self) -> None:
        """
        Получение всех проектов портала GET api/2.0/project
        :return: None
        """
        response = requests.get(self.url_API_project, headers=self.headers)
        data = response.json()

        print(f"Получение всех проектов с кодом:", response.status_code)
        print(data)


if __name__ == "__main__":
    """
**************************************************************************************************
    Данные для авторизации (при запуске подставлять свои значения)
**************************************************************************************************
    """
    url_auth = "http://192.168.25.179/api/2.0/authentication"
    data_auth = {
        "userName": "safin.marat@r7-office.ru",
        "password": "12345678"
    }
    """
**************************************************************************************************
    Данные для создания проекта
**************************************************************************************************
    """
    data_create_project = {
        "title": "New project",
        "responsibleID": "b53f1506-006d-11ee-bdfc-fa163e748144",
    }


    url_API_project = "http://192.168.25.179/api/2.0/project"

    project = Project(url_auth, data_auth, url_API_project)
    project.create_project(data_create_project)

