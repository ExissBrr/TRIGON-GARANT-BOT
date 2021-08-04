from aiogram.dispatcher.filters.state import StatesGroup, State


class ChangeRequisitesStates(StatesGroup):
    wait_requisite_data = State()