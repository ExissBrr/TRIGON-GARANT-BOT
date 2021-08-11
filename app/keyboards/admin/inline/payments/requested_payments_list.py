from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.keyboards.callback_data.transaction import transaction_cd, TransactionCommands
from app.utils.db_api.models.user import User
from app.utils.format_data.user import format_username


async def make_keyboard_payment_list(payments: list):
    markup = InlineKeyboardMarkup()
    for payment in payments:
        user = await User.get(payment.payer_user_id)
        markup.row(
            InlineKeyboardButton(
                text=f'{format_username(user)} {payment.amount}₽',
                callback_data=transaction_cd.new(comment=payment.comment, command=TransactionCommands.SHOW_PAYMENT_INFO)
            )
        )
    return markup
