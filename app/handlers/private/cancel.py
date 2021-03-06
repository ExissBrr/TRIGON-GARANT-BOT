from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.data.text.ru.button.reply import cancel
from app.loader import dp
from app.utils.bot import send_main_keyboard


@dp.message_handler(reply_command=cancel, state='*')
async def cancel_event(message: Message, state: FSMContext, user, lang_code):
    await send_main_keyboard(user, state)
