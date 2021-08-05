from aiogram.types import Message

from app import keyboards
from app.data import text
from app.data.types.feedback_data import FeedbackStatus
from app.filters.private.message.start_link import StartLink
from app.loader import dp
from app.utils.db_api.models.feedback import Feedback
from app.utils.db_api.models.user import User


@dp.message_handler(StartLink('feedback'))
async def send_feedback(message: Message, user, lang_code, message_args: dict):
    wanted_user: User = await User.get(int(message_args.get('feedback_user_id')))
    feedbacks = await Feedback.query.where(Feedback.status == FeedbackStatus.ACTIVE).where(
        Feedback.receiver_user_id == wanted_user.id).gino.all()
    if not feedbacks:
        return await message.answer(
            text=text[lang_code].default.message.wrong_data
        )

    await message.answer(
        text=text[lang_code].default.message.users_feedbacks.format(
            user_link=wanted_user.url_to_telegram,
            user_id=wanted_user.id,
        ),
        reply_markup=await keyboards.default.inline.feedbacks.show_feedback_list.make_keyboard_feedbacks_list(feedbacks)
    )
