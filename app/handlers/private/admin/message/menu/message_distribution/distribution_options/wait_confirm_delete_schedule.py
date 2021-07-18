from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.data import text
from app.data.text.ru.button.reply import confirm
from app.loader import dp
from app.states.private.message_distribution import MessageSendingStates
from app.utils.bot import send_main_keyboard
from app.utils.db_api.models.messages_for_sending import MessageForSending


@dp.message_handler(state=MessageSendingStates.wait_confirm_delete_schedule, reply_command=confirm)
async def delete_schedule(message: Message, lang_code, state: FSMContext, user, state_data: dict):
    schedule_id = int(state_data.get('schedule_id'))
    message_id = int(state_data.get('message_id'))
    await dp.bot.edit_message_reply_markup(
        chat_id=message.from_user.id,
        message_id=message_id
    )
    await send_main_keyboard(user, state)
    schedule_message = await MessageForSending.get(schedule_id)
    await schedule_message.delete()
    await message.answer(
        text=text[lang_code].default.message.schedule_was_deleted
    )
