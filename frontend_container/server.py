# 2. REST API Server

from flask import Flask, request, jsonify
import pickle

# Configuração do Flask
app = Flask(__name__)

# Caminho do modelo (arquivo gerado na parte 1)
MODEL_PATH = "/folder/association_rules.pkl"

# Variáveis globais
VERSION = "1.0"
MODEL_DATE = "2025-01-06"

# Carregar o modelo
try:
    with open(MODEL_PATH, "rb") as file:
        app.model = pickle.load(file)
except FileNotFoundError:
    print(f"Erro: o modelo não foi encontrado em {MODEL_PATH}. Verifique o caminho.")
    exit(1)

# Função para recomendar músicas
def recommend_songs(user_history, rules, top_n=5):
    recommendations = []
    for rule in rules:
        antecedent, consequent, confidence = rule
        if antecedent.issubset(user_history):
            recommendations.extend(consequent)
    recommendations = [song for song in recommendations if song not in user_history]
    return list(set(recommendations))[:top_n]

# Rota da API para recomendações
@app.route("/api/recommend", methods=["POST"]) # Caminho para acessar o servidor, aceita apenas requisições POST
def recommend():
    try:
        # Receber os dados enviados na requisição
        data = request.get_json(force=True)
        user_history = set(data.get("songs", []))

        # Gerar recomendações
        recommendations = recommend_songs(user_history, app.model)

        # Responder com as recomendações
        response = {
            "songs": recommendations,
            "version": VERSION,
            "model_date": MODEL_DATE,
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Iniciar o servidor
# host="0.0.0.0": Faz com que o servidor aceite conexões de qualquer endereço IP
# port=30502: Define a porta em que o servidor irá rodar
# debug=True: Ativa o modo de depuração, exibindo mensagens de log detalhadas
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=52056, debug=True)