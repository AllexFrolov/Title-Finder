import time
from importlib import reload

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import config
import telegram_bot
from telegram_bot.tele_config import token, user_id

telegram_bot = reload(telegram_bot)
from telegram_bot.telegram_bot import TelegramBot


class SiteBot(object):
    def __init__(self, driver_path, base_url, telegram_bot):
        self._path = driver_path
        self.site_link = base_url
        self.telegram_bot = telegram_bot

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--window-size=1920x1080')

        self._driver = webdriver.Chrome(executable_path=self._path, options=chrome_options)
        self._driver.wait = WebDriverWait(self._driver, 5)

    def go_to_the_page(self, page_number: int = 0):
        self._driver.get(self.site_link + str(page_number))
        time.sleep(2)
        self.capcha_check()

    def capcha_check(self):
        while True:
            try:
                capcha_box = self._driver.wait.until(EC.presence_of_element_located((By.NAME, 'rep')))
                button = self._driver.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'submit')))
                update_button = self._driver.wait.until(
                    EC.presence_of_element_located(
                        (By.CLASS_NAME, 'actions__button-image')
                    )
                )
                img = self._driver.find_element_by_class_name("captcha__image")
                self.telegram_bot.send_photo(img.screenshot_as_png)
                if self.telegram_bot.answer != 'new_captcha':
                    capcha_box.send_keys(self.telegram_bot.answer)
                    time.sleep(1)
                    button.click()
                else:
                    update_button.click()
            except TimeoutException:
                break

    def get_order_page(self, page_number: int = 0):
        self.go_to_the_page(page_number)
        html = self._driver.page_source
        return html


if __name__ == '__main__':
    tel_bot = TelegramBot(token, user_id)
    driver = SiteBot(config.driver_path, config.yandex_url, tel_bot)
    page = 0
    while True:
        print(page)
        html = driver.get_order_page(page)
        page += 1
