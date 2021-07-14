from aiogram.dispatcher.filters import CommandHelp
from aiogram.types import Message

from app.data import text
from app.data.types.user_data import UserRole
from app.loader import dp


@dp.message_handler(CommandHelp(), user_role=UserRole.ADMIN)
async def message_on(message: Message, lang_code):
    await message.answer(
        text=text[lang_code].default.message.command_help
    )
