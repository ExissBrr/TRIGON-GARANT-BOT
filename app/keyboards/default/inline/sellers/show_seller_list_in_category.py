from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.data.types.deal_data import FeedbackRate
from app.keyboards.callback_data.sellers import sellers_cd, CommandsSellers
from app.utils.db_api import db
from app.utils.db_api.models.feedback import Feedback
from app.utils.db_api.models.user import User
from app.utils.format_data.user import format_username, format_rate


async def make_keyboard_sellers_list(sellers: list, category_name):
    markup = InlineKeyboardMarkup()
    for seller in sellers:
        sel_user = await User.get(int(seller.user_id))
        feedback_count = await db.select([db.func.count(Feedback.rate)]). \
            where(Feedback.rate != FeedbackRate.NONE). \
            where(Feedback.receiver_user_id == sel_user.id).gino.scalar() or 0

        total_rate = await db.select([db.func.sum(Feedback.rate)]). \
            where(Feedback.rate != FeedbackRate.NONE). \
            where(Feedback.receiver_user_id == sel_user.id).gino.scalar() or 0

        markup.row(
            InlineKeyboardButton(
                text=f"{format_username(sel_user)} {format_rate(total_rate,feedback_count)}",
                callback_data=sellers_cd.new(seller_id=sel_user.id, category=category_name,
                                             command=CommandsSellers.show_seller_info)
            )
        )
    return markup
