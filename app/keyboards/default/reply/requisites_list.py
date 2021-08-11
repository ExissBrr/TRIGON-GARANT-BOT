from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from app.data import text


def keyboard(requisites: list[str], lang_code) -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(KeyboardButton(text[lang_code].button.reply.cancel))
    for requisite in requisites:
        markup.row(KeyboardButton(requisite))
    return markup
