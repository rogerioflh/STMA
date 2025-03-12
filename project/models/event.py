import json
import uuid
from datetime import datetime
# Classe base para eventos
class Event:
    def __init__(self, type, date, time, location):
        self.id = self.generate_id()  # Gera um ID único para cada evento
        self.type = type.capitalize()
        self.date = date
        self.time = time
        self.location = location
    
    @staticmethod
    def generate_id():
        return str(uuid.uuid4())  # Gera um UUID versão 4 como string
        
    def update_event_details(self, type=None, date=None, time=None, location=None):
        if type:
            self.type = type.capitalize()
        if date:
            self.date = date
        if time:
            self.time = time
        if location:
            self.location = location

    def check_status(self):
        try:
            datetime_evento = datetime.strptime(f"{self.date} {self.time}", "%d/%m/%Y %H:%M")
            return "O evento já ocorreu." if datetime_evento < datetime.now() else "O evento ainda não ocorreu."
        except ValueError:
            return "Formato de data ou hora inválido."
        
    

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "date": self.date,
            "time": self.time,
            "location": self.location
        }

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f" Tipo: {self.type}\n"
            f" Local: {self.location}\n"
            f" Data: {self.date} | Horário: {self.time}"
        )