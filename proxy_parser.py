from bs4 import BeautifulSoup as Soup

from config import proxies_url
from parse_func import get_page


def parse_proxies(html: str) -> list:
    bs = Soup(html, 'lxml')
    proxies = []
    for row in bs.find_all('tr')[1:]:
        items = row.find_all('td')
        proxies.append(items[5].text.strip().lower() + '://'
                       + items[1].text + ':' + items[2].text)
    return proxies


def main():
    url = proxies_url
    html = get_page(url)
    return parse_proxies(html)


if __name__ == '__main__':
    main()
