# Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
# seguintes atributos: número da conta, nome do correntista e saldo. 
# Os métodos : alterarNome, depósito e saque; 
# No construtor, saldo é opcional, com valor default zero 
# e os demais atributos são obrigatórios. 

meu_dicionario = {
    "samuel": "4002",
    "jose": "99840",
}

class Conta_Corrente():
    def __init__(self,numero_conta,nome_corretista,senha_conta,cont_transf="",saldo=0):
        self.numero_conta=numero_conta
        self.nome_corretista=nome_corretista
        self.saldo=saldo
        self.senha_conta=senha_conta
        self.cont_transf=cont_transf
    def alterar_nome(self):
        self.nome_corretista= input("Digite um nome para alterar: ")
        print("Nome alterado com sucesso!")

    #so deposita pra mim
    def deposito(self):
        
        conta=input("Digite o numero da conta que deseja depositar:")
        
        if conta == self.numero_conta:
            self.saldo=float(input(f"Quanto deseja depositar na conta do(a) {self.nome_corretista}:"))
            print(f"Seu saldo atual é de:{self.saldo}Reais")

            self.saldo=valor
            print(f"O saldo do {self.nome_corretista} saldo atual é de:{self.saldo}Reais")

    def saque(self):
        conta=float(input("Digite o numero da conta que deseja sacar: "))
        if conta == self.numero_conta:
            senha=int(input(f"digite sua senha {self.nome_corretista}:"))
            if senha ==  self.senha_conta:
                saque=float(input(f"Quanto deseja sacar da sua conta:"))
                self.saldo-=saque
                print(f"Seu saldo atual é de:{self.saldo}Reais")

    def tranferencia(self,valor,conta_destino):
        self.saldo-=valor
        self.cont_transf=conta_destino
        conta_destino.saldo += valor
        print(f"Transferência de R${valor:.2f} para {conta_destino} realizada com sucesso.")
           
    def status(self):
        print(f"Nome:{self.nome_corretista}")
        print(f"Numero da conta:{self.numero_conta}")
        print(f"saldo:{self.saldo}")

samuel=Conta_Corrente(4002,"samuel",123)
jose=Conta_Corrente(99840,"jose",321)

valor_procurado = input("Digite a conta que deseja transferir:")

for chave, valor in meu_dicionario.items():
    if valor == valor_procurado:
        nome=chave
print(nome)
samuel.tranferencia(4,input("digite a conta para passar o pix"))




print("")
jose.status()
samuel.status()

