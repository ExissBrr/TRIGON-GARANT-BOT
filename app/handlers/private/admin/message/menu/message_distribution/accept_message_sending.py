from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentType

from app.data import text
from app.loader import dp
from app.states.private.message_distribution import MessageSending
from app.utils.bot import send_main_keyboard
from app.utils.bot.sending_message import copy_message, forward_message


@dp.message_handler(state=MessageSending.wait_for_message, content_types=ContentType.POLL)
async def send_message_to_users(message: Message, state: FSMContext, user, lang_code):
    await forward_message(message=message)
    await message.answer(
        text='Опрос был отправлен'
    )
    await send_main_keyboard(user, state)


@dp.message_handler(state=MessageSending.wait_for_message, content_types=ContentType.ANY)
async def send_message_to_users(message: Message, state: FSMContext, user, lang_code):
    await copy_message(message=message)
    await message.answer(
        text='Сообщения разосланы'
    )
    await send_main_keyboard(user, state)
