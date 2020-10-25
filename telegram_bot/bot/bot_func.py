from telebot import types


def button_add() -> types.InlineKeyboardMarkup:
    """
    Button builder. Created button and returned them
    :return: types.InlineKeyboardMarkup
    """
    # create keyboard
    keyboard = types.InlineKeyboardMarkup()
    # create button
    button_1 = types.InlineKeyboardButton(text="Другой код", callback_data='button_1')
    keyboard.add(button_1)
    return keyboard