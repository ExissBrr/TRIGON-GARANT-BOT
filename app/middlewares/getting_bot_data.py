from aiogram import Dispatcher
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message, CallbackQuery, InlineQuery


class BotDataMiddleware(BaseMiddleware):

    async def on_process_message(self, message: Message, data: dict):
        dp = Dispatcher.get_current()
        data['bot_data'] = await dp.bot.get_me()

    async def on_process_callback_query(self, call: CallbackQuery, data: dict):
        dp = Dispatcher.get_current()
        data['bot_data'] = await dp.bot.get_me()

    async def on_process_inline_query(self, query: InlineQuery, data: dict):
        dp = Dispatcher.get_current()
        data['bot_data'] = await dp.bot.get_me()
