import os, requests

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT"]

print("token len:", len(TOKEN))  # só pra depurar

msg = "ping"
url = f"https://api.telegram.org/bot{8656227637:AAH4qVemew_e6O55Y2yc48x-Ko9eh8Ad-BI}/sendMessage"
r = requests.post(url, json={"chat_id": CHAT_ID, "text": msg})
print(r.status_code, r.json())