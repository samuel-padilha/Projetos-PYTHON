#Faça um Programa que leia um vetor A com 10 números inteiros,
#  calcule e mostre a soma dos quadrados dos elementos do vetor. 


vetorA=[]
x=0

for i in range (0,2):
    vetorA.append(int(input("\ndigite um numero inteiro: \n")))

print(vetorA)
for i in vetorA:
    q=0
    q =i*i
    
    print(f"o quadrado de {vetorA[x]} é: {q}\n")
    x+=1