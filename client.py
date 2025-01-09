import requests
import json
import os

# URL do servidor Flask
url = "http://localhost:52056/api/recommend"

# Arquivo JSON com as músicas
input_file = "user_history.json"

# Verificar se o arquivo existe no diretório
if not os.path.exists(input_file):
    print(f"Erro: O arquivo '{input_file}' não foi encontrado no diretório atual.")
    exit(1)

# Ler o arquivo JSON com as músicas
try:
    with open(input_file, "r") as f:
        user_history = json.load(f)
except json.JSONDecodeError as e:
    print(f"Erro ao ler o arquivo JSON: {e}")
    exit(1)

# Verificar a chave "songs"
if "songs" not in user_history or not isinstance(user_history["songs"], list):
    print("Erro: O arquivo JSON deve conter uma chave 'songs' com uma lista de músicas.")
    exit(1)

# Enviar a requisição POST para o servidor Flask
print(f"Enviando requisição para {url} com as músicas: {user_history['songs']}")
response = requests.post(url, json=user_history)

# Processar a resposta do servidor
if response.status_code == 200:
    print("Recomendações recebidas:")
    print(json.dumps(response.json(), indent=4))
else:
    print(f"Erro: {response.status_code}")
    print(response.text)