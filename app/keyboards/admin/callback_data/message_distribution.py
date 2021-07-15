from aiogram.utils.callback_data import CallbackData


class DistributionCommands:
    ADD_SCHEDULE = '0'
    SHOW_SCHEDULE = '1'


distribution_cd = CallbackData('distribution', 'id', 'command')
