import requests

TOKEN = "8656227637:AAFAceWhP-4n9XFrj1YFPxfHWLTxfBRu0Tk"
CHAT_ID = "@achadinhosshopeebr4"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

res = requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": "🚀 TESTE: BOT FUNCIONANDO!"
})

print(res.text)