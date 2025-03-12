import json
from models.event import Event

class TrainingManager(Event):
    training_sessions = []
    loaded_ids = set()  # Conjunto para armazenar IDs únicos

    def __init__(self, type, date, time, duration, location, professional):
        super().__init__(type, date, time, location)
        self.duration = duration
        self.professional = professional
        self.status = False

        # Verifica se o ID já existe antes de adicionar
        if self.id not in TrainingManager.loaded_ids:
            TrainingManager.training_sessions.append(self)
            TrainingManager.loaded_ids.add(self.id)
            TrainingManager.save_to_json()
        else:
            print(f"Treino com ID {self.id} já existe e não será adicionado novamente.")

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
                cls.training_sessions = []  # Limpa a lista antes de carregar
                cls.loaded_ids = set()  # Limpa o conjunto de IDs
                for item in data:
                    if item["id"] not in cls.loaded_ids:  # Verifica se o ID já foi carregado
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
                        cls.loaded_ids.add(item["id"])
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
            f"\nDuração: {self.duration} min\n"
            f"Profissional: {self.professional}\n"
            f"Status: {status_text}"
        )