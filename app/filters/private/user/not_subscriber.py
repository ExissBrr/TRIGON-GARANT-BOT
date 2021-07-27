from typing import Union

from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message, CallbackQuery

from app.loader import config


class NotSubscribedChat(BoundFilter):

    async def check(self, obj: Union[Message, CallbackQuery]) -> Union[bool, dict[str, dict[str, str]]]:

        # If not main_chats_id
        if not config.bot.chats_id:
            return False

        bot = obj.bot
        user_id = obj.from_user.id
        chats = [await bot.get_chat(chat_id) for chat_id in config.bot.chats_id]

        links_chat_not_subscribed = {}

        for chat in chats:
            user = await chat.get_member(user_id)
            if user.is_chat_member() or user.is_chat_admin() or user.is_chat_creator():
                continue
            links_chat_not_subscribed[chat.title] = chat.invite_link
        if links_chat_not_subscribed:
            return {'links_chat': links_chat_not_subscribed}

        return False
