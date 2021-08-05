from aiogram.utils.callback_data import CallbackData


class MenuProfileCD:
    top_up_balance = '0'
    withdraw_balance = '1'
    show_menu_deals = '2'
    menu_requisites = '3'
    show_feedbacks = '4'


menu_profile_cd = CallbackData('menu_profile', 'command')
