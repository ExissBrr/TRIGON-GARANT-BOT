from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app import keyboards
from app.data import text
from app.data.types.bargain_data import FeedbackRate, DealStatusType
from app.data.types.feedback_data import FeedbackStatus
from app.loader import dp
from app.states.private.search_seller import SellerSearch
from app.utils.bot.generate_links import make_start_link
from app.utils.db_api import db
from app.utils.db_api.models.deals import Deal
from app.utils.db_api.models.feedback import Feedback
from app.utils.db_api.models.sellers import Seller
from app.utils.db_api.models.user import User
from app.utils.format_data.user import format_username, format_rate


@dp.message_handler(state=SellerSearch.wait_for_seller_number)
async def show_seller_info(message: Message, state: FSMContext, lang_code):
    await state.finish()
    if not message.text.isdigit():
        return await message.answer(
            text=text[lang_code].default.message.wrong_data
        )
    seller_number = int(message.text)

    if not await Seller.get(seller_number):
        return await message.answer(
            text=text[lang_code].admin.message.wrong_seller
        )

    seller = await Seller.get(seller_number)
    user = await User.get(seller.user_id)

    deal_count = await db.select([db.func.count(Deal.id)]).where(Deal.seller_user_id == user.id).where(
        Deal.status == DealStatusType.CLOSED).gino.scalar()
    feedback_count = await db.select([db.func.count(Feedback.id)]).where(Feedback.receiver_user_id == user.id).where(
        Feedback.status == FeedbackStatus.ACTIVE).gino.scalar()
    total_rate = await db.select([db.func.sum(Feedback.rate)]). \
        where(Feedback.rate != FeedbackRate.NONE). \
        where(Feedback.receiver_user_id == user.id).gino.scalar() or 0

    bot_data = await message.bot.get_me()
    link_feedback = text[lang_code].default.message.none_feedbacks
    if feedback_count >= 1:
        link_feedback = make_start_link(bot_data.username, 'feedback', feedback_user_id=user.id)

    await message.answer(
        text=text[lang_code].admin.message.show_seller_info.format(
            seller_username=format_username(user),
            seller_id=seller.id,
            count_closed_successfully=deal_count,
            feedback_count=feedback_count,
            total_rate=format_rate(total_rate, feedback_count),
            seller_description=seller.description,
            user_id=user.id,
            seller_status=seller.status,
            user_link_feedback=link_feedback
        ),
        reply_markup=await keyboards.admin.inline.sellers.reveal_hide_seller.make_keyboard_modify_seller(seller_number,
                                                                                                         lang_code)
    )
