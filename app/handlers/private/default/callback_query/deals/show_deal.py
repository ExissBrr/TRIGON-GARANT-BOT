from venv import logger

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from loguru import logger

from app import keyboards
from app.data import text
from app.data.types.bargain_data import DealStatusType
from app.keyboards.callback_data.deal import deal_cd, DealCommands
from app.loader import dp
from app.utils.db_api.models.deals import Deal
from app.utils.db_api.models.user import User
from app.utils.format_data.time import timezone
from app.utils.format_data.user import format_username


@dp.callback_query_handler(deal_cd.filter(command=DealCommands.SHOW_DEAL))
async def show_sale_deals(call: CallbackQuery, state: FSMContext, callback_data: dict, lang_code, user):
    await call.answer(cache_time=30, text='One moment..')
    deal_id = int(callback_data.get('deal_id'))
    deal = await Deal.query.where(Deal.qf(id=deal_id)).where(
        Deal.qf(op='or', buyer_user_id=user.id, seller_user_id=user.id)).gino.first()

    if not deal:
        await call.message.answer(
            text=text[lang_code].default.call.message.deal_not_exist
        )
        return False

    buyer = await User.get(deal.buyer_user_id)
    seller = await User.get(deal.seller_user_id)
    is_seller = True
    if user.id == deal.buyer_user_id:
        is_seller = False
    if deal.status == DealStatusType.CLOSED:
        closed_date = timezone(deal.update_at, user.timezone).strftime('%Y-%m-%d %H:%M')
    else:
        closed_date = '-'
    if deal.status == DealStatusType.CLOSED:
        keyboard = None
    else:
        keyboard = keyboards.default.inline.deals.deal_operations.keyboard_deal_operate(lang_code=lang_code,
                                                                                        deal_id=deal.id,
                                                                                        deal_status=deal.status,
                                                                                        is_seller=is_seller)
    await call.message.answer(
        text=text[lang_code].default.message.deal_info.format(
            deal_id=deal.id,
            buyer_id=buyer.id,
            buyer_username=format_username(buyer.username),
            buyer_link=buyer.url_to_telegram,
            seller_id=seller.id,
            seller_link=seller.url_to_telegram,
            seller_username=format_username(seller.username),
            deal_amount=deal.amount,
            deal_start=timezone(deal.create_at, user.timezone).strftime('%Y-%m-%d %H:%M'),
            deal_closed=closed_date
        ),
        reply_markup=keyboard
    )