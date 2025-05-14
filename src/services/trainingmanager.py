import json
import os
from datetime import datetime
from src.utils.event import Event


def ensure_dir_exists(filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)


class TrainingSession(Event):
    def __init__(self, type, date, time, duration, location, professional, status=False):
        super().__init__(type, date, time, location)
        self._duration = duration
        self._professional = professional
        self._status = status

    def mark_completed(self):
        self._status = True

    def check_status(self):
        try:
            datetime_event = datetime.strptime(f"{self.get_date()} {self.get_time()}", "%d/%m/%Y %H:%M")
            if datetime_event < datetime.now():
                return "O treinamento já ocorreu."
            return "O treinamento ainda não ocorreu."
        except ValueError:
            return "Formato de data ou hora inválido."

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "duration": self._duration,
            "professional": self._professional,
            "status": self._status
        })
        return data

    def __str__(self):
        status_text = "Concluído" if self._status else "Agendado"
        return (
            super().__str__() +
            f"\nDuração: {self._duration} min\n"
            f"Profissional: {self._professional}\n"
            f"Status: {status_text}"
        )


class TrainingFacade:
    _sessions = []
    _loaded_ids = set()

    @classmethod
    def load(cls, filename="json/trainings.json"):
        ensure_dir_exists(filename)
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                cls._sessions.clear()
                cls._loaded_ids.clear()
                for item in data:
                    if item["id"] not in cls._loaded_ids:
                        session = TrainingSession(
                            item["type"],
                            item["date"],
                            item["time"],
                            item["duration"],
                            item["location"],
                            item["professional"],
                            item["status"]
                        )
                        cls._sessions.append(session)
                        cls._loaded_ids.add(item["id"])
        except FileNotFoundError:
            print(f"Arquivo {filename} não encontrado. Iniciando com lista vazia.")
        except json.JSONDecodeError:
            print(f"Erro ao ler o arquivo {filename}. Pode estar corrompido.")

    @classmethod
    def save(cls, filename="json/trainings.json"):
        ensure_dir_exists(filename)
        with open(filename, "w") as file:
            json.dump([s.to_dict() for s in cls._sessions], file, indent=4)

    @classmethod
    def add_session(cls, type, date, time, duration, location, professional):
        new_session = TrainingSession(type, date, time, duration, location, professional)
        if new_session.get_id() in cls._loaded_ids:
            print(f"Treinamento com ID {new_session.get_id()} já existe.")
            return None
        cls._sessions.append(new_session)
        cls._loaded_ids.add(new_session.get_id())
        cls.save()
        return new_session

    @classmethod
    def get_session_by_id(cls, session_id):
        return next((s for s in cls._sessions if s.get_id() == session_id), None)

    @classmethod
    def list_sessions(cls):
        for session in cls._sessions:
            print(session)

    @classmethod
    def mark_completed(cls, session_id):
        session = cls.get_session_by_id(session_id)
        if session:
            session.mark_completed()
            cls.save()
            return True
        return False

    @classmethod
    def remove_session(cls, session_id):
        session = cls.get_session_by_id(session_id)
        if session:
            cls._sessions.remove(session)
            cls._loaded_ids.discard(session_id)
            cls.save()
            return True
        return False
