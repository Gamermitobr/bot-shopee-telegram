import requests

TOKEN = "SEU_TOKEN"
CHAT_ID = "@achadinhosshopeebr4"

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": "🔥 BOT NOVO FUNCIONANDO"
    }
)