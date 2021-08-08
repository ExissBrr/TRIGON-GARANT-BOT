from aiogram.types import CallbackQuery

from app.data import text
from app.keyboards.callback_data.admin import admin_menu_cd, SellerMenuChoice
from app.loader import dp
from app.states.private.search_seller import SellerSearch


@dp.callback_query_handler(admin_menu_cd.filter(command=SellerMenuChoice.SEARCH_SELLER))
async def search_seller(call: CallbackQuery,lang_code):
    await call.answer(cache_time=5)
    await call.message.answer(
        text=text[lang_code].admin.message.enter_seller_number
    )
    await SellerSearch.wait_for_seller_number.set()
