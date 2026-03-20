import requests
from bs4 import BeautifulSoup

TOKEN = "SEU_TOKEN"
CHAT_ID = "@seucanal"

def pegar_ofertas():
    url = "https://www.pelando.com.br/grupo/shopee"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    ofertas = []

    for item in soup.select(".thread-link")[:5]:
        titulo = item.get_text().strip()
        link = "https://www.pelando.com.br" + item.get("href")

        ofertas.append({
            "titulo": titulo,
            "link": link
        })

    return ofertas

def gerar_mensagem(oferta):
    return f"""🔥 PROMOÇÃO REAL 🔥

🛒 {oferta['titulo']}

👉 {oferta['link']}

⏰ Corre antes que acabe!
"""

def enviar(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

if __name__ == "__main__":
    ofertas = pegar_ofertas()

    for oferta in ofertas:
        msg = gerar_mensagem(oferta)
        enviar(msg)