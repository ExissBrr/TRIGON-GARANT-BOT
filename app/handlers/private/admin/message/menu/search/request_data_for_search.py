from aiogram.types import Message

from app.data import text
from app.loader import dp
from app.data.text.ru.admin.button.reply import search
from app.data.types.user_data import UserRole
from app.states.private.search import SearchStates


@dp.message_handler(reply_command=search, user_role=UserRole.ADMIN)
async def request_data_for_search(message: Message, lang_code):
    await message.answer(
        text=text[lang_code].admin.message.ask_for_user_data
    )
    await SearchStates.wait_for_data.set()
