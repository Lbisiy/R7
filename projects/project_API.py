import datetime
import requests

from authentication.auth_API import Authentication
from people.people_API import People


class Project:

    def __init__(self, url_auth: str, data_auth: dict) -> None:
        token = Authentication().request_auth(url_auth, data_=data_auth)
        self.headers = {'Authorization': f'Bearer {token}'}

        self.url_API_project = url_auth + '/api/2.0/project'
        print("Инициализация Модуля Проекты")
        print("***************************************************")

    def create_project(self, data_create_project: dict) -> int:
        """
        Создание проекта POST api/2.0/project
        :param data_create_project: данные создаваемого проекта
        :return: id проекта
        """
        response = requests.post(self.url_API_project, json=data_create_project, headers=self.headers)
        data = response.json()

        # with open(f"projects/projects_{datetime.date.today()}.txt", "a") as f:
        #     f.writelines(str(data) + '\n')
        print(f"Создание проекта с кодом:", response.status_code)
        return data['response']['id']

    def get(self) -> None:
        """
        Получение всех проектов портала GET api/2.0/project
        :return: None
        """
        response = requests.get(self.url_API_project, headers=self.headers)
        data = response.json()
        print(data)
        print(f"Получение всех проектов с кодом:", response.status_code)

    def update_project(self, data_update_project: dict, project_id: int) -> None:
        """
        Обновление проекта PUT api/2.0/project/{id}
        :param data_update_project: данные обновляемого проекта
        :param project_id: уникальный идентификатор проекта
        :return: None
        """
        url_update_project = self.url_API_project + f'/{project_id}'
        response = requests.put(url_update_project, json=data_update_project, headers=self.headers)
        print(f'Обновление проекта <<id={project_id}>> с кодом:', response.status_code)

    def delete_project(self, project_id: int) -> None:
        """
        Удаление проекта с указанным в запросе идентификатором с портала DELETE api/2.0/project/{id}
        :param project_id: уникальный идентификатор проекта
        :return: None
        """
        url_delete_project = self.url_API_project + f'/{project_id}'
        response = requests.delete(url_delete_project, headers=self.headers)
        print(f'Удаление проекта <<id={project_id}>> с кодом:', response.status_code)

    def create_task(self, data_create_task: dict, project_id: int) -> int:
        """
        Создание задачи в выбранном проекте POST api/2.0/project/{projectid}/task
        :param data_create_task: данные создаваемой задачи
        :param project_id: уникальный идентификатор проекта
        :return: id задачи
        """
        url_create_task = self.url_API_project + f'/{project_id}/task'
        response = requests.post(url_create_task, json=data_create_task, headers=self.headers)
        data = response.json()

        # with open(f"projects/tasks_{datetime.date.today()}.txt", "a") as f:
        #     f.writelines(str(data) + '\n')
        print(f"Создание задачи с кодом:", response.status_code)
        return data['response']['id']

    def get_task(self, project_id: int) -> dict:
        """
        Получение задачи конкретного проекта GET api/2.0/project/{projectid}/task
        :param project_id: уникальный идентификатор проекта
        :return: задача проекта
        """
        url_get_task = self.url_API_project + f'/{project_id}/task'
        response = requests.get(url_get_task, headers=self.headers)
        data = response.json()
        print(f"Получение задачи с кодом:", response.status_code)
        return data

    def delete_task(self, task_id: int) -> None:
        """
        Удаления задачи проекта DELETE api/2.0/project/task/{taskid}
        :param task_id: id задачи
        :return: None
        """
        url_delete_task = self.url_API_project + f'/task/{task_id}'
        response = requests.delete(url_delete_task, headers=self.headers)
        print(f"Удаление задачи с кодом:", response.status_code)

    def update_task(self, data_update_task: dict, task_id: int) -> None:
        """
        Изменение задачи проекта PUT api/2.0/project/task/{taskid}
        :param data_update_task: данные изменяемой задачи
        :param task_id: id задачи
        :return: None
        """
        url_update_task = self.url_API_project + f'/task/{task_id}'
        response = requests.put(url_update_task, json=data_update_task, headers=self.headers)
        print(f"Обновление задачи с кодом:", response.status_code)

    def create_milestone(self, data_create_milestone: dict, project_id: int) -> int:
        """
        Создание вехи в выбранном проекте POST api/2.0/project/{id}/milestone
        :param data_create_milestone: данные создаваемой вехи
        :param project_id: id проекта
        :return: id вехи
        """
        url_create_milestone = self.url_API_project + f'/{project_id}/milestone'
        response = requests.post(url_create_milestone, json=data_create_milestone, headers=self.headers)
        data = response.json()

        # with open(f"projects/tasks_{datetime.date.today()}.txt", "a") as f:
        #     f.writelines(str(data) + '\n')
        print(f"Создание вехи с кодом:", response.status_code)
        return data['response']['id']

    def update_milestone(self, data_update_milestone: dict, milestone_id: int) -> None:
        """
        Изменение вехи проекта PUT api/2.0/project/milestone/{id}
        :param data_update_milestone: данные изменяемой вехи
        :param milestone_id: id вехи
        :return: None
        """
        url_update_milestone = self.url_API_project + f'/milestone/{milestone_id}'
        response = requests.put(url_update_milestone, json=data_update_milestone, headers=self.headers)
        print(f"Обновление вехи с кодом:", response.status_code)

    def delete_milestones(self, milestone_id: int) -> None:
        """
        Удаление вехи DELETE api/2.0/project/milestone/{id}
        :return: None
        """
        url_delete_milestone = self.url_API_project + f'/milestone/{milestone_id}'
        response = requests.delete(url_delete_milestone, headers=self.headers)
        print(f"Удаление вехи с кодом:", response.status_code)

    def create_discussion(self, data_create_discussion: dict, project_id: int) -> str:
        """
        Создание обсуждения в проекте POST api/2.0/project/{projectid}/message
        :param data_create_discussion: данные созданного обсуждения
        :param project_id: id проекта
        :return: id обсуждения
        """
        url_create_discussion = self.url_API_project + f'/{project_id}/message'
        response = requests.post(url_create_discussion, json=data_create_discussion, headers=self.headers)
        data = response.json()
        print(f"Создание обсуждения с кодом:", response.status_code)
        return data['response']['id']

    def update_discussion(self, data_update_discussion: dict, discussion_id: str) -> None:
        """
        Изменение обсуждения в проекте PUT api/2.0/project/message/{messageid}
        :param data_update_discussion: данные изменяемого обсуждения
        :param discussion_id: id обсуждения
        :return: None
        """
        url_update_discussion = self.url_API_project + f'/message/{discussion_id}'
        response = requests.put(url_update_discussion, json=data_update_discussion, headers=self.headers)
        print(f"Обновление обсуждения с кодом:", response.status_code)

    def delete_discussion(self, discussion_id: str) -> None:
        """
        Удаление обсуждения в проекте DELETE api/2.0/project/message/{messageid}
        :param discussion_id: id обсуждения
        :return: None
        """
        url_delete_discussion = self.url_API_project + f'/message/{discussion_id}'
        response = requests.delete(url_delete_discussion, headers=self.headers)
        print(f"Удаление обсуждения с кодом:", response.status_code)

    def create_report(self, data_create_report: dict) -> None:
        """
        Создание отчета по проектам POST api/2.0/project/report
        :param data_create_report: данные создаваемого отчета
        :return: None
        """
        url_create_report = self.url_API_project + '/report'
        response = requests.post(url_create_report, json=data_create_report, headers=self.headers)
        print(f"Создание отчета <<{data_create_report['reportType']}>> с кодом:", response.status_code)


