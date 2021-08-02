from aiogram.types import Message

from app.data.text.ru.button.reply import send_messages
from app.data.types.user_data import UserRole
from app.handlers.private.admin.message.menu.message_distribution.distribution_options._request_data import \
    request_for_roles
from app.loader import dp
from app.states.private.message_distribution import MomentaryMessageSendingStates


@dp.message_handler(reply_command=send_messages, user_role=UserRole.ADMIN)
async def wait_for_roles(message: Message, lang_code):
    await MomentaryMessageSendingStates.wait_for_roles.set()
    await request_for_roles(message, lang_code)
