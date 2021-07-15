from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from app.data import text


def keyboard(lang_code) -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text[lang_code].default.button.reply.profile)
            ],
            [
                KeyboardButton(text[lang_code].admin.button.reply.message_sending)
            ]
        ]
    )
    return markup
