# 🟡 Intermediário

#     Contagem de Palavras
#         Peça ao usuário para inserir uma frase 
#         e conte a frequência de cada palavra,
#         armazenando o resultado em um dicionário.

#     Inversão de Dicionário
#         Dado um dicionário {1: "um", 2: "dois", 3: "três"}, crie um novo dicionário invertendo as chaves e valores.

#     Mesclar Dicionários
#         Dado dois dicionários:

# d1 = {"a": 1, "b": 2}
# d2 = {"b": 3, "c": 4}

#     Mescle os dois dicionários. Se houver chaves repetidas, mantenha o maior valor.


from collections import Counter

texto = "gato cachorro gato pássaro cachorro gato"
palavras = texto.split()  # Divide o texto em palavras
frequencia = Counter(palavras)

print(frequencia)  # Saída: Counter({'gato': 3, 'cachorro': 2, 'pássaro': 1})




d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

d1.update(d2)  # Modifica d1 diretamente

print(d1)  # Saída: {'a': 1, 'b': 3, 'c': 4}
