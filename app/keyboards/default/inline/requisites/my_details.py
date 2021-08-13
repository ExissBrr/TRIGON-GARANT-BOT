from typing import List

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from app.data import text


def make_keyboard(details: List[str],lang_code) -> ReplyKeyboardMarkup:
    """Формирует и возвращает клавиатуру с сохраненными реквизитами"""
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(KeyboardButton(text=text[lang_code].button.reply.cancel))
    for detail in details:
        markup.row(
            KeyboardButton(text=f'{detail}')
        )
    return markup