from bs4 import BeautifulSoup
import requests
def wiki_header(url):
    responce = requests.get(url)
    html_cd = responce.text
    url = BeautifulSoup(html_cd,'html.parser')
    zagolovok = url.find('h1').text
    return zagolovok


print(wiki_header('https://en.wikipedia.org/wiki/Operating_system'))