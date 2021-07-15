from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentType
from loguru import logger

from app.loader import dp
from app.utils.bot import send_main_keyboard


@dp.message_handler(state='*', content_types=ContentType.ANY)
async def unknown_command(message: Message, state: FSMContext, user, lang_code):
    logger.debug(await state.get_state())
    await send_main_keyboard(user, state)
