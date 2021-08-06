from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.keyboards.callback_data.deal import deal_cd, DealCommands, DealAdminCommands
from app.utils.db_api.models.user import User


async def make_keyboard_controversies_list(deals: list):
    markup = InlineKeyboardMarkup()
    for deal in deals:
        buyer: User = await User.get(deal.buyer_user_id)
        markup.row(
            InlineKeyboardButton(
                text=f'{deal.amount}₽ {buyer.id} ',
                callback_data=deal_cd.new(deal_id=deal.id, command=DealAdminCommands.SHOW_ADMIN_DEAL_DETAILS)
            )
        )
    return markup
