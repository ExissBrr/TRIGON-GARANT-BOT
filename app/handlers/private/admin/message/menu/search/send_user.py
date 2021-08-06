from aiogram.dispatcher.handler import SkipHandler
from aiogram.types import Message

from app.data import text
from app.data.types.tmp_files import ExcelFile
from app.loader import dp
from app.states.private.search import SearchStates
from app.utils.db_api.models.user import User
from app.utils.format_data.user import format_username, format_fullname


@dp.message_handler(state=SearchStates.wait_for_data)
async def send_user_info(message: Message, lang_code):
    user = await User.query.where(User.qf(username=message.text, op='or', id=message.text)).gino.first()
    if not user:
        await message.answer(
            text=text[lang_code].default.message.user_not_found
        )
        raise SkipHandler

    user_file_data = ExcelFile()
    user_file_data.write_data(
        id=user.id,
        username=user.username,
        fullname=user.fullname,
        lang_code=user.lang_code,
        deep_link=user.deep_link,
        phone=user.phone,
        role=user.role,
        username_history=user.get_username_history,
        full_name_history=user.get_full_name_history,
        is_read_rules=user.is_read_rules,
        is_blocked=user.is_blocked,
        is_active=user.is_active,
        reason_for_blocking=user.reason_for_blocking,
        online_at=user.online_at,
    )
    await message.answer_document(
        document=user_file_data.input_file,
        caption=text[lang_code].admin.message.user_info.format(
            user_id=user.id,
            user_fullname=format_fullname(user.fullname),
            user_username=format_username(user),
            user_url_to_telegram=user.url_to_telegram,
        )
    )
    raise SkipHandler
