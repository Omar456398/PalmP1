import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json
import re

BASE_URL = "https://repossessedhousesforsale.com"
LISTINGS_URL = f"{BASE_URL}/properties/"
OUTPUT_FILE = "listings.json"


def scrape_listings():
    page_num = 0
    listings = []
    while 1:
        page_num += 1
        response = requests.get(f"{LISTINGS_URL}?page={page_num}")
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        is_empty = True
        for listing in soup.find_all('a', class_='archive-properties-title-link'):
            is_empty = False
            title = listing.get_text(strip=True)
            href = listing.get('href')
            link = urljoin(BASE_URL, href)

            loc_icon = listing.find_next('img', alt=lambda v: v and 'location' in v.lower())
            location = loc_icon.find_next('div', class_=["carlito"]).get_text(strip=True) if loc_icon else None

            price_icon = listing.find_next('img', alt=lambda v: v and 'pound' in v.lower())
            price_raw = price_icon.find_next('div', class_=["carlito-bold"]).get_text(strip=True) if price_icon else None
            price = price_raw.replace(',', '') if price_raw else None

            listings.append({
                'title': title,
                'price': price,
                'location': location,
                'link': link
            })
        if is_empty:
            break
        print(f'scraped page {page_num}')

    with open(OUTPUT_FILE, 'w') as f:
        json.dump(listings, f, indent=2)
        print('all done!')


if __name__ == '__main__':
    scrape_listings()