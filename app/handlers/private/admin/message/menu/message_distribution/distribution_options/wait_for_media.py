from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.handler import SkipHandler
from aiogram.types import Message, ContentType

from app.loader import dp
from app.states.private.message_distribution import MessageSendingStates


@dp.message_handler(state=MessageSendingStates.wait_for_media, content_types=ContentType.PHOTO)
@dp.message_handler(state=MessageSendingStates.wait_for_media, content_types=ContentType.VIDEO)
@dp.message_handler(state=MessageSendingStates.wait_for_media, content_types=ContentType.TEXT)
async def wait_for_media(message: Message, state: FSMContext, lang_code):
    if message.content_type is ContentType.VIDEO:
        video_id = message.video.file_id
        await state.update_data(media_type=ContentType.VIDEO)
        await state.update_data(media_id=video_id)
    elif message.content_type is ContentType.PHOTO:
        photo_id = message.photo[-1].file_id
        await state.update_data(media_type=ContentType.PHOTO)
        await state.update_data(media_id=photo_id)

    await MessageSendingStates.request_confirm_create_schedule.set()
    raise SkipHandler
