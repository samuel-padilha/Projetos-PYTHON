# Biblioteca do sistema operacional
import os

# Biblioteca operações matemáticas
import math

# Variavel responsavel por executar loop
r="s"


os.system("clear")
while r == "s" :
    

    # Cabeçalho
    print("---"*10)
    print("calculador de numeros")
    print(f"---"*10, )
    print("\n")

    
    # Funções para efetuar as operações
    def soma(n1,n2):
        return n1+n2
    
    def subtração(n1,n2):
        return n1-n2
    
    def multiplicação(n1,n2):
        return n1*n2
    
    def divisao(n1,n2):
        return n1/n2
    
    def resto(n1,n2):
        return n1%n2
    
    def potencia(n1,n2):
        return n1**n2
    
    def raiz():
        quad1= math.sqrt(n1)
        quad2= math.sqrt(n2)
        return quad1,quad2



    # Informar os dados
    n1= int(input("informe um numero:"))
    n2= int(input("informe um outro numero:"))
    print("\n")

    
    # Chamada das funções
    som= soma(n1,n2)
    sub= subtração(n1,n2)
    mult= multiplicação(n1,n2)
    div= divisao(n1,n2)
    rest= resto(n1,n2)
    pot= potencia(n1,n2)
    q1,q2 =raiz()



    # Exibição do resultado
    print(f"A soma de {n1} e {n2} é: {som}")
    print(f"A subtração de {n1} e {n2} é: {sub}")
    print(f"A multiplicação de {n1} e {n2} é: {mult}")
    print(f"{n1} dividido por {n2} é: {div}")
    print(f"O resto da divisão é: {rest}")
    print(f"{n1} elevado a {n2} é: {pot}")
    print(f"Raiz quadrada de {n1} é: {q1}")
    print(f"Raiz quadrada de {n2} é: {q2}")
    

    # Pergunta para continuar o programa ou encerrar
    r = input("Deseja continuar calculando (s/n) ?")
    os.system("clear")
    print("Obrigado,tenha um bom dia!")