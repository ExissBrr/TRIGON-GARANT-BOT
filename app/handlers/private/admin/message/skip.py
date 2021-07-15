from aiogram.types import Message

from app import dp
from app.data.text.ru.default.button.reply import skip


@dp.message_handler(reply_command=skip)
async def skip(message: Message):
    pass
