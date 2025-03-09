import json
from datetime import datetime
# Classe base para eventos
class Event:
    def __init__(self, type, date, time, location):
        self.type = type.capitalize()
        self.date = date
        self.time = time
        self.location = location

    def check_status(self):
        try:
            datetime_evento = datetime.strptime(f"{self.date} {self.time}", "%d/%m/%Y %H:%M")
            return "O evento já ocorreu." if datetime_evento < datetime.now() else "O evento ainda não ocorreu."
        except ValueError:
            return "Formato de data ou hora inválido."

    def to_dict(self):
        return {
            "type": self.type,
            "date": self.date,
            "time": self.time,
            "location": self.location
        }

    def __str__(self):
        return (
            f" Tipo: {self.type}\n"
            f" Local: {self.location}\n"
            f" Data: {self.date} | Horário: {self.time}"
        )