from asyncio import sleep

from aiogram.types import Message

from app.data.types.start_link import StartLinkType
from app.filters.private.message.start_link import StartLink
from app.loader import dp
from app.utils.db_api.models.start_link import StartLinkHistory


@dp.message_handler(StartLink('easter_egg_profile'))
async def send_easter_egg(message: Message, user, message_args: dict):
    await StartLinkHistory.insert(
        type=StartLinkType.USED,
        prefix=message_args.pop('prefix'),
        args=message.get_args(),
        user_id=user.id
    )
    await message.answer('Easter egg :)')
