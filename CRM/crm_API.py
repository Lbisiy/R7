import datetime

import requests

from authentication.auth_API import Authentication


class CRM:

    def __init__(self, url_auth: str, data_auth: dict) -> None:
        token = Authentication().request_auth(url_auth, data_=data_auth)
        self.headers = {'Authorization': f'Bearer {token}'}
        self.url_API_project = url_auth + '/api/2.0/crm'

    def create_person(self, data_create_person) -> int:
        """
        POST api/2.0/crm/contact/person
        :return:
        """
        url_create_person = self.url_API_project + '/contact/person'
        response = requests.post(url_create_person, json=data_create_person, headers=self.headers)
        data = response.json()

        print(f"Создание персоны с кодом:", response.status_code)
        return data['response']['id']

    def delete_contact(self, contact_id):
        """
        Удаление компании или персоны
        DELETE api/2.0/crm/contact/{contactid}
        :param contact_id:
        :return:
        """
        url_delete_contact = self.url_API_project + f'/contact/{contact_id}'
        response = requests.delete(url_delete_contact, headers=self.headers)
        print(f"Удаление контакта с кодом:", response.status_code)

    def update_person(self, data_update_person, person_id):
        """
        PUT api/2.0/crm/contact/person/{personid}
        :param data_update_person:
        :return:
        """
        url_update_person = self.url_API_project + f'/contact/person/{person_id}'
        response = requests.put(url_update_person, json=data_update_person, headers=self.headers)
        print(f"Изменение персоны с кодом:", response.status_code)

    def create_company(self, data_create_company) -> int:
        """
        POST api/2.0/crm/contact/company
        :param data_create_company:
        :return:
        """
        url_create_company = self.url_API_project + '/contact/company'
        response = requests.post(url_create_company, json=data_create_company, headers=self.headers)
        data = response.json()

        print(f"Создание компании с кодом:", response.status_code)
        return data['response']['id']

    def update_company(self, data_update_company, company_id):
        """
        PUT api/2.0/crm/contact/company/{companyid}
        :return:
        """
        url_update_company = self.url_API_project + f'/contact/company/{company_id}'
        response = requests.put(url_update_company, json=data_update_company, headers=self.headers)

        print(f"Изменение компании с кодом:", response.status_code)

    def create_task(self, data_create_task):
        """
        POST api/2.0/crm/task
        :return:
        """
        url_create_task = self.url_API_project + '/task'
        response = requests.post(url_create_task, json=data_create_task, headers=self.headers)
        data = response.json()

        print(f"Создание задачи с кодом:", response.status_code)
        return data['response']['id']

    def update_task(self, data_update_crm_task, task_crm_id):
        """
        PUT api/2.0/crm/task/{taskid}
        :return:
        """
        url_update_task = self.url_API_project + f'/task/{task_crm_id}'
        response = requests.put(url_update_task, json=data_update_crm_task, headers=self.headers)
        print(f"Изменение задачи с кодом:", response.status_code)

    def delete_task(self, task_id):
        """
        DELETE api/2.0/crm/task/{taskid}
        :param task_id:
        :return:
        """
        url_delete_task = self.url_API_project + f'/task/{task_id}'
        response = requests.delete(url_delete_task, headers=self.headers)
        print(f"Удаление задачи с кодом:", response.status_code)

    def create_opportunity(self, data_create_opportunity):
        """
        POST api/2.0/crm/opportunity
        :return:
        """
        url_create_opportunity = self.url_API_project + '/opportunity'
        response = requests.post(url_create_opportunity, json=data_create_opportunity, headers=self.headers)
        data = response.json()

        print(f"Создание возможной сделки с кодом:", response.status_code)
        return data['response']['id']

    def update_opportunity(self, data_update_opportunity, opportunity_id):
        """
        PUT api/2.0/crm/opportunity/{opportunityid}
        :param data_update_opportunity:
        :return:
        """
        url_update_opportunity = self.url_API_project + f'/opportunity/{opportunity_id}'
        response = requests.put(url_update_opportunity, json=data_update_opportunity, headers=self.headers)
        print(f"Изменение возможной сделки с кодом:", response.status_code)

    def delete_opportunity(self, opportunity_id):
        """
        DELETE api/2.0/crm/opportunity/{opportunityid}
        :param opportunity_id:
        :return:
        """
        url_delete_opportunity = self.url_API_project + f'/opportunity/{opportunity_id}'
        response = requests.delete(url_delete_opportunity, headers=self.headers)
        print(f"Удаление возможной сделки с кодом:", response.status_code)

    def create_invoice(self, data_create_invoice: dict) -> int:
        """
        POST api/2.0/crm/invoice
        :return:
        """
        url_create_invoice = self.url_API_project + '/invoice'
        response = requests.post(url_create_invoice, json=data_create_invoice, headers=self.headers)
        data = response.json()

        print(f"Создание счета с кодом:", response.status_code)
        return data['response']['id']

    def create_invoice_item(self, data_invoice_item: dict) -> int:
        """
        POST api/2.0/crm/invoiceitem
        :param data_invoice_item:
        :return:
        """
        url_create_invoice_item = self.url_API_project + '/invoiceitem'
        response = requests.post(url_create_invoice_item, json=data_invoice_item, headers=self.headers)
        data = response.json()

        print(f"Создание товара с кодом:", response.status_code)
        return data['response']['id']

    def update_invoice(self, data_update_invoice, invoice_id):
        """
        PUT api/2.0/crm/invoice/{id}
        :return:
        """
        url_update_invoice = self.url_API_project + f'/invoice/{invoice_id}'
        response = requests.put(url_update_invoice, json=data_update_invoice, headers=self.headers)
        print(f"Изменение инвойса с кодом:", response.status_code)

    def delete_invoice(self, invoice_id):
        """
        DELETE api/2.0/crm/invoice/{invoiceid}
        :param invoice_id:
        :return:
        """
        url_delete_invoice = self.url_API_project + f'/invoice/{invoice_id}'
        response = requests.delete(url_delete_invoice, headers=self.headers)
        print(f"Удаление инвойса с кодом:", response.status_code)

    def create_event(self, data_create_event: dict) -> int:
        """
        POST api/2.0/crm/history
        :param data_create_event:
        :return:
        """
        url_create_event = self.url_API_project + '/history'
        response = requests.post(url_create_event, json=data_create_event, headers=self.headers)
        data = response.json()

        print(f"Создание мероприятия с кодом:", response.status_code)
        return data['response']['id']

    def delete_event(self, event_id):
        """
        DELETE api/2.0/crm/history/{id}
        :return:
        """
        url_delete_event = self.url_API_project + f'/history/{event_id}'
        response = requests.delete(url_delete_event, headers=self.headers)
        print(f"Удаление мероприятия <<id={event_id}>> с кодом:", response.status_code)

    def generate_report(self, data_generate_report):
        """
        POST api/2.0/crm/report/generate
        :return:
        """
        url_generate_report = self.url_API_project + '/report/generate'
        response = requests.post(url_generate_report, json=data_generate_report, headers=self.headers)
        data = response.json()
        print(f"Создание отчета <<{data_generate_report['type']}>> с кодом:", response.status_code)
        return data['response']['fileId']

    def delete_report_file(self, file_id):
        """
        DELETE api/2.0/crm/report/file/{fileid}
        :return:
        """
        url_delete_report = self.url_API_project + f'/report/{file_id}'
        response = requests.delete(url_delete_report, headers=self.headers)
        print(f"Удаление отчета с кодом:", response.status_code)


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
    Данные для создания персоны
