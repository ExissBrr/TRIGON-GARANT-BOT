import datetime as dt

from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message, CallbackQuery, InlineQuery
from loguru import logger

from app.data.types.user_data import UserRole
from app.loader import config
from app.utils.bot.languages import get_lang_code
from app.utils.db_api.models.user import User


class GettingUserFromDataBaseMiddleware(BaseMiddleware):
    async def on_process_message(self, message: Message, data: dict):
        user_id = message.from_user.id
        user = await User.get(user_id)
        lang_code = await get_lang_code()

        if not user:
            data['user'] = None
            data['lang_code'] = lang_code
            return False

        if not user.is_role(UserRole.ADMIN) and user.id == config.bot.admin_id:
            await user.update_data(role=UserRole.ADMIN)

        if not user.is_active:
            await user.update_data(is_active=True)

        if (user.online_at + dt.timedelta(minutes=1)) < dt.datetime.utcnow():
            await user.update_data(online_at=dt.datetime.utcnow())

        await user.update_username(message.from_user.username)
        await user.update_fullname(message.from_user.full_name)

        data['user'] = user
        data['lang_code'] = lang_code

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
        await user.update_fullname(call.from_user.full_name)

        data['user'] = user
        data['lang_code'] = user.lang_code


    async def on_process_inline_query(self, query: InlineQuery, data: dict):
        user_id = query.from_user.id
        user = await User.get(user_id)
        if not user:
            data['user'] = None
            data['lang_code'] = config.bot.languages[0]
            return False

        if (user.online_at + dt.timedelta(minutes=1)) < dt.datetime.utcnow():
            await user.update_data(online_at=dt.datetime.utcnow())

        await user.update_username(query.from_user.username)
        await user.update_fullname(query.from_user.full_name)

        data['user'] = user
        data['lang_code'] = user.lang_code