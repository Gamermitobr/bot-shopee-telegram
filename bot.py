import feedparser
import requests
import os

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
RSS_URL = os.getenv("RSS_URL")

ARQUIVO = "ultimo.txt"

def enviar(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def ler_ultimo():
    try:
        with open(ARQUIVO, "r") as f:
            return f.read().strip()
    except:
        return ""

def salvar_ultimo(link):
    with open(ARQUIVO, "w") as f:
        f.write(link)

feed = feedparser.parse(RSS_URL)

if feed.entries:
    video = feed.entries[0]
    titulo = video.title
    link = video.link

    ultimo = ler_ultimo()

    if link != ultimo:
        mensagem = f"""🔥 NOVO VÍDEO!

{titulo}

📺 Assista agora:
{link}

🚀 Entra no canal pra mais dicas!"""
        
        enviar(mensagem)
        salvar_ultimo(link)