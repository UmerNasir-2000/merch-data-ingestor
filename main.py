import json
from typing import List
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

from item import Item

def main() -> None:
    url = "https://www.wrestlingstore.pk/products/wwe-t-shirts.phps"
    soup = BeautifulSoup(get_html(url), "html.parser")
    
    item_boxes = soup.find_all("div", class_="item-box")
    items: List[Item] = [extract_item_data(item_box) for item_box in item_boxes]
    
    json_str = json.dumps([item.__dict__ for item in items], indent=4)
    with open("items.json", "w") as f:
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
