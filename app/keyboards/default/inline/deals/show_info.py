from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.data import text
from app.keyboards.callback_data.deal import deal_cd, DealCommands


def keyboard_show_deal_info(deal_id, lang_code):
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(
            text=text[lang_code].button.inline.deal_details,
            callback_data=deal_cd.new(deal_id=deal_id, command=DealCommands.SHOW_DEAL_INFO)
        )
    )
    return markup
