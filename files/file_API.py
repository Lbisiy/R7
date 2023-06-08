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

    def get_from_my_chapter(self) -> None:
        """
        Получение всех файлов и папок из раздела «Мои документы» GET api/2.0/files/@my
        :return: None
        """
        url_get_in_my = self.url_API_files + '/@my'
        response = requests.get(url_get_in_my, headers=self.headers)
        date = response.json()

        print(f"Получение содержимого «Мои документы» с кодом:", response.status_code)
        print(date)

    def get_from_accessible_chapter(self) -> None:
        """
        Получение всех файлов и папок из раздела «Доступно для меня» GET api/2.0/files/@share
        :return: None
        """
        url_get_in_common = self.url_API_files + '/@share?searchInContent=True&withSubfolders=True'
        response = requests.get(url_get_in_common, headers=self.headers)
        data = response.json()

        print(f"Получение содержимого «Доступно для меня» с кодом:", response.status_code)
        print(data)

    def get_all_chapters(self) -> None:
        """
        Получение содерживого всех разделов GET api/2.0/files/@root
        :return: None
        """
        url_get_all_chapters = self.url_API_files + '/@root?searchInContent=True&withSubfolders=True&withoutTrash=True&withoutAdditionalFolder=True'
        response = requests.get(url_get_all_chapters, headers=self.headers)
        data = response.json()

        print(f"Получение содержимого всех разделов с кодом:", response.status_code)
        print(data)

    def get_from_common_chapter(self) -> None:
        """
        Получение списка файлов и папок, находящихся в разделе «Общие» GET api/2.0/files/@common
        :return: None
        """
        url_get_from_common = self.url_API_files + '/@common?searchInContent=True&withSubfolders=True'
        response = requests.get(url_get_from_common, headers=self.headers)
        data = response.json()

        print(f"Получение содержимого «Общие» с кодом:", response.status_code)
        print(data)

    def get_from_favorite_chapter(self) -> None:
        """
        Получение файлов и папок раздела «Избранное» GET api/2.0/files/@favorites
        :return: None
        """
        url_get_from_favorite = self.url_API_files + '/@favorites?searchInContent=True&withSubfolders=True'
        response = requests.get(url_get_from_favorite, headers=self.headers)
        data = response.json()

        print(f"Получение содержимого «Избранное» с кодом:", response.status_code)
        print(data)

    def rename_folder(self, data_rename_folder: dict, folder_id: int) -> None:
        """
        Переименование папки PUT api/2.0/files/folder/{folderId}
        :param data_rename_folder: новое название папки
        :param folder_id: идентификатор переименуемой папки
        :return: None
        """
        url_rename_folder = self.url_API_files + f'/folder/{folder_id}'
        response = requests.put(url_rename_folder, json=data_rename_folder, headers=self.headers)
        data = response.json()

        print(f"Переименование папки id={folder_id} с кодом:", response.status_code)
        print(data)

    def move_to_folder(self, data_move_file: dict) -> None:
        """
        Перемещение файлов и папок в указанную папку PUT api/2.0/files/fileops/move
        :param data_move_file: данные о перемещаемых папках и файлах и папке назначения
        :return: None
        """
        url_move_file = self.url_API_files + '/fileops/move'
        response = requests.put(url_move_file, json=data_move_file, headers=self.headers)
        data = response.json()

        print(f"Перемещение в папку с кодом:", response.status_code)
        print(data)

    def delete_list(self, data_delete: dict) -> None:
        """
        Удаление папок и файлов PUT api/2.0/files/fileops/delete
        :param data_delete: данные об удаляемых файлах и папках
        :return: None
        """
        url_delete_list = self.url_API_files + '/fileops/delete'
        response = requests.put(url_delete_list, json=data_delete, headers=self.headers)
        data = response.json()

        print(f"Удаление с кодом:", response.status_code)
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
    Данные для создания папки
**************************************************************************************************
    """
    data_create_folder = {
        "title": "My folder2",
    }
    """
**************************************************************************************************
    Данные для переименования папки
**************************************************************************************************
    """
    data_rename_folder = {
        "title": "Renamed folder"
    }
    """
**************************************************************************************************
    Данные для перемещения папок и файла в папку
**************************************************************************************************
      """
    data_move_file = {
        "destFolderId": "2",
        "folderIds": [
            "36",
            "35",
        ],
        "fileIds": [
        ],
        "conflictResolveType": "Overwrite",
        "deleteAfter": True
    }
    """
**************************************************************************************************
    Данные для удаления папок и файлов
**************************************************************************************************
      """
    data_delete = {

        "folderIds": [
            "34",
            "35",
            "36"
        ],
        "fileIds": [

        ],
        "deleteAfter": True,
        "immediately": True
    }

    files = Files(url_auth, data_auth)
    files.delete_list(data_delete)
