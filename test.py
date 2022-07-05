import requests
from bs4 import BeautifulSoup


def get_title():
    page = requests.get('https://panet.co.il/')
    page.encoding = page.apparent_encoding
    soup = BeautifulSoup(page.content, 'lxml')
    news = soup.find('div', class_='panet-articles panet-horizontal')
    title = news.find_all('div', class_='panet-title')
    return title


for x in get_title():
    print(x.text)
