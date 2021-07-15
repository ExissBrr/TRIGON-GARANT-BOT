from typing import Union

from aiogram.types import Message, CallbackQuery

from app.data import text
from app.filters.private.message.not_command import NotCommand
from app.filters.private.user.not_subscriber import NotSubscribedChat
from app.keyboards.default.inline import generator_button_url
from app.loader import dp


@dp.callback_query_handler(NotSubscribedChat())
@dp.message_handler(NotCommand('start'), NotSubscribedChat(), state='*')
async def not_subscriber(obj: Union[Message, CallbackQuery], lang_code, links_chat):
    await obj.bot.send_message(
        chat_id=obj.from_user.id,
        text=text[lang_code].default.text.subscribe_to_the_chat,
        reply_markup=generator_button_url.keyboard(links_chat)
    )
