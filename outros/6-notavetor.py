#Faça um Programa que peça as quatro notas de 10 alunos, 
#calcule e armazene num vetor a média de cada aluno,
#imprima o número de alunos com média maior ou igual a 7.0. 

vetor=[]


for i in range (5):
    numero=int(input(f"digite a {i+1}ª numero: "))
    vetor.append(numero)