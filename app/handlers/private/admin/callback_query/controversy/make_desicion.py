from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.utils.markdown import quote_html

from app.data import text
from app.data.types.bargain_data import DealStatusType
from app.keyboards.callback_data.deal import DealAdminCommands, deal_cd
from app.loader import dp, config
from app.states.private.percent_controversy_division import StateDivideAmount
from app.utils.db_api.models.deals import Deal
from app.utils.db_api.models.user import User
from app.utils.format_data.user import format_username


@dp.callback_query_handler(deal_cd.filter(command=DealAdminCommands.ON_SELLERS_SIDE))
async def choose_seller(call: CallbackQuery, callback_data: dict, lang_code):
    deal_id = int(callback_data.get('deal_id'))
    deal = await Deal.get(deal_id)
    buyer: User = await User.get(deal.buyer_user_id)
    seller = await User.get(deal.seller_user_id)

    if deal.status != DealStatusType.CONTROVERSY:
        await call.message.edit_text(
            text=text[lang_code].admin.message.controversy_already_solved
        )
        return False

    await deal.update_data(status=DealStatusType.CLOSED)
    await seller.update_data(balance=seller.balance + deal.amount)
    await call.message.edit_text(
        text=text[lang_code].admin.message.decision_results.format(
            deal_id=deal.id,
            user1_username=format_username(seller),
            user1_link=seller.url_to_telegram,
            user2_username=format_username(buyer),
            user2_link=buyer.url_to_telegram,
            winner_username=format_username(seller),
            winner_link=seller.url_to_telegram,
        )
    )
    await call.message.bot.send_message(
        chat_id=seller.id,
        text=text[lang_code].default.message.controversy_was_won.format(
            deal_id=deal_id,
            user_username=format_username(buyer)
        )
    )
    await call.message.bot.send_message(
        chat_id=buyer.id,
        text=text[lang_code].default.message.controversy_was_lost.format(
            deal_id=deal_id,
            user_username=format_username(seller)
        )
    )
    await call.message.bot.send_message(
        chat_id=config.bot.main_chats_id,
        text=text.message.menu.default.controversy_chosen_side.format(
            deal_id=deal.id,
            seller_id=seller.id,
            seller_fullname=quote_html(seller),
            buyer_id=buyer.id,
            buyer_fullname=quote_html(buyer),
            deal_amount=deal.amount,
            winner_fullname=quote_html(seller)
        )
    )
    await call.answer()


@dp.callback_query_handler(deal_cd.filter(command=DealAdminCommands.ON_BUYERS_SIDE))
async def choose_seller(call: CallbackQuery, callback_data: dict, lang_code):
    deal_id = int(callback_data.get('deal_id'))
    deal = await Deal.get(deal_id)
    buyer: User = await User.get(deal.buyer_user_id)
    seller = await User.get(deal.seller_user_id)

    if deal.status != DealStatusType.CONTROVERSY:
        await call.message.edit_text(
            text=text[lang_code].admin.message.controversy_already_solved
        )
        return False

    await deal.update_data(status=DealStatusType.CLOSED)
    await buyer.update_data(balance=buyer.balance + deal.amount)
    await call.message.edit_text(
        text=text[lang_code].admin.message.decision_results.format(
            deal_id=deal.id,
            user1_username=format_username(seller),
            user1_link=seller.url_to_telegram,
            user2_username=format_username(buyer),
            user2_link=buyer.url_to_telegram,
            winner_username=format_username(buyer),
            winner_link=buyer.url_to_telegram,
        )
    )
    await call.message.bot.send_message(
        chat_id=seller.id,
        text=text[lang_code].default.message.controversy_was_lost.format(
            deal_id=deal_id,
            user_username=format_username(buyer)
        )
    )
    await call.message.bot.send_message(
        chat_id=buyer.id,
        text=text[lang_code].default.message.controversy_was_won.format(
            deal_id=deal_id,
            user_username=format_username(seller)
        )
    )
    await call.message.bot.send_message(
        chat_id=config.bot.main_chats_id,
        text=text.message.menu.default.controversy_chosen_side.format(
            deal_id=deal.id,
            seller_id=seller.id,
            seller_fullname=quote_html(seller),
            buyer_id=buyer.id,
            buyer_fullname=quote_html(buyer),
            deal_amount=deal.amount,
            winner_fullname=quote_html(buyer)
        )
    )
    await call.answer()


@dp.callback_query_handler(deal_cd.filter(command=DealAdminCommands.PERCENT_DIVISION))
async def divide_amount(call: CallbackQuery, state: FSMContext, callback_data: dict, lang_code):
    deal_id = int(callback_data.get('deal_id'))
    deal = await Deal.get(deal_id)

    if deal.status != DealStatusType.CONTROVERSY:
        await call.message.edit_text(
            text=text[lang_code].admin.message.controversy_already_solved
        )
        return False

    await state.update_data(deal_id=deal_id)
    await call.message.edit_text(
        text=text[lang_code].admin.message.percent_division
    )
    await StateDivideAmount.wait_for_percent.set()
    await call.answer()
