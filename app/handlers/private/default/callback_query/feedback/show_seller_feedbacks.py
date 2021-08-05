from aiogram.types import CallbackQuery

from app import keyboards
from app.data import text
from app.data.types.feedback_data import FeedbackStatus
from app.keyboards.callback_data.user import user_cd, UserCommand
from app.loader import dp
from app.utils.db_api.models.feedback import Feedback
from app.utils.db_api.models.user import User


@dp.callback_query_handler(user_cd.filter(command=UserCommand.GET_SELLER_FEEDBACKS))
async def show_feedback(call: CallbackQuery, callback_data: dict, user, lang_code):
    await call.answer(text='One moment..', cache_time=5)
    seller = await User.get(int(callback_data.get('user_id')))

    feedbacks = await Feedback.query.where(Feedback.status == FeedbackStatus.ACTIVE).where(
        Feedback.receiver_user_id == seller.id).gino.all()
    if not feedbacks:
        return await call.message.answer(
            text=text[lang_code].default.message.wrong_data
        )

    await call.message.answer(
        text=text[lang_code].default.message.users_feedbacks.format(
            user_link=seller.url_to_telegram,
            user_id=seller.id,
        ),
        reply_markup=await keyboards.default.inline.feedbacks.show_feedback_list.make_keyboard_feedbacks_list(feedbacks)
    )
