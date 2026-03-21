  # bot.py
  import os, requests
  TOKEN = os.getenv("8656227637:AAG1wxbRplphnglvWrLmpnbwyrEslqlsvKg")
  CHAT_ID = os.getenv("@achadinhosshopeebr4")
  URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
  requests.get(URL, params={"chat_id": CHAT_ID, "text": "🔥 Mensagem automática 🚀"})
   print("Resposta Telegram:", resp.json())