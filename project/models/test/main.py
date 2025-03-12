import json
import atexit
from manager import menu_equipamentos, menu_eventos, menu_financeiro, menu_jogadores, menu_midia, menu_partidas, menu_principal, menu_recrutamento, menu_treinamentos
import json
import atexit
from datetime import datetime
from models.financial import Financial
from models.healthMonitor import HealthMonitor
from models.inventory import Inventory
from models.matchScheduler import MatchScheduler
from models.mediaManager import MediaManager
from models.player import Player
from models.performance import Performance
from models.recruitmentPlayer import RecruitmentManager
from models.trainingmanager import TrainingManager
from models.event import Event
from STMA.project.models.test.user import GerenciadorUsuarios


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
    usuario_autenticado = autenticar_usuario()
    menu_principal(usuario_autenticado)
