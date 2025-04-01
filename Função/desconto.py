#Crie uma função chamada calcular_desconto que receba o valor de um produto 
# e um percentual de desconto.
# A função deve retornar o valor com o desconto aplicado.

# def calcular_desconto(val_prod,desconto):
#     calculo_desc= val_prod*desconto//100

#     print(f'O desconto será de {calculo_desc}')
#     print(f'Esse é o valor com o desconto aplicado: {val_prod-calculo_desc}')

# produto=int(input("Digite o valor do produto:"))
# desconto=int(input("Digite a porcentagem de desconto:"))

# calcular_desconto(produto,desconto)


#Programa modularizado
# def calcular_desconto(val_prod,desconto):
#     calculo=val_prod*desconto//100
#     desconto_aplicado= val_prod-calculo
#     return desconto_aplicado
   
# def informar_produto():
#     produto=int(input("Digite o valor do produto:"))
#     desconto=int(input("Digite a porcentagem de desconto:"))
#     calculo=calcular_desconto(produto,desconto)
#     print(f'Esse é o valor com o desconto aplicado: {calculo}')

# informar_produto()

# 📌 Desafio extra: Modifique a função para aceitar um número variável de produtos 
# e calcular o total com desconto.

def calcular_desconto(val_prod,desconto):
    calculo=val_prod*desconto//100
    desconto_aplicado= val_prod-calculo
    return desconto_aplicado
   
def informar_produto():
   
    lista_produtos=[0]
    numero_produtos=int(input("Quantos produtos deseja calcular"))
    for i in range (1,numero_produtos+1):
        produto=int(input(f"Digite o valor do {i}º produto:"))
        lista_produtos.append(produto)
    produtos=sum(lista_produtos)
    desconto=int(input("Digite a porcentagem de desconto:"))   
    
    calculo=calcular_desconto(produtos,desconto)
    print(f'Esse é o valor com o desconto aplicado: {calculo}')


informar_produto()