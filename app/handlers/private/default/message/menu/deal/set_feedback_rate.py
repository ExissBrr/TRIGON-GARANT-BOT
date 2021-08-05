from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app import keyboards
from app.data import text
from app.loader import dp
from app.states.private.left_feedback import FeedbackForSeller
from app.utils.format_data.user import format_rate


@dp.message_handler(state=FeedbackForSeller.wait_rate)
async def set_bargain_rate(message: Message, state: FSMContext, state_data: dict, lang_code):
    if not message.text.isdigit():
        return await message.answer(
            text=text[lang_code].default.message.wrong_data
        )
    if 0 > int(message.text) or int(message.text) > 5:
        return await message.answer(
            text=text[lang_code].default.message.wrong_data
        )
    await state.update_data(rate=message.text)
    feedback_comment = state_data.get('comment')
    await message.answer(
        text=text[lang_code].default.message.approve_feedback.format(
            feedback_comment=feedback_comment,
            feedback_rate=format_rate(int(message.text), 1),
        ),
        reply_markup=keyboards.default.reply.confirm_cancel.keyboard(lang_code)
    )
    await FeedbackForSeller.approve_feedback.set()
