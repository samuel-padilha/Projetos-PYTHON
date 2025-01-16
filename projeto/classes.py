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
