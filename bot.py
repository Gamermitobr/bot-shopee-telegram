import requests

TOKEN = "8656227637:AAHSMvZd31r_aG70NZG5eyFoYmivjCgx4UA"
CHAT_ID = "@achadinhosshopeebr4"

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": "🔥 BOT LIMPO FUNCIONANDO"
    }
)