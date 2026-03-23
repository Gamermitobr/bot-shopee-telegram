import os
import requests

TOKEN = os.getenv("8656227637:AAH4qVemew_e6O55Y2yc48x-Ko9eh8Ad-BI")  # coloca o token nos Secrets também
CHAT_ID = -1003562877087  # <-- teu canal

def main():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": "teste do Actions"}
    r = requests.post(url, data=payload)
    print(r.json())

if __name__ == "__main__":
    main()