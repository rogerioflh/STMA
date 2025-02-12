from datetime import datetime
import uuid

class Competition:
    competitions_list = [] 

    def __init__(self, type, location, date, time, opponent):
        self.type = type.capitalize()
        self.location = location
        self.date = date
        self.time = time
        self.opponent = opponent
        Competition.competitions_list.append(self)  

    def schedule_match(self):
        return f"Partida agendada: {self.type} contra {self.opponent} em {self.location}, no dia {self.date} às {self.time}."

    def check_status(self):
        try:
            datetime_evento = datetime.strptime(f"{self.date} {self.time}", "%d/%m/%Y %H:%M")
            return "O evento já ocorreu." if datetime_evento < datetime.now() else "O evento ainda não ocorreu."
        except ValueError:
            return "Formato de data ou hora inválido."

    def __str__(self):
        return (
            f" Competição: {self.type}\n"
            f" Local: {self.location}\n"
            f" Data: {self.date}  Horário: {self.time}\n"
            f" Adversário: {self.opponent}"
        )

class Inventory:
    inventory_list = {} 

    def __init__(self, type_object, sector, team, registration_year, last_use_date):
        self.id = str(uuid.uuid4())[:8]  
        self.type_object = type_object
        self.sector = sector
        self.team = team
        self.registration_year = registration_year
        self.last_use_date = last_use_date
        self.available = True 
        Inventory.inventory_list[self.id] = self  

    def register_object(self):
        return f"Objeto '{self.type_object}' registrado com ID {self.id}."

    def availability_request(self):
        return "Disponível" if self.available else "Indisponível"

    def __str__(self):
        return (
            f" ID: {self.id} | Objeto: {self.type_object}\n"
            f" Setor: {self.sector} |  Equipe: {self.team}\n"
            f" Ano de Registro: {self.registration_year} |  Último uso: {self.last_use_date}\n"
            f" Status: {self.availability_request()}"
        )

class Training:
    training_list = []  

    def __init__(self, type, date, time, duration, location, professional, status=False):
        self.type = type.capitalize()
        self.date = date
        self.time = time
        self.duration = duration
        self.location = location
        self.professional = professional
        self.status = status 
        Training.training_list.append(self)  

    def mark_completed(self):
        self.status = True
        return f"Treino de {self.type} em {self.date} às {self.time} foi concluído."

    def schedule(self):
        return f"Treino de {self.type} agendado para {self.date} às {self.time} com {self.professional}."

    def __str__(self):
        status_text = " Realizado" if self.status else " Agendado"
        return (
            f" Treino: {self.type}\n"
            f" Local: {self.location}\n"
            f" Data: {self.date}  Horário: {self.time} ({self.duration} min)\n"
            f" Profissional: {self.professional}\n"
            f" Status: {status_text}"
        )

class Team:
    def __init__(self, name, cnpj, contact, address, responsible):
        self.name = name
        self.cnpj = cnpj
        self.contact = contact
        self.address = address
        self.responsible = responsible

    def get_info(self):
        return f"Equipe '{self.name}' registrada com CNPJ {self.cnpj}."

    def __str__(self):
        return (
            f" Equipe: {self.name}\n"
            f" CNPJ: {self.cnpj}\n"
            f" Contato: {self.contact}\n"
            f" Endereço: {self.address}\n"
            f" Responsável: {self.responsible}"
        )


def main():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Criar uma Competição")
        print("2 - Criar um Objeto de Inventário")
        print("3 - Criar um Treino")
        print("4 - Criar uma Equipe")
        print("5 - Consultar disponibilidade de um item (ID)")
        print("6 - Listar todas as Competições")
        print("7 - Listar todos os Treinos")
        print("0 - Sair")

        escolha = input("Digite a opção: ")

        if escolha == "1":
            type = input("Tipo da competição: ")
            location = input("Local: ")
            date = input("Data (DD/MM/AAAA): ")
            time = input("Horário (HH:MM): ")
            opponent = input("Adversário: ")
            match = Competition(type, location, date, time, opponent)
            print(match.schedule_match())
            print(match)

        elif escolha == "2":
            type_object = input("Tipo do objeto: ")
            sector = input("Setor: ")
            team = input("Equipe responsável: ")
            registration_year = input("Ano de registro: ")
            last_use_date = input("Última data de uso (DD/MM/AAAA): ")
            item = Inventory(type_object, sector, team, registration_year, last_use_date)
            print(item.register_object())
            print(item)

        elif escolha == "3":
            type = input("Tipo do treino: ")
            date = input("Data (DD/MM/AAAA): ")
            time = input("Horário (HH:MM): ")
            duration = int(input("Duração em minutos: "))
            location = input("Local: ")
            professional = input("Profissional responsável: ")
            training = Training(type, date, time, duration, location, professional)
            print(training.schedule())
            print(training)

        elif escolha == "4":
            name = input("Nome da equipe: ")
            cnpj = input("CNPJ: ")
            contact = input("Contato: ")
            address = input("Endereço: ")
            responsible = input("Responsável: ")
            team = Team(name, cnpj, contact, address, responsible)
            print(team.get_info())
            print(team)

        elif escolha == "5":
            id_item = input("Digite o ID do item: ")
            if id_item in Inventory.inventory_list:
                print(Inventory.inventory_list[id_item])
            else:
                print("ID não encontrado.")

        elif escolha == "6":
            for comp in Competition.competitions_list:
                print(comp)

        elif escolha == "7":
            for training in Training.training_list:
                print(training)

        elif escolha == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main() 