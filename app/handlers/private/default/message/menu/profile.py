from aiogram.types import Message

from app.data import text
from app.data.text.ru.button.reply import profile
from app.loader import dp
from app.utils.bot.generate_links import make_start_link
from app.utils.db_api.models.user import User
from app.utils.format_data.time import timezone
from app.utils.format_data.user import format_username


@dp.message_handler(reply_command=profile)
async def send_menu_profile(message: Message, user: User, bot_data, lang_code):
    profile_text = text[lang_code].default.message.profile.format(
        user_id=user.id,
        user_username=format_username(user.username),
        datetime_register=timezone(user.create_at, user.timezone).strftime('%Y-%m-%d %H:%M'),
        start_link_easter_egg=make_start_link(bot_data.username, 'easter_egg_profile'),
    )
    photos = (await message.from_user.get_profile_photos()).photos
    if photos:
        await message.answer_photo(
            photo=photos[0][-1].file_id,
            caption=profile_text
        )
    else:
        await message.answer(
            text=profile_text
        )
