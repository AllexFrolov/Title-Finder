from telebot import TeleBot

from .bot.bot_func import button_add


class TelegramBot:
    def __init__(self, token: str, user_id: str):
        self.user_id = user_id
        self.bot = TeleBot(token)
        # current answer from bot.
        # Can be '' or 'new_captcha'
        self.answer = None

        @self.bot.message_handler()
        def company_receiving(message):
            self.bot.send_message(message.from_user.id, 'Received')
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
