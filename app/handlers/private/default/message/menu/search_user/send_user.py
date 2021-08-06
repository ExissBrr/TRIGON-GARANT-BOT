from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.handler import SkipHandler
from aiogram.types import Message
from sqlalchemy import distinct

from app import keyboards
from app.data import text
from app.data.types.bargain_data import FeedbackRate
from app.loader import dp
from app.loader import links
from app.states.private.search import UserSearchStates
from app.utils.bot import send_main_keyboard
from app.utils.db_api import db
from app.utils.db_api.models.deals import Deal
from app.utils.db_api.models.feedback import Feedback
from app.utils.db_api.models.user import User
from app.utils.db_api.models.user_views import UserView
from app.utils.format_data.time import timezone
from app.utils.format_data.user import format_rate, format_username


@dp.message_handler(state=UserSearchStates.wait_for_user_data)
async def send_user_profile(message: Message, state: FSMContext, lang_code, user):
    if message.forward_from:
        userdata = str(message.forward_from.id)
    else:
        userdata = message.text.replace('@', '').lower()

    if userdata.isdigit():
        if user.id == int(userdata):
            await message.answer(
                text=text[lang_code].default.message.cant_search_yourself
            )
            raise SkipHandler
        found_user = await User.query.where(User.qf(id=userdata)).gino.first()
    else:
        found_user = await User.query.where(db.func.lower(User.username) == userdata).gino.first()

    await send_main_keyboard(user, state)
    if not found_user:
        await message.answer(
            text=text[lang_code].default.message.user_not_found
        )
        return False

    await UserView.insert(
        viewer_user_id=message.from_user.id,
        user_id=found_user.id
    )

    found_user_photos = (await message.bot.get_user_profile_photos(user_id=found_user.id)).photos
    if found_user_photos:
        found_user_photo = found_user_photos[0][-1].file_id
    else:
        found_user_photo = links.photo.user_no_photo

    keyboard = await keyboards.default.inline.user_search.user_interaction.make_keyboard_user_interaction(
        lang_code=lang_code,
        found_user_id=found_user.id,
        user_id=user.id)

    view_count = await db.select([db.func.count(distinct(UserView.viewer_user_id))]).where(
        UserView.user_id == found_user.id).gino.scalar()
    feedback_count = await db.select([db.func.count(Feedback.rate)]). \
        where(Feedback.rate != FeedbackRate.NONE). \
        where(Feedback.receiver_user_id == found_user.id).gino.scalar() or 0
    total_rate = await db.select([db.func.sum(Feedback.rate)]). \
        where(Feedback.rate != FeedbackRate.NONE). \
        where(Feedback.receiver_user_id == user.id).gino.scalar() or 0

    count_sale_bargains = await db.select([db.func.count(Deal.id)]). \
        where(Deal.seller_user_id == found_user.id).gino.scalar()

    count_buy_bargains = await db.select([db.func.count(Deal.id)]). \
        where(Deal.buyer_user_id == found_user.id).gino.scalar()

    count_all_bargains = count_sale_bargains + count_buy_bargains

    await message.answer_photo(
        photo=found_user_photo,
        caption=text[lang_code].default.message.user_info.format(
            rate_star=format_rate(total_rate, feedback_count),
            user_datetime_register=timezone(found_user.create_at, user.timezone).strftime('%Y-%m-%d %H:%M'),
            user_id=found_user.id,
            user_prefix=found_user.prefix,
            user_username=format_username(found_user),
            user_views=view_count,
            count_all_bargains=count_all_bargains,
            count_sale_bargains=count_sale_bargains,
            count_buy_bargains=count_buy_bargains,
        ),
        reply_markup=keyboard
    )
