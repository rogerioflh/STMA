import json
class Player:
    players_list = []  # Lista para armazenar todos os jogadores

    def __init__(self, name, position, passes, goals, assists, meters):
        self.name = name
        self.position = position
        self.passes = passes
        self.goals = goals
        self.assists = assists
        self.meters = meters
        self.performance = {}  # Dicionário para armazenar métricas de desempenho
        Player.players_list.append(self)
        Player.save_to_json()

    def update_performance(self, new_metrics):
        self.performance.update(new_metrics)
        Player.save_to_json()

    def get_performance(self):
        return self.performance

    @classmethod
    def save_to_json(cls, filename="players.json"):
        with open(filename, "w") as file:
            json.dump([player.to_dict() for player in cls.players_list], file, indent=4)

    @classmethod
    def load_from_json(cls, filename="players.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                cls.players_list = [
                    Player(
                        player["name"],
                        player["position"],
                        player["passes"],
                        player["goals"],
                        player["assists"],
                        player["meters"]
                    ) for player in data
                ]
                # Carrega o desempenho de cada jogador
                for player in cls.players_list:
                    if "performance" in player.to_dict():
                        player.performance = player.to_dict()["performance"]
        except FileNotFoundError:
            print(f"Arquivo {filename} não encontrado. Iniciando com lista vazia.")

    def to_dict(self):
        return {
            "name": self.name,
            "position": self.position,
            "passes": self.passes,
            "goals": self.goals,
            "assists": self.assists,
            "meters": self.meters,
            "performance": self.performance  # Inclui o desempenho no dicionário
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
            f" Posição: {self.position}\n"
            f" Passes: {self.passes}\n"
            f" Gols: {self.goals}\n"
            f" Assistências: {self.assists}\n"
            f" Metros percorridos: {self.meters}\n"
            f" Desempenho: {self.performance}\n"
        )

# Classe derivada: Performance (herda de Player)
class Performance(Player):
    performance_data = {}  # Dicionário para armazenar o desempenho dos jogadores

    def __init__(self, name, position, passes, goals, assists, meters, performance_metrics):
        # Chama o construtor da classe base (Player)
        super().__init__(name, position, passes, goals, assists, meters)
        self.performance_metrics = performance_metrics
        Performance.performance_data[self.name] = self
        Performance.save_to_json()

    def update_performance(self, new_metrics):
        self.performance_metrics.update(new_metrics)
        Performance.save_to_json()

    def get_performance(self):
        return self.performance_metrics

    def to_dict(self):
        # Reutiliza o método to_dict da classe base e adiciona as métricas de desempenho
        player_dict = super().to_dict()
        player_dict["performance_metrics"] = self.performance_metrics
        return player_dict

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
                    performance_record = Performance(
                        item["name"],
                        item["position"],
                        item["passes"],
                        item["goals"],
                        item["assists"],
                        item["meters"],
                        item["performance_metrics"]
                    )
                    cls.performance_data[item["name"]] = performance_record
        except FileNotFoundError:
            print(f"Arquivo {filename} não encontrado. Iniciando com lista vazia.")
        except json.JSONDecodeError:
            print(f"Erro ao carregar {filename}. O arquivo pode estar corrompido.")

    def __str__(self):
        # Reutiliza o método __str__ da classe base e adiciona as métricas de desempenho
        player_info = super().__str__()
        return (
            f"{player_info}"
            f" Desempenho de {self.name}:\n"
            f" Métricas: {self.performance_metrics}\n"
        )