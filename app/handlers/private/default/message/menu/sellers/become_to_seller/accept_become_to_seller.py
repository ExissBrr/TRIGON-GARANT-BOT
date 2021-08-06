from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app import keyboards
from app.data import text
from app.loader import dp
from app.states.private.become_to_seller import BecomeToSeller


@dp.message_handler(state=BecomeToSeller.wait_description)
async def accept_become_to_seller(message: Message, state: FSMContext,lang_code):
    if len(message.text) > 400:
        await message.answer(
            text=f'{text[lang_code].default.message.too_big_text} (400)'
        )
        return
    state_data = await state.get_data()
    category = state_data.get('category')
    await message.answer(
        text=text[lang_code].default.message.accept_become_to_seller.format(
            seller_category=category,
            seller_description=message.text,
        ),
        reply_markup=keyboards.default.reply.sellers.accept_become_to_seller.keyboard(lang_code)
    )
    await state.update_data(description=message.text)
    await BecomeToSeller.wait_accept.set()
