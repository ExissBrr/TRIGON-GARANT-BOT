from aiogram import Dispatcher
from aiogram.dispatcher.handler import current_handler, CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message, ChatType
from aiogram.utils.exceptions import Throttled

from app.data import text
from app.loader import config
from app.utils.db_api.models.user import User


class AntiFloodMiddleware(BaseMiddleware):
    async def on_process_message(self, message: Message, data: dict):
        if not ChatType.is_private(message):
            return False


        handler = current_handler.get()
        dispatcher = Dispatcher.get_current()
        if handler and getattr(handler, 'no_limit', False):
            return False
        try:
            await dispatcher.throttle('key', rate=1.5)

        except Throttled as throttled:
            if await self.is_throttled(message, throttled):
                raise CancelHandler()

    async def is_throttled(self, message: Message, throttled: Throttled):
        if throttled.exceeded_count < 5:
            return False
        elif throttled.exceeded_count < 8:
            await message.answer(text=text[await self.lang_code(message)].default.message.antiflood_warning)
            return False
        elif throttled.exceeded_count == 8:
            await message.reply(text=text[await self.lang_code(message)].default.message.antiflood_mute)
            return True
        else:
            return True

    async def lang_code(self, message: Message):
        user = await User.get(message.from_user.id)
        if user:
            return user.lang_code
        return config.bot.languages[0]
