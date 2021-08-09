import datetime as dt

import pyqiwi
from aiogram.types import CallbackQuery

from app.data import text
from app.data.types.payment_data import PaymentSystemType, PaymentType, PaymentSystemStatus, PaymentStatus, \
    PaymentTransactionId
from app.keyboards.callback_data.payment_system import payment_system_cd
from app.keyboards.default.inline import generator_button_url
from app.loader import dp
from app.utils.db_api.models.payment_systems import PaymentSystem
from app.utils.db_api.models.payments import Payment
from app.utils.payments.qiwi_tools import QiwiWallet


@dp.callback_query_handler(payment_system_cd.filter(system=PaymentSystemType.QIWI, type=PaymentType.IN))
async def send_payment_details_qiwi(call: CallbackQuery, lang_code, user):
    await call.answer(cache_time=20, text='One moment..')
    qiwi_system: PaymentSystem = await PaymentSystem.query.where(PaymentSystem.system == PaymentSystemType.QIWI).where(
        PaymentSystem.status == PaymentSystemStatus.ACTIVE).gino.first()
    qiwi_wallet = QiwiWallet(qiwi_system.token)
    qiwi_account = qiwi_wallet.nickname

    # Платеж из бд
    payment = await (
        Payment.query.where(Payment.transaction_id == PaymentTransactionId.NONE).where(
            Payment.status == PaymentStatus.PENDING).where(Payment.payer_user_id == user.id)).where(
        Payment.create_at + dt.timedelta(hours=2) >= dt.datetime.utcnow()).gino.first()

    # Если платежа нет в бд, то создается новый
    if not payment:
        payment = await Payment.insert(
            type=PaymentType.IN,
            system_id=qiwi_system.id,
            status=PaymentStatus.PENDING,
            payer_user_id=user.id,
            account_in=qiwi_account,
            transaction_id=PaymentTransactionId.NONE,
        )

    payment_link = pyqiwi.generate_form_link(99999, qiwi_account, 100, payment.comment, ['account'], 1)

    await call.message.edit_text(
        text=text[lang_code].default.message.payment_details_qiwi.format(
            qiwi_account=qiwi_account,
            comment=payment.comment,
        ),

        reply_markup=generator_button_url.keyboard(
            {text[lang_code].button.inline.proceed_to_checkout: payment_link}
        )
    )
