import json
from typing import List
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

from item import Item

def main() -> None:
    url = "https://www.wrestlingstore.pk/products/wwe-t-shirts/"

    items = fetch_items(url)
    save_items_to_json(items, "items.json")

def fetch_items(base_url: str) -> List[Item]:
    page = 1
    items: List[Item] = []

    while True:
        url = f"{base_url}/{page}"
        html = get_html(url)
        if not html:
            break

        print(f"Fetching page {page}...")

        soup = BeautifulSoup(html, "html.parser")
        item_boxes = soup.find_all("div", class_="item-box")
        if not item_boxes:
            break

        items.extend([extract_item_data(item_box) for item_box in item_boxes])
        page += 1

    return items

def save_items_to_json(items: List[Item], filename: str) -> None:
    json_str = json.dumps([item.__dict__ for item in items], indent=4)
    with open(filename, "w") as f:
        f.write(json_str)    

def extract_item_data(item_box) -> Item:
    title = item_box.find("div", class_="item-txt-cnt").find("a").text
    price = item_box.find("div", class_="item-price").text
    image = item_box.find("img")["src"]
    link = item_box.find("a")["href"]
    discount = item_box.find("div", class_="item-discount").text
    return Item(title, price, image, link, discount.strip())

def get_html(url: str) -> str:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except RequestException as e:
        print(f"Error fetching {url}: {e}")
        return ""

if __name__ == "__main__":
    main()
