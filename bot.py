import requests

print("INICIANDO TESTE...")

url = "https://api.telegram.org/bot8656227637:AAG1wxbRplphnglvWrLmpnbwyrEslqlsvKg/sendMessage"

params = {
    "chat_id": "@achadinhosshopeebr4",
    "text": "🔥 MENSAGEM DIRETA VIA GITHUB 🔥"
}

r = requests.get(url, params=params)

print("STATUS:", r.status_code)
print("RESPOSTA:", r.text)