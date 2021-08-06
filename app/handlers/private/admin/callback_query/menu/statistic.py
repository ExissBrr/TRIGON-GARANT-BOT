from aiogram.types import Message, CallbackQuery

from data import text, Config
from filters.private.role_user import UserRoleFilter
from keyboards.callback_data.admin.admin_menu_choice import admin_menu_cd, AdminMenuChoice
from loader import dp
from utils.database_api.table_models.bargin import DBCommandsBargin, BarginStatusType
from utils.database_api.table_models.qiwi_transaction import DBCommandsQiwiTransaction, QiwiTransactionType
from utils.database_api.table_models.user import DBCommandsUser, UserRole


@dp.callback_query_handler(UserRoleFilter(UserRole.ADMIN), admin_menu_cd.filter(command=AdminMenuChoice.SHOW_STATISTIC))
async def send_admin_menu_statistic(call: CallbackQuery):
    await call.answer()
    """Отравляет статистику администратору"""

    amount_balance_all_users = sum([user.balance for user in await DBCommandsUser.get_users()])
    payments_in = await DBCommandsQiwiTransaction.get_transactions(type=QiwiTransactionType.IN)
    payments_out = await DBCommandsQiwiTransaction.get_transactions(type=QiwiTransactionType.OUT)
    closed_bargins = await DBCommandsBargin.get_bargins(
        status=BarginStatusType.CLOSED_NOT_SUCCESSFUL
    ) + await DBCommandsBargin.get_bargins(
        status=BarginStatusType.CLOSED_SUCCESSFUL
    )
    controversy_bargins = await DBCommandsBargin.get_bargins(status=BarginStatusType.CONTROVERSY)
    all_bargins = await DBCommandsBargin.get_bargins()
    active_bargins = await DBCommandsBargin.get_bargins(status=BarginStatusType.ACTIVE)

    await call.message.answer(
        text=text.message.menu.admin.statistic.format(
            count_users_in_db=await DBCommandsUser.get_count(),
            count_active_users=await DBCommandsUser.get_count(is_active=True),
            count_users_blocked=await DBCommandsUser.get_count(is_blocked=True),
            count_users_referred=await DBCommandsUser.get_count(is_referred=True),
            amount_balance_all_users=amount_balance_all_users,
            count_payment_in=len(payments_in),
            count_payment_out=len(payments_out),
            amount_payment_in=sum(payment.amount for payment in payments_in),
            amount_payment_out=sum(payment.amount for payment in payments_out),
            count_bargins=await DBCommandsBargin.get_count(),
            count_active_bargins=await DBCommandsBargin.get_count(status=BarginStatusType.ACTIVE),
            amount_all_bargins=sum(bargin.amount for bargin in all_bargins),
            amount_closed_bargins=sum(bargin.amount for bargin in closed_bargins),
            amount_controversy_bargins=sum(bargin.amount for bargin in controversy_bargins),
            amount_active_bargins=sum(bargin.amount for bargin in active_bargins),
            amount_abt_succor=sum(bargin.amount for bargin in active_bargins) / 100 * Config.qiwi.commission_percent,
        )
    )
