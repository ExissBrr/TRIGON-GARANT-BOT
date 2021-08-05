from aiogram.dispatcher.filters.state import StatesGroup, State


class CreateBargainStates(StatesGroup):
    wait_for_bargain_amount = State()
    wait_confirm_bargain = State()


class CreateBargainFromTemplateBargainStates(StatesGroup):
    wait_confirm_bargain = State()
