from aiogram.types import CallbackQuery

from app import keyboards
from app.data import text
from app.keyboards.callback_data.menu_profile import menu_profile_cd, MenuProfileCD
from app.loader import dp
from app.states.private.change_detail import StatesChangeDetails
from app.utils.db_api.models.user import User


@dp.callback_query_handler(menu_profile_cd.filter(command=MenuProfileCD.change_requisites))
async def request_detail_data(call: CallbackQuery, user: User, lang_code):
    await call.message.delete()
    if not user.requisites:
        list_requisites = []
    list_requisites = user.requisites.split()
    await call.message.answer(
        text=text[lang_code].default.message.request_detail_data,
        reply_markup=keyboards.default.inline.requisites.my_details.make_keyboard(list_requisites, lang_code)
    )
    await StatesChangeDetails.wait_details_data.set()
