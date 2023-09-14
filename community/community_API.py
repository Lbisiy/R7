import requests

from authentication.auth_API import Authentication


class Community:

    def __init__(self, url_auth: str, data_auth: dict) -> None:
        token = Authentication().request_auth(url_auth, data_=data_auth)
        self.headers = {'Authorization': f'Bearer {token}'}
        self.url_API_project = url_auth + '/api/2.0/community'

    def create_blog_post(self, data_create_blog):
        """
        POST api/2.0/community/blog
        :return:
        """
        url_create_blog = self.url_API_project + '/blog'
        response = requests.post(url_create_blog, json=data_create_blog, headers=self.headers)
        data = response.json()
        print(f"Создание записи блога с кодом:", response.status_code)
        return data['response']['id']

    def update_blog_post(self, data_update_blog_post, blog_post_id):
        """
        PUT api/2.0/community/blog/{postid}
        :param data_update_blog_post:
        :return:
        """
        url_update_blog = self.url_API_project + f'/blog/{blog_post_id}'
        response = requests.put(url_update_blog, json=data_update_blog_post, headers=self.headers)
        print(f"Изменение записи блога с кодом:", response.status_code)

    def delete_blog_post(self, blog_post_id):
        """
        DELETE api/2.0/community/blog/{postid}
        :return:
        """
        url_delete_blog = self.url_API_project + f'/blog/{blog_post_id}'
        response = requests.delete(url_delete_blog, headers=self.headers)
        print(f"Удаление записи блога с кодом:", response.status_code)

    def create_blog_comment(self, data_blog_comment):
        """
        POST api/2.0/community/blog/comment
        :return:
        """
        url_create_blog = self.url_API_project + '/blog/comment'
        response = requests.post(url_create_blog, json=data_blog_comment, headers=self.headers)
        print(f"Создание записи в блоге с кодом:", response.status_code)

    def create_event(self, data_create_event):
        """
        POST api/2.0/community/event
        :return:
        """
        url_create_event = self.url_API_project + '/event'
        response = requests.post(url_create_event, json=data_create_event, headers=self.headers)
        data = response.json()
        print(f"Создание новости с кодом:", response.status_code)
        return data['response']['id']

    def update_event(self, data_update_event, event_id):
        """
        PUT api/2.0/community/event/{feedid}
        :param data_update_event:
        :param event_id:
        :return:
        """
        url_update_event = self.url_API_project + f'/event/{event_id}'
        response = requests.put(url_update_event, json=data_update_event, headers=self.headers)
        print(f"Изменение новости с кодом:", response.status_code)

    def delete_event(self, event_id):
        """
        DELETE api/2.0/community/event/{feedid}
        :return:
        """
        url_delete_event = self.url_API_project + f'/event/{event_id}'
        response = requests.delete(url_delete_event, headers=self.headers)
        print(f"Удаление новости:", response.status_code)

    def create_forum(self, data_create_forum):
        """
        POST api/2.0/community/forum
        :return:
        """
        url_create_forum = self.url_API_project + '/forum'
        response = requests.post(url_create_forum, json=data_create_forum, headers=self.headers)
        data = response.json()
        print(f"Создание форума с кодом:", response.status_code)
        return data['response']['id']

    def delete_forum(self, forum_id):
        """
        DELETE api/2.0/community/forum/thread/{threadid}
        :param forum_id:
        :return:
        """
        url_delete_forum = self.url_API_project + f'/forum/thread/{forum_id}'
        response = requests.delete(url_delete_forum, headers=self.headers)
        print("Удаление форума с кодом:", response.status_code)

    def create_forum_topic(self, data_create_topic, forum_id):
        """
        POST api/2.0/community/forum/{threadid}
        :param data_create_topic:
        :return:
        """
        url_create_topic = self.url_API_project + f'/forum/{forum_id}'
        response = requests.post(url_create_topic, json=data_create_topic, headers=self.headers)
        data = response.json()
        print(f"Создание темы форума с кодом:", response.status_code)
        return data['response']['id']

    def update_forum_topic(self, data_update_topic, topic_id):
        """
        PUT api/2.0/community/forum/topic/{topicid}
        :param data_create_topic:
        :param topic_id:
        :return:
        """
        url_update_topic = self.url_API_project + f'/forum/topic/{topic_id}'
        response = requests.put(url_update_topic, json=data_update_topic, headers=self.headers)
        print(f"Изменение темы форума с кодом:", response.status_code)

    def create_wiki_page(self, data_create_wiki):
        """
        POST api/2.0/community/wiki
        :return:
        """
        url_create_wiki = self.url_API_project + '/wiki'
        response = requests.post(url_create_wiki, json=data_create_wiki, headers=self.headers)
        data = response.json()
        print("Создание wiki страницы с кодом:", response.status_code)
        return data['response']['Name']

    def update_wiki_page(self, data_update_wiki, page_name: str):
        """
        PUT api/2.0/community/wiki/{name}
        :return:
        """
        url_update_wiki = self.url_API_project + f'/wiki/{page_name}'
        response = requests.put(url_update_wiki, json=data_update_wiki, headers=self.headers)
        print("Изменение wiki страницы с кодом:", response.status_code)

    def delete_wiki(self, page_name):
        """
        DELETE api/2.0/community/wiki/{name}
        :param page_name:
        :return:
        """
        url_delete_wiki = self.url_API_project + f'/wiki/{page_name}'
        response = requests.delete(url_delete_wiki, headers=self.headers)
        print("Удаление wiki страницы с кодом:", response.status_code)


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
    Данные для создания записи в блоге
**************************************************************************************************
    """
    data_blog_comment = {
        "entityid": "some text",
        "content": "some text"
    }
    """
**************************************************************************************************
    Данные для создания блога
**************************************************************************************************
    """
    data_create_blog = {
        "title": "My blog",
        "content": "Blog content",
        "tags": "Me,Post,News",
        "subscribeComments": True
    }
    """
**************************************************************************************************
    Данные для создания новости
**************************************************************************************************
    """
    data_create_news = {
        "title": "New1",
        "content": "New content",
        "type": "News"
    }
    """
**************************************************************************************************
    Данные для создания форума
**************************************************************************************************
    """
    data_create_forum = {
        "categoryId": -1,
        "categoryName": "Forum",
        "threadName": "Forum",
        "threadDescription": "Forum content"
    }
    """
**************************************************************************************************
    Данные для создания топика
**************************************************************************************************
    """
    data_create_topic = {
        "subject": "Topic name",
        "content": "Topic content",
        "topicType": "Informational"
    }
    """
**************************************************************************************************
    Данные для создания топика
**************************************************************************************************
    """
    data_create_wiki_page = {
        "name": "Wiki_page",
        "body": "Wiki content"
    }
    """
**************************************************************************************************
    Данные для изменения записи блога
**************************************************************************************************
    """
    data_update_blog_post = {
        "title": "Updated blog",
        "content": "Updated blog content",
        "tags": "Me,Post,News"
    }
    """
**************************************************************************************************
    Данные для изменения новости
**************************************************************************************************
    """
    data_update_news = {
        "title": "Updated news",
        "content": "Updated news content",
        "type": "News"
    }
    """
**************************************************************************************************
    Данные для изменения темы форума
**************************************************************************************************
    """
    data_update_topic = {
        "subject": "Updated topic name",
        "sticky": False,
        "closed": False
    }
    """
**************************************************************************************************
    Данные для изменения wiki страницы
**************************************************************************************************
    """
    data_update_wiki_page = {
        "body": "Updated Wiki content"
    }


