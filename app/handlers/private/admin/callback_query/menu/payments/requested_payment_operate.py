from aiogram.types import CallbackQuery

from keyboards.callback_data.default.transaction import transaction_cd, TransactionCommands
from loader import dp
from utils.database_api.table_models.qiwi_transaction import DBCommandsQiwiTransaction


@dp.callback_query_handler(transaction_cd.filter(command=TransactionCommands.APPROVE_PAYMENT))
async def approve_payment(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=5)
    payment_comment = callback_data.get('comment')
    payment = await DBCommandsQiwiTransaction.get_transaction(comment=payment_comment)
    await payment.update(is_hold=False).apply()
    await call.message.edit_text(
        text='Заявка одобрена.'
    )


@dp.callback_query_handler(transaction_cd.filter(command=TransactionCommands.ABOLISH_PAYMENT))
async def approve_payment(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=5)
    payment_comment = callback_data.get('comment')
    payment = await DBCommandsQiwiTransaction.get_transaction(comment=payment_comment)
    await call.message.edit_text(
        text='Заявка отклонена'
    )
    await payment.delete()
