import requests
from bs4 import BeautifulSoup
import time

names = []
for i in range(1,2):
    url = f'https://books.toscrape.com/catalogue/page-{i}.html'
    response = requests.get(url)
    text = response.content
    data = BeautifulSoup(text, 'html.parser')
    names += data.find_all("article", class_='product_pod')

for item in names:
    Title = item.find("h3").find("a")["title"]
    Price = item.find("p", class_="price_color")
    print(f"{Title} : {Price.text}")