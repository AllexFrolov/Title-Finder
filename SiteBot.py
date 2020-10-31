import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SiteBot(object):
    """
    Selenium bot for Yandex.
    Loaded site, send the captcha to telegram, then send answer to the site
    """

    def __init__(self, driver_path, telegram_bot):
        """
        Open chrom browser with headless options
        :param driver_path: path to chromedriver.exe file
        :param telegram_bot: TelegramBot
        """
        self._path = driver_path
        self.telegram_bot = telegram_bot

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--window-size=1920x1080')

        self._driver = webdriver.Chrome(executable_path=self._path, options=chrome_options)
        self._driver.wait = WebDriverWait(self._driver, 5)

    def capcha_check(self):
        """
        try to find the captcha box and submit button.
        If finds it sends the photo to the telegram.
        """
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

    def get_order_page(self, url: str):
        """
        Upload site check captcha and return HTML code

        :param url: site url
        :return: HTML code
        """
        self._driver.get(url)
        time.sleep(2)
        self.capcha_check()
        html = self._driver.page_source
        return html
