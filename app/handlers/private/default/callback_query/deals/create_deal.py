from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from app import keyboards
from app.data import text
from app.keyboards.callback_data.user import user_cd, UserCommand
from app.loader import dp
from app.states.private.create_deal import CreateBargainStates


@dp.callback_query_handler(user_cd.filter(command=UserCommand.CREATE_DEAL))
async def request_bargain_amount(call: CallbackQuery, callback_data: dict, state: FSMContext, lang_code):
    await call.message.edit_reply_markup()
    await call.message.answer(
        text=text[lang_code].default.message.request_deal_amount,
        reply_markup=keyboards.default.reply.cancel.keyboard(lang_code)
    )

    await state.update_data(seller_id=callback_data.get('user_id'))
    await CreateBargainStates.wait_for_bargain_amount.set()
