from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from app.data import text


def keyboard(lang_code):
    markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text=text[lang_code].button.reply.request_seller_creation),
                KeyboardButton(text=text[lang_code].button.reply.cancel)
            ]
        ]
    )
    return markup
