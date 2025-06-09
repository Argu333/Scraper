import requests
from bs4 import BeautifulSoup
import time

names = []
url = f'https://books.toscrape.com/index.html'
response = requests.get(url)
text = response.content
data = BeautifulSoup(text, 'html.parser')
names += data.find("div", class_='side_categories').find("ul").find("ul").find_all("a")
for i in names:
    print(i.text.strip())