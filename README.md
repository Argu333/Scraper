# 🕷️ Web Scraper & Crawler in Python

A Python-based web scraper and crawler designed to extract structured data from various websites — including those with anti-scraping techniques like custom headers and CSRF protection.

---

## 🌐 Target Websites

- **[Books to Scrape](https://books.toscrape.com)**  
- **[Scraping Course – CSRF Protected Login](https://www.scrapingcourse.com/login/csrf)**  
- **[Scrape This Site – Advanced Headers Challenge](https://www.scrapethissite.com/pages/advanced/?gotcha=headers)**  

---

## 🛠️ Features

- ✅ Custom headers to bypass basic anti-bot detection  
- ✅ Automatic pagination support  
- ✅ CSRF token retrieval and session-based login handling  
- ✅ Output data to JSON 

---

## 📁 Project Structure

```bash
Scraper/
├── Sync/                     # Synchronous scraping modules
│   ├── Categories.py         # Gets all the books categories
│   ├── NamePrice.py          # Extracts book names and prices
│   └── Total.py              # Extracts book names and prices as per their categories
│
├── async.py                  # Asynchronous scraping module
├── header.py                 # Manages headers/user-agents
├── Login.py                  # Handles login/authentication
└── Scrape.json               # Scraping output for "async.py"
```
---

## 🧰 Tech Stack

- Python 3.11.9
- [requests](https://pypi.org/project/requests/) – HTTP requests
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) – HTML parsing
- asyncio, aiohttp
- json

---

## ⚙️ Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/Argu333/Scraper.git
cd Scraper
```
2. **Install the used libraries (if not installed)**
```bash
pip install requests
pip install beautifulsoup4
pip install aiohttp
```
