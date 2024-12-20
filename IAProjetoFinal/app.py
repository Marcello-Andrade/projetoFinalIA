#bibliotecas
from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Configurações da API
WEATHER_API_URL_CURRENT = "https://api.openweathermap.org/data/2.5/weather"
WEATHER_API_URL_FORECAST = "https://api.openweathermap.org/data/2.5/forecast"
WEATHER_API_KEY = "457069227dadad90c62567b1ebb615a8"

BASE_URL = "https://api.gemini-platform.com/v1/chat"
API_KEY = "AIzaSyBlLGAGUfIs4l37_uhjBVOlyDwn8K6Cj4o"

#Conexão da API_Gem para receber os dados e validar demais dias
BASE_API_KEY = BASE_URL + "?appid=https://api.openweathermap.org/data/2.5/forecast" + API_KEY + "https://api.gemini-platform.com/v1/chat" #proposição dos demais dias API_Gem e WeatherAPI


# Função para obter o clima atual
def obter_clima(cidade):
    params = {
        "q": cidade,
        "appid": WEATHER_API_KEY,
        "units": "metric",
        "lang": "pt"
    }
    response = requests.get(WEATHER_API_URL_CURRENT, params=params)
    if response.status_code == 200:
        dados = response.json()
        descricao = dados["weather"][0]["description"]
        temperatura = dados["main"]["temp"]
        icon = dados["weather"][0]["icon"]
        return {
            "descricao": descricao,
            "temperatura": temperatura,
            "icon": icon
        }
    else:
        return None


# Função para obter previsão estendida
def obter_previsao(cidade):
    params = {
        "gem_description": BASE_API_KEY, #uso da API para descrição dos demais dias
        "q": cidade,
        "appid": WEATHER_API_KEY,
        "units": "metric",
        "lang": "pt",
        "cnt": 40  # Número máximo de previsões (8 por dia em intervalos de 3 horas)
    }
    response = requests.get(WEATHER_API_URL_FORECAST, params=params)
    if response.status_code == 200:
        dados = response.json()
        previsoes = {}

        for item in dados["list"]:
            data = item["dt_txt"].split(" ")[0]  # Extrair apenas a data
            if data not in previsoes:  # Adicionar apenas uma previsão por dia
                previsoes[data] = {
                    "data": data,
                    "descricao": item["weather"][0]["description"],
                    "temp_max": item["main"]["temp_max"],
                    "temp_min": item["main"]["temp_min"],
                    "icon": item["weather"][0]["icon"]
                }

        # Retorna a lista filtrada
        return list(previsoes.values())
    else:
        return None


# Rota para servir o front-end
@app.route('/')
def home():
    return render_template("index.html")


# Rota para API de clima
@app.route('/clima', methods=['POST'])
def api_clima():
    dados = request.get_json()
    cidade = dados.get('cidade')
    if cidade:
        clima_atual = obter_clima(cidade)
        previsao_estendida = obter_previsao(cidade)

        if clima_atual and previsao_estendida:
            return jsonify({
                "resposta": f"O clima em {cidade} está {clima_atual['descricao']} com temperatura de {clima_atual['temperatura']}°C.",
                "icon": clima_atual["icon"],
                "previsao": previsao_estendida
            })
        else:
            return jsonify({"erro": "Não foi possível obter informações do clima."}), 500
    return jsonify({"erro": "Cidade não informada"}), 400


if __name__ == '__main__':
    app.run(debug=True)
