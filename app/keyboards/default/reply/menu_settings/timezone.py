from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from app.data import text


def keyboard(lang_code: str):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(KeyboardButton(text[lang_code].default.button.reply.cancel))
    for gmt in range(12, 0, -1):
        markup.row(KeyboardButton(f'+{gmt}'))
    markup.row(KeyboardButton('0'))
    for gmt in range(-1, -13, -1):
        markup.row(KeyboardButton(f'{gmt}'))
    return markup
