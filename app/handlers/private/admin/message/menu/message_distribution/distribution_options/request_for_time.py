from aiogram.types import Message, ContentTypes

from app.data import text
from app.loader import dp
from app.states.private.message_distribution import MessageSendingStates


@dp.message_handler(state=MessageSendingStates.request_for_time, content_types=ContentTypes.TEXT)
async def request_url_button(message: Message, lang_code):
    await message.answer(
        text=text[lang_code].admin.message.send_time,
    )
    await MessageSendingStates.wait_for_time.set()