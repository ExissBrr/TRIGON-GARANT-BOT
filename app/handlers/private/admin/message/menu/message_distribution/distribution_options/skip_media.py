from aiogram.types import Message

from app.data.text.ru.button.reply import skip
from app.handlers.private.admin.message.menu.message_distribution.distribution_options._request_data import \
    request_for_url_button
from app.loader import dp
from app.states.private.message_distribution import MessageSendingStates


@dp.message_handler(state=MessageSendingStates.wait_for_media, text=skip)
async def skip_media(message: Message, lang_code):
    await MessageSendingStates.wait_for_url.set()
    await request_for_url_button(message, lang_code)
