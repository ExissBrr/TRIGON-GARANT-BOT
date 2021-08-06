from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.data import text
from app.keyboards.callback_data.deal import deal_cd, DealAdminCommands


def make_keyboard_controversies_admin(deal_id, lang_code):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=text[lang_code].button.inline.on_sellers_side,
                    callback_data=deal_cd.new(deal_id=deal_id, command=DealAdminCommands.ON_SELLERS_SIDE)
                )
            ],
            [
                InlineKeyboardButton(
                    text=text[lang_code].button.inline.on_buyers_side,
                    callback_data=deal_cd.new(deal_id=deal_id, command=DealAdminCommands.ON_BUYERS_SIDE)
                )
            ],
            [
                InlineKeyboardButton(
                    text=text[lang_code].button.inline.percent_division,
                    callback_data=deal_cd.new(deal_id=deal_id, command=DealAdminCommands.PERCENT_DIVISION)
                )
            ]
        ]
    )
    return keyboard
