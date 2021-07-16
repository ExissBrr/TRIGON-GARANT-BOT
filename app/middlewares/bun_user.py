from aiogram import Dispatcher
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message, CallbackQuery

from app.utils.db_api.models.user import User


class UserBannedMiddleware(BaseMiddleware):

    async def on_process_message(self, message: Message, data: dict):
        user = await User.get(message.from_user.id)
        if user and user.is_blocked:
            raise CancelHandler

    async def on_process_callback_query(self, call: CallbackQuery, data: dict):
        user = await User.get(call.from_user.id)
        if user and user.is_blocked:
            raise CancelHandler
