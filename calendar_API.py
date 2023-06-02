import requests
import json

from auth_API import Authentication


class Calendar:

    def __init__(self) -> None:

        token = Authentication().request_auth(url_auth, data_=data_auth)
        self.headers = {'Authorization': f'Bearer {token}'}

    def create(self, url_create_calendar: str, data_create_calendar: dict) -> None:
        """
        Создание календаря POST api/2.0/calendar
        :param url_auth: URL для авторизации, например("http://192.168.25.179/api/2.0/authentication")
        :param url_create_calendar: URL для создания календаря, например("http://192.168.25.179/api/2.0/calendar")
        :param data_auth: словарь {логин, пароль}
        :param data_create_calendar: словарь {данные для создания словаря, см. пример ниже в if __name__ == "__main__":
    ""}
        :return: None
        """

        response = requests.post(url_create_calendar, json=data_create_calendar, headers=self.headers)
        data = response.json()

        with open("calendars/calendar.txt", "a") as f:
            f.writelines(str(data) + '\n')
        print("Создание календаря с кодом", response.status_code)

    def get_(self, url_create_calendar: str, calendar_id: int) -> None:
        """
        Получить календарь по идентификатору GET api/2.0/calendar/{calendarId}
        calendarId - число, его можно брать из файла calendar.txt при создании ("objectId": "10")
        :return: None
        """
        url_get_calendar = url_create_calendar + '/' + str(calendar_id)

        response = requests.get(url_get_calendar, headers=self.headers)
        print("Запрос календаря со статусом", response.status_code)
        print(response.json())

    def change(self, url_create_calendar: str, calendar_id: str, data_change_calendar: dict):
        """
        Обновление календаря PUT api/2.0/calendar/{calendarId}
        calendarId - число, его можно брать из файла calendar.txt при создании ("objectId": "10")
        :return: None
        """
        url_change_calendar = url_create_calendar + '/' + str(calendar_id)

        response = requests.put(url_change_calendar, json=data_change_calendar, headers=self.headers)
        print("Изменение календаря со статусом", response.status_code)
        print(response.json())

    def delete(self, url_create_calendar: str, calendar_id: int):
        """
        Удалить календарь по идентификатору DELETE api/2.0/calendar/{calendarId}
        calendarId - число, его можно брать из файла calendar.txt при создании ("objectId": "10")
        :return: None
        """
        url_delete_calendar = url_create_calendar + '/' + str(calendar_id)
        response = requests.delete(url_delete_calendar, headers=self.headers)
        print("Удаление календаря со статусом", response.status_code)

    def get_default_params(self, url_create_calendar: str):
        """
        Получить параметры доступа по умолчанию GET api/2.0/calendar/sharing
        :return: None
        """
        url_default_params = url_create_calendar + '/sharing'
        response = requests.get(url_default_params, headers=self.headers)
        print("Получение параметров доступа по умолчанию", response.status_code)
        print(response.json())

    def get_calendar_params(self, url_create_calendar: str, calendar_id: int):
        """
        Получить параметры доступа конкретного календаря GET api/2.0/calendar/{calendarId}/sharing
        :return: None
        """
        url_calendar_params = url_create_calendar + '/' + str(calendar_id) + '/sharing'
        response = requests.get(url_calendar_params, headers=self.headers)
        print("Получение параметров доступа календаря", response.status_code)
        print(response.json())


if __name__ == "__main__":
    """
**************************************************************************************************
    Данные для авторизации
**************************************************************************************************
    """
    url_auth = "http://192.168.25.179/api/2.0/authentication"
    data_auth = {
        "userName": "safin.marat@r7-office.ru",
        "password": "12345678"
    }

    """
**************************************************************************************************
    Данные для создания календаря/удаления календаря
**************************************************************************************************
    """
    url_create_calendar = "http://192.168.25.179/api/2.0/calendar"
    data_create_calendar = {
          "name": "Some calendar3",
          "description": "new_one2",
          "textColor": "rgb(0, 0, 0)",
          "backgroundColor": "rgb(223, 120, 149)",
          "alertType": "never",
          "hideEvents": False,
          "isEditable": True,
          "sharingOptions": [
            {}
          ],
          "isShared": True,
          "iCalUrl": "new_text3",
          "isTodo": 1234,
          "timeZone": '(UTC+02:00)',
    }

    """
******************************************************************************************************
    Данные для изменения календаря
******************************************************************************************************
    """
    data_change_calendar = {
          "name": "Old new calendar",
          "description": "some text",
          "textColor": "some text",
          "backgroundColor": "some text",
          "timeZone": "some text",
          "alertType": "never",
          "hideEvents": True,
          "sharingOptions": [
            {}
          ],
          "iCalUrl": "some text"
    }

    request = Calendar()

    request.create(url_create_calendar, data_create_calendar)
