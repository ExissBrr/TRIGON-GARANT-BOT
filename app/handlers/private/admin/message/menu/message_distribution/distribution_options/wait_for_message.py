from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.handler import SkipHandler
from aiogram.types import Message, ContentTypes

from app import keyboards
from app.data import text
from app.handlers.private.admin.message.menu.message_distribution.distribution_options._request_data import \
    request_for_time
from app.loader import dp
from app.states.private.message_distribution import MessageSendingStates


@dp.message_handler(state=MessageSendingStates.wait_for_delayed_message)
async def wait_for_url(message: Message, state: FSMContext, lang_code):
    if not message.text:
        await message.answer(
            text=text[lang_code].default.message.worng_data
        )
        return
    await state.update_data(mess=message.text)

    await MessageSendingStates.wait_for_time.set()

    # Request for time
    await request_for_time(message, lang_code)
