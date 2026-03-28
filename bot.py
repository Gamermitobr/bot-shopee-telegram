import feedparser
import requests
import os

TOKEN = os.getenv("8276947745:AAFwt9r7CnjGkzx_aNiYmiwf6B0QbDZ_9iA")
CHAT_ID = "@fftechsegredo"
RSS_URL = "https://www.youtube.com/feeds/videos.xml?channel_id=UCB0m5QfGQ0lF3ZVn9F0t9rA"

def enviar(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

feed = feedparser.parse(RSS_URL)

if feed.entries:
    video = feed.entries[0]
    titulo = video.title
    link = video.link

    mensagem = f"🔥 NOVO VÍDEO!\n\n{titulo}\n\n📺 Assista: {link}"
    enviar(mensagem)