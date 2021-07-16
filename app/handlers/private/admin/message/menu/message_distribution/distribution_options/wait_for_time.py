from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.handler import SkipHandler
from aiogram.types import Message, ContentType
from loguru import logger

from app import keyboards
from app.data import text
from app.handlers.private.admin.message.menu.message_distribution.distribution_options._request_data import \
    request_for_media
from app.loader import dp
from app.states.private.message_distribution import MessageSendingStates


@dp.message_handler(state=MessageSendingStates.wait_for_time)
async def wait_for_confirmation(message: Message, state: FSMContext, lang_code, state_data: dict):
    if len(message.text.split(':')) != 2 and not message.text.replace(':', '').isdigit():
        await message.answer(
            text=text[lang_code].default.message.wrong_data
        )
        return False
    hour, minute = map(int, message.text.split(':'))
    if hour > 23 or minute > 59:
        await message.answer(
            text=text[lang_code].default.message.wrong_data
        )
        return False
    await state.update_data(time=message.text)
    await MessageSendingStates.wait_for_media.set()

    # Request for media
    await request_for_media(message, lang_code)

