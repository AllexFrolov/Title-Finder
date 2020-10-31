# Title Finder
Добро пожаловать в небольшой пайплайн по анализу популярности кинотайтлов.

__Задача:__ Из новостных текстов вынимать количество упоминаний предопределенного 
списка именованных сущностей, в моём случае [Названий фильмов](data/titles.csv).
И на их основе сделать выводы.
 
 В качествсе базы данных был выбран сайт [Yandex.news](https://yandex.ru/news/smi) 
 где можно задать дату и тему новостей и выбрать сайты. 
 
 В итоге для задачи были выбраны Kinopoisk, LostFilm, Media-news, Kinoz, Kino.ru 
 и временной период с 01.01.2018 года по 01.01.2020 года.<br>
 Для парсинга ссылок с [Yandex.news](https://yandex.ru/news/smi) было принято решение 
 использовать SiteBot-а основанного на библиотеке Selenium. Для обхода капчи был использован 
 Telegram бот, который присылал капчу кожанному мешку (мне) и принимал мой ответ, а уже SiteBot 
 вводил ответ в поле и жал кнопку.
 
 Для парсинга новосных сайтов была использована библиотека Request и BeautifulSoup.
 ## Requirements
 1. Для работы Selenium необходимо скачать [chrome driver](https://chromedriver.chromium.org/) 
 и в файле [config.py](config.py) записать в переменную _driver_path_ путь к файлу. 
 2. Для работы Telegram бота нужно указать в файле [telegram_bot/tele_config.py](telegram_bot/tele_config.py) 
 _token_ который создает 
 [BotFather](https://telegram.me/BotFather#:~:text=BotFather%20is%20the%20one%20bot,and%20manage%20your%20existing%20bots.&text=BotFather%20right%20away.)
  а так же [User_id](https://telegram.me/userinfobot)
 3. Ну и естественно  ``` pip install -r requirements.txt```