import requests
import time

TOKEN = "8656227637:AAG1wxbRplphnglvWrLmpnbwyrEslqlsvKg"
CHAT_ID = "@achadinhosshopeebr4"
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

while True:
    requests.get(URL, params={"chat_id": CHAT_ID, "text": "🔥 Mensagem automática 🚀"})
    time.sleep(60)  # envia a cada 60 segundos