from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from app.data import text


def keyboard(lang_code):
    markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(
                    text=text[lang_code].default.button.reply.proceed
                )
            ]
        ]
    )
    return markup
