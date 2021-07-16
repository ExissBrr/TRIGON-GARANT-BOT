from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from app import keyboards
from app.data import text
from app.keyboards.admin.callback_data.message_distribution import distribution_cd, DistributionCommands
from app.loader import dp
from app.states.private.message_distribution import MessageSendingStates
from app.utils.db_api.models.messages_for_sending import MessageForSending


@dp.callback_query_handler(distribution_cd.filter(command=DistributionCommands.ACTIVATE_SCHEDULE))
async def delete_schedule(call: CallbackQuery, state: FSMContext, callback_data: dict, lang_code):
    await call.answer(cache_time=5, text='One moment..')
    schedule_id = callback_data.get('id')
    schedule_message = await MessageForSending.get(int(schedule_id))
    if not schedule_message:
        await call.message.answer(
            text=text[lang_code].admin.message.schedule_not_found
        )
        return False
    await call.message.answer(
        text=text[lang_code].admin.message.confirm_activate_schedule,
        reply_markup=keyboards.default.reply.confirm_cancel.keyboard(lang_code)
    )
    await state.update_data(message_id=schedule_id)
    await MessageSendingStates.wait_confirm_activate_schedule.set()
