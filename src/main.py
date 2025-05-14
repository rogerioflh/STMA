import json
import atexit
import json
import atexit
from datetime import datetime
from src.utils.financial import Financial
from src.models.healthMonitor import HealthMonitor
from src.services.inventory import Inventory
from src.services.matchScheduler import MatchScheduler
from src.services.mediaManager import MediaManager
from src.models.player import Player
from src.models.performance import Performance
from src.services.recruitmentPlayer import RecruitmentManager
from src.services.trainingmanager import TrainingManager
from src.utils.event import Event
from src.user import GerenciadorUsuarios


def load_data():
    try:
        Player.load_from_json()
        MatchScheduler.load_from_json()
        Financial.load_from_json()
        Inventory.load_from_json()
        TrainingManager.load_from_json()
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")

def save_data():
    try:
        Player.save_to_json()
        MatchScheduler.save_to_json()
        Inventory.save_to_json()
        TrainingManager.save_to_json()
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")

atexit.register(save_data)


def menu_principal(usuario):
    while True:
        print("\n MENU PRINCIPAL")
        print("Escolha como deseja prosseguir:\n")
        
        opcoes = {}
        
        if usuario.role in ["técnico", "gerente"]:
            opcoes["1"] = "Gerenciamento de Jogadores"
        if usuario.role == "secretário financeiro":
            opcoes["2"] = "Gerenciamento Financeiro"
        if usuario.role in ["técnico", "gerente"]:
            opcoes["3"] = "Gerenciamento de Compromissos"
        if usuario.role in ["atleta", "gerente"]:
            opcoes["4"] = "Gerenciamento de Equipamentos"
        if usuario.role in ["técnico", "gerente"]:
            opcoes["5"] = "Recrutamento de Jogadores"
        if usuario.role == "gerente":
            opcoes["6"] = "Gerenciamento de Mídia"

        opcoes["0"] = "Sair"

        for key, value in opcoes.items():
            print(f"{key}. {value}")

        escolha = input("Escolha uma opção: ")

        if escolha == "1" and usuario.role in ["técnico", "gerente"]:
            menu_jogadores()
        elif escolha == "2" and usuario.role == "secretário financeiro":
            menu_financeiro()
        elif escolha == "3" and usuario.role in ["técnico", "gerente"]:
            menu_eventos()
        elif escolha == "4" and usuario.role in ["atleta", "gerente"]:
            menu_equipamentos()
        elif escolha == "5" and usuario.role in ["técnico", "gerente"]:
            menu_recrutamento()
        elif escolha == "6" and usuario.role == "gerente":
            menu_midia()
        elif escolha == "0":
            
            break
        else:
            print(" Opção inválida ou sem permissão! Tente novamente.")


if __name__ == "__main__":
    load_data()
    gerenciador_usuarios = GerenciadorUsuarios()
    usuario_autenticado = gerenciador_usuarios.autenticar_usuario()
    menu_principal(usuario_autenticado)
