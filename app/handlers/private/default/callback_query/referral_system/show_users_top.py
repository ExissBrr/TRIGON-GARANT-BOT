from aiogram.types import CallbackQuery
from loguru import logger
from sqlalchemy import func

from app.data import text
from app.data.types.user_data import UserDeepLink
from app.keyboards.callback_data.menu_profile import menu_profile_cd, MenuProfileCD
from app.loader import dp
from app.utils.db_api import db
from app.utils.db_api.models.user import User
from app.utils.format_data.user import format_username
from app.utils.parce_data.user import get_users_id_top_referral_system


@dp.callback_query_handler(menu_profile_cd.filter(command=MenuProfileCD.show_top_referral))
async def show_menu(call: CallbackQuery, lang_code):
    users = await User.query.where(User.deep_link != UserDeepLink.NONE).gino.all()

    logger.debug(len(users))
    users_top = [await User.get(user_id) for user_id in get_users_id_top_referral_system(users)]
    if not users_top:
        await call.answer('Еще никто не не подключен к реферальной программе', cache_time=60)
        return False

    user_top_zip = []
    for user in users_top:
        count = await db.select([func.count(User.id)]).where(User.deep_link == user.id).gino.scalar()
        user_top_zip.append((user, count))
    user_top_zip.sort(key=lambda tup: tup[1], reverse=True)
    text_top = ''

    for user, count in user_top_zip[:10]:
        text_top += f'Username {format_username(user)} |' \
                    f'{await db.select([func.count(User.id)]).where(User.deep_link == user.id).gino.scalar()} рефералов\n'
    await call.message.edit_text(
        text=text[lang_code].default.message.users_top_referral_system.format(
            count_users_top=len(users_top),
            user_referral_system_data=text_top
        )
    )
