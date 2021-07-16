from aiogram.utils.callback_data import CallbackData


class DistributionCommands:
    ADD_SCHEDULE = '0'
    SHOW_SCHEDULE = '1'
    DELETE_SCHEDULE = '2'
    SUSPEND_SCHEDULE = '3'
    ACTIVATE_SCHEDULE = '4'


distribution_cd = CallbackData('distribution', 'id', 'command')
