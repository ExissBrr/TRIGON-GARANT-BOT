from aiogram.types import CallbackQuery

from app.data import text
from app.data.types.payment_data import PaymentStatus
from app.keyboards.callback_data.transaction import transaction_cd, TransactionCommands
from app.loader import dp
from app.utils.db_api.models.payments import Payment


@dp.callback_query_handler(transaction_cd.filter(command=TransactionCommands.APPROVE_PAYMENT))
async def approve_payment(call: CallbackQuery, callback_data: dict, lang_code):
    await call.answer(cache_time=5)
    payment_comment = callback_data.get('comment')
    payment = await Payment.query.where(Payment.comment == payment_comment).where(
        Payment.status == PaymentStatus.PENDING).gino.first()
    if not payment:
        await call.message.answer(
            text=text[lang_code].default.call.payment_request_already_processed
        )
        return False
    await payment.update_data(status=PaymentStatus.SUCCESS)
    await call.message.edit_text(
        text=text[lang_code].admin.message.application_approved
    )


@dp.callback_query_handler(transaction_cd.filter(command=TransactionCommands.ABOLISH_PAYMENT))
async def approve_payment(call: CallbackQuery, callback_data: dict, lang_code):
    await call.answer(cache_time=5)
    payment_comment = callback_data.get('comment')
    payment = await Payment.query.where(Payment.comment == payment_comment).where(
        Payment.status == PaymentStatus.PENDING).gino.first()
    if not payment:
        await call.message.answer(
            text=text[lang_code].default.call.payment_request_already_processed
        )
        return False
    await call.message.edit_text(
        text=text[lang_code].admin.message.application_declined
    )
    await payment.delete()
