from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from app.data import text


def make_keyboard_confirmation(lang_code):
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(
                    text=text[lang_code].default.button.reply.confirm
                ),
                KeyboardButton(
                    text=text[lang_code].default.button.reply.cancel
                )
            ]
        ]
    )
    return keyboard
