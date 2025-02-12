from datetime import datetime

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

class Competition:
    def __init__(self, type, location, date, time, opponent):
        self.type = type.capitalize()
        self.location = location
        self.date = date
        self.time = time
        self.opponent = opponent

    def schedule_match(self):
        
        return f"Partida agendada: {self.type} contra {self.opponent} em {self.location}, no dia {self.date} às {self.time}."

    def check_status(self):
        
        try:
            datetime_evento = datetime.strptime(f"{self.date} {self.time}", "%d/%m/%Y %H:%M")
            if datetime_evento < datetime.now():
                return "O evento já ocorreu."
            return "O evento ainda não ocorreu."
        except ValueError:
            return "Formato de data ou hora inválido."

    def __str__(self):
        return (
            f"Competição: {self.type}\n"
            f"Local: {self.location}\n"
            f"Data: {self.date}  Horário: {self.time}\n"
            f"⚔️ Adversário: {self.opponent}"
        )

class Inventory:
    def __init__(self, id, type_object, sector, team, registration_year, last_use_date):
        self.id = id
        self.type_object = type_object
        self.sector = sector
        self.team = team
        self.registration_year = registration_year
        self.last_use_date = last_use_date
        self.available = True  

    def register_object(self):
        
        return f"Objeto '{self.type_object}' registrado no setor {self.sector} pela equipe {self.team}."

    def availability_request(self):
       
        return "Disponível" if self.available else "Indisponível"

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f" Objeto: {self.type_object}\n"
            f" Setor: {self.sector} |  Equipe: {self.team}\n"
            f" Ano de Registro: {self.registration_year} |  Último uso: {self.last_use_date}\n"
            f" Status: {self.availability_request()}"
        )

class Training:
    def __init__(self, type, date, time, duration, location, professional, status=False):
        self.type = type.capitalize()
        self.date = date
        self.time = time
        self.duration = duration
        self.location = location
        self.professional = professional
        self.status = status  

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
        
def main():
    while True:
        print("\nEscolha uma opção para testar:")
        print("1 - Criar uma Competição")
        print("2 - Criar um Objeto de Inventário")
        print("3 - Criar um Treino")
        print("4 - Criar uma Equipe")
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
            print(match.check_status())
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
            print(f"Status de disponibilidade: {item.availability_request()}")

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
            finalizar = input("Deseja marcar o treino como concluído? (s/n): ")
            if finalizar.lower() == 's':
                training.mark_completed()
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

        elif escolha == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()