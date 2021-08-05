from aiogram.dispatcher.filters.state import State, StatesGroup


class FeedbackForSeller(StatesGroup):
    wait_comment = State()
    wait_rate = State()
    approve_feedback = State()
