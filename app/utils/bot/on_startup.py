import asyncio

from aiogram import Dispatcher

from app.data.types.user_data import UserRole
from app.loader import config
from app.schedule import on_startup_schedule
from app.utils import db_api
from app.utils.bot import sending_message
from app.utils.bot.set_commands import set_bot_commands


async def on_startup(dp: Dispatcher):
    await db_api.on_startup(drop_all=0)

    await set_bot_commands(dp)

    await sending_message.text_message('Бот включен', roles=UserRole.ADMIN, chats_id=config.bot.admin_id)

    asyncio.create_task(on_startup_schedule())
