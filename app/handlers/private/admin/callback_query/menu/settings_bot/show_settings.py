from aiogram.types import Message, CallbackQuery

from data import text, Config
from filters.private.role_user import UserRoleFilter
from keyboards import inline
from keyboards.callback_data.admin.admin_menu_choice import admin_menu_cd, AdminMenuChoice
from loader import dp, qiwi_wallet
from utils.database_api.table_models.user import UserRole


@dp.callback_query_handler(UserRoleFilter(UserRole.ADMIN),
                           admin_menu_cd.filter(command=AdminMenuChoice.SHOW_BOT_SETTINGS))
async def show_menu_bot_settings(call: CallbackQuery):
    await call.answer()
    await call.message.answer(
        text=text.message.menu.admin.info_bot_settings.format(
            qiwi_wallet=qiwi_wallet.number,
            qiwi_balance=qiwi_wallet.balance(),
            len_comment=Config.qiwi.comment_length,
            min_amount_withdraw=Config.qiwi.min_amount_withdraw,
            start_percent_commission=Config.qiwi.commission_percent,
            level_referral_system=Config.bot.level_referral_system,
        ),
        reply_markup=inline.admin.menu_settings_bot.keyboard
    )
