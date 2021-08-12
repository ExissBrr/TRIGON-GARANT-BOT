from aiogram.types import CallbackQuery

from app import keyboards
from app.data import text
from app.data.types.deal_data import DealStatusType, FeedbackRate
from app.data.types.feedback_data import FeedbackStatus
from app.data.types.seller_data import SellerStatus
from app.keyboards.callback_data.admin import seller_menu_cd, SellerMenuChoice
from app.loader import dp
from app.utils.bot.generate_links import make_start_link
from app.utils.db_api import db
from app.utils.db_api.models.deals import Deal
from app.utils.db_api.models.feedback import Feedback
from app.utils.db_api.models.sellers import Seller
from app.utils.db_api.models.user import User
from app.utils.format_data.user import format_username, format_rate


@dp.callback_query_handler(seller_menu_cd.filter(command=SellerMenuChoice.HIDE_SELLER))
async def hide_seller(call: CallbackQuery, callback_data: dict, lang_code):
    await call.answer(cache_time=5, text='One moment..')
    seller_number = int(callback_data.get('seller_number'))
    seller = await Seller.get(seller_number)
    user = await User.get(seller.user_id)
    await seller.update_data(status=SellerStatus.HIDDEN)
    deal_count = await db.select([db.func.count(Deal.id)]).where(Deal.seller_user_id == user.id).where(
        Deal.status == DealStatusType.CLOSED).gino.scalar()
    feedback_count = await db.select([db.func.count(Feedback.id)]).where(Feedback.receiver_user_id == user.id).where(
        Feedback.status == FeedbackStatus.ACTIVE).gino.scalar()
    total_rate = await db.select([db.func.sum(Feedback.rate)]). \
        where(Feedback.rate != FeedbackRate.NONE). \
        where(Feedback.receiver_user_id == user.id).gino.scalar() or 0

    bot_data = await call.bot.get_me()
    link_feedback = text[lang_code].default.message.none_feedbacks
    if feedback_count >= 1:
        link_feedback = make_start_link(bot_data.username, 'feedback', feedback_user_id=user.id)

    await call.message.edit_text(
        text=text[lang_code].admin.message.show_seller_info.format(
            seller_username=format_username(user),
            seller_id=seller.id,
            count_closed_successfully=deal_count,
            feedback_count=feedback_count,
            total_rate=format_rate(total_rate, feedback_count),
            seller_description=seller.description,
            user_id=user.id,
            user_link_feedback=user.link_feedback or link_feedback,
            seller_status=seller.status
        ),
        reply_markup=await keyboards.admin.inline.sellers.reveal_hide_seller.make_keyboard_modify_seller(seller_number,
                                                                                                         lang_code)
    )


@dp.callback_query_handler(seller_menu_cd.filter(command=SellerMenuChoice.REVEAL_SELLER))
async def hide_seller(call: CallbackQuery, callback_data: dict, lang_code):
    await call.answer(cache_time=5, text='One moment..')
    seller_number = int(callback_data.get('seller_number'))
    seller = await Seller.get(seller_number)
    user = await User.get(seller.user_id)

    await seller.update_data(status=SellerStatus.ACTIVE)

    deal_count = await db.select([db.func.count(Deal.id)]).where(Deal.seller_user_id == user.id).where(
        Deal.status == DealStatusType.CLOSED).gino.scalar()
    feedback_count = await db.select([db.func.count(Feedback.id)]).where(Feedback.receiver_user_id == user.id).where(
        Feedback.status == FeedbackStatus.ACTIVE).gino.scalar()
    total_rate = await db.select([db.func.sum(Feedback.rate)]). \
        where(Feedback.rate != FeedbackRate.NONE). \
        where(Feedback.receiver_user_id == user.id).gino.scalar() or 0

    bot_data = await call.bot.get_me()
    link_feedback = text[lang_code].default.message.none_feedbacks
    if feedback_count >= 1:
        link_feedback = make_start_link(bot_data.username, 'feedback', feedback_user_id=user.id)

    await call.message.edit_text(
        text=text[lang_code].admin.message.show_seller_info.format(
            seller_username=format_username(user),
            seller_id=seller.id,
            count_closed_successfully=deal_count,
            feedback_count=feedback_count,
            total_rate=format_rate(total_rate, feedback_count),
            seller_description=seller.description,
            user_id=user.id,
            user_link_feedback=user.link_feedback or link_feedback,
            seller_status=seller.status
        ),
        reply_markup=await keyboards.admin.inline.sellers.reveal_hide_seller.make_keyboard_modify_seller(seller_number,
                                                                                                         lang_code)
    )
