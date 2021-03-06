from typing import List

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Chat

from app.data import text


def keyboard(chats: List[Chat], lang_code, can_continue=True):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.row(KeyboardButton(text[lang_code].button.reply.cancel))
    if can_continue:
        markup.row(KeyboardButton(text[lang_code].button.reply.proceed))

    for chat in chats:
        title = chat.title
        id = chat.id
        markup.row(KeyboardButton(f'{id} {title}'))
    return markup
