from aiogram.types import Message

from app import keyboards
from app.data import text
from app.data.text.ru.button.reply import search_users
from app.loader import dp
from app.states.private.search import UserSearchStates


@dp.message_handler(reply_command=search_users)
async def request_data_for_search(message: Message, lang_code):
    await message.answer(
        text=text[lang_code].default.message.ask_for_user_data,
        reply_markup=keyboards.default.reply.cancel.keyboard(lang_code)
    )
    await UserSearchStates.wait_for_user_data.set()
