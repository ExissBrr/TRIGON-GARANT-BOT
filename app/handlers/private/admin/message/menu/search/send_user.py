from aiogram.dispatcher.handler import SkipHandler
from aiogram.types import Message

from app.data import text
from app.data.types.tmp_files import ExcelFile
from app.data.types.user_data import UserRole
from app.loader import dp
from app.states.private.search import SearchStates
from app.utils.db_api.models.user import User
from app.utils.format_data.user import format_username, format_fullname

from app.utils.format_data.time import timezone


@dp.message_handler(state=SearchStates.wait_for_data)
async def send_user_info(message: Message, user, lang_code):
    user_for_search = await User.query.where(User.qf(username=message.text.replace('@', ''), op='or', id=message.text)).gino.first()
    if not user_for_search:
        await message.answer(
            text=text[lang_code].default.message.user_not_found
        )
        raise SkipHandler

    user_file_data = ExcelFile()
    user_file_data.write_data(
        id=user_for_search.id,
        username=user_for_search.username,
        fullname=user_for_search.fullname,
        lang_code=user_for_search.lang_code,
        deep_link=user_for_search.deep_link,
        phone=user_for_search.phone,
        role=user_for_search.role,
        timezone=user_for_search.timezone,
        username_history=user_for_search.get_username_history,
        fullname_history=user_for_search.get_fullname_history,
        is_read_rules=user_for_search.is_read_rules,
        is_blocked=user_for_search.is_blocked,
        is_active=user_for_search.is_active,
        reason_for_blocking=user_for_search.reason_for_blocking,
        online_at=timezone(user_for_search.online_at, user.timezone).strftime('%Y-%m-%d %H:%M:%S'),
    )
    await message.answer_document(
        document=user_file_data.input_file,
        caption=text[lang_code].default.message.user_info.format(
            user_id=user_for_search.id,
            user_fullname=format_fullname(user_for_search.fullname),
            user_username=format_username(user_for_search.username),
            user_url_to_telegram=user_for_search.url_to_telegram,
        )
    )
    raise SkipHandler
