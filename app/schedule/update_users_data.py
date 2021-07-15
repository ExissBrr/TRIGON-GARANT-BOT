from typing import List

from aiogram import Bot
from loguru import logger

from app.data.types.user_data import UserRole
from app.utils.bot import sending_message
from app.utils.db_api.models.user import User


async def update_users_data():
    users: List[User] = await User.query.gino.all()
    bot = Bot.get_current()

    count_updates = 0

    for user_database in users:

        # User from telegram
        user_telegram = await bot.get_chat(user_database.id)

        if user_telegram.full_name != user_database.fullname:
            await user_database.update_data(fullname=user_telegram.full_name)
            count_updates += 1

        if user_telegram.username != user_database.username:
            await user_database.update_data(username=user_telegram.username)
            count_updates += 1

    if count_updates:
        await sending_message.text_message(
            text='Данные пользователей в базе данных обновлены.\n'
            f'Количество изменений: {count_updates}',
            roles=UserRole.ADMIN
        )
