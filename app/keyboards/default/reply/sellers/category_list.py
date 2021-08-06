from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from app.data import text
from app.data.types.category_data import ServiceCategoryType


def make_keyboard_scam_category_list(lang_code):
    markup = ReplyKeyboardMarkup()
    markup.row(
        KeyboardButton(
            text=text[lang_code].button.reply.cancel
        )
    )
    for category_name, category in ServiceCategoryType.__dict__.items():
        if category_name in ['__dict__', '__weakref__', '__doc__', '__module__']:
            continue
        markup.row(
            KeyboardButton(
                text=category
            )
        )

    return markup
