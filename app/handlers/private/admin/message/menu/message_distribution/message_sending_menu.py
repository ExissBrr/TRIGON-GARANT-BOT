from aiogram.types import Message

from app.data import text
from app.data.text.ru.button.reply import message_sending
from app.data.types.user_data import UserRole
from app.keyboards.admin import reply
from app.loader import dp


@dp.message_handler(reply_command=message_sending, user_role=UserRole.ADMIN)
async def send_distribution_menu(message: Message, lang_code):
    await message.answer(
        text=text[lang_code].default.message.choose_action,
        reply_markup=reply.menu_message_distribution.make_keyboard(lang_code)
    )
