import os


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
