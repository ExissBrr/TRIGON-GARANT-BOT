from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from loguru import logger

from app.data import text
from app.handlers.private.default.message.menu.withdraw_balance._request_data import request_confirm_withdraw_balance
from app.loader import dp
from app.states.private.withdraw_balance import WithdrawBalanceStates
from app.utils.format_data.requisite import format_card_code, format_phone
from app.utils.payments.requisites_tools import is_valid_card, is_valid_phone


@dp.message_handler(state=WithdrawBalanceStates.wait_requisite)
async def wait_requisite(message: Message, state: FSMContext, state_data:dict, lang_code):
    requisite_data_raw = message.text
    if is_valid_card(requisite_data_raw):
        requisite_data = format_card_code(requisite_data_raw)
    elif is_valid_phone(requisite_data_raw):
        requisite_data = format_phone(requisite_data_raw)
    else:
        await message.answer(text[lang_code].default.message.wrong_data)
        return False

    await state.update_data(requisite_data=requisite_data)

    await WithdrawBalanceStates.wait_confirm_withdraw_balance.set()
    await request_confirm_withdraw_balance(message, await state.get_data(), lang_code)

