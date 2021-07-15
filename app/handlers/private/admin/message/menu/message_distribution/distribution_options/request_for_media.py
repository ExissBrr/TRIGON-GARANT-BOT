from aiogram.types import Message

from app import keyboards
from app.data import text
from app.data.text.ru.default.button.reply import skip
from app.loader import dp
from app.states.private.message_distribution import MessageSendingStates

@dp.message_handler(state=MessageSendingStates.wait_for_url, text=skip)
@dp.message_handler(state=MessageSendingStates.request_for_media)
async def request_url_button(message: Message, lang_code):
    await message.answer(
        text=text[lang_code].admin.message.send_media
    )
    await MessageSendingStates.wait_for_media.set()