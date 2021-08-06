from aiogram.types import CallbackQuery

from app.data import text
from app.keyboards.callback_data.feedback import feedback_cd, FeedbackCommands
from app.loader import dp
from app.utils.db_api.models.feedback import Feedback
from app.utils.db_api.models.user import User
from app.utils.format_data.time import timezone
from app.utils.format_data.user import format_rate, format_username


@dp.callback_query_handler(feedback_cd.filter(command=FeedbackCommands.SHOW_FEEDBACK))
async def show_feedback(call: CallbackQuery, callback_data: dict,user, lang_code):
    await call.answer(text='One moment..', cache_time=5)
    feedback = await Feedback.get(int(callback_data.get('feedback_id')))
    buyer:User = await User.get(int(feedback.commentator_user_id))
    await call.message.answer(
        text=text[lang_code].default.message.feedback_text.format(
            deal_rate=format_rate(feedback.rate, 1),
            buyer_link=buyer.url_to_telegram,
            buyer_username=format_username(buyer),
            feedback_date=timezone(user.create_at, user.timezone).strftime('%Y-%m-%d %H:%M'),
            deal_comment=feedback.comment
        )
    )
