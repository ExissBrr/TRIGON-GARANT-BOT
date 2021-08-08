from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.data import text
from app.keyboards.callback_data.admin import admin_menu_cd, SellerMenuChoice


def make_keyboard_seller_menu(lang_code):
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(
            text=text[lang_code].button.inline.menu_seller_requests,
            callback_data=admin_menu_cd.new(command=SellerMenuChoice.SHOW_SELLER_REQUESTS)
        ),
        InlineKeyboardButton(
            text=text[lang_code].button.inline.seller_search,
            callback_data=admin_menu_cd.new(command=SellerMenuChoice.SEARCH_SELLER)
        )
    )
    return markup
