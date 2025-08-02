import requests
from bs4 import BeautifulSoup

url = "https://g1.globo.com"

resposta = requests.get(url)

if resposta.status_code ==200:
    soup =  BeautifulSoup(resposta.text, "html.parser")
    noticias = soup.findAll("a", class_="feed-post-link")

    print("Últimas noticias do G1:")
    for index, noticia in enumerate(noticias):
        print(f'{index+1}. {noticia.text}')