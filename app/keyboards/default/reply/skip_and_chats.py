from typing import List

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Chat

from app.data import text


def keyboard(chats: List[Chat], lang_code):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.row(KeyboardButton(text[lang_code].default.button.reply.cancel))
    markup.row(KeyboardButton(text[lang_code].default.button.reply.skip))
    for chat in chats:
        title = chat.title
        id = chat.id
        markup.row(KeyboardButton(f'{id} {title}'))
    return markup