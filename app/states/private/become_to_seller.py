from aiogram.dispatcher.filters.state import StatesGroup, State


class BecomeToSeller(StatesGroup):
    wait_category = State()
    wait_description = State()
    wait_accept = State()
