# Foram anotadas as idades e alturas de 30 alunos.
# Faça um Programa que determine quantos alunos
# com mais de 13 anos possuem altura inferior à média de altura desses alunos. 



altura = [1.10,1.20,1.30,1.40,1.50,1.60,1.70,1.80,1.40,2.00]
idade = [1,2,3,4,5,6,7,8,15,19]
soma=0
alunos=0

for i in altura:
    soma+=i
resut=soma/len(altura)
print('Media da altura: ',resut)

for i in range (len(idade)):
    if idade[i] >13 and altura[i]<resut:
        alunos+=1

print(f"Existe {alunos} aluno(s) com mais de 13 anos,com uma altura abaixo da média")