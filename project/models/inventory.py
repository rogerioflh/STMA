import uuid
class Inventory:
    inventory = {} 

    def __init__(self, type_object, sector, team, registration_year, last_use_date):
        
        self.id = str(uuid.uuid4())[:8]  # Gera um ID único para cada objeto cadastrado
        self.type_object = type_object
        self.sector = sector
        self.team = team
        self.registration_year = registration_year
        self.last_use_date = last_use_date
        self.available = True 
        Inventory.inventory[self.id] = self  

    def toggle_availability(self):
        self.available = not self.available  
        return f"Disponibilidade de {self.type_object} alterada para {self.available}."

    def __str__(self):
        return (
            f" ID: {self.id} | Objeto: {self.type_object}\n"
            f" Setor: {self.sector} | Equipe: {self.team}\n"
            f" Ano de Registro: {self.registration_year} | Último Uso: {self.last_use_date}\n"
            f" Status: {'Disponível' if self.available else 'Indisponível'}"
        )