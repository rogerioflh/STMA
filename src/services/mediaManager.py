import json

class Observer:
    def update(self, event_type, data):
        pass


class MediaObserver(Observer):
    def update(self, event_type, data):
        print(f"[Notificação] Evento: {event_type} | Dados: {data}")


class MediaManager:
    _press_releases = []
    _observers = []

    def __init__(self, title, content, date):
        self._title = title
        self._content = content
        self._date = date
        MediaManager._press_releases.append(self)
        MediaManager.notify_observers("Novo Press Release", self.to_dict())

    # Observer methods
    @classmethod
    def add_observer(cls, observer):
        cls._observers.append(observer)

    @classmethod
    def remove_observer(cls, observer):
        cls._observers.remove(observer)

    @classmethod
    def notify_observers(cls, event_type, data):
        for observer in cls._observers:
            observer.update(event_type, data)

    # Getters e Setters
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    def __str__(self):
        return (
            f" Título: {self._title}\n"
            f" Conteúdo: {self._content}\n"
            f" Data: {self._date}"
        )

    def to_dict(self):
        return {
            "title": self._title,
            "content": self._content,
            "date": self._date
        }

    # CRUD
    @classmethod
    def get_release_by_title(cls, title):
        return next((r for r in cls._press_releases if r.title == title), None)

    @classmethod
    def remove_release(cls, title):
        release = cls.get_release_by_title(title)
        if release:
            cls._press_releases.remove(release)
            cls.notify_observers("Remoção de Press Release", {"title": title})
            print(f"Press Release '{title}' removido!")
        else:
            print(f"Press Release '{title}' não encontrado.")

    @classmethod
    def list_releases(cls):
        for release in cls._press_releases:
            print(release)

    @classmethod
    def save_to_json(cls, filename="press_releases.json"):
        with open(filename, "w") as file:
            json.dump([release.to_dict() for release in cls._press_releases], file, indent=4)

    @classmethod
    def load_from_json(cls, filename="press_releases.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                cls._press_releases = []
                for item in data:
                    release = MediaManager(item["title"], item["content"], item["date"])
                    cls._press_releases.append(release)
        except FileNotFoundError:
            print(f"Arquivo {filename} não encontrado. Iniciando com lista vazia.")
        except json.JSONDecodeError:
            print(f"Erro ao carregar {filename}. O arquivo pode estar corrompido.")
