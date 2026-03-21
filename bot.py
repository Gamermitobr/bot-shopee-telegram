import os
import requests

TOKEN = os.getenv("8656227637:AAH4qVemew_e6O55Y2yc48x-Ko9eh8Ad-BI")
CHAT_ID = os.getenv("https://t.me/achadinhosshopeebr4")

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": "🔥 Teste do GitHub Actions funcionando!"
}

resp = requests.post(url, data=payload)
print("Resposta Telegram:", resp.json())