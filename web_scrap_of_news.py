import numpy as np
import requests
from bs4 import BeautifulSoup

# Define URL
url = "https://1news.org/?gad_source=1&gad_campaignid=21118567184&gbraid=0AAAAADmKmh0I7cntw1ku3biaZLC9u0rva&gclid=Cj0KCQjwndHEBhDVARIsAGh0g3AGWLELKHtjuFPrhXtaIKrLlG16S63YQ784pvWD-2PjwRfRq2L_2R8aAlKtEALw_wcB"

file = "news.txt"

def fetch_news():
    try:
        # Make HTTP request
        response = requests.get(url)
        
        # Check if request was successful
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            name = soup.find_all("a", class_="summary-title-link")

            # Write to file
            with open(file, "w", encoding="utf-8") as f:
                for news in name:
                    f.write(news.text.strip() + "\n")

            print("✅ Successfully written news headlines to news.txt.")
        else:
            print("❌ Request failed, try again. Status code:", response.status_code)

    except Exception as e:
        print("⚠️ Error occurred:", str(e))

# Call the function
fetch_news()
