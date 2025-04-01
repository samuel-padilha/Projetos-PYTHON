#Classe TV: Faça um programa que simule um televisor criando-o como um objeto.
# O usuário deve ser capaz de informar o número do canal
# e aumentar ou diminuir o volume.
# Certifique-se de que o número do canal
# e o nível do volume permanecem dentro de faixas válidas.
import os
import sys
class TV():
    def __init__(self,status=False,volume=0,numero_canal=0):
        self.numero_canal=numero_canal
        self.volume=volume
        self.status=status
    
    def mudar_canal(self):
        novo=int(input("digite o canal:"))
        self.numero_canal=novo
        
    def diminuir_vol(self):
          self.volume-=1
          print(f"O volume está em {self.volume}%")

    def aumentar_vol(self):
        self.volume+=1
        print(f"O volume está em {self.volume}%")


    def tela_inicial(self):
        print(f"[0]DESLIGAR")
        print(f"[1]LIGAR")
        print(f"[+]ALMENTAR VOLUME")
        print(f"[-]DIMINUIR VOLUME")
        print(f"[@]MUDAR DE CANAL")
        print(f"[%]MOSTRAR STATUS")
        print("[x]para sair")
        print("")
    
    def escolher(self):
        escolha=input("Digite uma opção: ")
        match escolha:
            case "0":
                self.status=False
                print("Desligando...")
            case "1":
                self.status=True
                print("Ligando...")
            case "+":
                if self.status==False:
                    print("Ligue a tv primeiro para poder aumentar o volume")
                else:
                    self.volume+=1
                    print("Volume aumentado")
            case "-":
                if self.status==False:
                    print("Ligue a tv primeiro para poder diminuir o volume")
                if self.volume==0:
                    print("O volume já está em 0%")
                else:
                    self.volume-=1
                    print("Volume diminuido")
            case "@":
                numero=int(input("Digite o canal:"))
                self.numero_canal=numero
            case "%":
                os.system("clear")
                print(f"A TV está ligada?{self.status}")
                print(f"Está no canal {self.numero_canal}")
                print(f"O volume esta em {self.volume}%")
                print(f"")
            case "x":
                sys.exit()

#------------------------------------------------------
if __name__ == "__main__":
    samsung= TV()
    while True:
        os.system("clear")
        samsung.tela_inicial()
        samsung.escolher()
        continuar=input("Pressione enter para continuar ")
        if continuar!="":
            break
   
  