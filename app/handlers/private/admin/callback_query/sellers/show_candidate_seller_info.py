from aiogram.types import CallbackQuery

from app import keyboards
from app.data import text
from app.data.types.deal_data import DealStatusType, FeedbackRate
from app.data.types.feedback_data import FeedbackStatus
from app.keyboards.callback_data.sellers import sellers_cd, CommandsSellers
from app.loader import dp
from app.utils.bot.generate_links import make_start_link
from app.utils.db_api import db
from app.utils.db_api.models.deals import Deal
from app.utils.db_api.models.feedback import Feedback
from app.utils.db_api.models.sellers import Seller
from app.utils.db_api.models.user import User
from app.utils.format_data.user import format_username, format_rate


@dp.callback_query_handler(sellers_cd.filter(command=CommandsSellers.show_seller_candidate_info))
async def show_info(call: CallbackQuery, callback_data: dict, lang_code):
    await call.answer(cache_time=5, text='One moment..')
    seller_id = int(callback_data.get('seller_id'))
    seller_category = callback_data.get('category')
    seller = await Seller.query.where(Seller.user_id == seller_id).where(
        Seller.category == seller_category).gino.first()
    user = await User.get(seller.user_id)
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
    await call.message.answer(
        text=text[lang_code].admin.message.show_seller_info.format(
            seller_username=format_username(user),
            seller_id=seller.id,
            count_closed_successfully=deal_count,
            feedback_count=feedback_count,
            total_rate=format_rate(total_rate, feedback_count),
            seller_description=seller.description,
            user_id=user.id,
            user_link_feedback=user.link_feedback or link_feedback
        ),
        reply_markup=keyboards.admin.inline.sellers.seller_request_decision.make_keyboard_seller_request_decision(
            seller_id=seller_id, category=seller_category, lang_code=lang_code)
    )
