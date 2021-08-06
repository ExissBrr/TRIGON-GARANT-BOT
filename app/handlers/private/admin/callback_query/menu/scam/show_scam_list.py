from aiogram.types import CallbackQuery

from filters.private.role_user import UserRoleFilter
from keyboards import inline
from keyboards.callback_data.admin.admin_menu_choice import admin_menu_cd, AdminMenuChoice
from loader import dp
from utils.database_api.table_models.scam_complain import DBCommandsScamList, ScamStatusType
from utils.database_api.table_models.user import UserRole


@dp.callback_query_handler(UserRoleFilter(UserRole.ADMIN),
                           admin_menu_cd.filter(command=AdminMenuChoice.SHOW_SCAM_LIST))
async def show_scam_list(call: CallbackQuery):
    await call.answer(cache_time=5)
    scam_complains = await DBCommandsScamList.get_scams(status=ScamStatusType.ACTIVE)
    if not scam_complains:
        await call.message.answer(
            text='На данный момент в базе нет скам жалоб'
        )
        return False
    await call.message.answer(
        text='Активные скам жалобы:',
        reply_markup=await inline.admin.scam.scam_list.make_keyboard_scam_list(scam_complains)
    )
