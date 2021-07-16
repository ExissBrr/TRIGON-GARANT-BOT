from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentType

from app import keyboards
from app.data import text
from app.loader import config


async def request_for_chat_id(message: Message, lang_code):
    chats = [await message.bot.get_chat(chat_id) for chat_id in config.bot.chats_id]
    await message.answer(
        text=text[lang_code].default.message.request_for_chat_id,
        reply_markup=keyboards.default.reply.skip_and_chats.keyboard(chats, lang_code),
    )


async def request_for_media(message: Message, lang_code):
    await message.answer(
        text=text[lang_code].admin.message.send_media,
        reply_markup=keyboards.default.reply.skip.keyboard(lang_code),
    )


async def request_for_url_button(message: Message, lang_code):
    await message.answer(
        text=text[lang_code].admin.message.send_btn_link,
        reply_markup=keyboards.default.reply.skip.keyboard(lang_code)
    )


async def request_for_time(message: Message, lang_code):
    await message.answer(
        text=text[lang_code].admin.message.send_time,
        reply_markup=keyboards.admin.reply.hours_and_minutes_list.keyboard(lang_code)
    )


async def request_confirm_create_schedule(message: Message, state_data, lang_code):
    distribution_message = state_data.get('mess', None)
    distribution_urls = state_data.get('urls', {})
    distribution_time = state_data.get('time', '15:00')
    distribution_media = state_data.get('media_id', None)
    distribution_media_type = state_data.get('media_type', ContentType.TEXT)
    view_text = text[lang_code].admin.message.message_preview.format(
        text=distribution_message,
        time=distribution_time
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
        text=text[lang_code].admin.message.confirm_create_schedule,
        reply_markup=keyboards.default.reply.confirm_cancel.keyboard(lang_code)
    )