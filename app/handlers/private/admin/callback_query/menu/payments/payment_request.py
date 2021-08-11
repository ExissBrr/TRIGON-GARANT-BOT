from aiogram.types import CallbackQuery

from app import keyboards
from app.data import text
from app.data.types.payment_data import PaymentType, PaymentStatus
from app.keyboards.callback_data.admin import admin_menu_cd, AdminMenuChoice
from app.loader import dp
from app.utils.db_api.models.payments import Payment


@dp.callback_query_handler(admin_menu_cd.filter(command=AdminMenuChoice.PAYMENTS))
async def show_requested_payments(call: CallbackQuery, lang_code):
    await call.answer(cache_time=5)
    requested_payments = await Payment.query.where(Payment.type == PaymentType.OUT).where(
        Payment.status == PaymentStatus.PENDING).gino.all()

    if not requested_payments:
        await call.message.answer(
            text=text[lang_code].default.message.not_withdraw_requests
        )
        return False
    await call.message.answer(
        text=text[lang_code].default.message.withdraw_requests_by_now,
        reply_markup=await keyboards.admin.inline.payments.requested_payments_list.make_keyboard_payment_list(
            requested_payments)
    )
