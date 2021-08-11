from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.data import text
from app.data.text.ru import button
from app.loader import dp, config
from app.states.private.left_feedback import FeedbackForSeller
from app.utils.bot import send_main_keyboard
from app.utils.db_api.models.deals import Deal
from app.utils.db_api.models.feedback import Feedback
from app.utils.db_api.models.user import User
from app.utils.format_data.user import format_username, format_rate


@dp.message_handler(state=FeedbackForSeller.approve_feedback, reply_command=button.reply.confirm)
async def create_feedback(message: Message, state: FSMContext, state_data: dict, lang_code, user):
    await send_main_keyboard(user, state)
    deal_id = int(state_data.get('deal_id'))
    feedback_text = state_data.get('comment')
    feedback_rate = int(state_data.get('rate'))
    deal = await Deal.get(deal_id)
    buyer: User = await User.get(deal.buyer_user_id)
    seller: User = await User.get(deal.seller_user_id)

    feedback = await Feedback.insert(
        receiver_user_id=seller.id,
        rate=feedback_rate,
        commentator_user_id=buyer.id,
        comment=feedback_text,
    )

    await deal.update_data(feedback_id=feedback.id)

    await message.answer(
        text=text[lang_code].default.message.feedback_was_created.format(
            buyer_username=format_username(buyer),
            seller_username=format_username(seller),
            seller_link=seller.url_to_telegram,
            buyer_link=buyer.url_to_telegram,
            deal_id=deal.id,
            feedback_rate=format_rate(feedback.rate,1),
            feedback_text=feedback.comment
        )
    )
    await message.bot.send_message(
        chat_id=config.bot.chat_id_service,
        text=text[lang_code].default.message.feedback_was_created.format(
            buyer_username=format_username(buyer),
            seller_username=format_username(seller),
            seller_link=seller.url_to_telegram,
            buyer_link=buyer.url_to_telegram,
            deal_id=deal.id,
            feedback_rate=format_rate(feedback.rate,1),
            feedback_text=feedback.comment
        )
    )
