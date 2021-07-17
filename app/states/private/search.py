from aiogram.dispatcher.filters.state import StatesGroup, State


class SearchStates(StatesGroup):
    wait_for_data = State()
