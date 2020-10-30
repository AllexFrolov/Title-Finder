from typing import Optional

import requests


def get_page(url: str,
             useragent: Optional[dict] = None,
             proxy: Optional[dict] = None,
             encoding: Optional[str] = None) -> str:
    page = requests.get(url, headers=useragent, proxies=proxy)
    if encoding:
        page.encoding = encoding
    if page.status_code != requests.codes.ok:
        print(f'{page.status_code}, Bad link {url}')
    return page.text
