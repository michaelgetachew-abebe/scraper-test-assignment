import requests
from bs4 import BeautifulSoup
import json

class Scraper:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
        }

    def scrape_by_url(self, url):
        response = requests.get(url, headers=self.headers, verify=False)
        if response.status_code != 200:
            print(f"Failed to fetch the webpage. Status code: {response.status_code}")
            return None

        soup = BeautifulSoup(response.text, "html.parser")
        return self.parse_product_data(soup)

    def scrape_by_category(self, category_url):
        pass

    def parse_product_data(self, soup):
        try:
            script_tag = soup.find("script", type="application/ld+json")
            if script_tag:
                product_data = json.loads(script_tag.string)
                product_name = product_data.get("name")
                price = product_data["offers"][0].get("price")
                image = product_data.get("image")

                return {
                    "Product Name": product_name,
                    "Product Price": price,
                    "Product Image": image
                }
            else:
                print("Product data not found in the script tag.")
                return None
        except Exception as e:
            print(f"An error occurred while parsing the product details: {e}")
            return None