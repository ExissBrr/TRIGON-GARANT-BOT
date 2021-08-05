from aiogram.utils.callback_data import CallbackData


class UserDealCommands:
    SHOW_SHOPPING_LIST = '0'
    SHOW_SELLING_LIST = '1'
    SHOW_CONTROVERSY_LIST = '2'


class DealCommands:
    SHOW_DEAL = '0'
    LEFT_FEEDBACK = '1'
    SHOW_DEAL_INFO = '2'
    CANCEL_DEAL = '3'
    PAY_DEAL = '4'
    CONTROVERSY_DEAL = '5'


user_deal_cd = CallbackData('user_deal', 'user_id', 'command')
deal_cd = CallbackData('deal', 'deal_id', 'command')
