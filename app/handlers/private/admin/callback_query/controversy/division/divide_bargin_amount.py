from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app import keyboards
from app.data import text
from app.loader import dp
from app.states.private.percent_controversy_division import StateDivideAmount
from app.utils.db_api.models.deals import Deal
from app.utils.db_api.models.user import User
from app.utils.format_data.user import format_username


@dp.message_handler(state=StateDivideAmount.wait_for_percent)
async def make_decision(message: Message, state: FSMContext,state_data:dict, lang_code):
    state_data = await state.get_data()
    deal_id = int(state_data.get('deal_id'))
    deal = await Deal.get(deal_id)
    buyer: User = await User.get(deal.buyer_user_id)
    seller: User = await User.get(deal.seller_user_id)
    try:
        buyer_share, seller_share = list(map(int, message.text.split('-')))
    except ValueError:
        return await message.answer(
            text=text[lang_code].default.message.wrong_data
        )

    if buyer_share + seller_share != 100:
        return await message.answer(
            text=text[lang_code].default.message.wrong_data
        )

    await state.update_data(buyer_share=buyer_share)
    await StateDivideAmount.accept_decision.set()
    await message.answer(
        text=text[lang_code].admin.message.confirm_devision_desicion.format(
            buyer_username=format_username(buyer),
            buyer_share=buyer_share,
            seller_username=format_username(seller),
            seller_share=seller_share
        ),
        reply_markup=keyboards.default.reply.confirm_cancel.keyboard(lang_code)
    )
