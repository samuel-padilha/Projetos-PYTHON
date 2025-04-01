#Faça um Programa que leia dois vetores com 10 elementos cada.
#Gere um terceiro vetor de 20 elementos,
#cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores. 

vet1=[2,6,8,3,5]
vet2=[9,6,0,5,1]
vet3=[]

for vet1,vet2 in zip (vet1,vet2):
    print(f'Vet1= {vet1}, vet2= {vet2}')
    vet3.append(vet1)
    vet3.append(vet2)
print(vet3)