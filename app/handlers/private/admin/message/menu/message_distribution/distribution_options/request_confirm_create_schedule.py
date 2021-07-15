from aiogram.dispatcher.handler import SkipHandler
from aiogram.types import Message, ContentType

from app import keyboards
from app.data import text
from app.loader import dp
from app.states.private.message_distribution import MessageSendingStates


@dp.message_handler(state=MessageSendingStates.request_confirm_create_schedule, content_types=ContentType.TEXT)
async def request_confirm_create_schedule(message: Message, state_data, lang_code):
    distribution_message = state_data.get('mess', None)
    distribution_urls = state_data.get('urls', None)
    distribution_media = state_data.get('media_id', None)
    distribution_media_type = state_data.get('media_type', None)
    view_text = text[lang_code].admin.message.message_preview.format(
        text=distribution_message,
        time=message.text
    )
    if distribution_media:
        if distribution_media_type == ContentType.VIDEO:
            await message.answer_video(
                video=distribution_media,
                caption=view_text,
                reply_markup=keyboards.default.inline.generator_button_url.keyboard(
                    links=distribution_urls)
            )
        elif distribution_media_type == ContentType.PHOTO:
            await message.answer_photo(
                photo=distribution_media,
                caption=view_text,
                reply_markup=keyboards.default.inline.generator_button_url.keyboard(links=distribution_urls)
            )
    else:
        await message.answer(
            text=view_text
        )
    await message.answer(
        text=text[lang_code].admin.message.wait_confirm_create_schedule,
        reply_markup=keyboards.default.reply.confirm_cancel.make_keyboard_confirmation(lang_code)
    )
    await MessageSendingStates.wait_confirm_create_schedule
