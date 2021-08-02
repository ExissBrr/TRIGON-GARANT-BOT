from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentType

from app import keyboards
from app.data import text
from app.loader import dp
from app.states.private.message_distribution import MomentaryMessageSendingStates


@dp.message_handler(state=MomentaryMessageSendingStates.wait_for_message, content_types=ContentType.ANY)
async def send_message_to_users(message: Message, state: FSMContext, state_data: dict, user, lang_code):
    await state.update_data(message=message)
    await message.answer(
        text=text[lang_code].default.message.confirm_distribution,
        reply_markup=keyboards.default.reply.confirm_cancel.keyboard(lang_code)
    )
    await MomentaryMessageSendingStates.wait_for_approval.set()
