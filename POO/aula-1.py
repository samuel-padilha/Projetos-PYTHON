#https://www.dio.me/articles/explorando-a-programacao-orientada-a-objetos-em-python-conceitos-essenciais-e-boas-praticas

class Caneta:
    def _init_(self,modelo,cor,ponta,carga,tampada,status):
        self.modelo = modelo
        self.cor = cor
        self.ponta = ponta
        self.carga = carga 
        self.tampada= tampada
        

    def status(self):
        print(f"Uma caneta {self.cor} ")
        print(f"Ponta: {self.ponta} cm")
        print(f"Está tampada? {self.tampada}")


    def rabiscar(self):
        if self.tampada is False:
            print("rabisco---#---#--")
        else:
            print("Para rabiscar destampe a caneta")
        
    def tampar(self):
        self.tampada=True
        print("Tampando a caneta")
        
    def destampar(self):
        self.tampada=False
        print("Destampando a caneta")

c1= Caneta()
c1.cor="azul"
c1.ponta="1.5"
c1.destampar()
c1.rabiscar()
c1.status()

print("")

c2 = Caneta()
c2.cor="Preta"
c2.ponta="2.00"
c2.tampar()
c2.rabiscar()
c2.status()
