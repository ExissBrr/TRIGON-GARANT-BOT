from aiogram.types import Message

from app.data import text
from app.data.types.user_data import UserRole
from app.loader import dp
from app.utils.db_api.models.user import User


@dp.message_handler(user_role=UserRole.ADMIN, commands='unbun')
async def unbun_user(message: Message, lang_code):
    user_data = message.get_args().replace('@', '')
    if len(user_data) < 1:
        await message.answer(
            text=text[lang_code].admin.message.error_command_args
        )
        return False
    user = await User.query.where(User.qf(op='or', id=user_data, username=user_data))

    if not user:
        await message.answer(
            text=text[lang_code].admin.message.error_search_user_not_found.format(search_data=user_data)
        )
        return False
    await user.update_data(is_banned=False)
    await message.answer(
        text=text[lang_code].admin.message.successfully_unbun_user
    )
