from typing import Optional

import requests


def get_page(url: str,
             useragent: Optional[dict] = None,
             proxy: Optional[dict] = None,
             encoding: Optional[str] = None) -> str:
    page = requests.get(url, headers=useragent, proxies=proxy)
    if encoding:
        page.encoding = encoding
    page.raise_for_status()
    return page.text
