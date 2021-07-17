from aiogram.dispatcher.filters.state import StatesGroup, State


class SettingUser(StatesGroup):
    wait_timezone = State()
