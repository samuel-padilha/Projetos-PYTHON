# Biblioteca do sistema operacional
import os


# Variavel responsavel por executar loop
r = "s"

# Cabeçalho
while r == "s" :
    print("---"*10)
    print("calculador de área de retângulo")
    print(f"---"*10, )
    print("\n")

    # Pede os dados para o usuário

    l= int(input("informe a medida do lado do seu retângulo:"))
    a= int(input("informe a medida da altura do seu retângulo:"))
    os.system("clear")

    # Imprime o resultado
    print(f"A area do seu retângulo é de {l*a}m")


    # Imprime borda superior:
    print('#' * l)


    # Imprime bordas laterais:
    for _ in range(a-2):
        print('#' + ' ' * (l-2) + '#')


    # Imprime borda inferior:
    print('#' * l)


    # Pergunta para continuar o programa ou encerrar
    r = input("Deseja continuar calculando (s/n) ?")
    os.system("clear")


    # Encerramento
os.system("clear")
print("Obrigado, tenha um bom dia!")


