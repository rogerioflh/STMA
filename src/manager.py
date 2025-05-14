import json
from abc import ABC


class Usuario:
    def __init__(self, nome, username, password, role):
        self.nome = nome
        self.username = username
        self.password = password
        self.role = role

    def autenticar(self, username, password):
        return self.username == username and self.password == password

    def __str__(self):
        return f"Nome: {self.nome}, Username: {self.username}, Função: {self.role}"


class Tecnico(Usuario):
    def __init__(self, nome, username, password, especializacao):
        super().__init__(nome, username, password, "técnico")
        self.especializacao = especializacao

    def __str__(self):
        return super().__str__() + f", Especialização: {self.especializacao}"


class Atleta(Usuario):
    def __init__(self, nome, username, password, posicao):
        super().__init__(nome, username, password, "atleta")
        self.posicao = posicao

    def __str__(self):
        return super().__str__() + f", Posição: {self.posicao}"


class SecretarioFinanceiro(Usuario):
    def __init__(self, nome, username, password, setor):
        super().__init__(nome, username, password, "secretário financeiro")
        self.setor = setor

    def __str__(self):
        return super().__str__() + f", Setor: {self.setor}"


class Gerente(Usuario):
    def __init__(self, nome, username, password, departamento):
        super().__init__(nome, username, password, "gerente")
        self.departamento = departamento

    def __str__(self):
        return super().__str__() + f", Departamento: {self.departamento}"


class UsuarioFactory(ABC):
    @staticmethod
    def criar_usuario(tipo, nome, username, password):
        if tipo == "1":
            return Tecnico(nome, username, password, "especialização indefinida")
        elif tipo == "2":
            return Atleta(nome, username, password, "posição indefinida")
        elif tipo == "3":
            return SecretarioFinanceiro(nome, username, password, "setor indefinido")
        elif tipo == "4":
            return Gerente(nome, username, password, "departamento indefinido")
        else:
            return None


class GerenciadorUsuarios:
    def __init__(self):
        self.usuarios = []
        self.carregar_usuarios()

    def autenticar_usuario(self, username, password):
        for usuario in self.usuarios:
            if usuario.autenticar(username, password):
                return usuario
        return None

    def criar_usuario(self):
        print("\nCriar Novo Usuário")
        nome = input("Nome completo: ")
        username = input("Username: ")
        password = input("Senha: ")

        print("Escolha um tipo de usuário:")
        print("1 - Técnico")
        print("2 - Atleta")
        print("3 - Secretário Financeiro")
        print("4 - Gerente")

        tipo = input("Digite o número da opção: ")
        usuario = UsuarioFactory.criar_usuario(tipo, nome, username, password)

        if usuario:
            self.adicionar_usuario(usuario)
            print("Usuário criado com sucesso! Agora você pode fazer login.")
        else:
            print("Tipo inválido!")

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def listar_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
        else:
            for usuario in self.usuarios:
                print(usuario)

    def salvar_usuarios(self, filename="usuarios.json"):
        with open(filename, "w") as file:
            json.dump([usuario.__dict__ for usuario in self.usuarios], file, indent=4)

    def carregar_usuarios(self, filename="usuarios.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.usuarios = []
                for item in data:
                    tipo = self.identificar_tipo(item["role"])
                    usuario = UsuarioFactory.criar_usuario(
                        tipo,
                        item["nome"],
                        item["username"],
                        item["password"]
                    )
                    if usuario:
                        if isinstance(usuario, Tecnico):
                            usuario.especializacao = item.get("especializacao", "não informado")
                        elif isinstance(usuario, Atleta):
                            usuario.posicao = item.get("posicao", "não informado")
                        elif isinstance(usuario, SecretarioFinanceiro):
                            usuario.setor = item.get("setor", "não informado")
                        elif isinstance(usuario, Gerente):
                            usuario.departamento = item.get("departamento", "não informado")
                        self.usuarios.append(usuario)
        except FileNotFoundError:
            print("Arquivo de usuários não encontrado. Iniciando com lista vazia.")

    @staticmethod
    def identificar_tipo(role):
        tipos = {
            "técnico": "1",
            "atleta": "2",
            "secretário financeiro": "3",
            "gerente": "4"
        }
        return tipos.get(role)
