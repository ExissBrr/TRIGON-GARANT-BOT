from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.keyboards.callback_data.feedback import feedback_cd, FeedbackCommands
from app.utils.db_api.models.user import User
from app.utils.format_data.user import format_username, format_rate


async def make_keyboard_feedbacks_list(feedbacks):
    markup = InlineKeyboardMarkup()
    for feedback in feedbacks[-9:]:
        buyer = await User.get(int(feedback.commentator_user_id))
        markup.row(
            InlineKeyboardButton(
                text=f'{format_username(buyer.username)}:\n {format_rate(feedback.rate, 1)}',
                callback_data=feedback_cd.new(feedback_id=feedback.id, command=FeedbackCommands.SHOW_FEEDBACK)
            )
        )
    return markup
