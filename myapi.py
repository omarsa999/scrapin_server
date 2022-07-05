from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()


page = requests.get('https://panet.co.il/')
page.encoding = page.apparent_encoding
soup = BeautifulSoup(page.content, 'lxml')
news = soup.find('div', class_='panet-articles panet-horizontal')
title = news.find_all('div', class_='panet-title')


@app.get("/")
def read_root():
    txt = title[0]
    #txt = txt.encode('cp1252')

    return {"Hello": txt.text}
