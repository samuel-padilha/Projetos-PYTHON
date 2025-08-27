
import os

# Biblioteca que faz requisições http
import requests


# URL da API para buscar a cotação
url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
response = requests.get(url)

# Confere se a requisição foi bem sucedida
if response.status_code == 200:

    # transformar a resposta (que vem como texto JSON) em um dicionário Python
    data = response.json()

    # recebe o dicionario de conversão em real
    dolar = data['USDBRL']

    # Da tabela mostra o valor do dolar em real 
    valor = float(dolar['bid'])
    

    # Informa valor do dolar
    os.system("clear")
    print(f"Cotação do Dólar:")
    print(f"O dolar custa :R$ {valor}")


    # Pede ao usuário quanto deseja converter
    c=float(input('Quantos reais deseja converte em dolar?'))



    # Imprime o resultado
    resultado = c / valor
    print(f"Voçe tera ${resultado:.2f} dólares")

else:
    print("Erro ao buscar a cotação.")

    