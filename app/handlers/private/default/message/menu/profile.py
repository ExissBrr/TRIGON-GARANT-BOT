from aiogram.types import Message

from data import text
from keyboards import inline
from loader import dp
from utils.database_api.table_models.bargin import DBCommandsBargin, BarginStatusType
from utils.database_api.table_models.feedback import DBCommandsFeedback
from utils.database_api.table_models.user import User
from utils.database_api.table_models.views import View, make_filter
from utils.parse_data.user import make_user_star_rate


@dp.message_handler(reply_command=text.button.reply.default.menu_profile)
async def send_profile(message: Message, user: User):
    list_shopping = await DBCommandsBargin.get_bargins(status=BarginStatusType.CLOSED_SUCCESSFUL, buyer_id=user.id)
    list_sales = await DBCommandsBargin.get_bargins(status=BarginStatusType.CLOSED_SUCCESSFUL, seller_id=user.id)
    photos = await message.from_user.get_profile_photos()
    try:
        photo = photos['photos'][0][-1].file_id
    except:
        # Загрузится аватарка бота, если у пользователя нет аватарки
        bot_data = await dp.bot.get_me()
        photos = await bot_data.get_profile_photos()
        photo = photos['photos'][0][-1].file_id

    link_feedback = 'Отзывы отсутствуют'

    bot_data = await dp.bot.get_me()
    if await DBCommandsFeedback.is_feedback(seller_user_id=message.from_user.id):
        link_feedback = f'<a href="t.me/{bot_data.username}?start=feedback_{user.id}">Ссылка на отзывы</a>'

    await message.answer_photo(
        photo=photo,
        caption=text.message.menu.default.profile.format(
            user_id=user.id,
            user_username=user.username,
            registration_date=str(user.create_at).split('.')[0],
            user_balance=round(user.balance, 2),
            user_rate=await make_user_star_rate(user),
            count_views=len(
                await View.query.distinct(View.viewer_user_id).where(make_filter(user_id=user.id)).gino.all()),
            total_amount_shopping=sum([bargin.amount for bargin in list_shopping]),
            total_amount_sales=sum([bargin.amount for bargin in list_sales]),
            link_feedback=link_feedback
        ),
        reply_markup=inline.default.menu.menu_profile.keyboard
    )
