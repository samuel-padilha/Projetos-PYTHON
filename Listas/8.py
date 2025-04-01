#Faça um Programa que peça a idade e a altura de 5 pessoas,
# armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida. 

altura = []
idade = []

for i in range (0,2):
    altura.append(input(f"digite sua {i} altura"))
    idade.append(input(f"digite sua {i} idade"))

print(f"alt:altura")
print("idade:",idade)

altura.reverse()
print(altura)