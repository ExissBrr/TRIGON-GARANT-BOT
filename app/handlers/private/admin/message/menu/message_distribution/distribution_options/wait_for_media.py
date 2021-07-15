from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentType

from app.data import text
from app.loader import dp
from app.states.private.message_distribution import MessageSending


@dp.message_handler(state=MessageSending.wait_for_media)
async def wait_for_media(message: Message, state: FSMContext, lang_code):
    if message.content_type is ContentType.VIDEO:
        video_id = message.video.file_id
        await state.update_data(content_type=ContentType.VIDEO)
        await state.update_data(media_id=message.video.file_id)
    elif message.content_type is ContentType.PHOTO:
        photo_id = message.photo[-1].file_id
        await state.update_data(content_type=ContentType.PHOTO)
        await state.update_data(media_id=message.photo[-1].file_id)
    await message.answer(
        text=text[lang_code].admin.message.send_time
    )
    await MessageSending.wait_for_time.set()
