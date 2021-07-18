from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from app.data import text
from app.keyboards.default.callback_data.message_distribution import distribution_cd, DistributionCommands
from app.keyboards.default import reply
from app.loader import dp
from app.states.private.message_distribution import MessageSendingStates


@dp.callback_query_handler(distribution_cd.filter(command=DistributionCommands.ADD_SCHEDULE))
async def add_schedule(call: CallbackQuery, state: FSMContext, lang_code):
    await call.answer(cache_time=5, text='One moment..')
    await call.message.answer(
        text=text[lang_code].default.message.send_message,
        reply_markup=reply.cancel.keyboard(lang_code)
    )
    await MessageSendingStates.wait_for_delayed_message.set()
