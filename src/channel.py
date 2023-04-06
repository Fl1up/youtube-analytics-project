import json

class Channel:
    """Класс для ютуб-канала"""
    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        with open("text.json","r") as file:
            for i in file:
                print(json.dumps(i.strip('\n,",",{},[]'), indent=2, ensure_ascii=False))