from aiogram.dispatcher.filters.state import StatesGroup, State


class SellerSearch(StatesGroup):
    wait_for_seller_number = State()
