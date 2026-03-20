import requests

TOKEN = "8656227637:AAG1wxbRplphnglvWrLmpnbwyrEslqlsvKg"
CHAT_ID = "@achadinhosshopeebr4"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

response = requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": "🔥 Teste do bot funcionando! Se chegou aqui, deu certo 🚀"
})

print(response.status_code)
print(response.text)