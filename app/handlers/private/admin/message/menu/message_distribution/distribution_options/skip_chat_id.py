from aiogram.types import Message

from app.data.text.ru.button.reply import skip
from app.handlers.private.admin.message.menu.message_distribution.distribution_options._request_data import \
    request_confirm_create_schedule
from app.loader import dp
from app.states.private.message_distribution import MessageSendingStates


@dp.message_handler(state=MessageSendingStates.wait_for_chat_id, text=skip)
async def skip_url(message: Message, state_data, lang_code):
    await MessageSendingStates.wait_confirm_create_schedule.set()
    await request_confirm_create_schedule(message, state_data, lang_code)
