from aiogram.dispatcher.filters import CommandHelp
from aiogram.types import Message

from app.data import text
from app.loader import dp
from app.utils.captcha.image_captcha import CaptchaImage


@dp.message_handler(CommandHelp())
async def message_on(message: Message, lang_code):
    await message.answer(
        text=text[lang_code].default.message.command_help
    )

