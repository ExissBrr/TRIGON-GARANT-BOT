from aiogram.dispatcher.filters.state import StatesGroup, State


class SearchStates(StatesGroup):
    wait_for_data = State()


class UserSearchStates(StatesGroup):
    wait_for_user_data = State()
