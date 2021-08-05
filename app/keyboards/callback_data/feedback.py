from aiogram.utils.callback_data import CallbackData


class FeedbackCommands:
    SHOW_FEEDBACK = '0'


feedback_cd = CallbackData('feedback', 'feedback_id', 'command')
