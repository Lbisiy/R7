import datetime

import requests

from authentication.auth_API import Authentication


class Files:

    def __init__(self, url_auth: str, data_auth: dict) -> None:
        token = Authentication().request_auth(url_auth, data_=data_auth)
        self.headers = {'Authorization': f'Bearer {token}'}

        self.url_API_files = url_auth + '/api/2.0/files'

    def upload_file(self, file_name: str) -> None:
        """
        Загрузка файла в раздел Мои документы POST api/2.0/files/@my/upload
        :param file_name: название добавляемого файла
        :return: None
        """
        url_load_file = self.url_API_files + '/@my/upload'

        with open(f'upload_source/{file_name}', 'rb') as file:
            response = requests.post(url_load_file, files={'file': file}, headers=self.headers)
        data = response.json()

        print(f"Загрузка файла {file_name} в Мои документы с кодом:", response.status_code)
        print(data)

    def upload_common_file(self, file_name: str) -> None:
        """
        Загрузка файла в Общий раздел POST api/2.0/files/@common/upload
        :param file_name: название добавляемого файла
        :return: None
        """
        url_load_file = self.url_API_files + '/@common/upload'

        with open(f'upload_source/{file_name}', 'rb') as file:
            response = requests.post(url_load_file, files={'file': file}, headers=self.headers)
        data = response.json()

        print(f"Загрузка файла {file_name} в общий раздел с кодом:", response.status_code)
        print(data)

    def create_folder(self, data_create_folder: dict, folder_id: int = 2) -> None:
        """
        Создание папки POST api/2.0/files/folder/{folderId}
        :param data_create_folder: данные изменяемой папки
        :param folder_id: номер родительской папки
        :return: None
        """
        url_create_folder = self.url_API_files + f'/folder/{folder_id}'
        response = requests.post(url_create_folder, data_create_folder, headers=self.headers)
        data = response.json()

        with open(f"created_folders/folders_{datetime.date.today()}.txt", "a") as f:
            f.writelines(str(data) + '\n')

        print(f"Создание папки в родительской папке id={folder_id} с кодом:", response.status_code)
        print(data)

    def get_all_from_my(self):
        """
        Получение всех файлов и папок в разделе Мои документы GET api/2.0/files/@my
        :return: None
        """
        url_get_in_my = self.url_API_files + '/@my'
        response = requests.get(url_get_in_my, headers=self.headers)
        date = response.json()

        print(f"Получение содержимого Мои документы с кодом:", response.status_code)
        print(date)


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
    Данные для создания папки
**************************************************************************************************
    """
    data_create_folder = {
        "title": "My folder2",
    }

    files = Files(url_auth, data_auth)
