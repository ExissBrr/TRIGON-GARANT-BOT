import datetime as dt

from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from loguru import logger

from app.data.types.user_data import UserRole
from app.loader import config
from app.utils.db_api.models.user import User


class GettingUserFromDataBaseMiddleware(BaseMiddleware):
    async def on_process_message(self, message: Message, data: dict):
        user_id = message.from_user.id
        user = await User.get(user_id)

        if not user:
            data['user'] = None
            data['lang_code'] = config.bot.languages[0]
            return False

        if not user.is_role(UserRole.ADMIN) and user.id == config.bot.admin_id:
            await user.update_data(role=UserRole.ADMIN)

        if not user.is_active:
            await user.update_data(is_active=True)


        if (user.online_at + dt.timedelta(minutes=1)) < dt.datetime.utcnow():
            await user.update_data(online_at=dt.datetime.utcnow())

        await user.update_username(message.from_user.username)
        await user.update_full_name(message.from_user.full_name)

        data['user'] = user
        data['lang_code'] = user.lang_code

    async def on_process_callback_query(self, call: CallbackQuery, data: dict):
        user_id = call.from_user.id
        user = await User.get(user_id)
        if not user:
            data['user'] = None
            data['lang_code'] = config.bot.languages[0]
            return False

        if (user.online_at + dt.timedelta(minutes=1)) < dt.datetime.utcnow():
            await user.update_data(online_at=dt.datetime.utcnow())

        await user.update_username(call.from_user.username)
        await user.update_full_name(call.from_user.full_name)

        data['user'] = user
        data['lang_code'] = user.lang_code
