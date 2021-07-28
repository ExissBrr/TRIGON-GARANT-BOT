from typing import Union

from aiogram.types import Message


def format_text_screening_html(text: Union[str, Message]):
    """Экранирует HTML разметку"""
    if isinstance(text, Message):
        text = text.text

    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')

    return text