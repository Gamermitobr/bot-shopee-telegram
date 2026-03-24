            import schedule
            import time
            import requests

            BOT_TOKEN = "SEU_TOKEN_DO_BOT" # Substitua pelo seu token
            CHANNEL_ID = "-1003562877087" # O ID do seu canal
            PROMOTION_TEXT = "⚡️ Nova promoção imperdível! Confira agora! ⚡️" # Sua mensagem

            def send_promotion():
                url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
                payload = {
                    "chat_id": CHANNEL_ID,
                    "text": PROMOTION_TEXT
                }
                try:
                    response = requests.post(url, data=payload)
                    response.raise_for_status() # Levanta um erro pra status codes HTTP ruins (4xx ou 5xx)
                    print(f"Promoção enviada: {PROMOTION_TEXT}")
                except requests.exceptions.RequestException as e:
                    print(f"Erro ao enviar promoção: {e}")

            # Agende a função pra rodar a cada X horas/minutos ou em um horário específico
            schedule.every().day.at("10:00").do(send_promotion) # Todo dia às 10:00
            schedule.every(6).hours.do(send_promotion) # A cada 6 horas

            while True:
                schedule.run_pending()
                time.sleep(1) # Espera 1 segundo pra não consumir muito CPU