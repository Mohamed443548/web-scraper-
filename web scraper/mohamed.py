#news_scraper.py
import requests
from bs4 import BeautifulSoup

# Example website
url ="https://timesofindia.indiatimes.com"
#Add User-Agent header to mimic browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Get the webpage with heades
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    #Find correct h3 tags with class 
    headlines = soup.find_all("h3", class_="gs-c-promo-heading__title") # BBC commonly uses <h2> for headlines

    # Save to text file
    with open("headlines.txt", "w", encoding="utf-8") as file:
        for i, headline in enumerate(headlines, start=1):
            title = headline.get_text(strip=True)
            file.write(f"{i}. {title}\n")

    print("Headlines saved to headlines.txt")
else:
    print("Failed to fetch webpage.")
