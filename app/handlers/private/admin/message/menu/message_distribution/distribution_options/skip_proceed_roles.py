from aiogram.types import Message

from app.data.text.ru.button.reply import proceed, skip
from app.handlers.private.admin.message.menu.message_distribution.distribution_options._request_data import \
    request_for_chat_id
from app.loader import dp
from app.states.private.message_distribution import MessageSendingStates


@dp.message_handler(state=MessageSendingStates.wait_for_roles, text=proceed)
async def request_message(message: Message, state_data: dict, lang_code):
    selected_roles: str = state_data.get('roles', None)
    await MessageSendingStates.wait_for_chat_id.set()
    await request_for_chat_id(message, lang_code, is_roles=selected_roles)


@dp.message_handler(state=MessageSendingStates.wait_for_roles, text=skip)
async def request_message(message: Message, state_data: dict, lang_code):
    selected_roles: str = state_data.get('roles', None)
    await MessageSendingStates.wait_for_chat_id.set()
    await request_for_chat_id(message, lang_code, selected_roles)
