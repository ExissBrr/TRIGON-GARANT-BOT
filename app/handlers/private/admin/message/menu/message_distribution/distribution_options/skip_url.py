from aiogram.types import Message

from app.data.text.ru.button.reply import skip
from app.handlers.private.admin.message.menu.message_distribution.distribution_options._request_data import \
    request_for_chat_id
from app.loader import dp
from app.states.private.message_distribution import MessageSendingStates


@dp.message_handler(state=MessageSendingStates.wait_for_url, text=skip)
async def skip_url(message: Message, lang_code):
    await MessageSendingStates.wait_for_chat_id.set()
    await request_for_chat_id(message, lang_code)
