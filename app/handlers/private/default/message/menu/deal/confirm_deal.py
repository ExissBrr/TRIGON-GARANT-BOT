from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.data import text
from app.data.text.ru.button.reply import confirm
from app.loader import dp, config
from app.states.private.create_deal import CreateBargainStates
from app.utils.bot import send_main_keyboard
from app.utils.db_api.models.deals import Deal
from app.utils.db_api.models.user import User
from app.utils.format_data.user import format_username


@dp.message_handler(reply_command=confirm, state=CreateBargainStates.wait_confirm_bargain)
async def create_new_deal(message: Message, state: FSMContext, state_data: dict, user, lang_code):
    seller_id = int(state_data.get('seller_id'))
    deal_amount = int(state_data.get('amount'))
    await send_main_keyboard(user, state)

    new_user_balance = user.balance - deal_amount
    if new_user_balance < 0:
        return await message.answer('Error user balance')

    seller = await User.get(seller_id)
    await user.update_data(balance=new_user_balance)

    deal = await Deal.insert(
        seller_user_id=seller.id,
        buyer_user_id=user.id,
        amount=deal_amount
    )
    await message.answer(
        text=text[lang_code].default.message.overview_created_deal.format(
            deal_id=deal.id,
            deal_amount=deal_amount,
            user_id=seller.id,
            user_username=format_username(seller),
        )
    )

    await message.bot.send_message(
        chat_id=seller_id,
        text=text[lang_code].default.message.deal_created_with.format(
            user_link=user.url_to_telegram,
            user_id=user.id,
            deal_amount=deal_amount,
        )
    )
    await message.bot.send_message(
        chat_id=user.id,
        text=text[lang_code].default.message.deal_was_created_chat_info.format(
            deal_id=deal.id,
            seller_link_to_telegram=seller.url_to_telegram,
            seller_user_id=seller.id,
            seller_user_prefix=seller.prefix,
            buyer_link_to_telegram=user.url_to_telegram,
            buyer_user_id=user.id,
            buyer_user_prefix=user.prefix,
            deal_amount=deal_amount,
        )
    )
