import json, os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel = self.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()
        self.id = self.channel['items'][0]["id"]
        self.title = self.channel['items'][0]["snippet"]["title"]
        self.description = self.channel['items'][0]["snippet"]["description"]
        self.count_subscribers = self.channel['items'][0]["statistics"]["subscriberCount"]
        self.video_count = self.channel['items'][0]["statistics"]["videoCount"]
        self.views_count = self.channel['items'][0]["statistics"]["viewCount"]
        self.url = f"https://www.youtube.com/channel/{self.id}"


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        printj(self.channel)

    @property
    def channel_id(self):
        return self.__channel_id

    @channel_id.setter
    def channel_id(self, new_name):
        print("AttributeError: property 'channel_id' of 'Channel' object has no setter")
    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('YT_API_KEY')
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self, file_name):
        """Cохраняет в файл значения атрибутов экземпляра класса `Channel`"""
        dictionary = {
            "id": self.__channel_id,
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "subscriberCount": self.count_subscribers,
            "video_count": self.video_count,
            "viewCount": self.views_count
        }
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(dictionary, file, ensure_ascii=False)

def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))



