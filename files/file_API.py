import datetime

import requests

from authentication.auth_API import Authentication
from people.people_API import People


class Files:

    def __init__(self, url_auth: str, data_auth: dict) -> None:
        token = Authentication().request_auth(url_auth, data_=data_auth)
        self.headers = {'Authorization': f'Bearer {token}'}

        self.url_API_files = url_auth + '/api/2.0/files'
        print("Инициализация Модуля Документы")
        print("***************************************************")

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

        print(f"Загрузка файла <<{file_name}>> в Мои документы с кодом:", response.status_code)
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

        print(f"Загрузка файла <<{file_name}>> в общий раздел с кодом:", response.status_code)
        print(data)

    def create_folder(self, data_create_folder: dict, folder_id: int = 1) -> int:
        """
        Создание папки POST api/2.0/files/folder/{folderId}
        :param data_create_folder: данные изменяемой папки
        :param folder_id: номер родительской папки
        :return: id папки
        """
        url_create_folder = self.url_API_files + f'/folder/{folder_id}'
        response = requests.post(url_create_folder, json=data_create_folder, headers=self.headers)
        data = response.json()

        # with open(f"created_folders/folders_{datetime.date.today()}.txt", "a") as f:
        #     f.writelines(str(data) + '\n')

        print(f"Создание папки в родительской папке <<id={folder_id}>> с кодом:", response.status_code)
        return data["response"]["id"]

    def delete_folder(self, data_delete_folder: dict, folder_id: int) -> None:
        """
        Удаление папки с заданным идентификатором DELETE api/2.0/files/folder/{folderId}
        :param data_delete_folder: словарь с параметрами удаления
        :param folder_id: идентификатор папки
        :return: None
        """
        url_delete_folder = self.url_API_files + f'/folder/{folder_id}'
        response = requests.delete(url_delete_folder, json=data_delete_folder, headers=self.headers)
        print(f"Удаление папки с кодом:", response.status_code)

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
        :param folder_id: идентификатор папки к переименованию
        :return: None
        """
        url_rename_folder = self.url_API_files + f'/folder/{folder_id}'
        response = requests.put(url_rename_folder, json=data_rename_folder, headers=self.headers)
        data = response.json()

        print(f"Переименование папки <<id={folder_id}>> с кодом:", response.status_code)
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

    def create_file(self, data_create_file: dict) -> int:
        """
        Создание файла в моем разделе POST api/2.0/files/@my/file
        :param data_create_file: словарь с названием и расширением файла
        :return: id созданного файла
        """
        url_create_file = self.url_API_files + '/@my/file'
        response = requests.post(url_create_file, json=data_create_file, headers=self.headers)
        data = response.json()
        print(f"Создание файла с кодом:", response.status_code)
        return data['response']['id']

    def update_file(self, file_id: str, data_update_file: dict) -> None:
    # не работает
        """
        Изменение содержимого файла с идентификатором PUT api/2.0/files/{fileId}/update
        :param file_id: идентификатор файла
        :param data_update_file: данные изменения файла
        :return: None
        """
        url_update_file = self.url_API_files + f'/{file_id}' + '/update'
        response = requests.put(url_update_file, json=data_update_file, headers=self.headers)
        print(f"Изменение файла с кодом:", response.status_code)

    def open_file(self, file_id: str) -> None:
        """
        Открытие файла GET api/2.0/files/file/{fileId}/openedit
        :param file_id: id файла
        :return: None
        """
        url_open_file = self.url_API_files + f'/file/{file_id}/openedit'
        response = requests.get(url_open_file, headers=self.headers)
        data = response.json()
        print(data)

    def get_file_version(self, file_id: str) -> None:
        """
        Получение истории файла GET api/2.0/files/file/{fileId}/history
        :param file_id: id файла
        :return: None
        """
        url_file_version = self.url_API_files + f'/file/{file_id}/history'
        response = requests.get(url_file_version, headers=self.headers)
        data = response.json()
        print(f"Получение истории файла с кодом:", response.status_code)
        print(data)

    def get_file_properties(self, file_id: str) -> None:
        """
        Получение свойств файла GET api/2.0/files/{fileId}/properties
        :param file_id: id файла
        :return: None
        """
        url_file_properties = self.url_API_files + f'/{file_id}/properties'
        response = requests.get(url_file_properties, headers=self.headers)
        data = response.json()
        print(f"Получение свойств файла с кодом:", response.status_code)
        print(data)

    def delete_file(self, file_id: int, data_delete_file: dict) -> None:
        """
        Удаление файла с заданным идентификатором DELETE api/2.0/files/file/{fileId}
        :param file_id: идентификатор файла
        :param data_delete_file: словарь с параметрами удаления
        :return: None
        """
        url_delete_file = self.url_API_files + f'/file/{file_id}'
        response = requests.delete(url_delete_file, json=data_delete_file, headers=self.headers)
        print(f"Удаление файла с кодом:", response.status_code)

    def share_file(self, data_share_file: dict, file_id: int) -> None:
        """
        Установить права общего доступа к файлу с идентификатром PUT api/2.0/files/file/{fileId}/share
        :param data_share_file: данные параметров доступа
        :param file_id: идентификатор файла

        :return: None
        """
        url_share_file = self.url_API_files + f'/file/{file_id}/share'
        response = requests.put(url_share_file, json=data_share_file, headers=self.headers)
        print(f"Расшаривание файла с правом <<{data_share_file['share'][0]['access']}>> (1-Полный, 2-Чтение) с кодом:", response.status_code)

    def delete_share_rights(self, data_delete_share_rights: dict) -> None:
        # не работает
        """
        Удаление шары группы папок DELETE api/2.0/files/share
        :param data_delete_share_rights: данные группы папок для удаления шары
        :return: None
        """
        url_share_file = self.url_API_files + f'/share'
        response = requests.delete(url_share_file, json=data_delete_share_rights, headers=self.headers)
        print(f"Удаление шары файлов: <<{data_delete_share_rights['fileIds']}>>, папок:\
        <<{data_delete_share_rights['folderIds']}>> с кодом:", response.status_code)

    def get_shared_file_info(self, file_id: str) -> None:
        """
        Получение детальной информации о расшаренном файле GET api/2.0/files/file/{fileId}/share
        :param file_id: id файла
        :return: None
        """
        url_share_file = self.url_API_files + f'/file/{file_id}/share'
        response = requests.get(url_share_file, headers=self.headers)
        data = response.json()
        print(f"Получение информации о расшаренном файле с кодом:", response.status_code)
        print(data)


