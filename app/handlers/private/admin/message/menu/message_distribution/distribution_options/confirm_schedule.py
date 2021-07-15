from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.loader import dp
from app.states.private.message_distribution import MessageSending


@dp.message_handler(state=MessageSending.confirm_schedule)
async def add_schedule_in_db(message: Message, state: FSMContext, user, lang_code):
    distribution_message = await state.get_data('message')
    distribution_urls = await state.get_data('urls')
    distribution_media=await state.get_data('media_id')
    distribution_time = await state.get_data('time')
