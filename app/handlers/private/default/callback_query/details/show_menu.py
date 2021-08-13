from aiogram.types import CallbackQuery

from app import keyboards
from app.data import text
from app.keyboards.callback_data.menu_profile import menu_profile_cd, MenuProfileCD
from app.loader import dp
from app.utils.db_api.models.user import User


@dp.callback_query_handler(menu_profile_cd.filter(command=MenuProfileCD.menu_requisites))
async def show_menu_details(call: CallbackQuery, user: User, lang_code):
    if not user.requisites:
        details_list = []
    details_list = user.requisites.split()
    if not details_list:
        await call.message.answer(
            text=text[lang_code].default.message.not_saved_requisites,
            reply_markup=keyboards.default.inline.requisites.change_details.make_keyboard(lang_code)
        )
        return False

    await call.message.answer(
        text=text[lang_code].default.message.my_details.format(
            details='\n'.join(details_list),
        ),
        reply_markup=keyboards.default.inline.requisites.change_details.make_keyboard(lang_code)
    )
