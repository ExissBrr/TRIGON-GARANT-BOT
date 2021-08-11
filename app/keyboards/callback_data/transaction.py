from aiogram.utils.callback_data import CallbackData


class TransactionCommands:
    SHOW_PAYMENT_INFO = '0'
    APPROVE_PAYMENT = '1'
    ABOLISH_PAYMENT = '2'


transaction_cd = CallbackData('transaction', 'comment', 'command')