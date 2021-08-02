from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from loguru import logger

from app import keyboards
from app.data import text
from app.loader import dp, config
from app.states.private.message_distribution import MomentaryMessageSendingStates


@dp.message_handler(state=MomentaryMessageSendingStates.wait_for_chats)
async def wait_for_message(message: Message, state: FSMContext, state_data: dict, lang_code):
    chats_id: str = state_data.get('chats_id', '')
    selected_roles: str = state_data.get('roles', None)

    chat_id = message.text.split()[0]

    if chats_id.find(chat_id) != -1:
        chats_id = chats_id.replace(chat_id, '')
    else:
        chats_id += f' {chat_id}'
    chats = [await message.bot.get_chat(chat_id) for chat_id in config.bot.chats_id]

    if not chats_id and not selected_roles:
        keyboard = keyboards.default.reply.skip_and_chats.keyboard(chats, lang_code,can_continue=False)
    else:
        keyboard = keyboards.default.reply.proceed_and_chats.keyboard(chats, lang_code)

    await state.update_data(chats_id=None or chats_id.strip())
    await message.answer(
        text=text[lang_code].default.message.selected_chats.format(
            chats_id='\n'.join(chats_id.split())
        ),
        reply_markup=keyboard
    )
