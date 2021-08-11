from aiogram.types import CallbackQuery

from app import keyboards
from app.data import text
from app.data.types.deal_data import DealStatusType
from app.keyboards.callback_data.deal import user_deal_cd, UserDealCommands
from app.loader import dp
from app.utils.db_api.models.deals import Deal


@dp.callback_query_handler(user_deal_cd.filter(command=UserDealCommands.SHOW_SELLING_LIST))
async def show_my_sales(call: CallbackQuery, user, lang_code):
    await call.answer(cache_time=5, text='One moment..')
    deals = await Deal.query.where(Deal.seller_user_id == user.id).where(
        Deal.status == DealStatusType.ACTIVE).gino.all()
    if not deals:
        return await call.message.answer(
            text=text[lang_code].default.message.empty_deals
        )

    await call.message.edit_text(
        text=text[lang_code].default.message.your_sales,
        reply_markup=await keyboards.default.inline.deals.show_deals_list.make_keyboard_selling_list(deals)
    )


@dp.callback_query_handler(user_deal_cd.filter(command=UserDealCommands.SHOW_SHOPPING_LIST))
async def show_my_sales(call: CallbackQuery, user, lang_code):
    await call.answer(cache_time=5, text='One moment..')
    deals = await Deal.query.where(Deal.buyer_user_id == user.id).where(
        Deal.status == DealStatusType.ACTIVE).gino.all()
    if not deals:
        return await call.message.answer(
            text=text[lang_code].default.message.empty_deals
        )

    await call.message.edit_text(
        text=text[lang_code].default.message.your_purchase,
        reply_markup=await keyboards.default.inline.deals.show_deals_list.make_keyboard_shopping_list(deals)
    )


@dp.callback_query_handler(user_deal_cd.filter(command=UserDealCommands.SHOW_CONTROVERSY_LIST))
async def show_my_sales(call: CallbackQuery, user, lang_code):
    await call.answer(cache_time=5, text='One moment..')
    deals = await Deal.query.where(Deal.qf(op='or', seller_user_id=user.id, buyer_user_id=user.id)).where(
        Deal.status == DealStatusType.CONTROVERSY).gino.all()
    if not deals:
        return await call.message.answer(
            text=text[lang_code].default.message.empty_deals
        )

    await call.message.edit_text(
        text=text[lang_code].default.message.your_controversy_deals,
        reply_markup=await keyboards.default.inline.deals.show_deals_list.make_keyboard_controversy_list(deals, user.id)
    )
