from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.data import text
from app.loader import dp
from app.states.private.message_distribution import MessageSendingStates
from app.utils.bot import send_main_keyboard
from app.utils.db_api.models.messages_for_sending import MessageForSending


@dp.message_handler(state=MessageSendingStates.wait_confirm_suspend_schedule)
async def delete_schedule(message: Message, lang_code, state: FSMContext, user, state_data: dict):
    schedule_id = int(state_data.get('message_id'))
    schedule_message = await MessageForSending.get(schedule_id)
    await schedule_message.update_data(is_active=False)
    await message.answer(
        text=text[lang_code].admin.message.schedule_was_suspended
    )
    await send_main_keyboard(user, state)
