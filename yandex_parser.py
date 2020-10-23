from typing import Tuple

from bs4 import BeautifulSoup as Soup


def parse_links(html: str) -> Tuple[list, list]:
    bs = Soup(html, 'lxml')
    site_links = []
    for order in bs.find_all(class_='document__title'):
        site_links.append(order.find('a').get('href'))

    pages = bs.find(class_='pager__group')
    page_links = []
    for page in pages.find_all('a')[1:]:
        page_links.append(page.get('href'))
    return site_links, page_links


if __name__ == '__main__':
    pass
