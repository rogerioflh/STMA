import json
# Gerenciar possíveis atletas a serem recrutados 
class RecruitmentManager:
    prospects_list = []  

    def __init__(self, name, position, age, stats=None):
        self.name = name
        self.position = position
        self.age = age
        self.stats = stats if stats else {}  
        RecruitmentManager.prospects_list.append(self) 
        RecruitmentManager.save_to_json() 

    def evaluate_prospect(self, evaluation):
        self.stats["evaluation"] = evaluation 
        RecruitmentManager.save_to_json()  

    def to_dict(self):
        return {
            "name": self.name,
            "position": self.position,
            "age": self.age,
            "stats": self.stats
        }
        
    @classmethod
    def save_to_json(cls, filename="recruitment_data.json"):
        with open(filename, "w") as file:
            json.dump([prospect.to_dict() for prospect in cls.prospects_list], file, indent=4)

    @classmethod
    def load_from_json(cls, filename="recruitment_data.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                cls.prospects_list = []  
                for item in data:
                    prospect = RecruitmentManager(item["name"], item["position"], item["age"], item["stats"])
                    cls.prospects_list.append(prospect)
        except FileNotFoundError:
            print(f"Arquivo {filename} não encontrado. Iniciando com lista vazia.")
        except json.JSONDecodeError:
            print(f"Erro ao carregar {filename}. O arquivo pode estar corrompido.")

    
    def __str__(self):
        return (
            f" Nome da possível contratação: {self.name}\n"
            f" Posição em que atua: {self.position}\n"
            f" Idade: {self.age}\n"
            f" Estatísticas: {self.stats}"
        )