if __name__ == "__main__":
    """
**************************************************************************************************
    Данные для авторизации (при запуске подставлять свои значения)
**************************************************************************************************
    """
    url_auth = "http://192.168.26.194/"
    data_auth = {
        "userName": "support@r7-office.ru",
        "password": "Hsuhsh35dr"
    }
    """
**************************************************************************************************
    Данные для создания проекта
**************************************************************************************************
    """
    data_create_project = {
        "title": "XXXXX222 project",
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
    Данные для обновления задачи
**************************************************************************************************
    """
    data_update_task = {
          "description": "Updated description",
          "priority": "Normal",
          "title": "Updated task",
    }

    """
**************************************************************************************************
    Данные для создания вехи
**************************************************************************************************
    """
    data_create_milestone = {
        "title": "Milestone",
        "deadline": "2024-01-01T06-30-00.000Z",
        "isKey": False,
        "isNotify": False,
        "description": "Some text",
        "responsible": "0",
        "notifyResponsible": False
    }
    """
**************************************************************************************************
    Данные для обновления вехи
**************************************************************************************************
    """
    data_update_milestone = {
        "title": "Updated",
        "deadline": "2011-03-23T14:27:14",
        "isKey": False,
        "status": "Open"
    }
    """
**************************************************************************************************
    Данные для создания обсуждения
**************************************************************************************************
    """
    data_create_discussion = {
          "title": "Discussion",
          "content": "Some text",
          "participants": [],
          "notify": False
    }
    """
**************************************************************************************************
    Данные для обновления обсуждения
**************************************************************************************************
    """
    data_update_discussion = {
        "projectid": 1234,
        "title": "Some text",
        "content": "Some text",
        "participants": "Some text",
        "notify": True
    }

    """
**************************************************************************************************
     Данные для создания пользователя
**************************************************************************************************
    """
    data_create_people = {
        "isVisitor": True,
        "email": "r7testmail@ya.ru",
        "firstname": "Fedor",
        "lastname": "Fedorov",
        "password": "Hsuhsh35dr"
    }
    """
**************************************************************************************************
     Данные для создания отчета
**************************************************************************************************
    """
    data_create_report = {
          "name": "Report",
          "autoGenerated": True,
          "reportType": "MilestonesNearest",
          "reportTimeInterval": "Absolute",
        }
