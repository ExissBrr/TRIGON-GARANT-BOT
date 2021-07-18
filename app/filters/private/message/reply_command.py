from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message
from loguru import logger

from app.data import text


class ReplyCommand(BoundFilter):
    key = 'reply_command'

    def __init__(self, reply_command: str):
        self.reply_button_text = reply_command
        self.langs = text._dirs

    async def check(self, message: Message) -> bool:
        for lang in self.langs:
            for key, value in text[lang].button.reply.__dict__.items():
                if value == self.reply_button_text:
                    for lang in self.langs:
                        if text[lang].button.reply.__dict__.get(key) == message.text:
                            return True
