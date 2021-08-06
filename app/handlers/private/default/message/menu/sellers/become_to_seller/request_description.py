from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app import keyboards
from app.data import text
from app.data.types.category_data import ServiceCategoryType
from app.loader import dp
from app.states.private.become_to_seller import BecomeToSeller


@dp.message_handler(state=BecomeToSeller.wait_category)
async def request_description(message: Message, state: FSMContext, lang_code):

    if message.text not in ServiceCategoryType.__dict__.values():
        return await message.answer(
            text=text[lang_code].default.message.choose_category_among_list
        )
    await state.update_data(category=message.text)
    await message.answer(
        text=text[lang_code].default.message.request_seller_description,
        reply_markup=keyboards.default.reply.cancel.keyboard(lang_code)
    )
    await BecomeToSeller.wait_description.set()
