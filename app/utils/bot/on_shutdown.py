from aiogram import Dispatcher

from app.data.types.user_data import UserRole
from app.loader import config
from app.utils.bot import sending_message
from app.utils.bot.set_commands import set_bot_commands


async def on_shutdown(dp: Dispatcher):
    await set_bot_commands(dp, None)

    await sending_message.text_message('Бот выключен', [UserRole.ADMIN], config.bot.admin_id)
