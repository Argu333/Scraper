import requests
from bs4 import BeautifulSoup

login_url = "https://www.scrapethissite.com/pages/advanced/?gotcha=headers"

head = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36", "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}

response = requests.get(login_url, headers=head)
soup = BeautifulSoup(response.text, "html.parser")
print(f"Status code: {((response.status_code))}")
pr = soup.find("div", class_="row").text.strip()
print(pr)