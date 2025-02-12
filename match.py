class Competitions:
    def __init__(self, type, location, date, time, opponent):
        self.type = type
        self.location = location
        self.date = date
        self.time = time
        self.opponent = opponent

    def schedule_match(self):
        
    def check_status(self):
        from datetime import datetime
        data_evento = datetime.strptime(self.date, "%d/%m/%Y")
        if data_evento < datetime.now():
            return "Evento já ocorreu."
        return "Evento ainda não ocorreu."

    def __str__(self):
        return f"Tipo: {self.type.capitalize()}, Local: {self.location}\nData: {self.date}, Horário: {self.time}, Adversário: {self.opponent}\n"