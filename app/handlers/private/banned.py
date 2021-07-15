from aiogram.types import ReplyKeyboardRemove

from app.data import text
from app.filters.private.user.is_blocking import UserBlocked
from app.loader import dp


@dp.callback_query_handler(UserBlocked())
@dp.message_handler(UserBlocked())
async def answer(obj, lang_code):
    await dp.bot.send_message(
        chat_id=obj.from_user.id,
        text=text[lang_code].default.message.bun_answer,
        reply_markup=ReplyKeyboardRemove()
    )
