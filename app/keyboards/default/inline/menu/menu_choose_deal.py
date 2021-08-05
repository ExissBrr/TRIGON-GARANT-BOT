from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.data import text
from app.data.types.bargain_data import DealStatusType
from app.keyboards.callback_data.deal import user_deal_cd, UserDealCommands
from app.utils.db_api import db
from app.utils.db_api.models.deals import Deal


async def make_keyboard(user_id: int, lang_code):
    count_seller_deals = await db.select([db.func.count(Deal.id)]).where(
        Deal.status == DealStatusType.ACTIVE).where(
        Deal.seller_user_id == user_id).gino.scalar()
    count_buyer_deals = await db.select([db.func.count(Deal.id)]).where(
        Deal.status == DealStatusType.ACTIVE).where(
        Deal.buyer_user_id == user_id).gino.scalar()
    count_controversy_deals = await db.select([db.func.count(Deal.id)]).where(
        Deal.status == DealStatusType.CONTROVERSY).where(
        Deal.qf(op='or', seller_user_id=user_id, buyer_user_id=user_id)).gino.scalar()
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton(
            text=f'{text[lang_code].button.inline.sales}({count_seller_deals})',
            callback_data=user_deal_cd.new(user_id=user_id, command=UserDealCommands.SHOW_SELLING_LIST)
        )
    )
    markup.insert(
        InlineKeyboardButton(
            text=f'{text[lang_code].button.inline.purchase}({count_buyer_deals})',
            callback_data=user_deal_cd.new(user_id=user_id, command=UserDealCommands.SHOW_SHOPPING_LIST)
        )
    )
    if count_controversy_deals != 0:
        markup.row(
            InlineKeyboardButton(
                text=f'{text[lang_code].button.inline.controversy_deals}({count_controversy_deals})',
                callback_data=user_deal_cd.new(user_id=user_id, command=UserDealCommands.SHOW_CONTROVERSY_LIST)
            )
        )
    return markup
