from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentType, ChatType
from aiogram.utils.exceptions import RetryAfter

from app.loader import dp
from app.utils.bot import send_main_keyboard


@dp.message_handler(state='*', content_types=ContentType.ANY, chat_type=ChatType.PRIVATE)
async def unknown_command(message: Message, state: FSMContext, user, lang_code):
    # raise RetryAfter(5)
    await send_main_keyboard(user, state)
