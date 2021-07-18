from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from app.data import text


def keyboard(lang_code):
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(
                    text=text[lang_code].button.reply.confirm
                ),
                KeyboardButton(
                    text=text[lang_code].button.reply.cancel
                )
            ]
        ]
    )
    return keyboard
