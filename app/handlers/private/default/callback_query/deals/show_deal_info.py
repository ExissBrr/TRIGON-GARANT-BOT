from aiogram.types import CallbackQuery

from app import keyboards
from app.data import text
from app.data.types.deal_data import DealStatusType
from app.keyboards.callback_data.deal import deal_cd, DealCommands
from app.loader import dp
from app.utils.db_api.models.deals import Deal
from app.utils.db_api.models.user import User
from app.utils.format_data.time import timezone
from app.utils.format_data.user import format_username


@dp.callback_query_handler(deal_cd.filter(command=DealCommands.SHOW_DEAL_INFO))
async def show_info(call: CallbackQuery, callback_data: dict, lang_code, user):
    await call.answer(cache_time=30, text='One moment..')
    deal_id = int(callback_data.get('deal_id'))
    deal = await Deal.get(deal_id)
    seller = await User.get(deal.seller_user_id)
    buyer = await User.get(deal.buyer_user_id)
    is_buyer = False
    if user.id == buyer.id:
        is_buyer = True
    if deal.status == DealStatusType.CLOSED:
        closed_date = timezone(deal.update_at, user.timezone).strftime('%Y-%m-%d %H:%M')
        keyboard = keyboards.default.inline.deals.left_feedback.keyboard_feedback(deal_id=deal.id,
                                                                                  is_buyer=is_buyer,
                                                                                  lang_code=lang_code)
    else:
        closed_date = '-'
        keyboard = None

    await call.message.answer(
        text=text[lang_code].default.message.deal_info.format(
            deal_id=deal.id,
            buyer_id=buyer.id,
            buyer_username=format_username(buyer),
            buyer_link=buyer.url_to_telegram,
            seller_id=seller.id,
            seller_link=seller.url_to_telegram,
            seller_username=format_username(seller),
            deal_amount=deal.amount,
            deal_start=timezone(deal.create_at, user.timezone).strftime('%Y-%m-%d %H:%M'),
            deal_closed=closed_date
        ),
        reply_markup=keyboard
    )
