from aiogram.types import CallbackQuery

from app import keyboards
from app.data import text
from app.keyboards.default.callback_data.settings_profile import choice_lang_cd
from app.loader import dp
from app.utils.bot import send_main_keyboard
from app.utils.format_data.user import format_lang_code


@dp.callback_query_handler(choice_lang_cd.filter())
async def menu_choice_language(call: CallbackQuery, callback_data: dict, user):
    await call.answer(cache_time=5)
    lang_code = callback_data.get('lang_code')
    await user.update_data(lang_code=lang_code)
    await call.answer(format_lang_code(user.lang_code))

    await call.message.edit_text(
        text=text[lang_code].default.message.menu_choice_language,
        reply_markup=keyboards.default.inline.menu_settings.languages.keyboard(user)
    )

    await send_main_keyboard(user)
