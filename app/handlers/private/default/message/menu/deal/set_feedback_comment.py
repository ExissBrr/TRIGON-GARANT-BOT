from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app import keyboards
from app.data import text
from app.loader import dp
from app.states.private.left_feedback import FeedbackForSeller


@dp.message_handler(state=FeedbackForSeller.wait_comment)
async def request_rate(message: Message, state: FSMContext, lang_code):
    if len(message.text) > 100:
        return await message.answer(
            text=text[lang_code].default.message.wrong_data
        )
    await state.update_data(comment=message.text)
    await message.answer(
        text=text[lang_code].default.message.request_rate_for_feedback,
        reply_markup=keyboards.default.reply.rates.keyboard_choose_rate()
    )
    await FeedbackForSeller.wait_rate.set()
