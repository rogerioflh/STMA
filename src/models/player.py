import json
import os

def ensure_dir_exists(filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)

class Player:
    players_list = []

    def __init__(self, name, age, height, weight, position):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.position = position
        Player.players_list.append(self)
        Player.save_to_json()

    @classmethod
    def save_to_json(cls, filename="json/players.json"):
        ensure_dir_exists(filename)
        with open(filename, "w") as file:
            json.dump([player.to_dict() for player in cls.players_list], file, indent=4)

    @classmethod
    def load_from_json(cls, filename="json/players.json"):
        ensure_dir_exists(filename)
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                cls.players_list = []
                for player in data:
                    builder = PlayerBuilder()\
                        .set_name(player.get("name", "Desconhecido"))\
                        .set_age(player.get("age", 0))\
                        .set_height(player.get("height", 0.0))\
                        .set_weight(player.get("weight", 0.0))\
                        .set_position(player.get("position", "Desconhecida"))

                    builder.build()
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
    
class PlayerBuilder:
    def __init__(self):
        self._name = None
        self._age = None
        self._height = None
        self._weight = None
        self._position = None

    def set_name(self, name):
        self._name = name
        return self

    def set_age(self, age):
        self._age = age
        return self

    def set_height(self, height):
        self._height = height
        return self

    def set_weight(self, weight):
        self._weight = weight
        return self

    def set_position(self, position):
        self._position = position
        return self

    def build(self):
        return Player(
            self._name or "Desconhecido",
            self._age or 0,
            self._height or 0.0,
            self._weight or 0.0,
            self._position or "Desconhecida"
        )
