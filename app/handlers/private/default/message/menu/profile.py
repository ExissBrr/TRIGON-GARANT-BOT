from aiogram.types import Message
from sqlalchemy import distinct

from app import keyboards
from app.data import text
from app.data.text.ru.button.reply import profile
from app.data.types.bargain_data import DealStatusType, FeedbackRate
from app.loader import dp
from app.utils.bot.generate_links import make_start_link
from app.utils.db_api import db
from app.utils.db_api.models.deals import Deal
from app.utils.db_api.models.feedback import Feedback
from app.utils.db_api.models.user import User
from app.utils.db_api.models.user_views import UserView
from app.utils.format_data.time import timezone
from app.utils.format_data.user import format_rate


@dp.message_handler(reply_command=profile)
async def send_profile(message: Message, user: User, bot_data, lang_code):
    list_shopping = await Deal.query.where(Deal.status == DealStatusType.CLOSED).where(
        Deal.buyer_user_id == user.id).gino.all()
    list_sales = await Deal.query.where(Deal.status == DealStatusType.CLOSED).where(
        Deal.seller_user_id == user.id).gino.all()

    feedback_count = await db.select([db.func.count(Feedback.rate)]). \
        where(Feedback.rate != FeedbackRate.NONE). \
        where(Feedback.receiver_user_id == user.id).gino.scalar() or 0

    total_rate = await db.select([db.func.sum(Feedback.rate)]). \
        where(Feedback.rate != FeedbackRate.NONE). \
        where(Feedback.receiver_user_id == user.id).gino.scalar() or 0

    view_count = await db.select([db.func.count(distinct(UserView.viewer_user_id))]).where(
        UserView.user_id == user.id).gino.scalar()

    photos = await message.from_user.get_profile_photos()
    try:
        photo = photos['photos'][0][-1].file_id
    except:
        # Загрузится аватарка бота, если у пользователя нет аватарки
        bot_data = await message.bot.get_me()
        photos = await bot_data.get_profile_photos()
        photo = photos['photos'][0][-1].file_id

    link_feedback = 'Отзывы отсутствуют'

    bot_data = await message.bot.get_me()
    feedbacks = await Feedback.query.where(Feedback.receiver_user_id == message.from_user.id).gino.all()
    if feedbacks:
        link_feedback = make_start_link(bot_data.username, 'feedback', feedback_user_id=user.id)

    await message.answer_photo(
        photo=photo,
        caption=text[lang_code].default.message.profile.format(
            user_id=user.id,
            user_prefix=user.prefix,
            user_username=user.username,
            registration_date=timezone(user.create_at, user.timezone).strftime('%Y-%m-%d %H:%M'),
            user_balance=round(user.balance, 2),
            user_rate=format_rate(total_rate, feedback_count),
            count_views=view_count,
            total_amount_shopping=sum([bargain.amount for bargain in list_shopping]),
            total_amount_sales=sum([bargain.amount for bargain in list_sales]),
            link_feedback=link_feedback
        ),
        reply_markup=keyboards.default.inline.menu_profile.keyboard(lang_code=lang_code)
    )
