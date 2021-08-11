from aiogram.types import CallbackQuery

from app import keyboards
from app.data import text
from app.data.types.deal_data import DealStatusType
from app.keyboards.callback_data.deal import deal_cd, DealCommands
from app.loader import dp, config
from app.utils.db_api.models.deals import Deal
from app.utils.db_api.models.user import User


@dp.callback_query_handler(deal_cd.filter(command=DealCommands.PAY_DEAL))
async def pay_deal(call: CallbackQuery, callback_data: dict, lang_code):
    deal_id = int(callback_data.get('deal_id'))
    deal = await Deal.get(deal_id)

    if deal.status == DealStatusType.CLOSED:
        await call.message.edit_reply_markup()
        await call.answer(
            cache_time=10, text=text[lang_code].default.call.deal_closed
        )
        return False

    await call.answer(cache_time=5, text='One moment..')
    await deal.update_data(status=DealStatusType.CLOSED)
    buyer: User = await User.get(deal.buyer_user_id)
    seller: User = await User.get(deal.seller_user_id)
    await seller.update_data(balance=seller.balance + deal.amount)
    await call.message.edit_text(
        text=text[lang_code].default.message.successfull_deal.format(
            user_link=seller.url_to_telegram,
            user_id=seller.id
        ),
        reply_markup=keyboards.default.inline.deals.show_info.keyboard_show_deal_info(deal_id=deal.id,
                                                                                      lang_code=lang_code)
    )
    await call.message.bot.send_message(
        chat_id=seller.id,
        text=text[lang_code].default.message.successfull_deal.format(
            user_link=buyer.url_to_telegram,
            user_id=buyer.id
        ),
        reply_markup=keyboards.default.inline.deals.show_info.keyboard_show_deal_info(deal_id=deal.id,
                                                                                      lang_code=lang_code)
    )
    await call.message.bot.send_message(
        chat_id=config.bot.chat_id_service,
        text=text[lang_code].default.message.successful_deal_info.format(
            seller_id=seller.id,
            buyer_id=buyer.id,
            deal_amount=deal.amount,
        )
    )


@dp.callback_query_handler(deal_cd.filter(command=DealCommands.CANCEL_DEAL))
async def cancel_deal(call: CallbackQuery, callback_data: dict, lang_code):
    deal_id = int(callback_data.get('deal_id'))
    deal = await Deal.get(deal_id)

    if deal.status == DealStatusType.CLOSED:
        await call.answer(
            cache_time=10, text=text[lang_code].default.call.deal_closed
        )
        return False

    await call.answer(cache_time=5, text='One moment..')
    await deal.update_data(status=DealStatusType.CLOSED)
    buyer = await User.get(deal.buyer_user_id)
    seller = await User.get(deal.seller_user_id)
    await buyer.update_data(balance=buyer.balance + deal.amount)

    await call.message.edit_text(
        text=text[lang_code].default.message.unsuccessfull_deal.format(
            user_link=buyer.url_to_telegram,
            user_id=buyer.id
        ),
        reply_markup=keyboards.default.inline.deals.show_info.keyboard_show_deal_info(deal_id=deal.id,
                                                                                      lang_code=lang_code)
    )
    await call.message.bot.send_message(
        chat_id=buyer.id,
        text=text[lang_code].default.message.unsuccessfull_deal.format(
            user_link=seller.url_to_telegram,
            user_id=seller.id
        ),
        reply_markup=keyboards.default.inline.deals.show_info.keyboard_show_deal_info(deal_id=deal.id,
                                                                                      lang_code=lang_code)
    )
    await call.message.bot.send_message(
        chat_id=config.bot.chat_id_service,
        text=text[lang_code].default.message.unsuccessful_deal_info.format(
            seller_link=seller.url_to_telegram,
            seller_id=seller.id,
            buyer_link=buyer.url_to_telegram,
            buyer_id=buyer.id,
            deal_amount=deal.amount,
        )
    )


@dp.callback_query_handler(deal_cd.filter(command=DealCommands.CONTROVERSY_DEAL))
async def make_controversy_deal(call: CallbackQuery, callback_data: dict, user, lang_code):
    deal_id = int(callback_data.get('deal_id'))
    deal = await Deal.get(deal_id)

    if deal.status == DealStatusType.CLOSED:
        await call.answer(
            cache_time=10, text=text[lang_code].default.call.deal_closed, show_alert=True
        )
        return False
    if deal.status == DealStatusType.CONTROVERSY:
        await call.answer(
            cache_time=10, text=text[lang_code].default.call.deal_controversy, show_alert=True
        )
        return False
    await call.answer(cache_time=5, text='One moment..')
    await deal.update_data(status=DealStatusType.CONTROVERSY)
    buyer = await User.get(deal.buyer_user_id)
    seller = await User.get(deal.seller_user_id)
    if buyer.id == user.id:
        caller:User = buyer
        expectant:User=seller
    else:
        caller:User = seller
        expectant:User=buyer

    await call.message.bot.send_message(
        chat_id=buyer.id,
        text=text[lang_code].default.message.controversy_created.format(
            user_link=seller.url_to_telegram,
            user_id=seller.id
        ),
        reply_markup=keyboards.default.inline.deals.show_info.keyboard_show_deal_info(deal_id=deal.id,
                                                                                      lang_code=lang_code)
    )
    await call.message.bot.send_message(
        chat_id=seller.id,
        text=text[lang_code].default.message.controversy_created.format(
            user_link=buyer.url_to_telegram,
            user_id=buyer.id
        ),
        reply_markup=keyboards.default.inline.deals.show_info.keyboard_show_deal_info(deal_id=deal.id,
                                                                                      lang_code=lang_code)
    )
    await call.message.bot.send_message(
        chat_id=config.bot.chat_id_service,
        text=text[lang_code].default.message.controversy_created_chat_info.format(
            user_caller_link=caller.url_to_telegram,
            user_caller_id=caller.id,
            user_expectant_link=expectant.url_to_telegram,
            user_expectant_id=expectant.id,
        )
    )
