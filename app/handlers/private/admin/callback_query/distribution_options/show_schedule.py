from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ContentType, InlineKeyboardButton

from app.data import text
from app.keyboards.admin.callback_data.message_distribution import distribution_cd, DistributionCommands
from app.keyboards.default.inline import generator_button_url
from app.loader import dp
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
    markup = generator_button_url.keyboard(message.get_links_btn)

    suspend_activate_button = InlineKeyboardButton(
        text=text[lang_code].admin.button.inline.suspend,
        callback_data=distribution_cd.new(id=message.id, command=DistributionCommands.SUSPEND_SCHEDULE)
    )
    if not message.is_active:
        suspend_activate_button = InlineKeyboardButton(
            text=text[lang_code].admin.button.inline.activate,
            callback_data=distribution_cd.new(id=message.id, command=DistributionCommands.ACTIVATE_SCHEDULE)
        )

    markup.add(
        suspend_activate_button,
        InlineKeyboardButton(
            text=text[lang_code].admin.button.inline.delete,
            callback_data=distribution_cd.new(id=message.id, command=DistributionCommands.DELETE_SCHEDULE)
        )
    )
    try:
        if message.is_content_type(ContentType.PHOTO):
            await call.message.answer_photo(
                photo=message.media_id,
                caption=view_text,
                reply_markup=markup
            )
        elif message.is_content_type(ContentType.VIDEO):
            await call.message.answer_video(
                video=message.media_id,
                caption=view_text,
                reply_markup=markup
            )
        else:
            await call.message.answer(
                text=view_text,
                reply_markup=markup
            )
    except Exception as ex:
        await call.message.answer(
            text=text[lang_code].admin.message.error_show_message.format(error=ex)
        )
