import json
# Agendar e consultar treinos da equipe
class TrainingManager:
    training_sessions = []  

    def __init__(self, type, date, time, duration, location, professional):
        self.type = type
        self.date = date
        self.time = time
        self.duration = duration
        self.location = location
        self.professional = professional
        self.status = False  
        TrainingManager.training_sessions.append(self)  
        TrainingManager.save_to_json()

    def mark_completed(self):
        self.status = True  
        TrainingManager.save_to_json()
        return f"Treinamento de {self.type} em {self.date} foi concluído."

    def to_dict(self):
        return {
            "type": self.type,
            "date": self.date,
            "time": self.time,
            "duration": self.duration,
            "location": self.location,
            "professional": self.professional,
            "status": self.status
        }

    @classmethod
    def save_to_json(cls, filename="trainings.json"):
        with open(filename, "w") as file:
            json.dump([training.to_dict() for training in cls.training_sessions], file, indent=4)
   
    @classmethod
    def load_from_json(cls, filename="trainings.json"):
        """Carrega os treinos do arquivo JSON."""
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
    def __str__(self):
        status_text = "Concluído" if self.status else "Agendado"
        return (
            f" Treinamento: {self.type}\n"
            f" Local: {self.location}\n"
            f" Data: {self.date} | Horário: {self.time} ({self.duration} min)\n"
            f" Profissional: {self.professional}\n"
            f" Status: {status_text}"
        )