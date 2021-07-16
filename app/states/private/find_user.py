from aiogram.dispatcher.filters.state import StatesGroup, State


class FindUser(StatesGroup):
    wait_for_data = State()
