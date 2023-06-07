import datetime

import requests

from authentication.auth_API import Authentication


class People:

    def __init__(self, url_auth, data_auth, url_API_people, url_API_group) -> None:

        token = Authentication().request_auth(url_auth, data_=data_auth)
        self.headers = {'Authorization': f'Bearer {token}'}

        self.url_API_people = url_API_people
        self.url_API_group = url_API_group

    def create(self, data_create_people: dict):
        """
        Создаение нового пользователя POST api/2.0/people
        :param data_create_people: данные создаваемого пользователя
        :return: None
        """
        response = requests.post(self.url_API_people, json=data_create_people, headers=self.headers)
        data = response.json()

        with open(f"people/people_{datetime.date.today()}.txt", "a") as f:
            f.writelines(str(data) + '\n')
        print(f"Создание пользователя с кодом:", response.status_code)

    def get_all(self):
        """
        Получение профилей всех пользователей GET api/2.0/people
        :return: None
        """
        response = requests.get(self.url_API_people, headers=self.headers)
        data = response.json()

        print(f"Получение профилей всех пользователей с кодом:", response.status_code)
        print(data)

    def update(self, data_update_people: dict, people_id: str):
        """
        Обновление пользователя PUT api/2.0/people/{userid}
        :param data_update_people: новые данные пользователя
        :param people_id: номер пользователя
        :return: None
        """
        url_update_people = self.url_API_people + f'/{people_id}'
        response = requests.put(url_update_people, json=data_update_people, headers=self.headers)
        data = response.json()

        print(f"Обновление профиля пользователя id={people_id} с кодом:", response.status_code)
        print(data)

    def delete_people_list(self, data_people_id: dict) -> None:
        """
        Удаление списка заблокированных пользователей с уникальными номерами, указанными в запросе
        PUT api/2.0/people/delete
        Заблокированные пользователи имеют статус: Terminated
        :param data_update_people: список уникальных идентификаторов пользователей
        :return: None
        """
        url_delete_people_list = self.url_API_people + '/delete'
        response = requests.put(url_delete_people_list, json=data_people_id, headers=self.headers)
        data = response.json()

        print(f'Удаление пользователей id={data_people_id["userIds"]} с кодом:', response.status_code)
        print(data)

    def delete_person(self, people_id: str) -> None:
        """
        Удаление заблокированного пользователя DELETE api/2.0/people/{userid}
        Заблокированный пользователь имеет статус: Terminated
        :param people_id: номер пользователя
        :return: None
        """
        url_delete_people = self.url_API_people + f'/{people_id}'
        response = requests.delete(url_delete_people, headers=self.headers)
        data = response.json()

        print(f'Удаление пользователя id= с кодом:', response.status_code)
        print(data)

    def get_status(self) -> None:
        """
        Получение статуса текущего пользователя GET api/2.0/people/import/status
        :return: None
        """
        url_get_status = self.url_API_people + '/import/status'
        response = requests.get(url_get_status, headers=self.headers)
        data = response.json()

        print(f'Получение статуса текущего пользователя с кодом:', response.status_code)
        print(data)

    def update_status(self, data_people_id: dict, status: str) -> None:
        """
        Изменение статуса пользователя PUT api/2.0/people/status/{status}
        :param data_people_id: список уникальных идентификаторов пользователей
        :param Active, Terminated, LeaveOfAbsence, Default, All
        :return: None
        """
        url_update_status = self.url_API_people + f'/status/{status}'
        response = requests.put(url_update_status, json=data_people_id, headers=self.headers)
        data = response.json()

        print(data)

    def get_profiles_by_status(self, status: str) -> None:
        """
        Получение профилей пользователей по статусу GET api/2.0/people/status/{status}
        :param status: Active, Terminated, LeaveOfAbsence, Default, All
        :return: None
        """
        url_update_status = self.url_API_people + f'/status/{status}'
        response = requests.get(url_update_status, headers=self.headers)
        data = response.json()

        print(f'Получение профилей пользователей по статусу={status} с кодом:', response.status_code)
        print(data)

    def update_type(self, data_people_id: dict, type: str) -> None:
        """
        Изменение типа пользователя PUT api/2.0/people/type/{type}
        :param список уникальных идентификаторов пользователей
        :param All, User, Visitor
        :return: None
        """
        url_update_type = self.url_API_people + f'/type/{type}'
        response = requests.put(url_update_type, json=data_people_id, headers=self.headers)
        data = response.json()

        print(f'Изменение пользователей id={data_people_id["userIds"]} на тип={type} с кодом:', response.status_code)
        print(data)

    def get_my_profile(self) -> None:
        """
        Получение информации о текущем профиле пользователя GET api/2.0/people/@self
        :return: None
        """
        url_my_profile = self.url_API_people + '/@self'
        response = requests.get(url_my_profile, headers=self.headers)
        data = response.json()

        print(f'Получение текущего профиля пользователя id={data["response"]["id"]} с кодом:', response.status_code)
        print(data)

    def create_group(self, data_create_group: dict) -> None:
        """
        Создание группы POST api/2.0/group
        :param данные создаваемой группы
        :return: None
        """
        response = requests.post(self.url_API_group, json=data_create_group, headers=self.headers)
        data = response.json()

        with open(f"people/group_{datetime.date.today()}.txt", "a") as f:
            f.writelines(str(data) + '\n')
        print(f"Создание группы с кодом:", response.status_code)

    def add_people_to_group(self, data_members_id: dict, group_id: str) -> None:
        """
        Добавление членов группы PUT api/2.0/group/{groupid}/members,
        сохраняя текущих участников и добавляя вместо них новых, указанных в запросе.
        :param индентификаторы членов группы
        :param инентификатор группы
        :return: None
        """
        url_people_to_group = self.url_API_group + f'/{group_id}/members'
        response = requests.put(url_people_to_group, json=data_members_id, headers=self.headers)
        data = response.json()

        print(f'Добавление нового пользователя id={data_members_id["members"]} с кодом:', response.status_code)
        print(data)

    def update_group(self, data_update_group: dict, group_id: str) -> None:
        """
        Изменение группы PUT api/2.0/group/{groupid}
        :param данные создаваемой группы
        :param group_id: идентификатор изменяемой группы
        :return: None
        """
        url_update_group = self.url_API_group + f'/{group_id}'
        response = requests.put(url_update_group, json=data_update_group, headers=self.headers)
        data = response.json()

        print(f'Изменение группы id={group_id} с кодом:', response.status_code)
        print(data)

    def get_all_groups(self) -> None:
        """
        Получение всех групп GET api/2.0/group
        :return: None
        """
        response = requests.get(self.url_API_group, headers=self.headers)
        data = response.json()

        print(f'Получение всех групп с кодом:', response.status_code)
        print(data)

    def delete_group(self, group_id: str) -> None:
        """
        Удаление группы DELETE api/2.0/group/{groupid}
        :param group_id: идентификатор удаляемой группы
        :return: None
        """
        url_delete_group = self.url_API_group + f'/{group_id}'
        response = requests.delete(url_delete_group, headers=self.headers)
        data = response.json()

        print(f'Удаление группы id={group_id} с кодом:', response.status_code)
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
    Данные для создания пользователя
