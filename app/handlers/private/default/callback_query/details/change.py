from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.loader import dp
from app.states.private.change_detail import StatesChangeDetails
from app.utils.bot import send_main_keyboard
from app.utils.db_api.models.user import User
from app.utils.payments.requisites_tools import is_valid_details


@dp.message_handler(state=StatesChangeDetails.wait_details_data)
async def change_details(message: Message, state: FSMContext, user: User):
    details_data = message.text

    details_list = details_data.split()
    for detail in details_list:
        if detail in user.requisites.split():
            await user.remove_detail(detail)
            await message.answer(f'Реквизит {detail} удален')
        elif is_valid_details(detail):
            details=user.requisites.split()
            details.append(detail)
            new_details = list(set(details))
            await user.update_data(requisites=' '.join(new_details))
            await message.answer(f'Реквизит {detail} сохранен')
        else:
            await message.answer(f'Реквизит {detail} неверного формата')
    await send_main_keyboard(user,state)