from aiogram.types import CallbackQuery
from loguru import logger

from app.data import text
from app.data.types.deal_data import DealStatusType
from app.data.types.transactions_data import QiwiTransactionType
from app.data.types.user_data import UserRole, UserDeepLink
from app.filters import UserRoleFilter
from app.keyboards.callback_data.admin import admin_menu_cd, AdminMenuChoice
from app.loader import dp
from app.utils.db_api import db
from app.utils.db_api.models.deals import Deal
from app.utils.db_api.models.payments import Payment
from app.utils.db_api.models.user import User


@dp.callback_query_handler(UserRoleFilter(UserRole.ADMIN), admin_menu_cd.filter(command=AdminMenuChoice.SHOW_STATISTIC))
async def send_admin_menu_statistic(call: CallbackQuery, lang_code):
    await call.answer()
    """Отравляет статистику администратору"""
    amount_balance_all_users = sum([user.balance for user in await User.query.gino.all()])
    payments_in = await Payment.query.where(Payment.type == QiwiTransactionType.IN).gino.all()
    payments_out = await Payment.query.where(Payment.type == QiwiTransactionType.OUT).gino.all()

    closed_deals = await Deal.query.where(Deal.status == DealStatusType.CLOSED).gino.all()

    controversy_deals = await Deal.query.where(Deal.status == DealStatusType.CONTROVERSY).gino.all()

    all_deals = await Deal.query.gino.all()
    active_deals = await Deal.query.where(Deal.status == DealStatusType.ACTIVE).gino.all()
    connected_to_referral_system = await db.select([db.func.count(User.id)]).where(
        User.deep_link != UserDeepLink.NONE).gino.scalar() or 0
    await call.message.answer(
        text=text[lang_code].default.message.statistic.format(
            count_users_in_db=await db.select([db.func.count(User.id)]).gino.scalar(),
            count_active_users=await db.select([db.func.count(User.id)]).where(User.is_active == True).gino.scalar(),
            count_users_blocked=await db.select([db.func.count(User.id)]).where(User.is_blocked == True).gino.scalar(),
            count_users_referred=connected_to_referral_system,
            amount_balance_all_users=amount_balance_all_users,
            count_payment_in=len(payments_in),
            count_payment_out=len(payments_out),
            amount_payment_in=sum(payment.amount for payment in payments_in),
            amount_payment_out=sum(payment.amount for payment in payments_out),
            count_deals=len(all_deals),
            count_active_deals=len(active_deals),
            amount_all_deals=sum(deal.amount for deal in all_deals),
            amount_closed_deals=sum(deal.amount for deal in closed_deals),
            amount_controversy_deals=sum(deal.amount for deal in controversy_deals),
            amount_active_deals=sum(deal.amount for deal in active_deals),
            amount_abt_succor=sum(deal.amount for deal in active_deals) / 100 * 5,
        )
    )
