from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentType

from app.data import text
from app.loader import dp
from app.states.private.message_distribution import MessageSendingStates
from app.utils.bot import send_main_keyboard
from app.utils.bot.sending_message import copy_message, forward_message


@dp.message_handler(state=MessageSendingStates.wait_for_message, content_types=ContentType.POLL)
async def send_message_to_users(message: Message, state: FSMContext, user, lang_code):
    await message.answer(
        text=text[lang_code].default.message.sent_by
    )
    await send_main_keyboard(user, state)
    await forward_message(message=message)


@dp.message_handler(state=MessageSendingStates.wait_for_message, content_types=ContentType.ANY)
async def send_message_to_users(message: Message, state: FSMContext, user, lang_code):
    await message.answer(
        text=text[lang_code].default.message.sent_by
    )
    await send_main_keyboard(user, state)
    await copy_message(message=message)
