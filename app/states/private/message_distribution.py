from aiogram.dispatcher.filters.state import StatesGroup, State


class MessageSendingStates(StatesGroup):
    wait_for_message = State()

    wait_for_delayed_message = State()
    request_for_delayed_message = State()

    wait_for_url = State()
    request_for_url = State()

    wait_for_media = State()
    request_for_media = State()

    wait_for_time = State()
    request_for_time = State()

    wait_confirm_create_schedule = State()
    request_confirm_create_schedule = State()
