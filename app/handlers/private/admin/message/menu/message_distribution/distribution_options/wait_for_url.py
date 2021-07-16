from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentType

from app.data import text
from app.handlers.private.admin.message.menu.message_distribution.distribution_options._request_data import \
    request_for_time, request_for_chat_id
from app.loader import dp
from app.states.private.message_distribution import MessageSendingStates


@dp.message_handler(state=MessageSendingStates.wait_for_url)
async def wait_for_media(message: Message, state: FSMContext, state_data, lang_code):
    raw_data = message.text.split()
    links = {}
    for data in raw_data:
        try:
            data = data.replace('https://', '').replace('http://', '')
            title, link = data.split(':')
            links.setdefault(title, link)
        except Exception:
            await message.answer(
                text=text[lang_code].default.message.wrong_data
            )
            return False

    await state.update_data(urls=links)

    await MessageSendingStates.wait_for_chat_id.set()

    # Request chats id
    await request_for_chat_id(message, lang_code)
