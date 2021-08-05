from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.data import text
from app.keyboards.callback_data.deal import deal_cd, DealCommands


def keyboard_feedback(deal_id, is_buyer, lang_code):
    markup = InlineKeyboardMarkup()
    if is_buyer:
        markup.add(
            InlineKeyboardButton(
                text=text[lang_code].button.inline.left_feedback,
                callback_data=deal_cd.new(deal_id=deal_id, command=DealCommands.LEFT_FEEDBACK)
            )
        )
    return markup
