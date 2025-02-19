import uuid
import json
#Gerenciar o inventário de objetos da equipe
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
        Inventory.save_to_json()


    def toggle_availability(self):
        self.available = not self.available 
        Inventory.save_to_json() 
        return f"Disponibilidade de {self.type_object} alterada para {self.available}."


    def to_dict(self):
        return {
            "id": self.id,
            "type_object": self.type_object,
            "sector": self.sector,
            "team": self.team,
            "registration_year": self.registration_year,
            "last_use_date": self.last_use_date,
            "available": self.available
        }


    @classmethod
    def save_to_json(cls, filename="inventory.json"):
        with open(filename, "w") as file:
            json.dump([item.to_dict() for item in cls.inventory.values()], file, indent=4)


    @classmethod
    def load_from_json(cls, filename="inventory.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                cls.inventory = {}  
                for item in data:
                    loaded_item = Inventory(
                        item["type_object"],
                        item["sector"],
                        item["team"],
                        item["registration_year"],
                        item["last_use_date"]
                    )
                    loaded_item.id = item["id"]  
                    loaded_item.available = item["available"]
                    cls.inventory[item["id"]] = loaded_item  
        except FileNotFoundError:
            print(f"Arquivo {filename} não encontrado. Iniciando com lista vazia.")


    def __str__(self):
        return (
            f" ID: {self.id} | Objeto: {self.type_object}\n"
            f" Setor: {self.sector} | Equipe: {self.team}\n"
            f" Ano de Registro: {self.registration_year} | Último Uso: {self.last_use_date}\n"
            f" Status: {'Disponível' if self.available else 'Indisponível'}"
        )