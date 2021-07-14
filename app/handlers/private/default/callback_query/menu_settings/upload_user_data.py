from aiogram.types import CallbackQuery

from app.loader import dp
from app.data import text
from app.data.types.menu_cd import MenuSettingsCD
from app.data.types.tmp_files import ExcelFile
from app.keyboards.default.callback_data.settings_profile import menu_settings_cd
from app.utils.db_api.models.user import User
from app.utils.format_data.user import format_username, format_lang_code


@dp.callback_query_handler(menu_settings_cd.filter(menu=MenuSettingsCD.upload_user_data))
async def upload_user_data(call: CallbackQuery, user: User, lang_code):
    await call.answer(
        text=text[lang_code].default.message.file_data,
        cache_time=60
    )
    user_data_file = ExcelFile()
    user_data_file.write_data(
        id=user.id,
        username=format_username(user.username),
        fullname=user.fullname,
        language=format_lang_code(user.lang_code),
        deep_link=user.deep_link,
        user_created=user.create_at
    )
    await call.message.answer_document(
        document=user_data_file.input_file,
        caption=text[lang_code].default.message.file_data
    )
