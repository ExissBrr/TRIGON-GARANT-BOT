from aiogram.utils.callback_data import CallbackData


class DealCommands:
    SHOW_SHOPPING_LIST = '0'
    SHOW_SELLING_LIST = '1'
    SHOW_CONTROVERSY_LIST = '2'


user_deal_cd = CallbackData('user_deal', 'user_id', 'command')
deal_cd = CallbackData('deal', 'deal_id', 'command')
