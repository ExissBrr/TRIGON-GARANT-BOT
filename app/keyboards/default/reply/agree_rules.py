from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from app.data import text


def keyboard(user_lang: str) -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.insert(KeyboardButton(text=text[user_lang].button.reply.agree_rules))
    return markup
