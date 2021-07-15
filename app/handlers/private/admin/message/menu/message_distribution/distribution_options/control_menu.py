import datetime

from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from loguru import logger

from app.data import text
from app.data.text.ru.admin.button.reply import distribution_settings
from app.data.types.user_data import UserRole
from app.keyboards.admin import inline
from app.loader import dp
from app.utils.bot import send_main_keyboard
from app.utils.db_api.models.messages_for_sending import MessageForSending


@dp.message_handler(reply_command=distribution_settings, user_role=UserRole.ADMIN)
async def show_menu(message: Message, state: FSMContext, user, lang_code):
    messages_in_schedule = await MessageForSending.query.gino.all()
    await message.answer(
        text=text[lang_code].default.message.choose_action,
        reply_markup=inline.menu_distribution_control.make_keyboard(lang_code, messages_in_schedule)
    )
    await send_main_keyboard(user)
