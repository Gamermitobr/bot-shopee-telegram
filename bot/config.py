# bot/config.py
import os
from dotenv import load_dotenv

load_dotenv() # Carrega as variáveis do arquivo .env

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
SHOPEE_URL = os.getenv("SHOPEE_URL", "https://shopee.com.br/Ofertas-do-Dia-cat.11048895.11048906")
# Você pode adicionar outras configurações aqui, como proxies, etc.