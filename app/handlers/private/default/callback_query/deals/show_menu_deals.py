from aiogram.types import CallbackQuery

from app import keyboards
from app.data import text
from app.keyboards.callback_data.menu_profile import menu_profile_cd, MenuProfileCD
from app.loader import dp
from app.utils.db_api.models.user import User


@dp.callback_query_handler(menu_profile_cd.filter(command=MenuProfileCD.show_menu_deals))
async def show_menu(call: CallbackQuery, user: User, lang_code):
    await call.message.answer(
        text=text[lang_code].default.message.choose_deal_type,
        reply_markup=await keyboards.default.inline.menu.menu_choose_deal.make_keyboard(user.id, lang_code)
    )
    await call.answer()
