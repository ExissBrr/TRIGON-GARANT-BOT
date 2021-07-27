from aiogram import Bot
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from app import keyboards
from app.data import text
from app.data.types.user_data import UserRole
from app.loader import config
from app.utils.bot.languages import get_lang_code
from app.utils.db_api.models.user import User


async def send_main_keyboard(user: User, state: FSMContext = None):
    """
    Send main keyboard depending on his role.
    Args:
        user: Object User from table users.
        state: User state to finished.

    Returns:
        None

    """
    if state:
        await state.finish()

    bot = Bot.get_current()

    lang_code = await get_lang_code()

    if user and user.is_role(UserRole.ADMIN) or user.id == config.bot.admin_id:
        keyboard = keyboards.admin.reply.main.keyboard(lang_code)
    elif user and user.is_blocked:
        keyboard = ReplyKeyboardRemove()
    else:
        keyboard = keyboards.default.reply.main.keyboard(lang_code)

    await bot.send_message(
        chat_id=user.id,
        text=text[lang_code].default.message.send_main_keyboard,
        reply_markup=keyboard
    )
