# Пример кода запуска тестирования на ВМ: python3 /CS_API/main.py http://192.168.26.130

import sys
import logging

from people.people_API import People
from authentication.auth_API import Authentication


DATA_AUTH = {
        "userName": "safin.marat@r7-office.ru",
        "password": "Hsuhsh35dr"
        }

DATA_PHONE = {
        "userName": "safin.marat@r7-office.ru",
        "password": "Hsuhsh35dr",
        "mobilePhone": "8(921)9516961"
    }

DATA_CREATE_PEOPLE = {
        "isVisitor": True,
        "email": "r7@mail.ru",
        "firstname": "Ivan",
        "lastname": "Ivanov",
        "password": "12345678"
        }

DATA_UPDATE_PEOPLE = {
        "isVisitor": False,
        "email": "r7testmail@mail.ru",
        "firstname": "Ivan",
        "lastname": "Ivan"
    }

logging.basicConfig(
    level=logging.INFO,  # Уровень логирования (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

if len(sys.argv) < 2:
    print("***************************************************")
    logging.error("Для запуска скрипта введите url Community Server")
    print("***************************************************")
else:
    URL = sys.argv[1]


def test_people(url=URL, data=DATA_AUTH, data_phone=DATA_PHONE):
    try:
        # модуль Аутентификация
        auth = Authentication()
        auth.request_auth(url, data)
        Authentication.set_phone(url, data_phone)
    except Exception:
        print("***************************************************")
        logging.info('Ошибка тестирования API модуля Аутентификация', Exception)
        print("***************************************************")

    else:
        print("***************************************************")
        logging.info('Тестирование API модуля Аутентификация прошло успешно')
        print("***************************************************")

    try:
        # модуль Люди
        people = People(url, data)
        people.create(DATA_CREATE_PEOPLE)
        people_list = people.get_all()
        people_id = people_list['response'][1]['id']
        people.update(data_update_people=DATA_UPDATE_PEOPLE, people_id=people_id)

    except Exception:
        print("***************************************************")
        logging.info('Ошибка тестирования API модуля Люди', Exception)
        print("***************************************************")

    else:
        print("***************************************************")
        logging.info('Тестирование API модуля Люди прошло успешно')
        print("***************************************************")


test_people()
