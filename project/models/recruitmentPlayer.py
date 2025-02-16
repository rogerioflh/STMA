# Gerenciar possíveis recrutamento de atletas
class RecruitmentManager:
    prospects_list = []  # Li

    def __init__(self, name, position, age, stats=None):
        self.name = name
        self.position = position
        self.age = age
        self.stats = stats if stats else {}  
        RecruitmentManager.prospects_list.append(self) 

    def evaluate_prospect(self, evaluation):
        self.stats["evaluation"] = evaluation  

    def __str__(self):
        return (
            f" Prospecto: {self.name}\n"
            f" Posição: {self.position}\n"
            f" Idade: {self.age}\n"
            f" Estatísticas: {self.stats}"
        )