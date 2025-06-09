from bs4 import BeautifulSoup
import requests

cats = []

url = f'https://books.toscrape.com/index.html'
response = requests.get(url)
text = response.content
data = BeautifulSoup(text, 'html.parser')
cats += data.find("div", class_='side_categories').find("ul").find("ul").find_all("a")
for i in cats:
    print(i.text.strip() + ": ")
    j = 2
    names=[]
    url = f'https://books.toscrape.com/{i["href"]}'
    response = requests.get(url)
    text = response.content
    data = BeautifulSoup(text, 'html.parser')
    names += data.find_all("article", class_='product_pod')
    while(True):
        url = f'https://books.toscrape.com/{i["href"][:-10]}page-{j}.html'
        response = requests.get(url)
        j+=1
        if response.status_code == 200:
            text = response.content
            data = BeautifulSoup(text, 'html.parser')
            names += data.find_all("article", class_='product_pod')
        else:
            for item in names:
                Title = item.find("h3").find("a")["title"]
                Price = item.find("p", class_="price_color")
                stock = item.find("p", class_="instock availability")
                print(f"{Title} : {Price.text} : {stock.text.strip()}")
            break