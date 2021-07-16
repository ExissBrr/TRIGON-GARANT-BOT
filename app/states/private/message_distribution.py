from aiogram.dispatcher.filters.state import StatesGroup, State


class MessageSendingStates(StatesGroup):
    wait_for_delayed_message = State()

    wait_for_message = State()

    wait_for_time = State()

    wait_for_media = State()

    wait_for_url = State()

    wait_for_chat_id = State()

    wait_confirm_create_schedule = State()

    wait_confirm_delete_schedule = State()

    wait_confirm_suspend_schedule = State()

    wait_confirm_activate_schedule = State()
