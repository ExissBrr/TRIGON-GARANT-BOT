from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.data import text
from app.data.types.seller_data import SellerStatus
from app.keyboards.callback_data.admin import seller_menu_cd, SellerMenuChoice
from app.utils.db_api.models.sellers import Seller


async def make_keyboard_modify_seller(seller_number: int,lang_code):
    seller = await Seller.get(seller_number)
    markup = InlineKeyboardMarkup()
    if seller.status == SellerStatus.ACTIVE:
        markup.add(
            InlineKeyboardButton(
                text=text[lang_code].button.inline.hide_seller,
                callback_data=seller_menu_cd.new(seller_number=seller_number, command=SellerMenuChoice.HIDE_SELLER)
            )
        )
    elif seller.status == SellerStatus.HIDDEN or seller.status == SellerStatus.APPROVAL:
        markup.add(
            InlineKeyboardButton(
                text=text[lang_code].button.inline.reveal_seller,
                callback_data=seller_menu_cd.new(seller_number=seller_number, command=SellerMenuChoice.REVEAL_SELLER)
            )
        )
    return markup
