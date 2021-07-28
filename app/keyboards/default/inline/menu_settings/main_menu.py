from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.data import text
from app.data.types.menu_cd import MenuSettingsCD
from app.keyboards.callback_data.settings_profile import menu_settings_cd
from app.loader import config


def keyboard(lang_code: str) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    if len(config.bot.languages) > 1:  # Меню отобразится, если в бот поддерживает больше 1 языка.
        markup.insert(
            InlineKeyboardButton(
                text=text[lang_code].button.inline.menu_setting_lang_code,
                callback_data=menu_settings_cd.new(menu=MenuSettingsCD.menu_setting_lang_code)
            )
        )

    # Настройка временной зоны
    markup.insert(
        InlineKeyboardButton(
            text=text[lang_code].button.inline.menu_setting_timezone,
            callback_data=menu_settings_cd.new(menu=MenuSettingsCD.menu_setting_timezone)
        )
    )

    # Выгрузка данных для пользователя
    markup.insert(
        InlineKeyboardButton(
            text=text[lang_code].button.inline.upload_user_data,
            callback_data=menu_settings_cd.new(menu=MenuSettingsCD.upload_user_data)
        )
    )

    return markup
