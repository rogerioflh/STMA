import json
import atexit
from datetime import datetime
from models.financial import Financial
from models.healthMonitor import HealthMonitor
from models.inventory import Inventory
from models.matchScheduler import MatchScheduler
from models.mediaManager import MediaManager
from models.performanceTracker import Performance
from models.player import Player
from models.recruitmentPlayer import RecruitmentManager
from models.trainingmanager import TrainingManager

# carregamento de dados do json
def load_data():
    Player.load_from_json()
    MatchScheduler.load_from_json()
    Financial.load_from_json()
    Inventory.load_from_json()
    TrainingManager.load_from_json()
    
def menu_principal():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Gerenciamento de Jogadores")
        print("2. Gerenciamento Financeiro")
        print("3. Gerenciamento de Treinamentos")
        print("4. Monitoramento de Saúde")
        print("5. Gerenciamento de Equipamentos")
        print("6. Recrutamento de Jogadores")
        print("7. Gerenciamento de Mídia")
        print("8. Gerenciamneto de Partidas")
        print("9. Gerenciamento de Desempenho")
        print("0. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            menu_jogadores()
            
        elif escolha == "2":
            menu_financeiro()
            
        elif escolha == "3":
            menu_treinamentos()
            
        elif escolha == "4":
            menu_saude()
            
        elif escolha == "5":
            menu_equipamentos()
            
        elif escolha == "6":
            menu_recrutamento()
            
        elif escolha == "7":
            menu_midia()
            
        elif escolha == "8":
            menu_partidas()
            
        elif escolha == "9":
            menu_desempenho()
            
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_jogadores():
    while True:
        print("\n--- Gerenciamento de Jogadores ---")
        print("1. Adicionar Jogador")
        print("2. Ver Jogadores")
        print("3. Atualizar Estatísticas")
        print("4. Voltar ao Menu Principal")
        
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do jogador: ")
            posicao = input("Posição do jogador: ")
            passes = input("Passes certos: ")
            gols = input("Gols: ")
            assistencias = input("Número de assistencias: ")
            metros = input("Metros percorridos pelo atleta: ")
            Player(nome, posicao, passes, gols, assistencias, metros)
            print("Jogador adicionado com sucesso!")
            
        elif escolha == "2":
            for jogador in Player.players_list:
                print(jogador)
                
        elif escolha == "3":
            nome = input("Nome do jogador: ")
            
            for jogador in Player.players_list:
                if jogador.name == nome:
                    print("Selecione qual estatística deseja atualizar: ")
                    print("1. Passes")
                    print("2. Gols")
                    print("3. Assistências")
                    print("4. Metros percorridos")
                    escolha = input("Escolha uma opção: ")
                    
                    if escolha == "1":
                        passes = input("Passes certos: ")
                        jogador.passes = passes
                        
                    elif escolha =="2":
                        gols = input("Gols: ")
                        jogador.goals = gols
                        
                    elif escolha =="3":
                        assistencias = input("Número de assistencias: ")
                        jogador.assists = assistencias
                        
                    elif escolha=="4":
                        metros = input("Metros percorridos pelo atleta: ")
                        jogador.meters = metros
                        
                break
                
            else:
                print("Jogador não encontrado.") 
                
        elif escolha == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_financeiro():
    financeiro = Financial()
    while True:
        print("\n--- Gerenciamento Financeiro ---")
        print("1. Ver Faturamento")
        print("2. Atualizar Gastos")
        print("3. Ver Resumo Financeiro")
        print("4. Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print(f"Faturamento Anual: R${financeiro.annual_revenue:.2f}")
            print(f"Faturamento Mensal: R${financeiro.monthly_revenue:.2f}")
        elif escolha == "2":
            categoria = input("Categoria (folha_pagamento, saude, alimentacao, manutencao, viagens): ")
            valor = float(input("Valor: "))
            financeiro.add_monthly_expense(categoria, valor)
            print("Gasto atualizado!")
        elif escolha == "3":
            print(financeiro)
        elif escolha == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_treinamentos():
    while True:
        print("\n--- Gerenciamento de Treinamentos ---")
        print("1. Agendar Treinamento")
        print("2. Ver Treinamentos")
        print("3. Marcar Treinamento como Concluído")
        print("4. Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            tipo = input("Tipo de treinamento: ")
            data = input("Data (dd/mm/aaaa): ")
            hora = input("Hora (hh:mm): ")
            duracao = int(input("Duração (minutos): "))
            local = input("Local: ")
            profissional = input("Profissional responsável: ")
            TrainingManager(tipo, data, hora, duracao, local, profissional)
            print("Treinamento agendado!")
        elif escolha == "2":
            for treinamento in TrainingManager.training_sessions:
                print(treinamento)
        elif escolha == "3":
            tipo = input("Tipo de treinamento: ")
            for treinamento in TrainingManager.training_sessions:
                if treinamento.type == tipo:
                    treinamento.mark_completed()
                    print("Treinamento marcado como concluído!")
                    break
            else:
                print("Treinamento não encontrado.")
        elif escolha == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_saude():
    while True:
        print("\n--- Monitoramento de Saúde ---")
        print("1. Registrar Lesão")
        print("2. Ver Status de Saúde")
        print("3. Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do jogador: ")
            for jogador in Player.players_list:
                if jogador.name == nome:
                    lesao = input("Relatório da lesão: ")
                    HealthMonitor(jogador, lesao)
                    print("Lesão registrada!")
                    break
            else:
                print("Jogador não encontrado.")
        elif escolha == "2":
            nome = input("Nome do jogador: ")
            for jogador in Player.players_list:
                if jogador.name == nome:
                    if jogador.name in HealthMonitor.health_records:
                        print(HealthMonitor.health_records[jogador.name])
                    else:
                        print("Nenhuma lesão registrada.")
                    break
            else:
                print("Jogador não encontrado.")
        elif escolha == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_equipamentos():
    while True:
        print("\n--- Gerenciamento de Equipamentos ---")
        print("1. Adicionar Equipamento")
        print("2. Ver Equipamentos")
        print("3. Alterar Disponibilidade")
        print("4. Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            tipo = input("Tipo do equipamento: ")
            setor = input("Setor: ")
            equipe = input("Equipe: ")
            ano = input("Ano de registro: ")
            ultimo_uso = input("Data do último uso (dd/mm/aaaa): ")
            Inventory(tipo, setor, equipe, ano, ultimo_uso)
            print("Equipamento adicionado!")
        elif escolha == "2":
            for equipamento in Inventory.inventory.values():
                print(equipamento)
        elif escolha == "3":
            id_equipamento = input("ID do equipamento: ")
            if id_equipamento in Inventory.inventory:
                Inventory.inventory[id_equipamento].toggle_availability()
                print("Disponibilidade alterada!")
            else:
                print("Equipamento não encontrado.")
        elif escolha == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_recrutamento():
    while True:
        print("\n--- Recrutamento de Jogadores ---")
        print("1. Adicionar Prospecto")
        print("2. Ver Prospectos")
        print("3. Avaliar Prospecto")
        print("4. Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do prospecto: ")
            posicao = input("Posição: ")
            idade = int(input("Idade: "))
            RecruitmentManager(nome, posicao, idade)
            print("Prospecto adicionado!")
        elif escolha == "2":
            for prospecto in RecruitmentManager.prospects_list:
                print(prospecto)
        elif escolha == "3":
            nome = input("Nome do atleta: ")
            for prospecto in RecruitmentManager.prospects_list:
                if prospecto.name == nome:
                    avaliacao = input("Avaliação: ")
                    prospecto.evaluate_prospect(avaliacao)
                    print("atleta avaliado!")
                    break
            else:
                print("atleta não encontrado.")
        elif escolha == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_midia():
    while True:
        print("\n--- Gerenciamento de Mídia ---")
        print("1. Adicionar Press Release")
        print("2. Ver Press Releases")
        print("3. Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            titulo = input("Título: ")
            conteudo = input("Conteúdo: ")
            data = input("Data (dd/mm/aaaa): ")
            MediaManager(titulo, conteudo, data)
            print("Press Release adicionado!")
        elif escolha == "2":
            for release in MediaManager.press_releases:
                print(release)
        elif escolha == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")
            
def menu_partidas():
    while True:
        print("\n--- Agendamento de Partidas ---")
        print("1. Agendar Partida")
        print("2. Ver Partidas Agendadas")
        print("3. Verificar Status da Partida")
        print("4. Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            tipo = input("Tipo da partida: ")
            local = input("Local: ")
            data = input("Data (dd/mm/aaaa): ")
            hora = input("Hora (hh:mm): ")
            adversario = input("Adversário: ")
            MatchScheduler(tipo, local, data, hora, adversario)
            print("Partida agendada!")
        elif escolha == "2":
            for partida in MatchScheduler.competitions_list:
                print(partida)
        elif escolha == "3":
            tipo = input("Tipo da partida: ")
            for partida in MatchScheduler.competitions_list:
                if partida.type == tipo:
                    print(partida.check_status())
                    break
            else:
                print("Partida não encontrada.")
        elif escolha == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")
            
def menu_desempenho():
    while True:
        print("\n--- Acompanhamento de Desempenho ---")
        print("1. Registrar Desempenho")
        print("2. Ver Desempenho de um Jogador")
        print("3. Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do jogador: ")
            for jogador in Player.players_list:
                if jogador.name == nome:
                    metricas = input("Métricas de desempenho: ")
                    metricas = json.loads(metricas) if metricas else {}
                    Performance(jogador, metricas)
                    print("Desempenho registrado!")
                    break
            else:
                print("Jogador não encontrado.")
        elif escolha == "2":
            nome = input("Nome do jogador: ")
            for jogador in Player.players_list:
                if jogador.name == nome:
                    if jogador.name in Performance.performance_data:
                        print(Performance.performance_data[jogador.name])
                    else:
                        print("Nenhum desempenho registrado.")
                    break
            else:
                print("Jogador não encontrado.")
        elif escolha == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")
            
import atexit

def save_data():
    Player.save_to_json()
    MatchScheduler.save_to_json()
    Financial.save_to_json()
    Inventory.save_to_json()
    TrainingManager.save_to_json()

atexit.register(save_data)

# Iniciar o menu principal
if __name__ == "__main__":
    load_data()
    save_data()
    menu_principal()
    