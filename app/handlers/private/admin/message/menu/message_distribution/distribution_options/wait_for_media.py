from typing import Union

from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentType, Video, Animation, PhotoSize

from app.handlers.private.admin.message.menu.message_distribution.distribution_options._request_data import \
    request_for_url_button
from app.loader import dp
from app.states.private.message_distribution import MessageSendingStates


@dp.message_handler(state=MessageSendingStates.wait_for_media, content_types=ContentType.PHOTO)
@dp.message_handler(state=MessageSendingStates.wait_for_media, content_types=ContentType.VIDEO)
@dp.message_handler(state=MessageSendingStates.wait_for_media, content_types=ContentType.ANIMATION)
async def wait_for_media(message: Message, state: FSMContext, lang_code):
    media = message.video or message.animation or message.photo
    if isinstance(media, Video):
        await state.update_data(media_type=ContentType.VIDEO, media_id=media.file_id)
    elif isinstance(media, Animation):
        await state.update_data(media_type=ContentType.ANIMATION, media_id=media.file_id)
    elif isinstance(media, PhotoSize):
        await state.update_data(media_type=ContentType.PHOTO, media_id=media.file_id)

    await MessageSendingStates.wait_for_url.set()

    # Request for url
    await request_for_url_button(message, lang_code)
