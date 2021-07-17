from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from app.data import text


def make_keyboard(lang_code):
    markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text[lang_code].default.button.reply.cancel)
            ],
            [
                KeyboardButton(text[lang_code].admin.button.reply.distribution_settings),
                KeyboardButton(text[lang_code].admin.button.reply.send_messages)
            ]
        ]
    )
    return markup
