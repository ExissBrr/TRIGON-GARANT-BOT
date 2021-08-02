from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentType

from app.data import text
from app.loader import dp
from app.states.private.message_distribution import MomentaryMessageSendingStates
from app.utils.bot import send_main_keyboard
from app.utils.bot.sending_message import forward_message, copy_message


@dp.message_handler(state=MomentaryMessageSendingStates.wait_for_approval)
async def send_message(message: Message, state: FSMContext, state_data: dict, lang_code, user):
    roles = state_data.get('roles', '')
    chats_id = state_data.get('chats_id', None)
    distribution_message: Message = state_data.get('message')
    if chats_id:
        chats_id = list(map(int, chats_id.split()))
    if distribution_message.content_type == ContentType.POLL:
        await forward_message(message=distribution_message,
                              roles=roles,
                              chats_id=chats_id)
    else:
        await copy_message(
            message=distribution_message,
            roles=roles.split(),
            chats_id=chats_id
        )
    await message.answer(
        text=text[lang_code].default.message.sent_by
    )
    await send_main_keyboard(user, state)
