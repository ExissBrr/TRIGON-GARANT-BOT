from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.data import text
from app.keyboards.callback_data.sellers import sellers_cd, CommandsSellers


def make_keyboard_seller_request_decision(seller_id: int, category: str, lang_code):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=text[lang_code].button.inline.approve_seller,
                    callback_data=sellers_cd.new(seller_id=seller_id, category=category,
                                                 command=CommandsSellers.confirm_seller)
                ),
                InlineKeyboardButton(
                    text=text[lang_code].button.inline.decline_seller,
                    callback_data=sellers_cd.new(seller_id=seller_id, category=category,
                                                 command=CommandsSellers.abolish_seller)
                )
            ]
        ]
    )
    return keyboard
