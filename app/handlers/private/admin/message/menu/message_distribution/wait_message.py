from aiogram.types import Message

from app.data import text
from app.data.text.ru.admin.button.reply import send_messages
from app.data.types.user_data import UserRole
from app.keyboards.default import reply
from app.loader import dp
from app.states.private.message_distribution import MessageSendingStates


@dp.message_handler(reply_command=send_messages, user_role=UserRole.ADMIN)
async def wait_for_message(message: Message,lang_code):
    await message.answer(
        text=text[lang_code].admin.message.send_message,
        reply_markup=reply.cancel.keyboard(lang_code)
    )
    await MessageSendingStates.wait_for_message.set()