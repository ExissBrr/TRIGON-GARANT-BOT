from aiogram.dispatcher.filters.state import StatesGroup, State


class StatesChangeDetails(StatesGroup):
    wait_details_data = State()