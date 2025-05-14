import json
from abc import ABC, abstractmethod
from src.models.player import Player

class Performance:
    performance_data = {}

    def __init__(self, player, passes, goals, assists, defenses, meters):
        self.player = player
        self.passes = passes
        self.goals = goals
        self.assists = assists
        self.defenses = defenses
        self.meters = meters
        Performance.performance_data[player.name] = self

    def update_info(self, passes=None, goals=None, assists=None, defenses=None, meters=None):
        if passes is not None:
            self.passes = passes
        if goals is not None:
            self.goals = goals
        if assists is not None:
            self.assists = assists
        if defenses is not None:
            self.defenses = defenses
        if meters is not None:
            self.meters = meters
        Performance.save_to_json()

    def to_dict(self):
        return {
            "player_name": self.player.name,
            "passes": self.passes,
            "goals": self.goals,
            "assists": self.assists,
            "defenses": self.defenses,
            "meters": self.meters
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
                    player = next((p for p in Player.players_list if p.name == item["player_name"]), None)
                    if player:
                        performance_record = Performance(
                            player,
                            item["passes"],
                            item["goals"],
                            item["assists"],
                            item["defenses"],
                            item["meters"]
                        )
                        cls.performance_data[item["player_name"]] = performance_record
        except FileNotFoundError:
            print(f"Arquivo {filename} não encontrado. Iniciando com lista vazia.")

    def __str__(self):
        return (
            f"Desempenho de {self.player.name}:\n"
            f"Passes: {self.passes}\n"
            f"Gols: {self.goals}\n"
            f"Assistências: {self.assists}\n"
            f"Defesas: {self.defenses}\n"
            f"Metros percorridos: {self.meters}\n"
        )


# ===== Padrão Decorator: estrutura implementada diretamente abaixo =====

class PerformanceDecorator(ABC):
    def __init__(self, performance: Performance):
        self._performance = performance

    @abstractmethod
    def describe(self):
        pass


class WeightedPerformance(PerformanceDecorator):
    def describe(self):
        weights = {
            "passes": 0.5,
            "goals": 5,
            "assists": 3,
            "defenses": 4,
            "meters": 0.001
        }

        score = (
            self._performance.passes * weights["passes"] +
            self._performance.goals * weights["goals"] +
            self._performance.assists * weights["assists"] +
            self._performance.defenses * weights["defenses"] +
            self._performance.meters * weights["meters"]
        )

        return f"Pontuação ponderada de {self._performance.player.name}: {score:.2f}"


class FormattedReport(PerformanceDecorator):
    def describe(self):
        return (
            f"[Relatório de Desempenho]\n"
            f"Jogador: {self._performance.player.name}\n"
            f"Passes: {self._performance.passes} | "
            f"Gols: {self._performance.goals} | "
            f"Assistências: {self._performance.assists} | "
            f"Defesas: {self._performance.defenses} | "
            f"Distância percorrida: {self._performance.meters}m"
        )
