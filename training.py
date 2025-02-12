class Treino:
    def __init__(self, type, date, time, duration, location, professional, status=False):
        self.type = type
        self.date = date
        self.time = time
        self.duration = duration
        self.location = location
        self.professional = professional
        self.status = status

    def markCompleted(self):
        
        
    def schedule(self):

    def __str__(self):
        status = "Realizado" if self.realizado else "Agendado"
        return f"Tipo: {self.type}, Data: {self.date}, Horário: {self.time}, Duração: {self.duration} min\nLocal: {self.location}, Profissional: {self.professional}, Status: {status}\n"