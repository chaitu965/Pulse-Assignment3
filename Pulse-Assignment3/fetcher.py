import requests
from bs4 import BeautifulSoup

def fetch_text(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        texts = []
        for tag in soup.find_all(["h1", "h2", "h3", "p", "li"]):
            text = tag.get_text(strip=True)
            if len(text) > 30:
                texts.append(text)

        return texts[:200]

    except Exception:
        return []
