from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def keyboard(links: dict, row_width: int = 2) -> InlineKeyboardMarkup:
    """Возвращает inline клавиатуру c ссылками"""
    markup = InlineKeyboardMarkup(row_width)
    for title, link in links.items():
        markup.insert(InlineKeyboardButton(text=title, url=link))

    return markup

