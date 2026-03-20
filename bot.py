import requests
import random
import json
import os

TOKEN = "8656227637:AAFAceWhP-4n9XFrj1YFPxfHWLTxfBRu0Tk"
CHAT_ID = "@achadinhosshopeebr4"

# 🔥 SUA VITRINE DE AFILIADO
VITRINE = "https://collshp.com/l6ucuzrolo235?view=storefront"

# 🔎 PALAVRAS-CHAVE (VARIA AUTOMATICAMENTE)
KEYWORDS = [
    "fone bluetooth",
    "smartwatch",
    "caixa de som",
    "led rgb",
    "teclado gamer",
    "mouse gamer",
    "carregador",
    "mini projetor",
    "ring light",
    "camera wifi"
]

# 🔎 BUSCAR PRODUTOS
def buscar_produtos():
    keyword = random.choice(KEYWORDS)

    url = "https://shopee.com.br/api/v4/search/search_items"

    params = {
        "by": "relevancy",
        "keyword": keyword,
        "limit": 20,
        "newest": 0,
        "order": "desc"
    }

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, params=params, headers=headers)
    data = r.json()

    produtos = []

    for item in data.get("items", []):
        nome = item.get("name")
        preco = item.get("price", 0) / 100000
        itemid = item.get("itemid")
        shopid = item.get("shopid")

        link = f"https://shopee.com.br/product/{shopid}/{itemid}"

        produtos.append({
            "nome": nome,
            "preco": preco,
            "link": link
        })

    return produtos

# 🔥 FILTRO
def filtrar(produtos):
    filtrados = []

    for p in produtos:
        if 5 < p["preco"] <= 120:
            filtrados.append(p)

    return filtrados

# 🚫 EVITAR REPETIDOS
def ja_postado(link):
    if not os.path.exists("postados.json"):
        return False

    with open("postados.json", "r") as f:
        data = json.load(f)

    return link in data

def salvar_postado(link):
    data = []

    if os.path.exists("postados.json"):
        with open("postados.json", "r") as f:
            data = json.load(f)

    data.append(link)

    with open("postados.json", "w") as f:
        json.dump(data, f)

# 🧠 MENSAGEM
def gerar_mensagem(p):
    chamadas = [
        "🔥 ISSO AQUI TÁ MUITO BARATO",
        "⚠️ OFERTA RELÂMPAGO",
        "💸 PREÇO IMPERDÍVEL",
        "🚨 ACHADINHO TOP"
    ]

    return f"""{random.choice(chamadas)}

🛒 {p['nome']}
💰 R${p['preco']:.2f}

👉 {p['link']}

🛍 Mais promoções:
{VITRINE}

⏰ Corre antes que acabe!
"""

# 📤 ENVIAR
def enviar(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": msg
    })

# 🚀 EXECUÇÃO
if __name__ == "__main__":
    produtos = buscar_produtos()
    filtrados = filtrar(produtos)

    enviados = 0

    for p in filtrados:
        if not ja_postado(p["link"]):
            enviar(gerar_mensagem(p))
            salvar_postado(p["link"])
            enviados += 1

        if enviados >= 3:
            break