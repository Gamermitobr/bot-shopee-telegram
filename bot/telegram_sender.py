# bot/telegram_sender.py
import json
from telegram import Bot
from telegram.error import TelegramError
import asyncio
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def send_deals_to_telegram(deals_file, bot_token, chat_id):
    if not bot_token or not chat_id:
        logging.error("TELEGRAM_BOT_TOKEN ou TELEGRAM_CHAT_ID não configurados.")
        return

    try:
        with open(deals_file, 'r', encoding='utf-8') as f:
            deals = json.load(f)
    except FileNotFoundError:
        logging.error(f"Arquivo de ofertas '{deals_file}' não encontrado.")
        return
    except json.JSONDecodeError:
        logging.error(f"Erro ao decodificar JSON do arquivo '{deals_file}'.")
        return

    if not deals:
        logging.info("Nenhuma oferta para enviar.")
        return

    bot = Bot(token=bot_token)
    logging.info(f"Iniciando envio de {len(deals)} ofertas para o chat ID: {chat_id}")

    for deal in deals:
        message_text = (
            f"✨ **NOVA OFERTA SHOPEE!** ✨\n\n"
            f"🛒 {deal.get('title', 'Produto desconhecido')}\n"
            f"💰 Preço: {deal.get('price', 'N/A')}\n"
            f"🔗 Link: {deal.get('link', '#')}\n\n"
            f"#Shopee #Oferta #Promoção"
        )
        try:
            await bot.send_message(chat_id=chat_id, text=message_text, parse_mode='Markdown', disable_web_page_preview=False)
            logging.info(f"Oferta enviada: {deal.get('title')}")
            await asyncio.sleep(1) # Pequeno atraso para evitar flood da API do Telegram
        except TelegramError as e:
            logging.error(f"Erro ao enviar mensagem para o Telegram: {e}")
            break # Parar se houver um erro sério de Telegram

    logging.info("Envio de ofertas finalizado.")

if __name__ == "__main__":
    from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
    deals_json_path = 'deals.json' # Caminho onde o scraper salvou
    
    # Executa a função assíncrona
    try:
        asyncio.run(send_deals_to_telegram(deals_json_path, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID))
    except RuntimeError as e:
        if "cannot run an event loop while another event loop is running" in str(e):
            logging.warning("Event loop already running, trying alternative execution for Telegram sender.")
            # This can happen in some environments, for simple scripts this might work
            import nest_asyncio
            nest_asyncio.apply()
            asyncio.run(send_deals_to_telegram(deals_json_path, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID))
        else:
            raise