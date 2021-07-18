from aiogram.types import CallbackQuery, InlineKeyboardButton

from app.data import text
from app.keyboards.default.callback_data.message_distribution import distribution_cd, DistributionCommands
from app.keyboards.default.inline import generator_button_url
from app.loader import dp
from app.utils.db_api.models.messages_for_sending import MessageForSending


@dp.callback_query_handler(distribution_cd.filter(command=DistributionCommands.UPDATE_ACTIVE_STATUS))
async def delete_schedule(call: CallbackQuery, callback_data: dict, lang_code):
    await call.answer(text='One moment..')
    schedule_id = callback_data.get('id')

    schedule_message: MessageForSending = await MessageForSending.get(int(schedule_id))

    if not schedule_message:
        await call.message.answer(
            text=text[lang_code].admin.message.schedule_not_found
        )
        return False

    markup = generator_button_url.keyboard(schedule_message.get_links_btn)

    if not schedule_message.is_active:
        markup.row(
            InlineKeyboardButton(
                text=text[lang_code].button.inline.suspend,
                callback_data=distribution_cd.new(
                    id=schedule_message.id,
                    command=DistributionCommands.UPDATE_ACTIVE_STATUS
                )
            )
        )
    else:
        markup.row(
            InlineKeyboardButton(
                text=text[lang_code].button.inline.activate,
                callback_data=distribution_cd.new(
                    id=schedule_message.id,
                    command=DistributionCommands.UPDATE_ACTIVE_STATUS
                )
            )
        )

    markup.insert(
        InlineKeyboardButton(
            text=text[lang_code].button.inline.delete,
            callback_data=distribution_cd.new(
                id=schedule_message.id,
                command=DistributionCommands.DELETE_SCHEDULE
            )
        )
    )
    await schedule_message.update_data(is_active=not schedule_message.is_active)
    await call.message.edit_reply_markup(markup)
