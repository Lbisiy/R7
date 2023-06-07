import datetime

import requests

from authentication.auth_API import Authentication


class Project:

    def __init__(self, url_auth: str, data_auth: dict) -> None:

        token = Authentication().request_auth(url_auth, data_=data_auth)
        self.headers = {'Authorization': f'Bearer {token}'}

        self.url_API_project = url_auth + '/api/2.0/project'

    def create_project(self, data_create_project: dict) -> None:
        """
        Создание проекта POST api/2.0/project
        :param data_create_project: данные создаваемого проекта
        :return: None
        """
        response = requests.post(self.url_API_project, json=data_create_project, headers=self.headers)
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

    def update(self, data_update_project: dict, project_id: int) -> None:
        """
        Обновление проекта PUT api/2.0/project/{id}
        :param data_update_project: данные обновляемого проекта
        :param project_id: уникальный идентификатор проекта
        :return: None
        """
        url_update_project = self.url_API_project + f'/{project_id}'

        response = requests.put(url_update_project, json=data_update_project, headers=self.headers)
        data = response.json()

        print(f'Обновление проекта id={project_id} с кодом:', response.status_code)
        print(data)

    def delete_project(self, project_id: int) -> None:
        """
        Удаление проекта с указанным в запросе идентификатором с портала DELETE api/2.0/project/{id}
        :param project_id: уникальный идентификатор проекта
        :return: None
        """
        url_delete_project = self.url_API_project + f'/{project_id}'

        response = requests.delete(url_delete_project, headers=self.headers)
        data = response.json()

        print(f'Удаление проекта id={project_id} с кодом:', response.status_code)
        print(data)

    def create_task(self, data_create_task: dict, project_id: int) -> None:
        """
        Создание задачи в выбранном проекте POST api/2.0/project/{projectid}/task
        :param data_create_task: данные создаваемой задачи
        :param project_id: уникальный идентификатор проекта
        :return: None
        """
        url_create_task = self.url_API_project + f'/{project_id}/task'
        response = requests.post(url_create_task, json=data_create_task, headers=self.headers)
        data = response.json()

        with open(f"projects/tasks_{datetime.date.today()}.txt", "a") as f:
            f.writelines(str(data) + '\n')

        print(f"Создание задачи с кодом:", response.status_code)
        print(data)

    def get_task(self, project_id: int) -> None:
        """
        Получение задачи конкретного проекта GET api/2.0/project/{projectid}/task
        :param project_id: уникальный идентификатор проекта
        :return: None
        """
        url_get_task = self.url_API_project + f'/{project_id}/task'
        response = requests.get(url_get_task, headers=self.headers)
        data = response.json()

        print(f"Получение задачи с кодом:", response.status_code)
        print(data)

    def delete_task(self, task_id: int) -> None:
        """
        DELETE api/2.0/project/task/{taskid}
        :return: None
        """
        url_delete_task = self.url_API_project + f'/task/{task_id}'
        response = requests.delete(url_delete_task, headers=self.headers)
        data = response.json()

        print(f"Удаление задачи с кодом:", response.status_code)
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
    Данные для создания проекта
**************************************************************************************************
    """
    data_create_project = {
        "title": "XXXXX project",
        "responsibleID": "b53f1506-006d-11ee-bdfc-fa163e748144",
    }
    """
**************************************************************************************************
    Данные для изменения проекта
**************************************************************************************************
       """
    data_update_project = {
        "title": "AAAAAA",
        "responsibleID": "b53f1506-006d-11ee-bdfc-fa163e748144",
    }
    """
**************************************************************************************************
    Данные для создания задачи
**************************************************************************************************
       """
    data_create_task = {
        "title": "EEEEE",
    }
    """
**************************************************************************************************
    """

    project = Project(url_auth, data_auth)
