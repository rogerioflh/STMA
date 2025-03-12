from datetime import datetime
import json
from models.event import Event

# Agendar participação em partidas ou torneios
# Classe para agendar partidas ou torneios
class MatchScheduler(Event):
    competitions_list = []

    def __init__(self, type, location, date, time, opponent):
        super().__init__(type, date, time, location)
        self.opponent = opponent
        self.status = False  
        MatchScheduler.competitions_list.append(self)
        MatchScheduler.save_to_json()

    def schedule_match(self):
        return f"Partida agendada: {self.type} contra {self.opponent} em {self.location}, no dia {self.date} às {self.time}."

    def mark_as_completed(self):
        self.status = True
        MatchScheduler.save_to_json()
        return f"Partida {self.type} contra {self.opponent} marcada como concluída."

    def mark_as_not_completed(self):
        self.status = False
        MatchScheduler.save_to_json()
        return f"Partida {self.type} contra {self.opponent} marcada como não concluída."

    @classmethod
    def save_to_json(cls, filename="matches.json"):
        with open(filename, "w") as file:
            json.dump([match.to_dict() for match in cls.competitions_list], file, indent=4)

    @classmethod
    def load_from_json(cls, filename="matches.json"):
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
                        item["opponent"]
                    )
                    match.status = item.get("status", False)  # Carrega o status, se existir
                    cls.competitions_list.append(match)
        except FileNotFoundError:
            print(f"Arquivo {filename} não encontrado. Iniciando com lista vazia.")

    def to_dict(self):
        event_dict = super().to_dict()
        event_dict["opponent"] = self.opponent
        event_dict["status"] = self.status
        return event_dict

    def __str__(self):
        status_text = "Concluída" if self.status else "Não concluída"
        return super().__str__() + (
            f"\n Adversário: {self.opponent}\n"
            f" Status: {status_text}"
        )