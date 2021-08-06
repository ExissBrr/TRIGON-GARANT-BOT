from aiogram.utils.callback_data import CallbackData


class SettingsCommands:
    HIDE_USERNAME = '0'
    REVEAL_USERNAME = '1'


menu_settings_cd = CallbackData('menu_settings_cd', 'menu')

choice_lang_cd = CallbackData('choice_lang', 'user_id', 'lang_code')

settings_cd = CallbackData('settings', 'user_id', 'command')
