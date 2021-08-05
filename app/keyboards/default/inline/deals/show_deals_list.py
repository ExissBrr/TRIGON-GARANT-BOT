from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.keyboards.callback_data.deal import deal_cd, DealCommands
from app.utils.db_api.models.user import User


async def make_keyboard_selling_list(deals: list):
    markup = InlineKeyboardMarkup()
    for deal in deals:
        buyer = await User.get(deal.buyer_user_id)
        markup.row(
            InlineKeyboardButton(
                text=f'{deal.amount}₽ {buyer.fullname} ',
                callback_data=deal_cd.new(deal_id=deal.id, command=DealCommands.SHOW_DEAL)
            )
        )
    return markup


async def make_keyboard_shopping_list(deals: list):
    markup = InlineKeyboardMarkup()
    for deal in deals:
        seller = await User.get(deal.seller_user_id)
        markup.row(
            InlineKeyboardButton(
                text=f'{deal.amount}₽ {seller.fullname} ',
                callback_data=deal_cd.new(deal_id=deal.id, command=DealCommands.SHOW_DEAL)
            )
        )
    return markup


async def make_keyboard_controversy_list(deals: list, owner_id: int):
    markup = InlineKeyboardMarkup()
    for deal in deals:
        if deal.seller_user_id != owner_id:
            opponent_id = deal.buyer_user_id
        else:
            opponent_id = deal.seller_user_id

        opponent = await User.get(int(opponent_id))
        markup.row(
            InlineKeyboardButton(
                text=f'{deal.amount}₽ {opponent.fullname} ',
                callback_data=deal_cd.new(deal_id=deal.id, command=DealCommands.SHOW_DEAL)
            )
        )
    return markup
