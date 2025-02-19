import json
# from player import Player
# Acompanhar desempenho dos atletas e da equipe

class Performance:
    performance_data = {} 

    def __init__(self, player, performance_metrics):
        self.player = player
        self.performance_metrics = performance_metrics
        Performance.performance_data[player.name] = performance_metrics  
        Performance.performance_data[self.player_name] = self 
        Performance.save_to_json() 

    def update_performance(self, new_metrics):
        self.performance_metrics.update(new_metrics)  
        Performance.save_to_json()

    def get_performance(self):
        return self.performance_metrics 
    def to_dict(self):
        return {
            "player_name": self.player_name,
            "performance_metrics": self.performance_metrics
        }

    @classmethod
    def save_to_json(cls, filename="performance_data.json"):
        with open(filename, "w") as file:
            json.dump([record.to_dict() for record in cls.performance_data.values()], file, indent=4)

    @classmethod
    def load_from_json(cls, filename="performance_data.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                cls.performance_data = {} 
                for item in data:
                    performance_record = Performance(item["player_name"], item["performance_metrics"])
                    cls.performance_data[item["player_name"]] = performance_record
        except FileNotFoundError:
            print(f"Arquivo {filename} não encontrado. Iniciando com lista vazia.")
        except json.JSONDecodeError:
            print(f"Erro ao carregar {filename}. O arquivo pode estar corrompido.")



    def __str__(self):
        return (
            f" Desempenho de {self.player.name}:\n"
            f" Métricas: {self.performance_metrics}"
        )