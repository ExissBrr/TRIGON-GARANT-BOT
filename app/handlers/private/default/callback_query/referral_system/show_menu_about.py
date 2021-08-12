from aiogram.types import CallbackQuery
from sqlalchemy import func

from app import keyboards
from app.data import text
from app.data.types.user_data import UserDeepLink
from app.keyboards.callback_data.menu_profile import menu_profile_cd, MenuProfileCD
from app.loader import dp
from app.utils.db_api import db
from app.utils.db_api.models.user import User


@dp.callback_query_handler(menu_profile_cd.filter(command=MenuProfileCD.show_referral_menu))
async def show_menu(call: CallbackQuery, user: User, lang_code):
    await call.answer(cache_time=5,text='One moment..')
    bot_data = await dp.bot.get_me()
    user_count = await db.select([func.count(User.id)]).where(User.deep_link != UserDeepLink.NONE).gino.scalar()
    await call.message.answer(
        disable_web_page_preview=True,
        text=text[lang_code].default.message.referral_menu.format(
            bot_username=bot_data.username,
            user_id=user.id,
            count_referred_users=user_count,
        ),
        reply_markup=keyboards.default.inline.menu.show_top_referral.keyboard(lang_code)
    )
