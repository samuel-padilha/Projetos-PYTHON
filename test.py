import os
from classes import Usuarios
class Usuario:
    def __init__(self):
        self.livros_emprestados = []  # Lista de livros emprestados
        self.list_usr = []

    def criar_usr(self, nome, senha):
        os.system("clear")
        user = {"usuario": nome, "senha": senha, "livros_emprestados": []}
        self.list_usr.append(user)
        print(f"Usuário {nome} criado com sucesso!")
        rep()

    def login(self, nome, senha):
        # Verifica se o usuário e a senha correspondem a algum usuário na lista
        for user in self.list_usr:
            if user['senha'] == senha and user['usuario'] == nome:
                print(f"Bem-vindo, {user['usuario']}!")
                meu(user)  # Passa o objeto user para o menu do usuário após login
                return True
        print("Usuário ou senha inválidos.")
        return False

    def listar_usr(self):
        print("Usuários cadastrados:")
        for user in self.list_usr:
            print(f"Usuário: {user['usuario']}")
        rep()

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, titulo, autor, ano, exemplares):
        livro = {"titulo": titulo, "autor": autor, "ano": ano, "exemplares": exemplares}
        self.livros.append(livro)
        os.system("clear")
        print(f"Livro '{titulo}' adicionado com sucesso!")
        rep()

    def remover_livro(self, indice):
        if 0 <= indice < len(self.livros):
            livro_removido = self.livros.pop(indice)
            print(f"Livro '{livro_removido['titulo']}' removido com sucesso!")
        else:
            print("Índice inválido.")
        rep()

    def listar_livros(self):
        os.system("clear")
        if not self.livros:
            print("Nenhum livro na biblioteca.")
        else:
            print("Livros na biblioteca:")
            for i, livro in enumerate(self.livros):
                print(f"{i+1}: Título: {livro['titulo']} - Autor: {livro['autor']} - Ano: {livro['ano']} - Exemplares: {livro['exemplares']}")
        rep()

    def emprestar_livro(self, usuario, livro_index):
        # Verifica se o livro está disponível e empresta
        if livro_index < 0 or livro_index >= len(self.livros):
            print("Índice de livro inválido.")
            return
        livro = self.livros[livro_index]
        if livro['exemplares'] > 0:
            livro['exemplares'] -= 1  # Reduz o número de exemplares na biblioteca
            usuario['livros_emprestados'].append(livro)  # Adiciona o livro aos livros emprestados do usuário
            print(f"Livro '{livro['titulo']}' emprestado com sucesso!")
        else:
            print(f"O livro '{livro['titulo']}' não está disponível no momento.")
        rep()

    def devolver_livro(self, usuario, livro_index):
        # Permite que o usuário devolva um livro
        if livro_index < 0 or livro_index >= len(usuario['livros_emprestados']):
            print("Índice de livro inválido.")
            return
        livro = usuario['livros_emprestados'].pop(livro_index)  # Remove o livro dos livros emprestados do usuário
        self.livros.append(livro)  # Adiciona o livro de volta à biblioteca
        livro['exemplares'] += 1  # Aumenta o número de exemplares disponíveis na biblioteca
        print(f"Livro '{livro['titulo']}' devolvido com sucesso!")
        rep()

def rep():
    input("Pressione Enter para continuar...")

def meu(usuario_logado):
    os.system("clear")
    op = ""
    while op != "0":
        print("Escolha: ")
        print("[0] Sair")
        print("[1] Adicionar livro")
        print("[2] Remover livro")
        print("[3] Listar livros")
        print("[4] Emprestar livro")
        print("[5] Devolver livro")
        print("[6] Ver livros emprestados")
        print("[7] Listar usuários")
        print("[8] Voltar a pagina inicial")
        op = input('Digite uma opção: ')

        if op == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor: ")
            ano = int(input("Digite o ano de publicação: "))
            exemplares = int(input("Digite o número de exemplares: "))
            biblioteca.adicionar_livro(titulo, autor, ano, exemplares)

        elif op == "2":
            biblioteca.listar_livros()
            indice = int(input("Qual livro deseja remover? (Digite o número) ")) - 1
            biblioteca.remover_livro(indice)

        elif op == "3":
            biblioteca.listar_livros()

        elif op == "4":
            biblioteca.listar_livros()                
            livro_index = int(input("Escolha o número do livro que deseja emprestar: ")) - 1
            biblioteca.emprestar_livro(usuario_logado, livro_index)

        elif op == "5":
            if not usuario_logado['livros_emprestados']:
                print("Você não tem livros emprestados.")
            else:
                print("Livros emprestados:")
                for i, livro in enumerate(usuario_logado['livros_emprestados']):
                    print(f"{i+1}: {livro['titulo']}")
                livro_index = int(input("Escolha o número do livro que deseja devolver: ")) - 1
                biblioteca.devolver_livro(usuario_logado, livro_index)

        elif op == "6":
            if not usuario_logado['livros_emprestados']:
                print("Você não tem livros emprestados.")
            else:
                print("Livros emprestados:")
                for livro in usuario_logado['livros_emprestados']:
                    print(f"- {livro['titulo']}")

        elif op == "7":
            usuario.listar_usr()

        elif op == "8":
            break

        elif op == "0":
            os.system("clear")
            print("Saindo...")

def painel():
    os.system("clear")
    global usuario, biblioteca
    usuario = Usuario()  # Cria a instância de Usuario
    biblioteca = Biblioteca()  # Cria a instância de Biblioteca

    while True:
        os.system("clear")
        print("Escolha: ")
        print("[0] Sair")
        print("[1] Criar usuário")
        print("[2] Fazer login")
        op = input('Digite uma opção: ')

        if op == "0":
            os.system("clear")
            print("Tenha um bom dia!")
            break  # Sai do loop

        elif op == "1":
            nome = input("Digite o nome do usuário: ")
            senha = input("Digite a senha do usuário: ")
            usuario.criar_usr(nome, senha)

        elif op == "2":
            os.system("clear")
            print("Tela de login:")
            nome = input("Digite seu usuário: ")
            senha = input("Digite sua senha: ")
            if not usuario.login(nome, senha):
                print("Falha no login, tente novamente.")

# Chama o painel para iniciar o programa
painel()
