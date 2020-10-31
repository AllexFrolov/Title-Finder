import pickle
from typing import List
from random import uniform
from time import sleep
from bs4 import BeautifulSoup as Soup

import config
import SiteBot
from importlib import reload
import telegram_bot.telegram_bot
SiteBot = reload(SiteBot)
telegram_bot.telegram_bot = reload(telegram_bot.telegram_bot)
from SiteBot import SiteBot

from telegram_bot.telegram_bot import TelegramBot
from telegram_bot.tele_config import token, user_id


def parse_links(html: str) -> List[str]:
    """
    Find links
    :param html: html text
    :return: list with links
    """
    bs = Soup(html, 'lxml')
    site_links = []
    for order in bs.find_all(class_='document__title'):
        site_links.append(order.find('a').get('href'))
    return site_links


def get_all_links(site: str, start_page: int = 0):
    """
    parse all links starting with start_page until there are no links left
    :param site: site name. Example: 'kinopoisk', 'lostfilm'
    :param start_page: page number to start parsing. Default: 0
    :return: NoneType
    """
    # Create telegram bot to send captcha
    tel_bot = TelegramBot(token, user_id)
    # get site token
    site_token = config.site_news_tokens.get(site, False)
    site_base_url = config.yandex_url
    if site_token:
        site_base_url += site_token + '&p='
    else:
        raise ValueError(f'site should be in {list(config.site_news_tokens.keys())}')

    driver = SiteBot(config.driver_path, tel_bot)

    links = []
    while True:
        print(start_page)
        sleep(uniform(2, 5))
        html = driver.get_order_page(site_base_url + str(start_page))

        site_links = parse_links(html)

        if len(site_links) > 0 and len(set(site_links) & set(links)) <= 12:
            links += site_links
            start_page += 1
        else:
            break

    with open(f'data/yandex_parse/{site}.pkl', 'wb') as f:
        pickle.dump(list(set(links)), f)


if __name__ == '__main__':
    get_all_links('filmz', 0)
