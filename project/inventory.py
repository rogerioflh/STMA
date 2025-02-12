class Inventory:
    def __init__(self, type_object, sector, team, registration_year, lastUse_date):
        self.type_object = type_object
        self.sector = sector
        self.team = team
        self.registration_year = registration_year
        self.registration_use = lastUse_date

    def register_object(self):
    
    def availability_request (self):
        
    def __str__(self):
       return f"{self.type_object} - {self.sector} (Equipe responsavel: {self.team}, Ano de registro: {self.registration_year}, Data do ultimo uso: {self.registration_use})"
   
    
    