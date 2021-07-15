import asyncio

import aioschedule

from app.schedule.sending_messages import sending_notifications
from app.schedule.update_users_data import update_users_data


async def on_startup_schedule():
    aioschedule.every(10).seconds.do(sending_notifications)
    aioschedule.every().day.at('4:00').do(update_users_data)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_shutdown_schedule():
    aioschedule.clear()
