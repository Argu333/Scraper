import asyncio
import aiohttp
from bs4 import BeautifulSoup
import json

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.text()

async def crawl():
    page = []
    response = await fetch('https://books.toscrape.com/index.html')
    data = BeautifulSoup(response, 'html.parser')
    cats = data.find("div", class_='side_categories').find("ul").find("ul").find_all("a")
    for i in cats:
        page.append('https://books.toscrape.com/' + i["href"])
    return page

async def scrape(link):
    books = []
    content = await fetch(link)
    soup = BeautifulSoup(content, 'html.parser')
    name = soup.find("div", class_='page-header action').find('h1')
    name = name.text
    book = soup.find_all("article", class_='product_pod')

    while (soup.find("li", class_='next') != None):
        content = await fetch(link[:-10] + soup.find("li", class_='next').find('a')['href'])
        soup = BeautifulSoup(content, 'html.parser')
        book += soup.find_all("article", class_='product_pod')

    for i in book:
        Title = i.find("h3").find("a")["title"]
        Price = i.find("p", class_="price_color")
        stock = i.find("p", class_="instock availability")
        books.append(f"{Title.strip()} : {Price.text.strip()} : {stock.text.strip()}")
    return [name, books]
    
async def main():
    links = await crawl()

    tasks = []
    for link in links:
        tasks.append(scrape(link))
    data = await asyncio.gather(*tasks)
    
    f = open("Scrape.json","w")
    for i in data:
        json.dump(i[0] + ": ", f)
        for j in i[1]:
            json.dump("\t"+j, f)
        json.dump('\n\n', f)

asyncio.run(main())