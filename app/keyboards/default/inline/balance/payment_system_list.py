from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.keyboards.callback_data.payment_system import payment_system_cd


def keyboard(payment_type, payment_system_list, lang_code):
    markup = InlineKeyboardMarkup(row_width=1)
    for payment_system in payment_system_list:
        markup.row(
            InlineKeyboardButton(
                text=payment_system.title,
                callback_data=payment_system_cd.new(system=payment_system.system, type=payment_type)
            )
        )
    return markup
