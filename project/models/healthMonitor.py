# Monitoramento de saúde dos atletas e lesões
class HealthMonitor:
    health_records = {} 

    def __init__(self, player, injury_report):
        self.player = player
        self.injury_report = injury_report
        HealthMonitor.health_records[player.name] = injury_report  

    def update_injury_report(self, new_report):
        self.injury_report = new_report  

    def get_health_status(self):
        return self.injury_report  

    def __str__(self):
        return (
            f" Status de Saúde de {self.player.name}:\n"
            f" Relatório: {self.injury_report}"
        )