from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentType

from app import keyboards
from app.data import text
from app.keyboards.default import reply
from app.loader import dp
from app.states.private.message_distribution import MessageSending


@dp.message_handler(state=MessageSending.wait_for_time)
async def wait_for_confirmation(message: Message, state: FSMContext, lang_code, state_data: dict):
    if ':' not in message.text and message.text.replace(':', '').isdigit():
        await message.answer(
            text=text[lang_code].default.message.wrong_data
        )
        return False
    hour, minute = map(int, message.text.split(':'))
    if hour > 23 or minute > 59:
        await message.answer(
            text=text[lang_code].default.message.wrong_data
        )
        return False
    await state.update_data(time=message.text)

    distribution_message = state_data.get('mess', None)
    distribution_urls: dict = state_data.get('urls', None)
    distribution_media = state_data.get('media_id', None)
    distribution_media_type = state_data.get('media_type', None)
    view_text = text[lang_code].admin.message.message_preview.format(
        text=distribution_message,
        time=message.text)
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
        text=text[lang_code].admin.message.confirm_schedule,
        reply_markup=reply.confirm_cancel.make_keyboard_confirmation(lang_code)
    )
    await MessageSending.confirm_schedule.set()
