from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app import keyboards
from app.data import text
from app.data.types.user_data import UserRole
from app.loader import dp
from app.states.private.message_distribution import MessageSendingStates


@dp.message_handler(state=MessageSendingStates.wait_for_roles)
async def wait_for_chats(message: Message, state: FSMContext, state_data: dict, lang_code):
    selected_roles: str = state_data.get('roles', '')
    role = message.text
    if selected_roles.find(role) != -1:
        selected_roles = selected_roles.replace(role, '')
    else:
        selected_roles += f' {role}'

    roles = UserRole.ROLES

    if not selected_roles:
        keyboard = keyboards.default.reply.skip_and_roles.keyboard(roles, lang_code)
    else:
        keyboard = keyboards.default.reply.proceed_and_roles.keyboard(roles, lang_code)

    await state.update_data(roles=None or selected_roles.strip())
    await message.answer(
        text=text[lang_code].default.message.selected_roles.format(
            roles='\n'.join(selected_roles.strip().split())
        ),
        reply_markup=keyboard
    )
