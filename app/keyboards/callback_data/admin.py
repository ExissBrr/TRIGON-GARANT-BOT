from aiogram.utils.callback_data import CallbackData


class AdminMenuChoice:
    SEND_MESSAGES = '0'
    SHOW_STATISTIC = '1'
    SHOW_BOT_SETTINGS = '2'
    ADD_SCAMMER = '3'
    SHOW_SCAM_LIST = '4'
    SHOW_CONTROVERSY_DEALS = '5'
    PAYMENTS = '6'
    SHOW_SELLER_MENU = '7'


class SellerMenuChoice:
    SHOW_SELLER_REQUESTS = '01'
    SEARCH_SELLER = '02'
    HIDE_SELLER = '03'
    REVEAL_SELLER = '04'


admin_menu_cd = CallbackData('admin_choice', 'command')
seller_menu_cd = CallbackData('seller_menu', 'seller_number', 'command')
