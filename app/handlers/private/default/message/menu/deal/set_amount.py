from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram.utils.markdown import quote_html

from app import keyboards
from app.data import text
from app.loader import dp
from app.states.private.create_deal import CreateBargainStates
from app.utils.db_api.models.user import User
from app.utils.format_data.user import format_username


@dp.message_handler(state=CreateBargainStates.wait_for_bargain_amount)
async def request_bargain_category(message: Message, state: FSMContext, state_data: dict, user, lang_code):
    deal_amount = message.text
    if not deal_amount.isdigit() or '-' in deal_amount:
        await message.answer(
            text=text[lang_code].default.message.wrong_data
        )
        return False
    if float(deal_amount) < 12:
        await message.answer(
            text=text[lang_code].default.message.wrong_data
        )
        return False
    if float(deal_amount) > user.balance:
        await message.answer(
            text=text[lang_code].default.message.not_enough_money
        )
        return False

    seller_id = int(state_data.get('seller_id'))
    seller = await User.get(seller_id)
    await state.update_data(amount=deal_amount)
    await message.answer(
        text=text[lang_code].default.message.confirm_deal_creation.format(
            bargin_amount=deal_amount,
            user_fullname=quote_html(seller.fullname),
            user_id=seller.id,
            user_username=format_username(seller.username)
        ),
        reply_markup=keyboards.default.reply.confirm_cancel.keyboard(lang_code)
    )
    await CreateBargainStates.wait_confirm_bargain.set()
