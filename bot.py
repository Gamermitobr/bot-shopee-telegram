import requests

print("BOT RODANDO AGORA")

response = requests.get(
    "https://api.telegram.org/bot8656227637:AAG1wxbRplphnglvWrLmpnbwyrEslqlsvKg/sendMessage",
    params={
        "chat_id": "@achadinhosshopeebr4",
        "text": "🔥 TESTE DIRETO DO GITHUB 🔥"
    }
)

print(response.text)