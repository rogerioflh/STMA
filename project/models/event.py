from abc import ABC, abstractmethod
import json
import uuid
from datetime import datetime

# Classe base para eventos (abstrata)
class Event(ABC):
    def __init__(self, type, date, time, location):
        self.id = self.generate_id() 
        self.type = type.capitalize()
        self.date = date
        self.time = time
        self.location = location
    
    @staticmethod
    def generate_id():
        return str(uuid.uuid4()) 
        
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
        """Retorna um dicionário com os atributos comuns a todos os eventos."""
        return {
            "id": self.id,
            "type": self.type,
            "date": self.date,
            "time": self.time,
            "location": self.location
        }

    def __str__(self):
        """Retorna uma representação em string dos atributos comuns a todos os eventos."""
        return (
            f"ID: {self.id}\n"
            f"Tipo: {self.type}\n"
            f"Data: {self.date}\n"
            f"Hora: {self.time}\n"
            f"Localização: {self.location}"
        )