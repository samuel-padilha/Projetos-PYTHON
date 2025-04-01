import requests

# Faz a requisição para obter os usuários
response = requests.get("https://jsonplaceholder.typicode.com/users")

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    data = response.json()  # Converte a resposta para JSON

    user_id = 4  # ID do usuário que deseja encontrar

    # Busca o usuário pelo ID
    user = next((user for user in data if user["id"] == user_id), None)

    if user:
        # Exibe as informações separadamente
        print(f"Nome: {user['name']}")
        print(f"Email: {user['email']}")
        print(f"Empresa: {user['company']['name']}")
        print(f"Endereço: {user['address']['street']}, {user['address']['city']}")
    else:
        print("Usuário não encontrado!")

else:
    print("Erro ao buscar dados:", response.status_code)

print(data)