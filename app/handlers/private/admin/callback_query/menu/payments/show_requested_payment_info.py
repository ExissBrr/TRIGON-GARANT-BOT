from aiogram.types import CallbackQuery

from app import keyboards
from app.data import text
from app.data.types.payment_data import PaymentStatus, PaymentType
from app.keyboards.callback_data.transaction import transaction_cd, TransactionCommands
from app.loader import dp
from app.utils.db_api.models.payments import Payment
from app.utils.db_api.models.user import User


@dp.callback_query_handler(transaction_cd.filter(command=TransactionCommands.SHOW_PAYMENT_INFO))
async def show_info(call: CallbackQuery, callback_data: dict, lang_code):
    await call.answer(cache_time=5)
    payment_comment = callback_data.get('comment')
    payment = await Payment.query. \
        where(Payment.comment == payment_comment). \
        where(Payment.status == PaymentStatus.PENDING). \
        where(Payment.type == PaymentType.OUT).gino.first()
    if not payment:
        await call.message.answer(
            text=text[lang_code].default.call.payment_request_already_processed
        )
        return False
    payer_user: User = await User.get(int(payment.payer_user_id))
    await call.message.answer(
        text=text[lang_code].admin.message.payment_info.format(
            details=payment.account_in,
            amount=payment.amount,
            commission_amount=payment.commission_amount,
            total_amount=payment.amount - payment.commission_amount,
            user_link=payer_user.url_to_telegram,
        ),
        reply_markup=keyboards.admin.inline.payments.make_decision.make_keyboard_payment_decision(payment_comment,
                                                                                                  lang_code)
    )
