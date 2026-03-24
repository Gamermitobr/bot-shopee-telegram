# send_promo.py
import requests
import os

# Pega o token e o ID do canal das variáveis de ambiente.
# Isso é crucial para a segurança e para que o GitHub Actions funcione.
BOT_TOKEN = os.environ.get("8656227637:AAH4qVemew_e6O55Y2yc48x-Ko9eh8Ad-BI")
CHANNEL_ID = os.environ.get("-1003562877087")

# Sua mensagem de promoção
PROMOTION_TEXT = "🔔 Novidades! Nossas promoções frescas acabaram de chegar! 🎁"

def send_promotion():
    if not BOT_TOKEN or not CHANNEL_ID:
        print("Erro: TELEGRAM_BOT_TOKEN ou TELEGRAM_CHANNEL_ID não configurados.")
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": PROMOTION_TEXT
    }
    try:
        response = requests.post(url, data=payload)
        response.raise_for_status() # Verifica se a requisição foi bem-sucedida (status 2xx)
        print(f"Promoção enviada com sucesso para o canal {CHANNEL_ID}: {PROMOTION_TEXT}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao enviar promoção para o canal {CHANNEL_ID}: {e}")

if __name__ == "__main__":
    send_promotion()