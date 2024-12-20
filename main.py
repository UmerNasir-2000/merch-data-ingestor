import requests
from requests.exceptions import RequestException

def main() -> None:
    url = "https://www.wrestlingstore.pk/products/wwe-t-shirts.phps"
    print(get_html(url))
    

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
