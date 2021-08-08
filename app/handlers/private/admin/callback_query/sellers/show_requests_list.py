from aiogram.types import CallbackQuery

from app import keyboards
from app.data import text
from app.data.types.seller_data import SellerStatus
from app.keyboards.callback_data.admin import admin_menu_cd, SellerMenuChoice
from app.loader import dp
from app.utils.db_api.models.sellers import Seller


@dp.callback_query_handler(admin_menu_cd.filter(command=SellerMenuChoice.SHOW_SELLER_REQUESTS))
async def show_seller_requests(call: CallbackQuery, lang_code):
    sellers = await Seller.query.where(Seller.status == SellerStatus.APPROVAL).gino.all()
    await call.message.answer(
        text=text[lang_code].admin.message.seller_requests_for_now,
        reply_markup=await keyboards.admin.inline.sellers.seller_request_list.make_keyboard_sellers_list(sellers)
    )
