from aiogram import Bot
from aiogram.dispatcher import FSMContext

from app import keyboards
from app.data import text
from app.data.types.user import UserRole
from app.utils.db_api.models.user import User


async def send_main_keyboard(user: User, state: FSMContext = None):
    if state:
        await state.finish()

    bot = Bot.get_current()

    if user.is_role(UserRole.ADMIN):
        keyboard = keyboards.admin.reply.main.keyboard(user.lang_code)
    else:
        keyboard = keyboards.default.reply.main.keyboard(user.lang_code)

    await bot.send_message(
        chat_id=user.id,
        text=text[user.lang_code].message.default.send_main_keyboard,
        reply_markup=keyboard
    )
