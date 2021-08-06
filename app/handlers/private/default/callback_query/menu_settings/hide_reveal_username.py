from aiogram.types import CallbackQuery

from app.data import text
from app.loader import dp
from app.keyboards.callback_data.settings_profile import settings_cd, SettingsCommands


@dp.callback_query_handler(settings_cd.filter(command=SettingsCommands.HIDE_USERNAME))
async def hide_username(call: CallbackQuery,user, callback_data: dict,lang_code):
    await call.answer(cache_time=5)
    await user.update_data(is_anonymous=True)
    await call.message.edit_text(
        text=text[lang_code].default.message.username_was_hidden
    )


@dp.callback_query_handler(settings_cd.filter(command=SettingsCommands.REVEAL_USERNAME))
async def hide_username(call: CallbackQuery,user, callback_data: dict,lang_code):
    await call.answer(cache_time=5)
    await user.update_data(is_anonymous=False)
    await call.message.edit_text(
        text=text[lang_code].default.message.username_was_revealed
    )
