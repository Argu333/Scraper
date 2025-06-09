import requests
from bs4 import BeautifulSoup

login_url = "https://www.scrapingcourse.com/login/csrf"

ses = requests.Session()
response = ses.get(login_url)
soup = BeautifulSoup(response.text, "html.parser")
tok = soup.find("input", {"name": "_token"})["value"]

payload = {"_token": tok, "email": "admin@example.com", "password": "password"}

response = ses.post(login_url, data=payload)

print(f"Status code: {((response.status_code))}")

soup = BeautifulSoup(response.text, "html.parser")

page_title = soup.title.string

print(f"Page title: {page_title}")