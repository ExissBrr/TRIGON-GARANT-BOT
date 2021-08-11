from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from app import keyboards
from app.data import text
from app.data.types.payment_data import PaymentType
from app.keyboards.callback_data.payment_system import payment_system_cd
from app.loader import dp
from app.states.private.withdraw_balance import WithdrawBalanceStates


@dp.callback_query_handler(payment_system_cd.filter(type=PaymentType.OUT))
async def request_amount_withdraw_balance(call: CallbackQuery, state: FSMContext, callback_data, lang_code):
    await state.update_data(payment_system=callback_data.get('system'))
    await call.answer(cache_time=5,text='One moment..')
    await call.message.answer(
        text=text[lang_code].default.message.request_amount_withdraw,
        reply_markup=keyboards.default.reply.cancel.keyboard(lang_code)
    )
    await WithdrawBalanceStates.wait_amount.set()
