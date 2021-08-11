from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.data import text
from app.data.text.ru.button.reply import confirm
from app.data.types.payment_data import PaymentType, PaymentStatus
from app.loader import dp
from app.states.private.withdraw_balance import WithdrawBalanceStates
from app.utils.bot import send_main_keyboard
from app.utils.db_api.models.payments import Payment
from app.utils.format_data.time import timezone


@dp.message_handler(state=WithdrawBalanceStates.wait_confirm_withdraw_balance, reply_command=confirm)
async def add_payment_out(message: Message, state: FSMContext, state_data: dict, user, lang_code):
    amount = state_data.get('amount')
    requisite_data = state_data.get('requisite_data')
    payment_system = state_data.get('payment_system')
    await send_main_keyboard(user, state)
    if user.balance < amount:
        await message.answer(text[lang_code].default.message.not_enough_money)
        return False

    await user.update_data(balance=user.balance - amount)

    payment = await Payment.insert(
        type=PaymentType.OUT,
        status=PaymentStatus.PENDING,
        system=payment_system,
        commission_amount=0,
        amount=amount,
        payer_user_id=user.id,
        account_in=requisite_data,
    )
    await message.answer(
        text=text[lang_code].default.message.success_create_payment_out.format(
            payment_id=payment.id,
            payment_create_at=timezone(payment.create_at, user.timezone).strftime('%Y-%m-%d %H:%M'),
            user_id=payment.payer_user_id,
            payment_system=payment_system,
            requisite_data=payment.account_in,
            total_amount=payment.amount - payment.commission_amount,
        )
    )
