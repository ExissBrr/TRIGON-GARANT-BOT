from aiogram.types import CallbackQuery

from keyboards import inline
from keyboards.callback_data.admin.admin_menu_choice import admin_menu_cd, AdminMenuChoice
from loader import dp


@dp.callback_query_handler(admin_menu_cd.filter(command=AdminMenuChoice.SHOW_SELLER_MENU))
async def show_sellers_menu(call: CallbackQuery):
    await call.answer(cache_time=5)
    await call.message.answer(
        text='Выберите действие:',
        reply_markup=inline.admin.sellers.seller_menu.make_keyboard_seller_menu()
    )
