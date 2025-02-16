from datetime import datetime
import json

# Agendar participação em partidas ou torneios

class MatchScheduler:
    competitions_list = []  
    def __init__(self, type, location, date, time, opponent):
        self.type = type.capitalize()
        self.location = location
        self.date = date
        self.time = time
        self.opponent = opponent
        MatchScheduler.competitions_list.append(self)
        MatchScheduler.save_to_json() 

    def schedule_match(self):
        return f"Partida agendada: {self.type} contra {self.opponent} em {self.location}, no dia {self.date} às {self.time}."

    def check_status(self):
        try:
            datetime_evento = datetime.strptime(f"{self.date} {self.time}", "%d/%m/%Y %H:%M")
            return "O evento já ocorreu." if datetime_evento < datetime.now() else "O evento ainda não ocorreu."
        except ValueError:
            return "Formato de data ou hora inválido."

    @classmethod
    def save_to_json(cls, filename="matches.json"):

        with open(filename, "w") as file:
            json.dump([match.to_dict() for match in cls.competitions_list], file, indent=4)

    @classmethod
    def load_from_json(cls, filename="matches.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                cls.competitions_list = [
                    MatchScheduler(match["type"], match["location"], match["date"], match["time"], match["opponent"])
                    for match in data
                ]
        except FileNotFoundError:
            print(f"Arquivo {filename} não encontrado. Iniciando com lista vazia.")

    def to_dict(self):
        return {
            "type": self.type,
            "location": self.location,
            "date": self.date,
            "time": self.time,
            "opponent": self.opponent
        }

    def __str__(self):
        return (
            f" Competição: {self.type}\n"
            f" Local: {self.location}\n"
            f" Data: {self.date}  Horário: {self.time}\n"
            f" Adversário: {self.opponent}"
        )