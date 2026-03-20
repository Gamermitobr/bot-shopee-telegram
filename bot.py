import requests

TOKEN = "8656227637:AAG1wxbRplphnglvWrLmpnbwyrEslqlsvKg"
CHAT_ID = "@achadinhosshopeebr4"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

response = requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": "Mensagem enviada pelo GitHub 🚀"
})

print(response.text)
print("BOT INICIADO")