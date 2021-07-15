from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.data import text
from app.keyboards.default import reply
from app.loader import dp
from app.states.private.message_distribution import MessageSending


@dp.message_handler(state=MessageSending.wait_for_time)
async def wait_for_confirmation(message: Message, state: FSMContext, lang_code):
    await state.update_data(time=message.text)
    await message.answer(
        text=text[lang_code].admin.message.confirm_schedule,
        reply_markup=reply.confirm_cancel.make_keyboard_confirmation(lang_code)
    )
    await MessageSending.confirm_schedule.set()
