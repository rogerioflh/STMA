from abc import ABC, abstractmethod
import uuid
from datetime import datetime


class Event(ABC):
    def __init__(self, type, date, time, location):
        self._id = self._generate_id()
        self._type = type.capitalize()
        self._date = date
        self._time = time
        self._location = location

    @staticmethod
    def _generate_id():
        return str(uuid.uuid4())

    # Getters
    def get_id(self):
        return self._id

    def get_type(self):
        return self._type

    def get_date(self):
        return self._date

    def get_time(self):
        return self._time

    def get_location(self):
        return self._location

    # Setters
    def set_type(self, type):
        self._type = type.capitalize()

    def set_date(self, date):
        self._date = date

    def set_time(self, time):
        self._time = time

    def set_location(self, location):
        self._location = location

    def update_event_details(self, type=None, date=None, time=None, location=None):
        if type is not None:
            self.set_type(type)
        if date is not None:
            self.set_date(date)
        if time is not None:
            self.set_time(time)
        if location is not None:
            self.set_location(location)

    def is_upcoming(self):
        """Verifica se o evento ainda não aconteceu."""
        try:
            event_datetime = datetime.strptime(f"{self._date} {self._time}", "%d/%m/%Y %H:%M")
            return event_datetime > datetime.now()
        except ValueError:
            return False  # Se data ou hora forem inválidas

    @abstractmethod
    def check_status(self):
        """Método abstrato que deve verificar o status do evento."""
        pass

    def to_dict(self):
        return {
            "id": self._id,
            "type": self._type,
            "date": self._date,
            "time": self._time,
            "location": self._location
        }

    def __str__(self):
        return (
            f"ID: {self._id}\n"
            f"Tipo: {self._type}\n"
            f"Data: {self._date}\n"
            f"Hora: {self._time}\n"
            f"Localização: {self._location}"
        )
