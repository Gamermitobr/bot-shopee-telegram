import requests

TOKEN = "8656227637:AAHSMvZd31r_aG70NZG5eyFoYmivjCgx4UA"
CHAT_ID = 3562877087

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

res = requests.post(url, json={
    "chat_id": CHAT_ID,
    "text": "🔥 TESTE DEBUG",
})

print("STATUS:", res.status_code)
print("RESPOSTA:", res.text)