from aiogram.types import CallbackQuery

from app import keyboards
from app.data import text
from app.keyboards.callback_data.admin import admin_menu_cd, AdminMenuChoice
from app.loader import dp


@dp.callback_query_handler(admin_menu_cd.filter(command=AdminMenuChoice.SHOW_SELLER_MENU))
async def show_sellers_menu(call: CallbackQuery, lang_code):
    await call.answer(cache_time=5)
    await call.message.answer(
        text=text[lang_code].default.message.choose_action,
        reply_markup=keyboards.admin.inline.sellers.menu_sellers.make_keyboard_seller_menu(lang_code)
    )
