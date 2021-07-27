import asyncio

import aioschedule

from app.schedule.sending_messages import sending_notifications, sending_user_statistics, \
    sending_start_link_history_statistics
from app.schedule.update_users_data import update_users_data


async def on_startup_schedule():
    aioschedule.every(40).seconds.do(sending_notifications)
    aioschedule.every().day.at('00:00').do(sending_user_statistics)
    aioschedule.every().day.at('00:00').do(sending_start_link_history_statistics)
    aioschedule.every().day.at('6:00').do(update_users_data)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_shutdown_schedule():
    aioschedule.clear()
