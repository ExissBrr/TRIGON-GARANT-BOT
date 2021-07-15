from typing import Union

from aiogram.types import Message, CallbackQuery

from app.data import text
from app.filters.private.message.not_command import NotCommand
from app.filters.private.user import NewUser
from app.loader import dp


@dp.callback_query_handler(NewUser())
@dp.message_handler(NewUser(), NotCommand('start'))
async def user_not_db(obj: Union[Message, CallbackQuery], lang_code):
    await dp.bot.send_message(
        chat_id=obj.from_user.id,
        text=text[lang_code].default.message.user_not_found_in_user_database
    )
