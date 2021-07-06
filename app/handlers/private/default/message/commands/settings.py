from aiogram.dispatcher.filters import CommandSettings
from aiogram.types import Message

from app import keyboards
from app.data import text
from app.loader import dp


@dp.message_handler(CommandSettings())
async def send_menu_settings(message: Message, user, lang_code):
    await message.answer(
        text=text[lang_code].message.default.command_settings,
        reply_markup=keyboards.default.inline.menu_settings.main_menu.keyboard(lang_code)
    )
