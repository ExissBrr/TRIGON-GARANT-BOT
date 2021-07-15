from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from app.data import text
from app.keyboards.admin.callback_data.message_distribution import distribution_cd, DistributionCommands
from app.keyboards.default import reply
from app.loader import dp
from app.states.private.message_distribution import MessageSending


@dp.callback_query_handler(distribution_cd.filter(command=DistributionCommands.SHOW_SCHEDULE))
async def add_schedule(call: CallbackQuery, state: FSMContext, callback_data: dict, lang_code):
    await call.answer(cache_time=5, text='One moment..')
    distribution_message_id = callback_data.get('id')
    await call.message.answer(
        text=text[lang_code].admin.message.send_message,
        reply_markup=reply.cancel.make_keyboard_cancel(lang_code)
    )
    await MessageSending.wait_for_delayed_message.set()
