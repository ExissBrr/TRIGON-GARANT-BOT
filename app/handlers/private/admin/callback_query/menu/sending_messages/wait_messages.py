from aiogram.types import Message, CallbackQuery
from data import text
from filters.private.role_user import UserRoleFilter
from keyboards import reply
from keyboards.callback_data.admin.admin_menu_choice import admin_menu_cd, AdminMenuChoice
from loader import dp
from states.admin.sending_messages import StatesSendingMessages
from utils.database_api.table_models.user import UserRole


@dp.callback_query_handler(UserRoleFilter(UserRole.ADMIN), admin_menu_cd.filter(command=AdminMenuChoice.SEND_MESSAGES))
async def wait_message(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer(
        text='Введите сообщение, которое нужно разослать',
        reply_markup=reply.default.cancel.keyboard
    )
    await StatesSendingMessages.wait_messages.set()
