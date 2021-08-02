import asyncio
import time
from builtins import isinstance

from aiogram.dispatcher.handler import CancelHandler
from aiogram.types import Update
from aiogram.utils.exceptions import RetryAfter
from loguru import logger

import app
from app.loader import dp, flood_defender_time, flood_user_in_processing


@dp.errors_handler()
async def on_flood_defender(update: Update, exception):
    if isinstance(exception, RetryAfter):
        logger.warning(f'Бот упал')
        if app.loader.is_flood_defender:
            raise CancelHandler

        app.loader.is_flood_defender = True

        updates = await dp.bot.get_updates()
        await dp.process_updates(updates)

        time.sleep(exception.timeout+4)

        updates = await dp.bot.get_updates()

        await dp.process_updates(updates)

        await asyncio.sleep(flood_defender_time)

        app.loader.is_flood_defender = False

        flood_user_in_processing.clear()
