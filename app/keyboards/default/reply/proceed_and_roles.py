from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from app.data import text


def keyboard(roles: list[str], lang_code):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.row(KeyboardButton(text[lang_code].button.reply.cancel))
    markup.row(KeyboardButton(text[lang_code].button.reply.proceed))
    for role in roles:
        markup.row(KeyboardButton(role))
    return markup
