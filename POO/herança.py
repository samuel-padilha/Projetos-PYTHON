class jogador():
    def __init__(self,nome,data_nasc=0):
        self.nome=nome
        self.data_nasc=data_nasc

class classico(jogador):
    def __init__(self,nome,data_nasc,velocidade):
       self.velocidade=velocidade
       super().__init__(nome,data_nasc)
    
samuel= classico ("sam",20.06,80)
print(samuel.nome)
print(samuel.data_nasc)
print(samuel.velocidade)
       
arthur= jogador("arthur")
print(arthur.data_nasc)