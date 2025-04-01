from banco_completo import Conta_Corrente

lista_usr=[]
def tela_login():
    print(f"--------Bem-vindo ao Banco--------")
    print(f"1 -Criar uma conta")
    print(f"2 -logar na conta ")
    print(f"0 -sair")



def logar():
    op=int(input("Digite uma opção"))
    if op==1:
        qtd=int(input("Digite quantas contas deseja criar: "))
        for i in range(0,qtd):
            titular = input("Digite o nome do titular: ")
            num_conta = int(input("Digite o número da conta: "))
            senha = int(input("Digite a senha da conta: "))
            lista_usr[titular] = Conta_Corrente(titular,num_conta,titular,senha,)

    if op ==2:
        
        tela_app()
    if op ==3:
        print(lista_usr[titular])
        
    if op ==0: exit    



def tela_app(self):
    print(f"1 - Depositar")
    self
    print(f"2 - Sacar")
    print(f"3 - Transferir")
    print(f"4 - Status da sua conta")
    print(f"5 - Ir para a tela de login")

def ir_app():
    pass