# Exercício:
# Crie uma classe chamada Carro que tenha os seguintes métodos:

#     ligar(), que imprime "Carro ligado"
#     desligar(), que imprime "Carro desligado"
#     acelerar(velocidade), que imprime "Acelerando para X km/h"

class Carro():
    def __init__(self,vel_atual=0):
        self.vel_atual=vel_atual


    def ligar(self):
        print("Carro ligado!")

    def desligar(self):
        print("Carro desligado!")

    def status(self):
        print(f"Velocidade atual:{self.vel_atual}")

    def acelerar(self):
        velocidade=int(input("Digite a quanto deseja acelerar:"))
        print(f"Acelerando para {velocidade} km/h")
        self.vel_atual+=velocidade

    def frear(self):
        freio=int(input("qunto deseja frear?"))
        print(f"Velocidade antes de frear: {self.vel_atual}")
        self.vel_atual -= freio
        print(f"Velocidade depois de frear: {self.vel_atual}")
        

ferrari= Carro()
ferrari.ligar()

ferrari.acelerar()
ferrari.frear()

ferrari.desligar()