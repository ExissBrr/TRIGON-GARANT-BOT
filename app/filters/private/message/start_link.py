from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message
from loguru import logger

from app.utils.bot.generate_links import get_data_from_start_link


class StartLink(BoundFilter):

    def __init__(self, prefix: str):
        self.prefix = prefix.lower()

    async def check(self, message: Message) -> bool:
        if message.text.find(self.prefix) == 0:
            data = get_data_from_start_link(message.text)
        elif message.get_args() and message.get_args().find(self.prefix) == 0:
            data = get_data_from_start_link(message.get_args())
        else:
            return False

        if data is None:
            return False
        await message.delete()
        return {'message_args': data}

