from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.data import text
from app.data.text.ru.button.reply import request_seller_creation
from app.loader import dp
from app.states.private.become_to_seller import BecomeToSeller
from app.utils.bot import send_main_keyboard
from app.utils.db_api.models.sellers import Seller
from app.utils.db_api.models.user import User


@dp.message_handler(reply_command=request_seller_creation, state=BecomeToSeller.wait_accept)
async def create_request(message: Message, state: FSMContext, user: User, lang_code):
    state_data = await state.get_data()
    category = state_data.get('category')
    description = state_data.get('description')
    await send_main_keyboard(user,state)

    await Seller.insert(
        user_id=user.id,
        description=description,
        category=category,
    )
    await message.answer(
        text=text[lang_code].default.message.application_was_sent
    )

