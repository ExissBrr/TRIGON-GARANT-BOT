from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.data import text
from app.data.types.menu_cd import MenuSettingsCD
from app.keyboards.default.callback_data.settings_profile import menu_settings_cd
from app.utils.db_api.models.user import User


def keyboard(lang_code) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                        text=text[lang_code].default.button.inline.menu_setting_lang_code,
                    callback_data=menu_settings_cd.new(menu=MenuSettingsCD.menu_setting_lang_code)
                )
            ],
            [
                InlineKeyboardButton(
                    text=text[lang_code].default.button.inline.menu_setting_timezone,
                    callback_data=menu_settings_cd.new(menu=MenuSettingsCD.menu_setting_timezone)
                )
            ],
            [
                InlineKeyboardButton(
                    text=text[lang_code].default.button.inline.upload_user_data,
                    callback_data=menu_settings_cd.new(menu=MenuSettingsCD.upload_user_data)
                )
            ]
        ]
    )

    return markup
