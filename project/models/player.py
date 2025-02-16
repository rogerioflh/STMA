import json
from datetime import datetime
# Gerenciar informações sobre atletas da equipe

class Player:
    players_list = []  

    def __init__(self, name, position, stats=None):
        self.name = name
        self.position = position
        self.stats = stats if stats else {}
        Player.players_list.append(self)
        Player.save_to_json() 

    def update_stats(self, new_stats):
        self.stats.update(new_stats)
        Player.save_to_json()  

    @classmethod
    def save_to_json(cls, filename="players.json"):
        """Salva a lista de jogadores em um arquivo JSON."""
        with open(filename, "w") as file:
            json.dump([player.to_dict() for player in cls.players_list], file, indent=4)

    @classmethod
    def load_from_json(cls, filename="players.json"):
        """Carrega a lista de jogadores de um arquivo JSON."""
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                cls.players_list = [Player(player["name"], player["position"]) for player in data]
        except FileNotFoundError:
            print(f"Arquivo {filename} não encontrado. Iniciando com lista vazia.")

    def to_dict(self):
        """Converte o objeto Player em um dicionário."""
        return {
            "name": self.name,
            "position": self.position,
          #  "stats": self.stats
        }

    def carregar_dados():
      """Carrega todos os dados dos arquivos JSON."""
      Player.load_from_json()

    def salvar_dados():
         """Salva todos os dados nos arquivos JSON."""
         Player.save_to_json()
         
    def __str__(self):
        return (
            f" Jogador: {self.name}\n"
            f" Posição: {self.position}\n"
          #  f" Estatísticas: {self.stats}"
        )