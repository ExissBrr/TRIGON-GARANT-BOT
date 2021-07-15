from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loguru import logger


def keyboard(links: dict, row_width: int = 2) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width)
    for title, link in links.items():
        markup.insert(InlineKeyboardButton(text=title, url=link))

    return markup
