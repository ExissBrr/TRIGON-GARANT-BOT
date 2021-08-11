from aiogram.types import CallbackQuery

from app import keyboards
from app.data import text
from app.data.types.user_data import UserRole
from app.filters import UserRoleFilter
from app.keyboards.callback_data.admin import admin_menu_cd, AdminMenuChoice
from app.loader import dp
from app.states.private.message_distribution import MomentaryMessageSendingStates


@dp.callback_query_handler(UserRoleFilter(UserRole.ADMIN), admin_menu_cd.filter(command=AdminMenuChoice.SEND_MESSAGES))
async def wait_for_roles(call: CallbackQuery, lang_code):
    await MomentaryMessageSendingStates.wait_for_roles.set()
    roles = UserRole.ROLES
    await call.message.answer(
        text=text[lang_code].default.message.send_distribution_roles,
        reply_markup=keyboards.default.reply.skip_and_roles.keyboard(roles, lang_code),
    )
