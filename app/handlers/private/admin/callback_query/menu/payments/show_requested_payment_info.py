from aiogram.types import CallbackQuery

from data import text
from keyboards import inline
from keyboards.callback_data.default.transaction import transaction_cd, TransactionCommands
from loader import dp
from utils.database_api.table_models.qiwi_transaction import DBCommandsQiwiTransaction


@dp.callback_query_handler(transaction_cd.filter(command=TransactionCommands.SHOW_PAYMENT_INFO))
async def show_info(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=5)
    payment_comment = callback_data.get('comment')
    if not await DBCommandsQiwiTransaction.is_transaction(comment=payment_comment):
        await call.message.answer(
            text='Заявка уже обработана'
        )
        return False
    payment = await DBCommandsQiwiTransaction.get_transaction(comment=payment_comment)
    if not payment.is_hold:
        await call.message.answer(
            text='Заявка уже обработана'
        )
        return False
    await call.message.answer(
        text=text.message.menu.admin.info_payment.format(
            details=payment.user_wallet_account,
            amount=payment.amount,
            commission_amount=payment.commission,
            total_amount=payment.amount - payment.commission,
            user_id=payment.user_id
        ),
        reply_markup=inline.admin.payments.make_decision.make_keyboard_payment_decision(comment=payment_comment)
    )
