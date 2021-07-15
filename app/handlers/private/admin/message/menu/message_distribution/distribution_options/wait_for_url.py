from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.handler import SkipHandler
from aiogram.types import Message
from loguru import logger

from app.data import text
from app.loader import dp
from app.states.private.message_distribution import MessageSendingStates


@dp.message_handler(state=MessageSendingStates.wait_for_url)
async def wait_for_media(message: Message, state: FSMContext, lang_code):
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
    await MessageSendingStates.request_for_media.set()
    raise SkipHandler
