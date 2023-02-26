import requests
import selectorlib
from datetime import datetime
from headers import HEADERS

URL = "https://programmer100.pythonanywhere.com/"
temp_file = "temp_data.txt"


def scrape(url):
    """ Scrape page source from URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["home"]
    return value


def get_time():
    now = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    return now


def store(current_time, extracted_data):
    with open(temp_file, "a") as file:
        file.write(f"{current_time},{extracted_data}" + "\n")


if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    timestamp = get_time()
    store(timestamp, extracted)

