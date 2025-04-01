# Remoção de Elementos

#     Remova a chave idade do dicionário.
#     Verifique se a chave idade ainda está presente.

#alunos = {"Ana": 8.5, "Carlos": 7.0, "Beatriz": 9.2}

# alunos.pop('Ana')
# print(alunos)

# print(alunos.get('Ana'))
# print('ana' in alunos.keys())



# Iteração sobre um Dicionário

#     Percorra um dicionário com nomes e notas de alunos, imprimindo cada nome e nota.



alunos = {"Ana": 8.5, "Carlos": 7.0, "Beatriz": 9.2}
x=0
for i,l in alunos.items():
    x+=1
    print(f"{x}º aluno: {i}")
    print(f"nota: {l}\n")