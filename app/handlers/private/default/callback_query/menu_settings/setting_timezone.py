from datetime import datetime

from aiogram.types import CallbackQuery

from app import keyboards
from app.data import text
from app.data.types.menu_cd import MenuSettingsCD
from app.keyboards.callback_data.settings_profile import menu_settings_cd
from app.loader import dp
from app.states.private.setting_user import SettingUser
from app.utils.db_api.models.user import User
from app.utils.format_data.time import timezone


@dp.callback_query_handler(menu_settings_cd.filter(menu=MenuSettingsCD.menu_setting_timezone))
async def send_menu_choice_timezone(call: CallbackQuery, user: User, lang_code: str):
    await call.message.delete()
    await call.message.answer(
        text=text[lang_code].default.message.setting_timezone.format(
            time_now=timezone(datetime.utcnow(), user.timezone).strftime('%Y-%d-%m %H:%M:%S'),
            user_gmt=user.timezone,
        ),
        reply_markup=keyboards.default.reply.menu_settings.timezone.keyboard(lang_code)
    )
    await SettingUser.wait_timezone.set()
