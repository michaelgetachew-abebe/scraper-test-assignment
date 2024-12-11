import requests
from bs4 import BeautifulSoup
import json

target_url = "https://www.walmart.com/ip/Squishmallows-Molded-Lip-Balm-2-Pack-Coconut-Strawberry/574902716"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(target_url, headers=headers, verify=False)
if response.status_code != 200:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

try:
    script_tag = soup.find("script", type="application/ld+json")
    if script_tag:
        product_data = json.loads(script_tag.string)
        print(product_data, "\n")
        product_name = product_data.get("name")
        price = product_data["offers"][0].get("price")
        image = product_data.get("image")

        print(f"Product Name: {product_name}\nProduct Price: {price}\nProduct Image: {image}")
    else:
        print("Product data not found in the script tag.")
except Exception as e:
    print(f"An error occurred while parsing the product details: {e}")