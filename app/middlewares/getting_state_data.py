from aiogram import Dispatcher
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message, CallbackQuery, InlineQuery


class StateDataMiddleware(BaseMiddleware):

    async def on_process_message(self, message: Message, data: dict):
        dp = Dispatcher.get_current()
        data['state_data'] = await dp.storage.get_data(chat=message.from_user.id)

    async def on_process_callback_query(self, call: CallbackQuery, data: dict):
        dp = Dispatcher.get_current()
        data['state_data'] = await dp.storage.get_data(chat=call.from_user.id)

    async def on_process_inline_query(self, query: InlineQuery, data: dict):
        dp = Dispatcher.get_current()
        data['state_data'] = await dp.storage.get_data(chat=query.from_user.id)