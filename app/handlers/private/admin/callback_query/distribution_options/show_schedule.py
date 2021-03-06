from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ContentType, InlineKeyboardButton

from app.data import text
from app.keyboards.callback_data.message_distribution import distribution_cd, DistributionCommands
from app.keyboards.default.inline import generator_button_url
from app.loader import dp
from app.utils.db_api.models.messages_for_sending import MessageForSending


@dp.callback_query_handler(distribution_cd.filter(command=DistributionCommands.SHOW_SCHEDULE))
async def add_schedule(call: CallbackQuery, state: FSMContext, callback_data: dict, lang_code):
    await call.answer(cache_time=5, text='One moment..')
    distribution_message_id = callback_data.get('id')
    message: MessageForSending = await MessageForSending.get(int(distribution_message_id))

    if not message:
        await call.answer(
            cache_time=200,
            text=text[lang_code].default.call.message_deleted
        )
        messages_in_schedule = await MessageForSending.query.gino.all()

        await call.message.edit_reply_markup(
            reply_markup=app.keyboards.default.inline.menu_distribution_control.make_keyboard(lang_code, messages_in_schedule)
        )
        return False

    view_text = text[lang_code].default.message.message_preview.format(
        text=message.text,
        time=message.time
    )
    markup = generator_button_url.keyboard(message.get_links_btn)
    if message.is_active:
        markup.row(
            InlineKeyboardButton(
                text=text[lang_code].button.inline.suspend,
                callback_data=distribution_cd.new(
                    id=message.id,
                    command=DistributionCommands.UPDATE_ACTIVE_STATUS
                )
            )
        )
    else:
        markup.row(
            InlineKeyboardButton(
                text=text[lang_code].button.inline.activate,
                callback_data=distribution_cd.new(
                    id=message.id,
                    command=DistributionCommands.UPDATE_ACTIVE_STATUS
                )
            )
        )
    markup.insert(
        InlineKeyboardButton(
            text=text[lang_code].button.inline.delete,
            callback_data=distribution_cd.new(
                id=message.id,
                command=DistributionCommands.DELETE_SCHEDULE
            )
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
        elif message.is_content_type(ContentType.ANIMATION):
            await call.message.answer_animation(
                animation=message.media_id,
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
            text=text[lang_code].default.message.error_show_message.format(error=ex)
        )
