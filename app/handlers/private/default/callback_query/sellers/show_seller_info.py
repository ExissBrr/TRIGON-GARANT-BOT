from aiogram.types import CallbackQuery

from app.data import text
from app.data.types.deal_data import DealStatusType, FeedbackRate
from app.keyboards.callback_data.sellers import CommandsSellers, sellers_cd
from app.loader import dp
from app.utils.bot.generate_links import make_start_link
from app.utils.db_api import db
from app.utils.db_api.models.deals import Deal
from app.utils.db_api.models.feedback import Feedback
from app.utils.db_api.models.sellers import Seller
from app.utils.db_api.models.user import User
from app.utils.format_data.user import format_username, format_rate


@dp.callback_query_handler(sellers_cd.filter(command=CommandsSellers.show_seller_info))
async def show_seller_stat(call: CallbackQuery, callback_data: dict, lang_code):
    await call.answer(cache_time=30)
    seller_id = int(callback_data.get('seller_id'))
    seller_category = callback_data.get('category')
    seller = await Seller.query.where(Seller.user_id == seller_id).where(
        Seller.category == seller_category).gino.first()
    user_seller: User = await User.get(seller_id)

    link_feedback = text[lang_code].default.message.none_feedbacks

    bot_data = await dp.bot.get_me()
    feedbacks = await Feedback.query.where(Feedback.receiver_user_id == user_seller.id).gino.all()

    if feedbacks:
        link_feedback = make_start_link(bot_data.username, 'feedback', feedback_user_id=user_seller.id)

    feedback_count = await db.select([db.func.count(Feedback.rate)]). \
        where(Feedback.rate != FeedbackRate.NONE). \
        where(Feedback.receiver_user_id == user_seller.id).gino.scalar() or 0

    total_rate = await db.select([db.func.sum(Feedback.rate)]). \
        where(Feedback.rate != FeedbackRate.NONE). \
        where(Feedback.receiver_user_id == user_seller.id).gino.scalar() or 0
    await call.message.answer(
        text=text[lang_code].default.message.show_seller_info.format(
            seller_username=format_username(user_seller),
            seller_id=seller.id,
            count_closed_successfully=await Deal.query.where(Deal.seller_user_id == user_seller.id).where(
                Deal.status == DealStatusType.CLOSED).gino.scalar(),
            feedback_count=feedback_count,
            total_rate=format_rate(total_rate,feedback_count),
            seller_description=seller.description,
            user_id=seller_id,
            user_link_feedback=link_feedback
        ),
        disable_web_page_preview=True
    )
