from aiogram.utils.callback_data import CallbackData


class UserInteractionCommands:
    CREATE_BARGAIN = '0'
    FEEDBACKS = '1'


class UserCommandType:
    SHOW_MORE_INFO = '0'
    GET_ARCHIVE_TRANSACTION = '1'
    GET_ARCHIVE_DEALS = '2'
    SET_ADMIN_ROLE = '3'
    SET_DEFAULT_ROLE = '4'
    CHANGE_PERCENT_WITHDRAW = '5'
    GET_SELLER_FEEDBACKS = '6'
    CHANGE_LINK_FEEDBACK = '7'


default_user_interaction_cd = CallbackData('user_interaction', 'user_id', 'command')
user_cd = CallbackData('user_command', 'user_id', 'command')
