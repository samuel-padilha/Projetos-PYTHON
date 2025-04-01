#Classe Pessoa: Crie uma classe que modele uma pessoa:
    # Atributos: nome, idade, peso e altura
    # Métodos: Envelhercer, engordar, emagrecer, crescer.
    # Obs: Por padrão, a cada ano que nossa pessoa envelhece,
    # sendo a idade dela menor que 21 anos,ela deve crescer 0,5 cm. 

class Pessoa():
    def __init__(self,nome,idade,peso,altura):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.altura=altura

    def envelhecer(self):
        self.idade+=1
        print("VC ficou 1 ano mais velho(a)")
        self.Crescer()

    def crescer(self):
        if self.idade<21:
            self.altura+=0.5
            print("E vc cresceu 0.5 cm")
    def engordar(self):
        self.peso+=1
        print(f"Vc engordou 1kg agora vc tem {self.peso}kg")

    def emagrecer(self):
        self.peso-=1
        print(f"Vc emagreceu 1kg agora vc tem {self.peso}kg")

    def status(self):
        print("Nome:",self.nome)
        print("Idade:",self.idade)
        print("Peso:",self.peso)
        print("Altura:",self.altura)

p1= Pessoa("Samuel",18,56,1.56)
p1.status()
p1.envelhecer()
p1.status()