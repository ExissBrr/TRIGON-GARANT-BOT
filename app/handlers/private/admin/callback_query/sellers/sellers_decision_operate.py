from aiogram.types import CallbackQuery

from app.data import text
from app.data.types.seller_data import SellerStatus
from app.keyboards.callback_data.sellers import sellers_cd, CommandsSellers
from app.loader import dp
from app.utils.db_api.models.sellers import Seller
from app.utils.db_api.models.user import User
from app.utils.format_data.user import format_username


@dp.callback_query_handler(sellers_cd.filter(command=CommandsSellers.confirm_seller))
async def approve_seller(call: CallbackQuery, callback_data: dict, lang_code):
    await call.answer()
    seller_id = int(callback_data.get('seller_id'))
    seller_category = callback_data.get('category')
    seller = await Seller.query.where(Seller.user_id == seller_id).where(
        Seller.category == seller_category).gino.first()
    user = await User.get(seller.user_id)
    if seller.status != SellerStatus.APPROVAL:
        return await call.message.edit_text(
            text=text[lang_code].default.call.application_already_solved
        )
    await seller.update_status(SellerStatus.ACTIVE)
    await call.message.edit_text(
        text=text[lang_code].admin.message.seller_approve.format(
            user_username=format_username(user),
            category=seller_category,
        )
    )


@dp.callback_query_handler(sellers_cd.filter(command=CommandsSellers.abolish_seller))
async def approve_seller(call: CallbackQuery, callback_data: dict, lang_code):
    await call.answer()
    seller_id = int(callback_data.get('seller_id'))
    seller_category = callback_data.get('category')
    seller = await Seller.query.where(Seller.user_id == seller_id).where(
        Seller.category == seller_category).gino.first()
    user = await User.get(seller.user_id)
    if seller.status != SellerStatus.APPROVAL:
        await call.message.edit_text(
            text=text[lang_code].default.call.application_already_solved
        )
        return False
    await seller.update_status(SellerStatus.HIDDEN)
    await call.message.edit_text(
        text=text[lang_code].admin.message.seller_decline.format(
            user_username=format_username(user)
        )
    )
