from aiogram.types import Message

from app.data import text
from app.data.text.ru.button.reply import distribution_settings
from app.data.types.user_data import UserRole
from app.loader import dp
from app.utils.bot import send_main_keyboard
from app.utils.db_api.models.messages_for_sending import MessageForSending


@dp.message_handler(reply_command=distribution_settings, user_role=UserRole.ADMIN)
async def show_menu(message: Message, user, lang_code):
    await send_main_keyboard(user)
    messages_in_schedule = await MessageForSending.query.gino.all()
    await message.answer(
        text=text[lang_code].default.message.choose_action,
        reply_markup=app.keyboards.default.inline.menu_distribution_control.make_keyboard(lang_code, messages_in_schedule)
    )
