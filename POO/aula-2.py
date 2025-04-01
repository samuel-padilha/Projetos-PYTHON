#Classe Quadrado: Crie uma classe que modele um quadrado:
#   Atributos: Tamanho do lado
#   Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área; 

class Quadrado():
    def __init__(self,tamanho_lado):
        self.tamanho_lado=tamanho_lado


    def Mudar_valor_lado(self):
        t=int(input("digite o tamanho do lado do quadrado: "))
        self.tamanho_lado =t

    def Retornar_valor_do_lado(self):
        print("O tamanho do lado:",self.tamanho_lado)
        
    def calcular_area(self):
        area= self.tamanho_lado*self.tamanho_lado
        print("A área desse quadrado é:",area,"cm²")
    
q1 = Quadrado(0)
q1.Mudar_valor_lado()
q1.Retornar_valor_do_lado()
q1.calcular_area()