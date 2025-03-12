class Usuario:
    def __init__(self, nome, username, password, role):
        self.nome = nome
        self.username = username
        self.password = password  
        self.role = role  # Papel do usuário (ex: "técnico", "atleta", "secretário", "gerente")

    def autenticar(self, username, password):
        return self.username == username and self.password == password

    def __str__(self):
        return f"Nome: {self.nome}, Username: {self.username}, Função: {self.role}"
    
class Tecnico(Usuario):
    def __init__(self, nome, username, password, especializacao):
        super().__init__(nome, username, password, role="técnico")
        self.especializacao = especializacao  # Ex: "futebol", "vôlei", etc.

    def __str__(self):
        return super().__str__() + f", Especialização: {self.especializacao}"
    
class Atleta(Usuario):
    def __init__(self, nome, username, password, posicao):
        super().__init__(nome, username, password, role="atleta")
        self.posicao = posicao  # Ex: "atacante", "goleiro", etc.

    def __str__(self):
        return super().__str__() + f", Posição: {self.posicao}"
    
class SecretarioFinanceiro(Usuario):
    def __init__(self, nome, username, password, setor):
        super().__init__(nome, username, password, role="secretário financeiro")
        self.setor = setor  # Ex: "contabilidade", "folha de pagamento", etc.

    def __str__(self):
        return super().__str__() + f", Setor: {self.setor}"
    
class Gerente(Usuario):
    def __init__(self, nome, username, password, departamento):
        super().__init__(nome, username, password, role="gerente")
        self.departamento = departamento  # Ex: "futebol", "marketing", etc.

    def __str__(self):
        return super().__str__() + f", Departamento: {self.departamento}"
    
import json

class GerenciadorUsuarios:
    def __init__(self):
        self.usuarios = []

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def salvar_usuarios(self, filename="usuarios.json"):
        with open(filename, "w") as file:
            json.dump([usuario.__dict__ for usuario in self.usuarios], file, indent=4)

    def carregar_usuarios(self, filename="usuarios.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.usuarios = []
                for item in data:
                    if item["role"] == "técnico":
                        self.usuarios.append(Tecnico(item["nome"], item["username"], item["password"], item["especializacao"]))
                    elif item["role"] == "atleta":
                        self.usuarios.append(Atleta(item["nome"], item["username"], item["password"], item["posicao"]))
                    elif item["role"] == "secretário financeiro":
                        self.usuarios.append(SecretarioFinanceiro(item["nome"], item["username"], item["password"], item["setor"]))
                    elif item["role"] == "gerente":
                        self.usuarios.append(Gerente(item["nome"], item["username"], item["password"], item["departamento"]))
        except FileNotFoundError:
            print("Arquivo de usuários não encontrado. Iniciando com lista vazia.")