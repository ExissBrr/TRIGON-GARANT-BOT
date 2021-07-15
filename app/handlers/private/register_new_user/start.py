from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message

from app import keyboards, dp
from app.data import text
from app.data.types.user_data import UserDeepLink, UserRole
from app.filters.private.user import NewUser
from app.loader import links, config
from app.states.private.registration_new_user import RegistrationNewUser
from app.utils.db_api.models.user import User
from app.utils.format_data.user import format_fullname, format_lang_code


@dp.message_handler(CommandStart(), NewUser())
async def message_on(message: Message, lang_code):
    # deep link
    try:
        deep_link = int(message.get_args())
    except:
        deep_link = UserDeepLink.NONE

    # Re
    if message.from_user.id == config.bot.admin_id:
        role = UserRole.ADMIN
    else:
        role = UserRole.DEFAULT

    user = User(
        id=message.from_user.id,
        fullname=message.from_user.full_name,
        username=message.from_user.username,
        role=role,
        deep_link=deep_link,
    )

    # Add new user in database
    await user.create()

    await message.answer_video(
        video=links.video.window_windows_xp,
        caption=text[lang_code].default.text.welcome.format(
            user_fullname=format_fullname(user.fullname),
            default_lang=format_lang_code(config.bot.languages[0])
        ),
        reply_markup=keyboards.default.reply.menu_settings.languages.keyboard()
    )

    await RegistrationNewUser.choice_language.set()
