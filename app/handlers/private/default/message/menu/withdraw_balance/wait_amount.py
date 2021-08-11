from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app import dp
from app.data import text
from app.handlers.private.default.message.menu.withdraw_balance._request_data import request_requisite
from app.states.private.withdraw_balance import WithdrawBalanceStates


@dp.message_handler(state=WithdrawBalanceStates.wait_amount)
async def wait_amount(message: Message, state: FSMContext, user, lang_code):
    amount = message.text

    if not amount.isdigit() or int(amount) <= 0:
        await message.answer(text[lang_code].default.message.wrong_data)
        return False

    amount = int(amount)

    if amount > user.balance:
        await message.answer(text[lang_code].default.message.not_enough_money)
        return False

    await state.update_data(amount=amount)

    await WithdrawBalanceStates.wait_requisite.set()
    await request_requisite(message, user, lang_code)
