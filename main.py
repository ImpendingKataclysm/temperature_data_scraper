import requests
import selectorlib
from headers import HEADERS

URL = "https://programmer100.pythonanywhere.com/"
temp_file = "temp_data.txt"


def scrape(url):
    """ Scrape page source from URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


if __name__ == "__main__":
    print(scrape(URL))
