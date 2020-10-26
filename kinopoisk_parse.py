import pickle
from time import sleep
from tqdm import tqdm
import pandas as pd
from bs4 import BeautifulSoup as Soup

from config import headers
from parse_func import get_page


def get_news(html) -> pd.DataFrame:
    bs = Soup(html, 'lxml')
    header = ''
    h1 = bs.find('h1')
    if h1:
        header = h1.find('span').text
    date = bs.find(class_ = 'media-news__published-date').text
    text = bs.find(class_='media-news__body-wrapper').text

    return pd.DataFrame([[date, header, text]], columns=['date', 'head', 'text'])


def get_all_news():
    with open('data/yandex_parse/kinopoisk.pkl', 'rb') as f:
        all_url = pickle.load(f)

    dataset = pd.DataFrame(columns=['head', 'text'])
    for url in tqdm(all_url):
        html = get_page(url, headers)
        data = get_news(html)
        dataset = pd.concat((dataset, data), axis=0, ignore_index=True)
        sleep(1)
    dataset.to_csv('data/kinopoisk_data.csv', index=False)


if __name__ == '__main__':
    get_all_news()
