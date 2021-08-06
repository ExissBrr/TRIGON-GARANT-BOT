from aiogram.types import CallbackQuery

from keyboards import inline
from keyboards.callback_data.admin.admin_menu_choice import admin_menu_cd, AdminMenuChoice
from loader import dp
from utils.database_api.table_models.qiwi_transaction import DBCommandsQiwiTransaction, QiwiTransactionType


@dp.callback_query_handler(admin_menu_cd.filter(command=AdminMenuChoice.PAYMENTS))
async def show_requested_payments(call: CallbackQuery):
    await call.answer(cache_time=5)
    requested_payments = await DBCommandsQiwiTransaction.get_transactions(type=QiwiTransactionType.OUT, is_hold=True)
    if not requested_payments:
        await call.message.answer(
            text='На данный момент нет запросов на вывод.'
        )
        return False
    await call.message.answer(
        text='Запрошенные выплаты на данный момент:',
        reply_markup=await inline.admin.payments.requested_payments_list.make_keyboard_payment_list(
            requested_payments)
    )
