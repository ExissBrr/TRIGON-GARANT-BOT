from aiogram.types import Message

from app.loader import dp
from app.data.text.ru.admin.button.reply import search
from app.data.types.user_data import UserRole


@dp.message_handler(text=search, user_role=UserRole.ADMIN)
async def request_data_for_search(message: Message):
    await message.