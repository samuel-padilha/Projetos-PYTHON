# 3️⃣ Manipular arrays e listas

# Exercício:
# Crie uma  que receba uma lista de números e 
# retorne uma nova lista contendo apenas os números pares.



def receber_lista(lista_numero,opt):
    lista_nova=[]
    if opt == "par":
        for i in lista_numero:
            if i%2 == 0 :
                lista_nova.append(i)
        return lista_nova
    elif opt == "impar":
        for i in lista_numero:
            if i%2 != 0 :
                lista_nova.append(i)
        return lista_nova

lista=receber_lista(lista_numero=[1,4,3,7,9,16,5,8],opt="par")
print(lista)