import json
from src.utils.event import Event
from datetime import datetime
import os

class MatchScheduler(Event):
    competitions_list = []

    def __init__(self, type, location, date, time, opponent, status=False):
        super().__init__(type, date, time, location)
        self.__opponent = opponent
        self.__status = status
        MatchScheduler.competitions_list.append(self)
        MatchScheduler.save_to_json()

    # Getters
    def get_opponent(self):
        return self.__opponent

    def get_status(self):
        return self.__status

    # Setters
    def set_opponent(self, opponent):
        self.__opponent = opponent
        MatchScheduler.save_to_json()

    def set_status(self, status):
        self.__status = status
        MatchScheduler.save_to_json()

    def schedule_match(self):
        return f"Partida agendada: {self.get_type()} contra {self.__opponent} em {self.get_location()}, no dia {self.get_date()} às {self.get_time()}."

    def mark_as_completed(self):
        self.__status = True
        MatchScheduler.save_to_json()
        return f"Partida {self.get_type()} contra {self.__opponent} marcada como concluída."

    def mark_as_not_completed(self):
        self.__status = False
        MatchScheduler.save_to_json()
        return f"Partida {self.get_type()} contra {self.__opponent} marcada como não concluída."

    def check_status(self):
        try:
            datetime_evento = datetime.strptime(f"{self.get_date()} {self.get_time()}", "%d/%m/%Y %H:%M")
            return "A partida já ocorreu." if datetime_evento < datetime.now() else "A partida ainda não ocorreu."
        except ValueError:
            return "Formato de data ou hora inválido."

    @classmethod
    def save_to_json(cls, filename="json/matches.json"):
        directory = os.path.dirname(filename)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(filename, "w") as file:
            json.dump([match.to_dict() for match in cls.competitions_list], file, indent=4)

    @classmethod
    def load_from_json(cls, filename="json/matches.json"):
        directory = os.path.dirname(filename)
        if directory:
            os.makedirs(directory, exist_ok=True)
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                cls.competitions_list = []
                for item in data:
                    match = MatchScheduler(
                        item["type"],
                        item["location"],
                        item["date"],
                        item["time"],
                        item["opponent"],
                        item.get("status", False)
                    )
                    cls.competitions_list.append(match)
        except FileNotFoundError:
            print(f"Arquivo {filename} não encontrado. Iniciando com lista vazia.")

    @classmethod
    def get_matches_by_opponent(cls, opponent_name):
        return [match for match in cls.competitions_list if match.get_opponent().lower() == opponent_name.lower()]

    def to_dict(self):
        event_dict = super().to_dict()
        event_dict["opponent"] = self.__opponent
        event_dict["status"] = self.__status
        return event_dict

    def __str__(self):
        status_text = "Concluída" if self.__status else "Não concluída"
        return super().__str__() + (
            f"\n Adversário: {self.__opponent}\n"
            f" Status: {status_text}"
        )

class MatchBuilder:
    def __init__(self):
        self._type = None
        self._location = None
        self._date = None
        self._time = None
        self._opponent = None
        self._status = False

    def set_type(self, type):
        self._type = type
        return self

    def set_location(self, location):
        self._location = location
        return self

    def set_date(self, date):
        self._date = date
        return self

    def set_time(self, time):
        self._time = time
        return self

    def set_opponent(self, opponent):
        self._opponent = opponent
        return self

    def set_status(self, status):
        self._status = status
        return self

    def build(self):
        if not all([self._type, self._location, self._date, self._time, self._opponent]):
            raise ValueError("Todos os campos obrigatórios devem ser preenchidos.")
        return MatchScheduler(
            self._type, self._location, self._date,
            self._time, self._opponent, self._status
        )
