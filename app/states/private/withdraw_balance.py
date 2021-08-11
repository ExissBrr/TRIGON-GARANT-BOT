from aiogram.dispatcher.filters.state import StatesGroup, State


class WithdrawBalanceStates(StatesGroup):
    wait_amount = State()
    wait_requisite = State()
    wait_confirm_withdraw_balance = State()
