import datetime

import requests

from authentication.auth_API import Authentication


class Calendar:

    def __init__(self, url_auth, data_auth, url_API_calendar) -> None:

        token = Authentication().request_auth(url_auth, data_=data_auth)
        self.headers = {'Authorization': f'Bearer {token}'}

        self.url_API_calendar = url_API_calendar

    def create(self, data_create_calendar: dict) -> None:
        """
        Создание календаря POST api/2.0/calendar
        :param url_auth: URL авторизации
        :param url_create_calendar: URL создания календаря
        :param data_auth: логин, пароль для авторизации
        :param data_create_calendar: данные для создаваемого словаря
        :return: None
        """

        response = requests.post(self.url_API_calendar, json=data_create_calendar, headers=self.headers)
        data = response.json()

        with open(f"calendars/calendars_{datetime.date.today()}.txt", "a") as f:
            f.writelines(str(data) + '\n')
        print(f"Создание календаря id={data['response']['objectId']} с кодом:", response.status_code)

    def get_(self, calendar_id: int) -> None:
        """
        Получить календарь по идентификатору GET api/2.0/calendar/{calendarId}
        :param calendar_id: номер календаря (номера смотрим в файле calendar.txt)
        :return: None
        """
        url_get_calendar = self.url_API_calendar + '/' + str(calendar_id)

        response = requests.get(url_get_calendar, headers=self.headers)
        print(f"Запрос календаря id={calendar_id} с кодом", response.status_code)
        print(response.json())

    def update(self, calendar_id: str, data_update_calendar: dict) -> None:
        """
        Обновление календаря PUT api/2.0/calendar/{calendarId}
        :param calendar_id: номер календаря (номера смотрим в файле calendar.txt)
        :param data_create_calendar: данные для изменяемого словаря
        :return: None
        """
        url_update_calendar = self.url_API_calendar + '/' + str(calendar_id)

        response = requests.put(url_update_calendar, json=data_update_calendar, headers=self.headers)
        print(f"Изменение календаря id={calendar_id} с кодом:", response.status_code)
        print(response.json())

    def delete(self, calendar_id: int) -> None:
        """
        Удалить календарь по идентификатору DELETE api/2.0/calendar/{calendarId}
        :param calendar_id: номер календаря (номера смотрим в файле calendar.txt)
        :return: None
        """
        url_delete_calendar = self.url_API_calendar + '/' + str(calendar_id)

        response = requests.delete(url_delete_calendar, headers=self.headers)
        print(f"Удаление календаря id={calendar_id} с кодом", response.status_code)

    def get_default_params(self) -> None:
        """
        Получить параметры доступа по умолчанию GET api/2.0/calendar/sharing
        :return: None
        """
        url_default_params = self.url_API_calendar + '/sharing'

        response = requests.get(url_default_params, headers=self.headers)
        print("Получение параметров доступа календаря по умолчанию с кодом:", response.status_code)
        print(response.json())

    def get_calendar_params(self, calendar_id: int) -> None:
        """
        Получить параметры доступа конкретного календаря GET api/2.0/calendar/{calendarId}/sharing
        :param calendar_id: номер календаря (номера смотрим в файле calendar.txt)
        :return: None
        """
        url_calendar_params = self.url_API_calendar + '/' + str(calendar_id) + '/sharing'
        response = requests.get(url_calendar_params, headers=self.headers)
        print(f"Получение параметров доступа календаря id={calendar_id} с кодом:", response.status_code)
        print(response.json())

    def create_event_default(self, data_create_event: dict) -> None:
        """
        Создание события в календаре по умолчанию POST api/2.0/calendar/event
        :param data_create_event: данные для изменяемого события
        :return: None
        """
        url_create_event_default = self.url_API_calendar + '/event'
        response = requests.post(url_create_event_default, json=data_create_event, headers=self.headers)
        data = response.json()

        with open(f"calendars/events_{datetime.date.today()}.txt", "a") as f:
            f.writelines(str(data) + '\n')
        print("Создание события в календаре по умолчанию с кодом:", response.status_code)

    def create_event_calendar(self, data_create_event: dict, calendar_id: int) -> None:
        """
        Создание события в указанном календаре POST api/2.0/calendar/{calendarId}/event
        :param data_create_event: данные для создаваемого события
        :param calendar_id: номер календаря
        :return: None
        """
        url_create_event_calendar = self.url_API_calendar + '/' + str(calendar_id) + '/event'
        response = requests.post(url_create_event_calendar, json=data_create_event, headers=self.headers)
        data = response.json()

        with open(f"calendars/events_{datetime.date.today()}.txt", "a") as f:
            f.writelines(str(data) + '\n')
        print(f"Создание события в календаре id={calendar_id} с кодом:", response.status_code)

    def get_event(self, event_id: int) -> None:
        """
        Получение события по идентификатору
        :param номер события
        :return: None
        """
        url_get_event = self.url_API_calendar + '/events/' + str(event_id) + '/historybyid'
        response = requests.get(url_get_event, headers=self.headers)
        data = response.json()

        calendar_id = data['response']['calendarId']
        print(f"Получение события id={event_id} из календаря id={calendar_id} с кодом:", response.status_code)
        print(response.json())

    def update_event(self, calendar_id: int, event_id: int, data_create_event: dict) -> None:
        """
        Обновление события PUT api/2.0/calendar/{calendarId}/{eventId}
        :param calendar_id: номер календаря
        :param event_id: номер события
        :param data_create_event: данные обновляемого события
        :return: None
        """
        url_update_event = self.url_API_calendar + f'/{calendar_id}/{event_id}'
        response = requests.put(url_update_event, data_create_event, headers=self.headers)
        data = response.json()

        print(f"Обновление события id={event_id} из календаря id={calendar_id} с кодом:", response.status_code)
        print(response.json())

    def delete_series_event(self, event_id: int) -> None:
        """
        Удаление серии событий DELETE api/2.0/calendar/events/{eventId}
        :return: None
        """
        url_delete_event = self.url_API_calendar + f'/events/{event_id}'
        response = requests.delete(url_delete_event, headers=self.headers)

        print(f"Удаление серии событий id={event_id} с кодом:", response.status_code)


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
    Данные для создания календаря/удаления календаря
**************************************************************************************************
    """
    url_API_calendar = "http://192.168.25.179/api/2.0/calendar"
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
          "timeZone": '(UTC+02:00)'
    }

    """
******************************************************************************************************
    Данные для изменения календаря
******************************************************************************************************
    """
    data_update_calendar = {
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

    """
**************************************************************************************************
    Данные для создания события календаря
**************************************************************************************************
    """
    data_create_event = {
          "name": "New event",
          "startDate": "2023-06-10",
          "endDate": "2023-06-10",
          "repeatType": "RRULE:FREQ=NEVER",
          "alertType": "default",
          "isAllDayLong": True,
          "sharingOptions": [
            {}
          ]
    }

    """
******************************************************************************************************
    Данные для изменения события календаря
******************************************************************************************************
    """
    data_update_event = {
          "name": "New event",
          "startDate": "2023-06-11",
          "endDate": "2023-06-11",
          "repeatType": "RRULE:FREQ=NEVER",
          "alertType": "never",
          "isAllDayLong": True,
          "sharingOptions": [
            {}
          ],
          "status": "tentative"
    }
    """
******************************************************************************************************
    """

    calendar = Calendar(url_auth, data_auth, url_API_calendar)
