import requests

print("INICIOU O BOT")

TOKEN = "8656227637:AAG1wxbRplphnglvWrLmpnbwyrEslqlsvKg"
CHAT_ID = "@achadinhosshopeebr4"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

try:
    response = requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": "Mensagem enviada pelo GitHub 🚀"
    })

    print("STATUS:", response.status_code)
    print("RESPOSTA:", response.text)

except Exception as e:
    print("ERRO:", e)

print("FIM DO BOT")