from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.data import text
from app.data.types.deal_data import DealStatusType
from app.keyboards.callback_data.deal import deal_cd, DealCommands


def keyboard_deal_operate(lang_code, deal_id, deal_status, is_seller=False):
    markup = InlineKeyboardMarkup()
    if is_seller:
        markup.add(
            InlineKeyboardButton(
                text=text[lang_code].button.inline.cancel_deal,
                callback_data=deal_cd.new(deal_id=deal_id, command=DealCommands.CANCEL_DEAL)
            )
        )
    else:
        markup.add(
            InlineKeyboardButton(
                text=text[lang_code].button.inline.pay,
                callback_data=deal_cd.new(deal_id=deal_id, command=DealCommands.PAY_DEAL)

            )
        )
    if deal_status != DealStatusType.CONTROVERSY:
        markup.insert(
            InlineKeyboardButton(
                text=text[lang_code].button.inline.start_controversy,
                callback_data=deal_cd.new(deal_id=deal_id, command=DealCommands.CONTROVERSY_DEAL)
            )
        )
    return markup
