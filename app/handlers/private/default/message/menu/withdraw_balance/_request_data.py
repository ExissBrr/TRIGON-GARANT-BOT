from aiogram.types import Message

from app import keyboards
from app.data import text
from app.utils.db_api.models.user import User


async def request_requisite(message: Message, user: User, lang_code):
    user_requisites = user.requisites.rstrip().split()
    await message.answer(
        text=text[lang_code].default.message.request_requisite,
        reply_markup=keyboards.default.reply.requisites_list.keyboard(user_requisites, lang_code)
    )


async def request_confirm_withdraw_balance(message: Message, state_data: dict, lang_code):
    await message.answer(
        text=text[lang_code].default.message.confirm_withdraw_balance.format(
            requisite_data=state_data.get('requisite_data'),
            payment_system=state_data.get('payment_system'),
            amount=state_data.get('amount')
        ),
        reply_markup=keyboards.default.reply.confirm_cancel.keyboard(lang_code)
    )
