#Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
# Imprima os três vetores. 




vetor=[]
vetorpar=[]
vetorimpar=[]

for i in range (5):
    numero=int(input(f"digite a {i+1}ª numero: "))
    vetor.append(numero)

    if numero%2==0:
        
        vetorpar.append(numero)
    else:
        vetorimpar.append(numero)
        


print('')

print("todos :",vetor)

print("Pares :",vetorpar)

print("Impares :",vetorimpar)