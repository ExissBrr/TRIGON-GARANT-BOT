from aiogram.types import Message

from app.data import text
from app.data.types.user_data import UserRole
from app.loader import dp, config
from app.utils.db_api.models.user import User


@dp.message_handler(user_role=UserRole.ADMIN, commands='bun')
async def banned_user(message: Message, lang_code):
    args = message.get_args().replace('@', '').split()

    if len(args) < 1:
        await message.answer(
            text=text[lang_code].admin.message.error_command_args
        )
        return False
    user = await User.query.where(User.qf(op='or', id=args[0], username=args[0]))

    if not user:
        await message.answer(
            text=text[lang_code].admin.message.error_search_user_not_found.format(search_data=args.pop(0))
        )
        return False

    if user.id == config.bot.admin_id:
        await message.answer(
            text=text[lang_code].admin.message.error_blocking_admin,
        )
        return False

    await user.update_data(is_banned=True, reason_for_blocking=' '.join(args))
    await message.answer(
        text=text[lang_code].admin.message.successfull_banned_user
    )


