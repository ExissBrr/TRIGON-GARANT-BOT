from aiogram.utils.callback_data import CallbackData


class UserCommand:
    CREATE_DEAL= '0'
    SHOW_MORE_INFO = '1'
    GET_ARCHIVE_TRANSACTION = '2'
    GET_ARCHIVE_DEALS = '3'
    SET_ADMIN_ROLE = '4'
    SET_DEFAULT_ROLE = '5'
    CHANGE_PERCENT_WITHDRAW = '6'
    GET_SELLER_FEEDBACKS = '7'
    CHANGE_LINK_FEEDBACK = '8'


user_cd = CallbackData('user', 'user_id', 'command')
