# bot/scraper.py
import requests
from bs4 import BeautifulSoup
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_shopee_deals(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() # Lança um erro para códigos de status HTTP ruins (4xx ou 5xx)
    except requests.exceptions.RequestException as e:
        logging.error(f"Erro ao acessar a URL {url}: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    deals = []

    # Este seletor CSS é um EXEMPLO. A Shopee usa JavaScript para carregar conteúdo dinâmico,
    # então um scraper simples pode não pegar tudo. Você pode precisar de Selenium/Playwright
    # ou encontrar uma API interna que a Shopee use (o que é mais difícil e arriscado).
    # Para páginas estáticas, procure por divs, classes ou IDs que contenham os produtos.

    # Exemplo genérico: encontrar elementos que parecem produtos
    # Você precisará inspecionar a página da Shopee com as ferramentas de desenvolvedor do navegador
    # para encontrar os seletores CSS/HTML corretos.
    # Por exemplo, se cada oferta estiver em uma div com a classe 'product-card':
    product_cards = soup.find_all('div', class_='shopee-item-card') # Ajuste esta classe!

    for card in product_cards:
        try:
            # Novamente, os seletores abaixo são exemplos.
            title_element = card.find('div', class_='shopee-item-card__name')
            price_element = card.find('div', class_='shopee-item-card__current-price')
            link_element = card.find('a', class_='shopee-item-card__link') # A URL do produto

            title = title_element.text.strip() if title_element else 'N/A'
            price = price_element.text.strip() if price_element else 'N/A'
            link = "https://shopee.com.br" + link_element['href'] if link_element and 'href' in link_element else '#'

            if title != 'N/A' and price != 'N/A':
                deals.append({
                    'title': title,
                    'price': price,
                    'link': link
                })
        except Exception as e:
            logging.warning(f"Erro ao parsear um cartão de produto: {e}")
            continue
    
    logging.info(f"Encontradas {len(deals)} ofertas.")
    return deals

if __name__ == "__main__":
    from config import SHOPEE_URL
    logging.info(f"Iniciando raspagem de ofertas da Shopee em: {SHOPEE_URL}")
    deals = get_shopee_deals(SHOPEE_URL)
    with open('deals.json', 'w', encoding='utf-8') as f:
        json.dump(deals, f, ensure_ascii=False, indent=4)
    logging.info("Ofertas salvas em 'deals.json'")