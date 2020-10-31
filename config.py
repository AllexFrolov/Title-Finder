headers = {'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/86.0.4240.111 Safari/537.36'}


yandex_url = r'https://newssearch.yandex.ru/yandsearch?rpt=nnews2&wiz_no_news=1&wiz_no_news=1&wiz_no_news=1&' \
             'wiz_no_news=1&wiz_no_news=1&wiz_no_news=1&wiz_no_news=1&wiz_no_news=1&wiz_no_news=1&wiz_no_news=1&' \
             'wiz_no_news=1&wiz_no_news=1&wiz_no_news=1&wiz_no_news=1&wiz_no_news=1&wiz_no_news=1&wiz_no_news=1&' \
             'wiz_no_news=1&wiz_no_news=1&wiz_no_news=1&wiz_no_news=1&wiz_no_news=1&wiz_no_news=1&wiz_no_news=1&' \
             'wiz_no_news=1&wiz_no_news=1&showdups=1&within=777&from_day=01&from_month=01&from_year=2018&' \
             'to_day=01&to_month=01&to_year=2020&nsrc='

site_news_tokens = {'kinopoisk': '3840',
                    'lostfilm': '254054253',
                    'medianews': '254162628',
                    'filmz': '7249',
                    'filmru': '1079',
                    'cutinsight': '254147866',
                    'kinonews': '8430',
                    'moviestart': '254096436',
                    'madtosby': '254164883',
                    }

site_forms = {'kinopoisk': {'date': {'class_': 'media-news__published-date'},
                            'header': {'name': 'h1'},
                            'text': {'class_': 'media-news__body-wrapper'}
                            },
              'lostfilm': {'date': {'class_': 'news-date small'},
                           'header': {'class_': 'news-header'},
                           'text': {'class_': 'news-container'}
                           },
              'medianews': {'date': {'class_': 'onDate date published'},
                            'header': {'class_': 'entry-title'},
                            'text': {'class_': 'entry-content'}
                            },
              'filmz': {'date': {'class_': 'tags cent'},
                        'header': {'name': 'h1', 'class_': 'cent'},
                        'text': {'name': 'div', 'class_': 'text'}
                        },
              'filmru': {'date': {'name': 'div', 'class_': 'author'},
                         'header': {'name': 'h1', 'itemprop': 'headline'},
                         'text': {'name': 'div', 'class_': 'text'}
                         },
              }

driver_path = 'C:/Users/svetl/.local/bin/chromedriver.exe'
