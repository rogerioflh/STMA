# Acompanhar desempenho dos atletas e da equipe
class Performance:
    performance_data = {}  

    def __init__(self, player, performance_metrics):
        self.player = player
        self.performance_metrics = performance_metrics
        Performance.performance_data[player.name] = performance_metrics  

    def update_performance(self, new_metrics):
        self.performance_metrics.update(new_metrics)  

    def get_performance(self):
        return self.performance_metrics 

    def __str__(self):
        return (
            f" Desempenho de {self.player.name}:\n"
            f" Métricas: {self.performance_metrics}"
        )