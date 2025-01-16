#Faça um Programa que leia um vetor de 10 caracteres,
# e diga quantas consoantes foram lidas. 
# Imprima as consoantes. 



vetor=[]
for i in range (1,4):
    i =input(f"digite a {i}ª letra: ")
    vetor.append(i)
print('/n')

vogais = ["a", "e", "i", "o", "u"]


# Filtrando as consoantes
vetor = [char for char in vetor if char.lower() not in vogais]

# Apresentando as consoantes com seus índices
for i, consoante in enumerate(vetor):
    print(f"Índice {i+1}: {consoante}")

# Total de consoantes
ncons = len(vetor)
print(f"Foram lidas {ncons} consoantes")



