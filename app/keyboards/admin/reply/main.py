from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from app.data import text


def keyboard(lang_code) -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text[lang_code].button.reply.search_users),
                KeyboardButton(text[lang_code].button.reply.message_sending)
            ],
            [
                KeyboardButton(text[lang_code].button.reply.profile)
            ]
        ]
    )
    return markup
