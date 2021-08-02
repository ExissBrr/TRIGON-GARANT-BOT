from aiogram.types import Message

from app import keyboards
from app.data import text
from app.data.text.ru.button.reply import proceed, skip
from app.loader import dp
from app.states.private.message_distribution import MomentaryMessageSendingStates


@dp.message_handler(state=MomentaryMessageSendingStates.wait_for_chats, text=proceed)
async def request_message(message: Message, lang_code):
    await message.answer(
        text=text[lang_code].default.message.send_message,
        reply_markup=keyboards.default.reply.cancel.keyboard(lang_code)
    )
    await MomentaryMessageSendingStates.wait_for_message.set()


@dp.message_handler(state=MomentaryMessageSendingStates.wait_for_chats, text=skip)
async def request_message(message: Message, lang_code):
    await message.answer(
        text=text[lang_code].default.message.send_message,
        reply_markup=keyboards.default.reply.cancel.keyboard(lang_code)
    )
    await MomentaryMessageSendingStates.wait_for_message.set()
