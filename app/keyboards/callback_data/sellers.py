from aiogram.utils.callback_data import CallbackData


class CommandsSellers:
    become_seller = '0'
    show_seller_info = '1'
    show_seller_candidate_info = '2'
    confirm_seller = '3'
    abolish_seller = '4'


sellers_cd = CallbackData('sellers', 'seller_id', 'category', 'command')
