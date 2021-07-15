from aiogram.dispatcher.filters.state import StatesGroup, State


class MessageSending(StatesGroup):
    wait_for_message = State()
    wait_for_delayed_message = State()
    wait_for_url = State()
    wait_for_media = State()
    wait_for_time = State()
    confirm_schedule = State()
