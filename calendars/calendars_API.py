import requests

from authentication.auth_API import Authentication


class Calendar:

    def __init__(self, url_auth: str, data_auth: dict) -> None:
        token = Authentication().request_auth(url_auth, data_=data_auth)
        self.headers = {'Authorization': f'Bearer {token}'}

        self.url_API_calendar = url_auth + '/api/2.0/calendar'
        print("Инициализация Модуля Календарь")
        print("***************************************************")

    def create_calendar(self, data_create_calendar: dict) -> int:
        """
        Создание календаря POST api/2.0/calendar
        :param data_create_calendar: данные для создаваемого словаря
        :return: id календаря
        """
        response = requests.post(self.url_API_calendar, json=data_create_calendar, headers=self.headers)
        data = response.json()
        print(f"Создание календаря с кодом:", response.status_code)
        return data['response']['objectId']

    def create_event_default_calendar(self, data_create_event: dict) -> int:
        """
        Создание события в календаре по умолчанию POST api/2.0/calendar/event
        :param data_create_event: данные для изменяемого события
        :return: id события
        """
        url_create_event_default = self.url_API_calendar + '/event'
        response = requests.post(url_create_event_default, json=data_create_event, headers=self.headers)
        data = response.json()
        print("Создание события в календаре по умолчанию с кодом:", response.status_code)
        return data['response'][0]['objectId']

    def create_event_calendar(self, data_create_event: dict, calendar_id: int) -> int:
        """
        Создание события в указанном календаре POST api/2.0/calendar/{calendarId}/event
        :param data_create_event: данные для создаваемого события
        :param calendar_id: номер календаря
        :return: id календаря
        """
        url_create_event_calendar = self.url_API_calendar + '/' + str(calendar_id) + '/event'
        response = requests.post(url_create_event_calendar, json=data_create_event, headers=self.headers)
        data = response.json()
        print(f"Создание события в календаре id={calendar_id} с кодом:", response.status_code)
        return data['response'][0]['objectId']

    def get_calendar(self, calendar_id: int) -> None:
        """
        Получить календарь по идентификатору GET api/2.0/calendars/{calendarId}
        :param calendar_id: номер календаря (номера смотрим в файле calendars.txt)
        :return: None
        """
        url_get_calendar = self.url_API_calendar + '/' + str(calendar_id)

        response = requests.get(url_get_calendar, headers=self.headers)
        print(f"Запрос календаря id={calendar_id} с кодом", response.status_code)
        print(response.json())

    def get_default_calendar_params(self) -> None:
        """
        Получить параметры доступа по умолчанию GET api/2.0/calendar/sharing
        :return: None
        """
        url_default_params = self.url_API_calendar + '/sharing'
        response = requests.get(url_default_params, headers=self.headers)
        data = response.json()
        print("Получение параметров доступа календаря по умолчанию с кодом:", response.status_code)
        print(data)

    def update_calendar(self, data_update_calendar: dict, calendar_id: str) -> None:
        """
        Обновление календаря PUT api/2.0/calendar/{calendarId}
        :param calendar_id: номер календаря (номера смотрим в файле calendars.txt)
        :param data_create_calendar: данные для изменяемого словаря
        :return: None
        """
        url_update_calendar = self.url_API_calendar + '/' + str(calendar_id)

        response = requests.put(url_update_calendar, json=data_update_calendar, headers=self.headers)
        print(f"Изменение календаря id={calendar_id} с кодом:", response.status_code)
        print(response.json())

    def update_event(self, data_update_event: dict, calendar_id: int, event_id: int) -> None:
        """
        Обновление события PUT api/2.0/calendar/{calendarId}/{eventId}
        :param calendar_id: номер календаря
        :param event_id: номер события
        :param data_create_event: данные обновляемого события
        :return: None
        """
        url_update_event = self.url_API_calendar + f'/{calendar_id}/{event_id}'
        response = requests.put(url_update_event, data_update_event, headers=self.headers)
        print(f"Обновление события <<id={event_id}>> из календаря <<id={calendar_id}>> с кодом:",
              response.status_code)

    def delete_calendar(self, calendar_id: int) -> None:
        """
        Удалить календарь по идентификатору DELETE api/2.0/calendars/{calendarId}
        :param calendar_id: номер календаря (номера смотрим в файле calendars.txt)
        :return: None
        """
        url_delete_calendar = self.url_API_calendar + '/' + str(calendar_id)

        response = requests.delete(url_delete_calendar, headers=self.headers)
        print(f"Удаление календаря id={calendar_id} с кодом", response.status_code)

    def delete_event(self, event_id: int) -> None:
        """
        Удаление события DELETE api/2.0/calendar/events/{eventId}
        :param event_id: id события
        :return: None
        """
        url_delete_event = self.url_API_calendar + f'/events/{event_id}'
        response = requests.delete(url_delete_event, headers=self.headers)
        print(f"Удаление серии событий <<id={event_id}>> из календаря с кодом:", response.status_code)

    def get_calendar_params(self, calendar_id: int) -> None:
        """
        Получить параметры доступа конкретного календаря GET api/2.0/calendars/{calendarId}/sharing
        :param calendar_id: номер календаря (номера смотрим в файле calendars.txt)
        :return: None
        """
        url_calendar_params = self.url_API_calendar + '/' + str(calendar_id) + '/sharing'
        response = requests.get(url_calendar_params, headers=self.headers)
        print(f"Получение параметров доступа календаря id={calendar_id} с кодом:", response.status_code)

    def get_event(self, event_id: int) -> None:
        """
        Получение события по идентификатору GET api/2.0/calendar/events/{eventId}/historybyid
        :param event_id: id события
        :return: None
        """
        url_get_event = self.url_API_calendar + '/events/' + str(event_id) + '/historybyid'
        response = requests.get(url_get_event, headers=self.headers)
        data = response.json()

        calendar_id = data['response']['calendarId']
        print(f"Получение события id={event_id} из календаря id={calendar_id} с кодом:", response.status_code)
        print(response.json())


if __name__ == "__main__":
    """
**************************************************************************************************
    Данные для авторизации (при запуске подставлять свои значения)
**************************************************************************************************
    """
    url_auth = "http://192.168.26.194"
    data_auth = {
        "userName": "support@r7-office.ru",
        "password": "Hsuhsh35dr"
    }

    """
**************************************************************************************************
    Данные для создания календаря/удаления календаря
**************************************************************************************************
    """
    data_create_calendar = {
        "name": "some text",
        "description": "some text",
        "textColor": "rgb(0, 0, 0)",
        "backgroundColor": "rgb(223, 120, 149)",
        "timeZone": "(UTC+02:00)",
        "alertType": "Never",
        "sharingOptions": [
            {}
        ],
        "iCalUrl": "some text"
        }

    """
******************************************************************************************************
    Данные для изменения календаря
******************************************************************************************************
    """
    data_update_calendar = {
        "name": "Old new calendars",
        "description": "some text",
        "textColor": "rgb(0, 0, 0)",
        "backgroundColor": "rgb(223, 120, 149)",
        "timeZone": "(UTC+03:00)",
        "alertType": "Never",
        "hideEvents": True,
        "sharingOptions": [
            {}
        ]
    }

    """
**************************************************************************************************
    Данные для создания события календаря
**************************************************************************************************
    """
    data_create_event = {
        "name": "New event",
        "description": "New event content",
        "startDate": "2023-10-10T06-30-00.000Z",
        "endDate": "2023-10-10T06-30-00.000Z",
        "repeatType": "RRULE:FREQ=NEVER",
        "alertType": "Never",
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
        "name": "EVENT",
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