**************************************************************************************************
    """
    data_create_person = {
          "firstName": "Fedor",
          "lastName": "Fedorov",
          "shareType": "None"
    }
    """
**************************************************************************************************
    Данные для создания компании
**************************************************************************************************
    """
    data_create_company = {
          "companyName": "Company1"
    }
    """
**************************************************************************************************
    Данные для создания задачи
**************************************************************************************************
    """
    data_create_task = {
          "title": "New task",
          "description": "Task content",
          "deadline": "2025-01-01T06-30-00.000Z",
          "responsibleId": "9924256A-739C-462b-AF15-E652A3B1B6EB",
          "categoryId": 1234,
    }
    """
**************************************************************************************************
    Данные для создания возможной сделки
**************************************************************************************************
    """
    data_create_opportunity = {
          "contactid": 0,
          "title": "Possible deal",
          "responsibleid": "0",
          "bidType": "FixedBid",
          "bidValue": 1000000,
          "bidCurrencyAbbr": "RUB",
          "perPeriodValue": 1,
          "stageid": 1,
          "isPrivate": True,
        }
    """
**************************************************************************************************
    Данные для создания счета
**************************************************************************************************
    """
    data_create_invoice = {
               "number": "invoice000001",
               "issueDate": f"2023-12-12T06-30-00.000Z",
               "contactId": 10,
               "dueDate": "2025-06-01T00:00:00",
               "language": "es-ES",
               "currency": "RUB",
               "exchangeRate": 1.1,
               "terms": "Terms for this invoice",
               "invoiceLines":
               [{
                     "invoiceItemID": 1,
                     "description": "description for invoice line 1",
                     "quantity": 100,
                     "price": 7.7,
                     "discount": 0
               }]
    }
    """
**************************************************************************************************
    Данные для создания товара
**************************************************************************************************
    """
    data_create_item = {
        "title": "Item1",
        "price": 1.1
    }
    """
**************************************************************************************************
    Данные для создания мероприятия
**************************************************************************************************
    """
    data_create_event = {
        "contactId": 0,
        "content": "Exhibition",
        "categoryId": 1,
        }
    """
**************************************************************************************************
    Данные для генерации отчета
**************************************************************************************************
    """
    data_generate_report = {
        "type": "SalesByManagers",
        "timePeriod": "DuringAllTime",
        "managers": [
            "0",
        ]
    }
    """
**************************************************************************************************
    Данные для изменения компании
**************************************************************************************************
    """
    data_update_company = {
        "companyName": "Updated company",
        "about": "Updated company content",
        "shareType": "None"
    }
    """
**************************************************************************************************
    Данные для изменения персоны
**************************************************************************************************
    """
    data_update_person = {
        "firstName": "Boris",
        "lastName": "Borisov",
        "shareType": "None",
        "managerList": ["0"]
        }
    """
**************************************************************************************************
    Данные для изменения задачи
**************************************************************************************************
    """
    data_update_task = {
        "title": "Updated task",
        "description": "Updated task content",
        "deadline": "2026-01-01T06-30-00.000Z",
        "responsibleid": "0",
        "categoryid": 1234,
        "contactid": 1234,
        "entityType": "Case",
        "entityid": 1234,
        "isNotify": True,
        }
    """
**************************************************************************************************
    Данные для изменения возможной сделки
**************************************************************************************************
    """
    data_update_opportunity = {
        "contactid": 1234,
        "title": "Updated opportunity",
        "description": "Updated opportunity content",
        "responsibleid": "0"
        }
