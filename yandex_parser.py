import pickle
from random import uniform
from time import sleep
from bs4 import BeautifulSoup as Soup

import config
import SiteBot
from importlib import reload
SiteBot = reload(SiteBot)
from SiteBot import SiteBot
from telegram_bot.telegram_bot import TelegramBot

def parse_links(html: str) -> list:
    bs = Soup(html, 'lxml')
    site_links = []
    for order in bs.find_all(class_='document__title'):
        site_links.append(order.find('a').get('href'))
    return site_links


def get_all_links(page: int):
    links = []
    tel_bot = TelegramBot()
    driver = SiteBot(config.driver_path, config.yandex_url, tel_bot)

    while True:
        print(page)
        sleep(uniform(2, 5))
        html = driver.get_order_page(page)

        site_links = parse_links(html)
        print(len(site_links))
        if len(site_links) > 0:
            links += site_links
            page += 1
        else:
            break

    with open('data/yandex_parse/kinopoisk.pkl', 'wb') as f:
        pickle.dump(links, f)


if __name__ == '__main__':
    get_all_links(0)
    with open('data/yandex_parse/kinopoisk.pkl', 'rb') as f:
        links = pickle.load(f)
    print(links)
