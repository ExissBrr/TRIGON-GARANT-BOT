from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from app import keyboards
from app.data import text
from app.data.types.category_data import ServiceCategoryType
from app.data.types.links import category_link
from app.data.types.seller_data import SellerStatus
from app.loader import dp
from app.utils.db_api.models.sellers import Seller


@dp.message_handler(Command('seller_category'))
async def show_sellers_in_category(message: Message, lang_code):
    category_from_args = message.text.split(':')[-1]
    await message.delete()

    if category_from_args not in ServiceCategoryType.__dict__.values():
        await message.answer(
            text=text[lang_code].default.message.choose_category_among_list
        )
        return False

    for key, value in ServiceCategoryType.__dict__.items():
        if value == category_from_args:
            photo_url = category_link[key]

    sellers = await Seller.query.where(Seller.status == SellerStatus.ACTIVE).where(
        Seller.category == category_from_args).gino.all()
    await message.answer_photo(
        photo=photo_url,
        caption=text[lang_code].default.message.seller_list_in_category.format(category=category_from_args),
        reply_markup=await keyboards.default.inline.sellers.show_seller_list_in_category.make_keyboard_sellers_list(
            sellers=sellers,
            category_name=category_from_args)
    )
