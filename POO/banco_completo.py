# Módulo principal do banco

class ContaCorrente:
    def __init__(self, nome_correntista, numero_conta, senha_conta, ativacao=False, saldo=0):
        self.nome_correntista = nome_correntista
        self.numero_conta = numero_conta
        self.senha_conta = senha_conta
        self.saldo = saldo
        self.ativacao = ativacao
    
    def __repr__(self):
        return f'Conta(nome={self.nome_correntista}, conta={self.numero_conta})'

    def alterar_nome(self, novo_nome):
        self.nome_correntista = novo_nome
        print("Nome alterado com sucesso!")

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        else:
            print("O valor do depósito deve ser positivo.")

    def saque(self, senha, valor):
        if senha == self.senha_conta:
            if 0 < valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
            else:
                print("Saldo insuficiente ou valor inválido.")
        else:
            print("Senha incorreta.")

    def status(self):
        print(f"Nome: {self.nome_correntista}\nNúmero da conta: {self.numero_conta}\nSaldo: R${self.saldo:.2f}\n")

    def transferencia(self, valor, conta_destino):
        if valor > self.saldo:
            print("❌ Saldo insuficiente para transferência.")
        else:
            self.saldo -= valor
            conta_destino.saldo += valor
            print(f"✅ Transferência de R${valor:.2f} realizada com sucesso!")
            print(f"Novo saldo de {self.nome_correntista}: R${self.saldo:.2f}")
            print(f"Novo saldo de {conta_destino.nome_correntista}: R${conta_destino.saldo:.2f}")
contas = {}



def criar_conta():
    nome = input("Digite o nome do titular: ")
    num_conta = input("Digite o número da conta: ")
    senha = input("Digite a senha: ")
    contas[num_conta] = ContaCorrente(nome, num_conta, senha)
    print(f"Conta criada com sucesso para {nome}!")

def acessar_conta():
    num_conta = input("Digite o número da conta: ")
    senha = input("Digite a senha: ")
    if num_conta in contas and contas[num_conta].senha_conta == senha:
        interagir_conta(contas[num_conta])
    else:
        print("❌ Conta não encontrada ou senha incorreta.")

def menu_principal():
    while True:
        print("\n--- Menu Principal ---")
        print("1 - Criar uma conta")
        print("2 - Acessar conta")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_conta()
        elif opcao == "2":
            acessar_conta()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def interagir_conta(conta):
    while True:
        print("\n--- Menu da Conta ---")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Transferir")
        print("4 - Ver status da conta")
        print("5 - Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor para depósito: "))
            conta.deposito(valor)
        elif opcao == "2":
            senha = input("Digite sua senha: ")
            valor = float(input("Digite o valor para saque: "))
            conta.saque(senha, valor)
        elif opcao == "3":
            num_destino = input("Digite o número da conta de destino: ")
            if num_destino in contas:
                valor = float(input("Digite o valor para transferência: "))
                conta.transferencia(valor, contas[num_destino])
            else:
                print("Conta de destino não encontrada.")
        elif opcao == "4":
            conta.status()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")






if __name__ == "__main__":
    menu_principal()

#sennha router: %0|F?H@f!berhO3e