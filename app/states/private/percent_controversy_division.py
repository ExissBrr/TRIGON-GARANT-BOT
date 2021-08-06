from aiogram.dispatcher.filters.state import StatesGroup, State


class StateDivideAmount(StatesGroup):
    wait_for_percent = State()
    accept_decision = State()
