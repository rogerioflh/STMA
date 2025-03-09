import json
from models.event import Event
# Agendar e consultar treinos da equipe

# Classe para gerenciar treinamentos
class TrainingManager(Event):
    training_sessions = []

    def __init__(self, type, date, time, duration, location, professional):
        super().__init__(type, date, time, location)
        self.duration = duration
        self.professional = professional
        self.status = False
        TrainingManager.training_sessions.append(self)
        TrainingManager.save_to_json()

    def mark_completed(self):
        self.status = True
        TrainingManager.save_to_json()
        return f"Treinamento de {self.type} em {self.date} foi concluído."

    @classmethod
    def save_to_json(cls, filename="trainings.json"):
        with open(filename, "w") as file:
            json.dump([training.to_dict() for training in cls.training_sessions], file, indent=4)

    @classmethod
    def load_from_json(cls, filename="trainings.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                cls.training_sessions = []
                for item in data:
                    training = TrainingManager(
                        item["type"],
                        item["date"],
                        item["time"],
                        item["duration"],
                        item["location"],
                        item["professional"]
                    )
                    training.status = item["status"]
                    cls.training_sessions.append(training)
        except FileNotFoundError:
            print(f"Arquivo {filename} não encontrado. Iniciando com lista vazia.")

    def to_dict(self):
        event_dict = super().to_dict()
        event_dict.update({
            "duration": self.duration,
            "professional": self.professional,
            "status": self.status
        })
        return event_dict

    def __str__(self):
        status_text = "Concluído" if self.status else "Agendado"
        return super().__str__() + (
            f"\n Duração: {self.duration} min\n"
            f" Profissional: {self.professional}\n"
            f" Status: {status_text}"
        )