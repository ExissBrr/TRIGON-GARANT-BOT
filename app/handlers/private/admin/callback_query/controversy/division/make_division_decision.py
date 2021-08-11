from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.data import text
from app.data.text.ru.button.reply import confirm
from app.data.types.deal_data import DealStatusType
from app.loader import dp
from app.states.private.percent_controversy_division import StateDivideAmount
from app.utils.bot import send_main_keyboard
from app.utils.db_api.models.deals import Deal
from app.utils.db_api.models.user import User
from app.utils.format_data.user import format_username


@dp.message_handler(reply_command=confirm, state=StateDivideAmount.accept_decision)
async def accept_controversy_decision(message: Message, user, state: FSMContext, state_data: dict, lang_code):
    state_data = await state.get_data()
    deal_id = int(state_data.get('deal_id'))
    buyer_share = int(state_data.get('buyer_share'))
    seller_share = 100 - buyer_share

    deal = await Deal.get(deal_id)
    buyer: User = await User.get(deal.buyer_user_id)
    seller: User = await User.get(deal.seller_user_id)
    if deal.status != DealStatusType.CONTROVERSY:
        await message.edit_text(
            text=text[lang_code].admin.message.controversy_already_solved
        )
        return False

    await deal.update_data(status=DealStatusType.CLOSED)

    buyer_amount = (buyer_share * deal.amount) / 100
    seller_amount = (seller_share * deal.amount) / 100
    await buyer.update_data(balance=buyer.balance + buyer_amount)
    await seller.update_data(balance=seller.balance + seller_amount)

    await message.answer(
        text=text[lang_code].admin.message.decision_division_taken.format(
            deal_id=deal.id,
            seller_username=format_username(seller),
            seller_amount=seller_amount,
            buyer_username=format_username(buyer),
            buyer_amount=buyer_amount,
        )
    )
    await message.bot.send_message(
        chat_id=buyer.id,
        text=text[lang_code].default.message.controversy_money_return.format(
            user_username=format_username(seller),
            share=buyer_share,
            amount=buyer_amount
        )
    )
    await message.bot.send_message(
        chat_id=seller.id,
        text=text[lang_code].default.message.controversy_money_return.format(
            user_username=format_username(buyer),
            share=seller_share,
            amount=seller_amount
        )
    )
    await send_main_keyboard(user, state)
