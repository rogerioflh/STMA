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

    def mark_completed(self):
        self.status = True  
        return f"Treinamento de {self.type} em {self.date} foi concluído."

    def __str__(self):
        status_text = "Concluído" if self.status else "Agendado"
        return (
            f" Treinamento: {self.type}\n"
            f" Local: {self.location}\n"
            f" Data: {self.date} | Horário: {self.time} ({self.duration} min)\n"
            f" Profissional: {self.professional}\n"
            f" Status: {status_text}"
        )