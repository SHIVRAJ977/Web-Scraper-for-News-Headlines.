# 📰 News Headline Scraper

This is a simple Python script that scrapes the latest news headlines from [1news.org](https://1news.org) and saves them into a local text file named `news.txt`.

---

## 🚀 Features

- Fetches latest headlines from the homepage
- Uses `requests` and `BeautifulSoup` for web scraping
- Saves headlines into a UTF-8 encoded text file
- Error handling for failed requests

---

## 🛠️ Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`
- `lxml` (recommended for fast parsing)

Install dependencies using pip:

```bash
pip install requests beautifulsoup4 lxml

📦 How to Run
python news_scraper.py
After running, a file named news.txt will be created containing the latest headlines.

📁 Sample Output (news.txt)
June 6th is Secure Your Load Day
Cleaning Up with GIS
Environmental Marketing is Failing
Transforming Outdoor Preparedness: GOES Health Launches PrecisionAlert

📄 Files in This Project
File	             Description
news_scraper.py	   Python script that scrapes and saves headlines
news.txt	         Output file containing latest headlines
README.md	         Project documentation

