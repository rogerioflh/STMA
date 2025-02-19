import json
from datetime import datetime


# Gerenciar informações sobre atletas da equipe
class Player:
    players_list = []  

    def __init__(self, name, position, passes, goals, assists, meters, stats=None):
        self.name = name
        self.position = position
        self.passes = passes
        self.goals = goals
        self.assists = assists
        self.meters = meters
        self.stats = stats if stats else {}
        Player.players_list.append(self)
        Player.save_to_json() 



    def update_stats(self, new_stats):
        self.stats.update(new_stats)
        Player.save_to_json()  


    # Salva a lista de jogadores em um arquivo JSON. 
    @classmethod
    def save_to_json(cls, filename="players.json"):
        with open(filename, "w") as file:
            json.dump([player.to_dict() for player in cls.players_list], file, indent=4)


    # Carrega a lista de jogadores de um arquivo JSON.
    @classmethod
    def load_from_json(cls, filename="players.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                cls.players_list = [Player(player["name"], player["position"], player["passes"], player["goals"], player["assists"], player["meters"]) for player in data]
        except FileNotFoundError:
            print(f"Arquivo {filename} não encontrado. Iniciando com lista vazia.")


    # Carrega o dicionário com as variáveis
    def to_dict(self):
        return {
            "name": self.name,
            "position": self.position,
            "passes": self.passes,
            "goals": self.goals,
            "assists": self.assists,
            "meters": self.meters
        }
        
        
    # Carrega todos os dados dos arquivos JSON.
    def carregar_dados():
      Player.load_from_json()


    # Salva todos os dados nos arquivos JSON
    def salvar_dados():
         Player.save_to_json()
       
         
    def __str__(self):
        return (
            f" Jogador: {self.name}\n"
            f" Posição: {self.position}\n"
            f" Passes: {self.passes}\n"
            f" Gols: {self.goals}\n"
            f" Assistências: {self.assists}\n"
            f" Metros percorridos: {self.meters}\n"
        )