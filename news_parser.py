import pickle
from importlib import reload
from time import sleep

import pandas as pd
from bs4 import BeautifulSoup as Soup
from tqdm import tqdm

import config
import parse_func

parse_func = reload(parse_func)
config = reload(config)
from config import headers
from parse_func import get_page


def get_news(html, site: str) -> pd.DataFrame:
    """
    Finding header, text and date news
    :param html: html code of site
    :param site: site name. Example 'kinopoisk', 'lostfilm'
    :return: DataFrame consist of date, head, text
    """
    bs = Soup(html, 'lxml')
    header = config.site_forms[site].get('header', '')
    date = config.site_forms[site].get('date', '')
    text = config.site_forms[site].get('text', '')
    # find header
    try:
        if header:
            header = bs.find(**header).text
        if date:
            date = bs.find(**date).text
        if text:
            text = bs.find(**text).text
    except Exception as e:
        print(e)
        header = None
        date = None
        text = None

    return pd.DataFrame([[date, header, text]], columns=['date', 'head', 'text'])


def get_all_news(site: str):
    """
    parse all news from the site and write in the csv file.
    :param site: site name. Example 'kinopoisk', 'lostfilm'
    :return: NoneType
    """
    with open(f'data/yandex_parse/{site}.pkl', 'rb') as f:
        all_url = pickle.load(f)
    dataset = pd.DataFrame(columns=['head', 'text'])
    for url in tqdm(set(all_url)):
        html = get_page(url, headers)
        data = get_news(html, site)
        dataset = pd.concat((dataset, data), axis=0, ignore_index=True)
        sleep(1)
    dataset.to_csv(f'data/{site}_data.csv', index=False)


if __name__ == '__main__':
    get_all_news('filmru')
