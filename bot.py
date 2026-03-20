import requests

TOKEN = "8656227637:AAG1wxbRplphnglvWrLmpnbwyrEslqlsvKg"
CHAT_ID = "https://t.me/achadinhosshopeebr4"

msg = "Teste do bot funcionando 🚀"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
data = {
    "chat_id": CHAT_ID,
    "text": msg
}

r = requests.post(url, data=data)
print(r.text)