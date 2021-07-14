from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from app.loader import config
from app.utils.format_data.user import format_lang_code


def keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for lang in config.bot.languages:
        markup.insert(
            KeyboardButton(format_lang_code(lang))
        )
    return markup
