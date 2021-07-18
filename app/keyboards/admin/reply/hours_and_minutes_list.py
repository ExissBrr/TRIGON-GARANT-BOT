from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loguru import logger

from app.data import text


def keyboard(lang_code):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.row(KeyboardButton(text[lang_code].button.reply.cancel))
    for hour in range(12, 24):
        for minute in range(0, 60, 5):
            markup.row(KeyboardButton(f'{hour:02d}:{minute:02d}'))

    for hour in range(0, 12):
        for minute in range(0, 60, 5):
            markup.row(KeyboardButton(f'{hour:02d}:{minute:02d}'))

    return markup
