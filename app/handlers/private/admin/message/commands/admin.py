from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from app import keyboards
from app.data import text
from app.loader import dp
from app.data.types.user_data import UserRole


@dp.message_handler(Command('admin'),user_role=UserRole.ADMIN)
async def send_admin_keyboard(message: Message,lang_code):
    await message.answer(
        text=text[lang_code].default.message.choose_action,
        reply_markup=keyboards.admin.inline.menu_admin.make_keyboard_admin_menu(lang_code)
    )
