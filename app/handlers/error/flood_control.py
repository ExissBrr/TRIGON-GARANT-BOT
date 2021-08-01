import asyncio
import time
from aiogram.types import Update
from aiogram.utils.exceptions import RetryAfter

from app.loader import dp, flood_defender_time
import app

@dp.errors_handler(exception=RetryAfter)
async def on_flood_defender(update: Update, exception: RetryAfter):
    app.loader.is_flood_defender = True
    time.sleep(exception.timeout+5)
    await asyncio.time(flood_defender_time)
    app.loader.is_flood_defender = False
