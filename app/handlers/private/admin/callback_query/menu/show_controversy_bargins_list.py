from aiogram.types import CallbackQuery

from app import keyboards
from app.data import text
from app.data.types.bargain_data import DealStatusType
from app.data.types.user_data import UserRole
from app.filters import UserRoleFilter
from app.keyboards.callback_data.admin import admin_menu_cd, AdminMenuChoice
from app.loader import dp
from app.utils.db_api.models.deals import Deal


@dp.callback_query_handler(UserRoleFilter(UserRole.ADMIN),
                           admin_menu_cd.filter(command=AdminMenuChoice.SHOW_CONTROVERSY_BARGINS))
async def show_controversy_list(call: CallbackQuery, lang_code):
    await call.answer(cache_time=5)
    controversies = await Deal.query.where(Deal.status == DealStatusType.CONTROVERSY).gino.all()
    if controversies:
        await call.message.answer(
            text=text[lang_code].admin.message.controversies_for_now,
            reply_markup=await keyboards.admin.inline.controversies_list.make_keyboard_controversies_list(controversies)
        )
    else:
        await call.message.answer(
            text=text[lang_code].default.message.none_controversies
        )
