from aiogram.types import CallbackQuery

from filters.private.role_user import UserRoleFilter
from keyboards.callback_data.admin.admin_menu_choice import admin_menu_cd, AdminMenuChoice
from loader import dp
from states.default.searching_scammer import ScammerSearch
from utils.database_api.table_models.user import UserRole


@dp.callback_query_handler(UserRoleFilter(UserRole.ADMIN),
                           admin_menu_cd.filter(command=AdminMenuChoice.ADD_SCAMMER))
async def wait_scammer_info(call: CallbackQuery):
    await call.answer(cache_time=3)
    await call.message.answer(
        text="Поиск пользователя/бота: @user или id"
    )
    await ScammerSearch.admin_waiting_for_scammer.set()
