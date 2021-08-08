from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.keyboards.callback_data.sellers import sellers_cd, CommandsSellers
from app.utils.db_api.models.user import User
from app.utils.format_data.user import format_username


async def make_keyboard_sellers_list(sellers):
    markup = InlineKeyboardMarkup()
    for seller in sellers:
        user = await User.get(seller.user_id)
        markup.row(
            InlineKeyboardButton(
                text=f'{format_username(user)} {seller.category}',
                callback_data=sellers_cd.new(seller_id=user.id, category=seller.category,
                                             command=CommandsSellers.show_seller_candidate_info)
            )
        )
    return markup
