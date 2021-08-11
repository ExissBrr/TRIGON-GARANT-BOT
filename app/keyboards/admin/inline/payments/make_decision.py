from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.data import text
from app.keyboards.callback_data.transaction import transaction_cd, TransactionCommands


def make_keyboard_payment_decision(comment: str, lang_code):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=text[lang_code].button.inline.approve_seller,
                    callback_data=transaction_cd.new(comment=comment, command=TransactionCommands.APPROVE_PAYMENT)
                ),
                InlineKeyboardButton(
                    text=text[lang_code].button.inline.decline_seller,
                    callback_data=transaction_cd.new(comment=comment, command=TransactionCommands.ABOLISH_PAYMENT)
                )
            ]
        ]
    )
    return keyboard
