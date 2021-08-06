from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.data import text
from app.keyboards.callback_data.sellers import sellers_cd, CommandsSellers


def make_keyboard_seller_requests(lang_code):
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(
            text=text[lang_code].button.inline.categories,
            switch_inline_query_current_chat='выберите категорию..'
        ),
        InlineKeyboardButton(
            text=text[lang_code].button.inline.request_seller_creation,
            callback_data=sellers_cd.new(seller_id=0, category=0, command=CommandsSellers.become_seller)
        )
    )

    return markup
