import requests
from bs4 import BeautifulSoup
from time import sleep

def get_url():
    for count in range(1,8):
        
        url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'

        response = requests.get(url)

        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find_all("div",class_="w-full rounded border")

        for i in data:
            card_url = 'https://scrapingclub.com' + i.find("a").get("href")
            yield card_url

def make_array():
    for card_url in get_url():
        sleep(1)
        response = requests.get(card_url)
        soup = BeautifulSoup(response.text, "lxml")
        name = soup.find(class_ = 'card-title').text
        price = soup.find(class_ = 'my-4 card-price').text
        description = soup.find(class_ = "card-description").text
        array = [name,price,description]
        yield array





