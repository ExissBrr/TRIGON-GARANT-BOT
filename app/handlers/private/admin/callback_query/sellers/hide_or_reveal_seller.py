from aiogram.types import CallbackQuery

from app import keyboards
from app.data import text
from app.data.types.seller_data import SellerStatus
from app.keyboards.callback_data.admin import seller_menu_cd, SellerMenuChoice
from app.loader import dp
from app.utils.db_api.models.sellers import Seller


@dp.callback_query_handler(seller_menu_cd.filter(command=SellerMenuChoice.HIDE_SELLER))
async def hide_seller(call: CallbackQuery, callback_data: dict, lang_code):
    await call.answer(cache_time=30)
    seller_number = int(callback_data.get('seller_number'))
    seller = await Seller.get(seller_number)
    await seller.update_data(status=SellerStatus.HIDDEN)
    await call.message.answer(
        text=text[lang_code].admin.call.seller_now_hidden
    )
    await call.message.edit_reply_markup(
        reply_markup=await keyboards.admin.inline.sellers.reveal_hide_seller.make_keyboard_modify_seller(seller_number,
                                                                                                         lang_code)
    )


@dp.callback_query_handler(seller_menu_cd.filter(command=SellerMenuChoice.REVEAL_SELLER))
async def hide_seller(call: CallbackQuery, callback_data: dict, lang_code):
    await call.answer(cache_time=30)
    seller_number = int(callback_data.get('seller_number'))
    seller = await Seller.get(seller_number)

    await seller.update_data(status=SellerStatus.ACTIVE)
    await call.message.answer(
        text=text[lang_code].admin.call.seller_revealed
    )
    await call.message.edit_reply_markup(
        reply_markup=await keyboards.admin.inline.sellers.reveal_hide_seller.make_keyboard_modify_seller(seller_number,
                                                                                                         lang_code)
    )
