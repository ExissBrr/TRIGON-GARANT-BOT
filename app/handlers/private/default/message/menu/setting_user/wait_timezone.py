from datetime import datetime

from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.data import text
from app.loader import dp
from app.states.private.setting_user import SettingUser
from app.utils.bot import send_main_keyboard
from app.utils.db_api.models.user import User
from app.utils.format_data.time import timezone


@dp.message_handler(state=SettingUser.wait_timezone)
async def update_timezone(message: Message, state: FSMContext, user: User, lang_code: str):
    message.text = message.text.replace('+', '')
    if not message.text.isdigit() or int(message.text) > 12 or int(message.text) < -12:
        await message.answer(
            text=text[lang_code].default.message.wrong_data
        )
        return False

    await user.update_data(timezone=int(message.text))
    await message.reply(
        text=text[lang_code].default.message.success_change_timezone.format(
            time_now=timezone(datetime.utcnow(), user.timezone).strftime('%Y-%m-%d %H:%M:%S'),
            user_gmt=user.timezone
        ),
    )
    await send_main_keyboard(user, state)
