from aiogram.types import Message
from sqlalchemy import distinct

from app import keyboards
from app.data import text
from app.data.types.bargain_data import BargainStatusType, BargainRate
from app.utils.db_api import db
from app.utils.db_api.models.bargain import Bargain
from app.utils.db_api.models.feedback import Feedback
from app.utils.db_api.models.user import User
from app.utils.db_api.models.views import View
from app.utils.format_data.user import format_rate


@dp.message_handler(reply_command=text.button.reply.default.menu_profile)
async def send_profile(message: Message, user: User, lang_code):
    list_shopping = await Bargain.query.where(Bargain.status == BargainStatusType.CLOSED_SUCCESSFUL).where(
        Bargain.buyer_id == user.id).gino.all()
    list_sales = await Bargain.query.where(Bargain.status == BargainStatusType.CLOSED_SUCCESSFUL).where(
        Bargain.seller_id == user.id).gino.all()
    feedback_count = await db.select([db.func.count(Bargain.rate)]). \
        where(Bargain.rate != BargainRate.NONE). \
        where(Bargain.seller_user_id == user.id).gino.scalar() or 0
    total_rate = await db.select([db.func.sum(Bargain.rate)]). \
        where(Bargain.rate != BargainRate.NONE). \
        where(Bargain.seller_user_id == user.id).gino.scalar() or 0

    view_count = await db.select([db.func.count(distinct(View.viewer_user_id))]).where(
        View.user_id == user.id).gino.scalar()

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
    feedbacks = await Feedback.query.where(Feedback.seller_user_id == message.from_user.id)
    if feedbacks:
        link_feedback = f'<a href="t.me/{bot_data.username}?start=feedback_{user.id}">Ссылка на отзывы</a>'

    await message.answer_photo(
        photo=photo,
        caption=text.message.menu.default.profile.format(
            user_id=user.id,
            user_username=user.username,
            registration_date=str(user.create_at).split('.')[0],
            user_balance=round(user.balance, 2),
            user_rate=await format_rate(total_rate, feedback_count),
            count_views=view_count,
            total_amount_shopping=sum([bargain.amount for bargain in list_shopping]),
            total_amount_sales=sum([bargain.amount for bargain in list_sales]),
            link_feedback=link_feedback
        ),
        reply_markup=keyboards.default.inline.menu_profile.keyboard(lang_code=lang_code)
    )