**************************************************************************************************
    """
    url_API_people = "http://192.168.25.179/api/2.0/people"
    data_create_people = {
        "isVisitor": True,
        "email": "maratsafin.let@yandex.ru",
        "firstname": "Marat",
        "lastname": "Marat",
        "password": "12345678"
    }

    """
**************************************************************************************************
    Данные для изменения пользователя
**************************************************************************************************
    """
    data_update_people = {
        "isVisitor": False,
        "email": "maratsafin.let@gmail.com",
        "firstname": "Ivan",
        "lastname": "Ivan"
    }

    """
**************************************************************************************************
    Данные для удаления пользователя/для изменения статуса пользователя/для изменения типа пользователя
**************************************************************************************************
    """
    data_people_id = {
        "userIds": [
        "6415a6f8-eedf-4a2f-9223-1e3bfa5bec0e",
        ]
    }

    """
**************************************************************************************************
    Данные для создания группы
**************************************************************************************************
    """
    url_API_group = "http://192.168.25.179/api/2.0/group"
    data_create_group = {
        "groupName": "New group",
    }

    """
**************************************************************************************************
    Данные для добавления членов группы
**************************************************************************************************
     """
    data_members_id = {
        "members": [
            "a9d2d6f5-e179-4864-b585-b2e81bc99ebe",
        ]
    }

    """
 **************************************************************************************************
     Данные для изменения группы
 **************************************************************************************************
     """
    data_update_group = {
        "groupName": "New-new group",
    }
    """
***************************************************************************************************
    """

    people = People(url_auth, data_auth, url_API_people, url_API_group)

    people.create(data_create_people)
