from aiogram.types import CallbackQuery

from app import keyboards
from app.loader import dp
from app.data import text
from app.data.types.menu_cd import MenuSettingsCD
from app.keyboards.default.callback_data.settings_profile import menu_settings_cd


@dp.callback_query_handler(menu_settings_cd.filter(menu=MenuSettingsCD.menu_setting_lang_code))
async def menu_choice_language(call: CallbackQuery, user, lang_code):
    await call.message.edit_text(
        text=text[lang_code].default.message.menu_choice_language,
        reply_markup=keyboards.default.inline.menu_settings.languages.keyboard(user)
    )