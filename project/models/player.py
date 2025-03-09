import json

import json

class Player:
    players_list = []  # Lista para armazenar todos os jogadores

    def __init__(self, name, age, height, weight, position):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.position = position
        Player.players_list.append(self)
        Player.save_to_json()

    @classmethod
    def save_to_json(cls, filename="players.json"):
        with open(filename, "w") as file:
            json.dump([player.to_dict() for player in cls.players_list], file, indent=4)

    @classmethod
    def load_from_json(cls, filename="players.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                cls.players_list = []
                for player in data:
                    # Verifica se todas as chaves necessárias estão presentes
                    name = player.get("name", "Desconhecido")
                    age = player.get("age", 0)  # Valor padrão se 'age' não existir
                    height = player.get("height", 0.0)  # Valor padrão se 'height' não existir
                    weight = player.get("weight", 0.0)  # Valor padrão se 'weight' não existir
                    position = player.get("position", "Desconhecida")  # Valor padrão se 'position' não existir

                    # Cria o jogador com os dados do JSON (ou valores padrão)
                    Player(name, age, height, weight, position)
        except FileNotFoundError:
            print(f"Arquivo {filename} não encontrado. Iniciando com lista vazia.")
        except json.JSONDecodeError:
            print(f"Erro ao carregar {filename}. O arquivo pode estar corrompido.")

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "height": self.height,
            "weight": self.weight,
            "position": self.position
        }

    @classmethod
    def carregar_dados(cls):
        cls.load_from_json()

    @classmethod
    def salvar_dados(cls):
        cls.save_to_json()

    def __str__(self):
        return (
            f" Jogador: {self.name}\n"
            f" Idade: {self.age}\n"
            f" Altura: {self.height}\n"
            f" Peso: {self.weight}\n"
            f" Posição: {self.position}\n"
        )