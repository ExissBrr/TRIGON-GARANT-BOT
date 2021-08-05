from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from app import keyboards
from app.data import text
from app.keyboards.callback_data.deal import DealCommands, deal_cd
from app.loader import dp
from app.states.private.left_feedback import FeedbackForSeller
from app.utils.db_api.models.deals import Deal


@dp.callback_query_handler(deal_cd.filter(command=DealCommands.LEFT_FEEDBACK))
async def request_comment(call: CallbackQuery, callback_data: dict, user, state: FSMContext, lang_code):
    await call.answer(cache_time=5, text='One moment..')
    await call.message.delete_reply_markup()
    deal_id = callback_data.get('deal_id')
    await call.message.answer(
        text=text[lang_code].default.message.request_comment_for_feedback,
        reply_markup=keyboards.default.reply.cancel.keyboard(lang_code)
    )
    await state.update_data(deal_id=deal_id)
    await FeedbackForSeller.wait_comment.set()
