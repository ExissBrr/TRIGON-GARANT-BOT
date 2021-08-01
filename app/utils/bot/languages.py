from aiogram.types import User as UserTelegram

from app.loader import config
from app.utils.db_api.models.user import User


async def get_lang_code() -> str:
    user_telegram = UserTelegram.get_current()
    if not user_telegram:
        return config.bot.languages[0]
    user_database: User = await User.get(user_telegram.id)

    if user_database and user_database.lang_code in config.bot.languages:
        return user_database.lang_code

    if user_telegram.language_code in config.bot.languages:
        return user_telegram.language_code

    return config.bot.languages[0]
