import os
biblioteca = Biblioteca()
usuario = Usuario()
op=""


class Usuario:
    def __init__(self):
        self.livros_emprestados = [0]
        self.list_usr = []

    def criar_usr(self,nome,senha):
        os.system("clear")
        user= {"usuario":nome,
            "senha":senha
            }
        self.list_usr.append(user)
        print(self.list_usr)
        rep()
    

    def login(self, nome, senha):
        
        # Verifica se o usuário e a senha correspondem a algum usuário na lista
        while True:
            for user in self.list_usr:
                if user['senha'] == senha and user['usuario'] == nome:
                    print(f"Encontrado: {user}")
                    meu()
                else:
                    print("Usuário ou senha inválidos.")
            return False

        
    
    def exibir_usr(self):
        return self.list_user
    
    
    def empres_livros(self):
        return (f"o usuario {self.nome} tem  {self.livros_emprestados}o usuario {self.nome} tem  {self.livros_emprestados} livros emprestados")
        
    def devolução_livro(self):
        pass
     
class Biblioteca():
    
    def __init__(self):
        self.livros = []  # Inicializa a lista de livros como vazia

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}, Exemplares: {self.exemplares}"

    def adicionar_livro(self, titulo, autor, ano, exemplares):
        livro = {
            "titulo": titulo,
            "autor": autor,
            "ano": ano,
            "exemplares": exemplares,
        }
        
        self.livros.append(livro)
        os.system("clear")
        print(f"Livro '{titulo}' adicionado com sucesso!")
        print(self.livros)
        print('')




    def remover_livro(self, indice):
        os.system("clear")
        livro_removido = self.livros.pop(indice-1)
        print(f"Livro '{livro_removido['titulo']}' removido com sucesso!")
        print('')
        

    def listar_livros(self):
        os.system("clear")
        if not self.livros:
            print("Nenhum livro na biblioteca.")
        else:
            print("Livros na biblioteca:")
            for i, livro in enumerate(self.livros):
                print(f"{i+1}: Título:{livro['titulo']} - Autor:{livro['autor']} - Ano:({livro['ano']}) - {livro['exemplares']} exemplares")
        print('')
   

def rep():
    test=" "
    if test ==" ":
        test=input("Enter pra continuar")
        os.system("clear")


def meu():
    os.system("clear")
    while op !="0":

        print("             Escolha:            ")
        print("[0] sair",)
        print("[1] criar usuário ",end='        ')
        print("[5] devolver livro ")
        print("[2] adcionar livro ",end='       ')
        print("[6] livro disponiveis")
        print("[3] remover livro ",end='        ')
        print("[7] lista usuarios")
        print("[4] emprestar livro ",end='      ')
        print("[8] livros emprestados")
        print("")
        
        op = input('digite uma opção: ')


        if op =="2":
            print()
            titulo = input("Digite o título do livro (ou 'sair' para encerrar): ")
            autor = input("Digite o autor: ")
            ano = int(input("Digite o ano de publicação: "))
            exemplares = int(input("Digite o número de exemplares: "))
            biblioteca.adicionar_livro(titulo, autor, ano, exemplares)
            rep()


        if op =="3":
            print(biblioteca.listar_livros())
            print("")
            indice=int(input("Qual livro que deseja remover: "))
            biblioteca.remover_livro(indice)
            rep()



        # if op =="4":
        #     os.system("clear")
        #     print(lista_livros)
        #     li=int(input("Qual livro deseja emprestar?"))
        #     emprest= lista_livros.pop(li-1)
        #     lista_emprestimo.append(emprest)
        #     os.system("clear")
        #     print("lista de emprestimo atualizada com sucesso!")
        #     print(lista_emprestimo)
        #     time.sleep(4)
        #     rep()
            

        # if op =="5":
        #     os.system("clear")
        #     print("Livros emprestados:")
        #     print(lista_emprestimo)
        #     dev=int(input("Qual livro deseja devolver?"))
        #     devolver= lista_emprestimo.pop(dev-1)
        #     lista_livros.append(devolver)
        #     os.system("clear")
        #     print("Devolução feita com sucesso!")
        #     rep()

            
        if op =="6":
            biblioteca.listar_livros()
            rep()
        # if op =="7":
        #     os.system("clear")
        #     print("Lista de usuarios adcionados:")
        #     print(lista_usr)
        #     rep()

        # if op =="8":
        #     os.system("clear")
        #     print("Lista de livros emprestados:")
        #     #verificar se a lista esta vazia
        #     print(lista_emprestimo)
        #     rep()

        elif op =="0":
            os.system("clear")
            print("Tenha um bom dia!")





def painel():
    usuario = Usuario()  # Cria a instância de Usuario
    
    while True:

        print("Escolha: ")
        print("[0] Sair")
        print("[1] Criar usuário")
        print("[2] Fazer login")
        op = input('Digite uma opção: ')

        if op == "0":
            os.system("clear")
            print("Tenha um bom dia!")
            break  # Sai do loop

        if op == "1":
            nome = input("Digite o nome do usuário: ")
            senha = input("Digite a senha do usuário: ")  # Senha como string
            usuario.criar_usr(nome, senha)

        if op == "2":
            os.system("clear")
            print("Tela de login:")
            nome = input("Digite seu usuário: ")
            senha = input("Digite sua senha: ")
            usuario.login(nome, senha)

painel()















