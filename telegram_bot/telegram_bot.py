from telebot import TeleBot

from .config import token, alex_id
from .bot.bot_func import button_add


class TelegramBot:
    def __init__(self):
        self.user_id = alex_id
        self.bot = TeleBot(token)
        self.answer = None

        @self.bot.message_handler()
        def company_receiving(message):
            self.bot.send_message(message.from_user.id, 'Ответ принят')
            self.bot.stop_polling()
            self.answer = message.text

        @self.bot.callback_query_handler(lambda query: query.data == 'button_1')
        def process_callback(query):
            self.bot.stop_polling()
            self.answer = 'new_captcha'

    def send_photo(self, img: bytes):
        keyboard = button_add()
        self.answer = ''
        self.bot.send_photo(self.user_id, photo=img, reply_markup=keyboard)
        self.bot.polling()


if __name__ == '__main__':
    telegram_bot = TelegramBot()
    with open('screen.png', 'rb') as f:
        img = f.read()
    telegram_bot.send_message(img)
