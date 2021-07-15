from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ContentType

from app.data import text
from app.keyboards.admin.callback_data.message_distribution import distribution_cd, DistributionCommands
from app.keyboards.default import reply
from app.keyboards.default.inline import generator_button_url
from app.loader import dp
from app.states.private.message_distribution import MessageSendingStates
from app.utils.db_api.models.messages_for_sending import MessageForSending


@dp.callback_query_handler(distribution_cd.filter(command=DistributionCommands.SHOW_SCHEDULE))
async def add_schedule(call: CallbackQuery, state: FSMContext, callback_data: dict, lang_code):
    await call.answer(cache_time=5, text='One moment..')
    distribution_message_id = callback_data.get('id')
    message: MessageForSending = await MessageForSending.get(int(distribution_message_id))
    view_text = text[lang_code].admin.message.message_preview.format(
        text=message.text,
        time=message.time
    )
    try:
        if message.is_content_type(ContentType.PHOTO):
            await call.message.answer_photo(
                photo=message.media_id,
                caption=view_text,
                reply_markup=generator_button_url.keyboard(message.get_links_btn)
            )
        elif message.is_content_type(ContentType.VIDEO):
            await call.message.answer_video(
                video=message.media_id,
                caption=view_text,
                reply_markup=generator_button_url.keyboard(message.get_links_btn)
            )
        else:
            await call.message.answer(
                text=view_text,
                reply_markup=generator_button_url.keyboard(message.get_links_btn))
    except Exception as ex:
        await call.message.answer(
            text=text[lang_code].admin.message.error_show_message.format(error=ex)
        )

