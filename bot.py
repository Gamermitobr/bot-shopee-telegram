import requests

TOKEN = "8656227637:AAHSMvZd31r_aG70NZG5eyFoYmivjCgx4UA"
CHAT_ID = "@achadinhosshopeebr4"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

res = requests.post(url, json={
    "chat_id": CHAT_ID,
    "text": "🔥 TESTE DIRETO JSON",
})

print(res.text)